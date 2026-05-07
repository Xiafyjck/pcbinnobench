from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from .result import ValidationResult

DEFAULT_KICAD_CLI = "/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli"


def find_kicad_cli() -> str | None:
    configured = os.environ.get("KICAD_CLI")
    if configured and Path(configured).is_file():
        return configured
    if Path(DEFAULT_KICAD_CLI).is_file():
        return DEFAULT_KICAD_CLI
    return shutil.which("kicad-cli")


def _run_command(cmd: list[str], cwd: Path, timeout: int = 120) -> dict[str, Any]:
    try:
        completed = subprocess.run(
            cmd,
            cwd=cwd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
        )
        return {
            "exit_code": completed.returncode,
            "stdout_tail": completed.stdout[-2000:],
            "stderr_tail": completed.stderr[-2000:],
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "exit_code": -124,
            "stdout_tail": (exc.stdout or "")[-2000:] if isinstance(exc.stdout, str) else "",
            "stderr_tail": ((exc.stderr or "") + "\ncommand timed out")[-2000:] if isinstance(exc.stderr, str) else "command timed out",
        }


def run_kicad_cli_checks(
    result: ValidationResult,
    workspace: Path,
    ground_truth: Path,
    schematic_file: str | None,
    pcb_file: str | None,
    checks: tuple[str, ...],
) -> None:
    if not checks:
        result.add("task_specific:kicad_cli_profile", False, "task-specific KiCad CLI check profile is empty")
        return

    cli = find_kicad_cli()
    if cli is None:
        result.add(
            "kicad_cli_available",
            True,
            "kicad-cli not found; executable ERC/DRC/netlist checks skipped on this host",
            skipped=True,
        )
        return
    result.add("kicad_cli_available", True, "kicad-cli found", path=cli)

    with tempfile.TemporaryDirectory(prefix="pcbinnobench_") as temp_text:
        temp = Path(temp_text)
        if "erc" in checks:
            if schematic_file is None:
                result.add("kicad_cli:erc", False, "no schematic file configured for ERC")
            else:
                report = temp / "erc.json"
                cmd = [cli, "sch", "erc", "--format", "json", "-o", str(report), str(workspace / schematic_file)]
                payload = _run_command(cmd, cwd=workspace)
                result.add("kicad_cli:erc", payload["exit_code"] == 0, "kicad-cli ERC command failed", command=cmd, **payload)

        if "drc" in checks:
            if pcb_file is None:
                result.add("kicad_cli:drc", False, "no PCB file configured for DRC")
            else:
                report = temp / "drc.json"
                cmd = [
                    cli,
                    "pcb",
                    "drc",
                    "--format",
                    "json",
                    "--schematic-parity",
                    "-o",
                    str(report),
                    str(workspace / pcb_file),
                ]
                payload = _run_command(cmd, cwd=workspace)
                result.add("kicad_cli:drc", payload["exit_code"] == 0, "kicad-cli DRC command failed", command=cmd, **payload)

        if "netlist_export" in checks:
            if schematic_file is None:
                result.add("kicad_cli:netlist_export", False, "no schematic file configured for netlist export")
            else:
                observed = temp / "observed.net"
                expected = temp / "expected.net"
                obs_cmd = [
                    cli,
                    "sch",
                    "export",
                    "netlist",
                    "--format",
                    "kicadsexpr",
                    "-o",
                    str(observed),
                    str(workspace / schematic_file),
                ]
                exp_cmd = [
                    cli,
                    "sch",
                    "export",
                    "netlist",
                    "--format",
                    "kicadsexpr",
                    "-o",
                    str(expected),
                    str(ground_truth / schematic_file),
                ]
                obs = _run_command(obs_cmd, cwd=workspace)
                exp = _run_command(exp_cmd, cwd=ground_truth)
                if obs["exit_code"] != 0 or exp["exit_code"] != 0:
                    result.add(
                        "kicad_cli:netlist_export",
                        False,
                        "kicad-cli netlist export failed",
                        observed_command=obs_cmd,
                        expected_command=exp_cmd,
                        observed=obs,
                        expected=exp,
                    )
                else:
                    observed_normalized = normalize_exported_netlist(observed.read_text(encoding="utf-8", errors="ignore"))
                    expected_normalized = normalize_exported_netlist(expected.read_text(encoding="utf-8", errors="ignore"))
                    observed_hash = hashlib.sha256(observed_normalized.encode("utf-8")).hexdigest()
                    expected_hash = hashlib.sha256(expected_normalized.encode("utf-8")).hexdigest()
                    result.add(
                        "kicad_cli:netlist_export",
                        observed_hash == expected_hash,
                        "exported schematic netlist differs from hidden ground truth",
                        observed_normalized_sha256=observed_hash,
                        expected_normalized_sha256=expected_hash,
                    )




def normalize_exported_netlist(text: str) -> str:
    normalized = re.sub(r'\(date "[^"]*"\)', '(date "<normalized>")', text)
    normalized = re.sub(r'\(source "[^"]*"\)', '(source "<normalized>")', normalized, count=1)
    return normalized


def _iter_blocks(text: str, head: str):
    marker = "(" + head
    start = 0
    while True:
        idx = text.find(marker, start)
        if idx < 0:
            return
        after = idx + len(marker)
        if after < len(text) and text[after] not in " \t\r\n)":
            start = after
            continue
        depth = 0
        in_string = False
        escaped = False
        for pos in range(idx, len(text)):
            char = text[pos]
            if in_string:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == '"':
                    in_string = False
                continue
            if char == '"':
                in_string = True
            elif char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    yield text[idx : pos + 1]
                    start = pos + 1
                    break
        else:
            return


def parse_pcb_footprints(pcb_file: Path) -> dict[str, dict[str, Any]]:
    text = pcb_file.read_text(encoding="utf-8", errors="ignore")
    footprints: dict[str, dict[str, Any]] = {}
    for block in _iter_blocks(text, "footprint"):
        footprint_match = re.search(r'^\(footprint\s+"([^"]+)"', block)
        reference_match = re.search(r'\(property\s+"Reference"\s+"([^"]+)"', block)
        at_match = re.search(r'\(at\s+([-+0-9.]+)\s+([-+0-9.]+)(?:\s+([-+0-9.]+))?', block)
        if not reference_match or not at_match:
            continue
        reference = reference_match.group(1)
        pads: dict[str, str] = {}
        for pad_block in _iter_blocks(block, "pad"):
            pad_match = re.search(r'^\(pad\s+"([^"]+)"', pad_block)
            net_match = re.search(r'\(net\s+\d+\s+"([^"]*)"', pad_block)
            if pad_match and net_match:
                pads[pad_match.group(1)] = net_match.group(1)
        footprints[reference] = {
            "footprint": footprint_match.group(1) if footprint_match else "",
            "x": float(at_match.group(1)),
            "y": float(at_match.group(2)),
            "rotation": float(at_match.group(3) or 0.0),
            "pads": pads,
        }
    return footprints


def check_component_positions(
    result: ValidationResult,
    workspace: Path,
    pcb_file: str | None,
    expected_positions: dict[str, dict[str, Any]],
    tolerance_mm: float,
    rotation_tolerance_deg: float,
) -> None:
    if not expected_positions:
        result.add("task_specific:component_positions", False, "component position check set is empty")
        return
    if pcb_file is None:
        result.add("task_specific:component_positions", False, "no PCB file configured for component position checks")
        return
    footprints = parse_pcb_footprints(workspace / pcb_file)
    for reference, expected in expected_positions.items():
        observed = footprints.get(reference)
        if observed is None:
            result.add(f"component_position:{reference}", False, "component missing from PCB")
            continue
        dx = abs(observed["x"] - expected["x"])
        dy = abs(observed["y"] - expected["y"])
        drot = abs(((observed["rotation"] - expected["rotation"] + 180.0) % 360.0) - 180.0)
        passed = (
            dx <= tolerance_mm
            and dy <= tolerance_mm
            and drot <= rotation_tolerance_deg
            and observed["footprint"] == expected["footprint"]
        )
        result.add(
            f"component_position:{reference}",
            passed,
            "component footprint, position, or rotation differs from hidden ground truth",
            observed=observed,
            expected=expected,
            tolerance_mm=tolerance_mm,
            rotation_tolerance_deg=rotation_tolerance_deg,
        )


def check_pcb_netlist(
    result: ValidationResult,
    workspace: Path,
    pcb_file: str | None,
    expected_nets: dict[str, dict[str, str]],
) -> None:
    if not expected_nets:
        result.add("task_specific:pcb_netlist", False, "PCB netlist check set is empty")
        return
    if pcb_file is None:
        result.add("task_specific:pcb_netlist", False, "no PCB file configured for PCB netlist checks")
        return
    footprints = parse_pcb_footprints(workspace / pcb_file)
    for reference, expected_pads in expected_nets.items():
        observed = footprints.get(reference)
        if observed is None:
            result.add(f"pcb_netlist:{reference}", False, "component missing from PCB")
            continue
        observed_pads = observed["pads"]
        mismatches = {
            pad: {"observed": observed_pads.get(pad), "expected": net}
            for pad, net in expected_pads.items()
            if observed_pads.get(pad) != net
        }
        result.add(
            f"pcb_netlist:{reference}",
            not mismatches,
            "component pad nets differ from hidden ground truth",
            mismatches=mismatches,
            checked_pads=sorted(expected_pads),
        )
