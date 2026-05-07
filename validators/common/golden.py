from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .kicad_checks import check_component_positions, check_pcb_netlist, run_kicad_cli_checks
from .project import contains_forbidden_hidden_path, has_balanced_parentheses, sha256_file
from .result import ValidationResult


@dataclass(frozen=True)
class TaskSpec:
    task_id: str
    project_files: list[str]
    golden_hashes: dict[str, str]
    source_hashes: dict[str, str | None]
    schematic_file: str | None = None
    pcb_file: str | None = None
    kicad_cli_checks: tuple[str, ...] = ()
    position_checks: dict[str, dict[str, Any]] = field(default_factory=dict)
    netlist_checks: dict[str, dict[str, str]] = field(default_factory=dict)
    position_tolerance_mm: float = 0.02
    rotation_tolerance_deg: float = 0.2


def validate_against_ground_truth(spec: TaskSpec, workspace_dir: str | Path, repo_root: str | Path | None = None) -> ValidationResult:
    workspace = Path(workspace_dir).resolve()
    root = Path(repo_root).resolve() if repo_root is not None else Path(__file__).resolve().parents[2]
    ground_truth = root / "evaluation" / "ground_truths" / spec.task_id
    result = ValidationResult(task_id=spec.task_id)

    result.add("workspace_exists", workspace.is_dir(), f"workspace not found: {workspace}")
    if not workspace.is_dir():
        return result

    result.add(
        "hidden_files_absent",
        not contains_forbidden_hidden_path(workspace),
        "workspace must not contain hidden evaluation or ground-truth files",
    )
    result.add("ground_truth_exists", ground_truth.is_dir(), f"hidden ground truth not found: {ground_truth}")

    result.add(
        "task_specific_profile_nonempty",
        bool(spec.kicad_cli_checks) and bool(spec.position_checks) and bool(spec.netlist_checks),
        "task-specific validator must include KiCad CLI, component-position, and PCB-netlist checks",
        kicad_cli_checks=spec.kicad_cli_checks,
        position_check_count=len(spec.position_checks),
        netlist_check_count=len(spec.netlist_checks),
    )

    for rel in spec.project_files:
        submission = workspace / rel
        golden = ground_truth / rel
        result.add(f"required_file:{rel}", submission.is_file(), f"missing required project file: {rel}")
        if not submission.is_file():
            continue
        if submission.suffix in {".kicad_sch", ".kicad_pcb", ".kicad_pro"}:
            result.add(f"parseable:{rel}", has_balanced_parentheses(submission), f"KiCad s-expression is not balanced: {rel}")
        if golden.is_file():
            result.add(f"golden_file:{rel}", True)
        else:
            result.add(f"golden_file:{rel}", False, f"missing hidden golden file: {rel}")
            continue

        observed = sha256_file(submission)
        expected = spec.golden_hashes.get(rel)
        source = spec.source_hashes.get(rel)
        changed_when_needed = source is None or source == expected or observed != source
        result.add(
            f"changed_if_required:{rel}",
            changed_when_needed,
            "submission is unchanged from the template for a file that differs in the ground truth",
        )
        result.add(
            f"matches_ground_truth:{rel}",
            observed == expected,
            "submission file does not match the calibrated golden design",
            expected_sha256=expected,
            observed_sha256=observed,
        )

    run_kicad_cli_checks(
        result,
        workspace,
        ground_truth,
        spec.schematic_file,
        spec.pcb_file,
        spec.kicad_cli_checks,
    )
    check_component_positions(
        result,
        workspace,
        spec.pcb_file,
        spec.position_checks,
        spec.position_tolerance_mm,
        spec.rotation_tolerance_deg,
    )
    check_pcb_netlist(result, workspace, spec.pcb_file, spec.netlist_checks)
    return result
