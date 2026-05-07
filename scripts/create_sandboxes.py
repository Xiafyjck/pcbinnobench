#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
from pathlib import Path

BRAND_PREFIXES = ("TI-", "ADI-", "Infineon-", "ST-", "Nordic-", "AMS-", "AMS_")


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_manifest(root: Path) -> dict:
    return json.loads((root / "manifest.json").read_text(encoding="utf-8"))


def clean_copytree(src: Path, dst: Path) -> None:
    def ignore(_dir, names):
        return {name for name in names if name in {".DS_Store", "__pycache__", ".pytest_cache"}}
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=ignore)


def datasheet_candidates(stem: str) -> list[str]:
    out: list[str] = []
    def add(value: str) -> None:
        if value and value not in out:
            out.append(value)
            out.append(value.lower())
    add(stem)
    for prefix in BRAND_PREFIXES:
        if stem.startswith(prefix):
            add(stem[len(prefix):])
            break
    return out


def find_datasheet_dir(datasheets_root: Path, stem: str) -> Path | None:
    if not datasheets_root.is_dir():
        return None
    entries = {path.name.lower(): path for path in datasheets_root.iterdir() if path.is_dir()}
    for candidate in datasheet_candidates(stem):
        hit = entries.get(candidate.lower())
        if hit is not None:
            return hit
    return None


def inject_mineru(workspace: Path, datasheets_root: Path) -> tuple[list[str], list[str]]:
    injected: list[str] = []
    unmatched: list[str] = []
    target_datasheets = workspace / "datasheets"
    if not target_datasheets.is_dir():
        return injected, unmatched
    for pdf in sorted(target_datasheets.glob("*.pdf")):
        hit = find_datasheet_dir(datasheets_root, pdf.stem)
        if hit is None:
            unmatched.append(pdf.name)
            continue
        target = target_datasheets / hit.name
        if not target.exists():
            clean_copytree(hit, target)
        if hit.name not in injected:
            injected.append(hit.name)
    return injected, unmatched


def select_tasks(manifest: dict, names: list[str]) -> list[dict]:
    tasks = manifest["tasks"]
    if names == ["all"]:
        return tasks
    wanted = set(names)
    selected = [task for task in tasks if task["task_id"] in wanted]
    missing = wanted - {task["task_id"] for task in selected}
    if missing:
        raise SystemExit(f"unknown task(s): {', '.join(sorted(missing))}")
    return selected


def main() -> None:
    parser = argparse.ArgumentParser(description="Create Forge sandboxes for PCBInnoBench tasks.")
    parser.add_argument("--out", required=True, type=Path, help="Run root to create, e.g. runs/forge_guidance")
    parser.add_argument("--variant", choices=["base", "guidance"], default="base")
    parser.add_argument("--tasks", nargs="+", default=["all"], help="Task ids or 'all'")
    parser.add_argument("--force", action="store_true", help="Remove an existing output directory first")
    parser.add_argument("--no-mineru", action="store_true", help="Do not inject MinerU markdown directories")
    args = parser.parse_args()

    root = repo_root()
    out = args.out if args.out.is_absolute() else root / args.out
    if out.exists():
        if not args.force:
            raise SystemExit(f"output already exists: {out} (use --force)")
        shutil.rmtree(out)
    out.mkdir(parents=True)

    manifest = load_manifest(root)
    tasks = select_tasks(manifest, args.tasks)
    agents = (root / "AGENTS.md").read_text(encoding="utf-8")
    datasheets_root = root / "datasheets"

    run_manifest = {
        "agent": "forge",
        "variant": args.variant,
        "created_at": now_utc(),
        "sandbox_count": len(tasks),
        "sandboxes": [],
    }

    for task in tasks:
        task_id = task["task_id"]
        task_root = root / task["task_path"]
        sandbox = out / f"{task_id}__{args.variant}"
        workspace = sandbox / "workspace"
        sandbox.mkdir(parents=True)
        clean_copytree(task_root / "workspace", workspace)

        prompt_file = "prompt.md" if args.variant == "base" else "prompt_with_guidance.md"
        prompt = (task_root / prompt_file).read_text(encoding="utf-8")
        (sandbox / "PROMPT.md").write_text(
            prompt.rstrip() + "\n\n---\n\n# General Agent Instructions\n\n" + agents.rstrip() + "\n",
            encoding="utf-8",
        )

        injected: list[str] = []
        unmatched: list[str] = []
        if not args.no_mineru:
            injected, unmatched = inject_mineru(workspace, datasheets_root)

        meta = {
            "task": task_id,
            "variant": args.variant,
            "agent": "forge",
            "prompt_source": f"{task['task_path']}/{prompt_file}",
            "prepared_at": now_utc(),
            "mineru_injected": injected,
            "mineru_unmatched": unmatched,
        }
        (sandbox / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        run_manifest["sandboxes"].append({
            "task": task_id,
            "sandbox": sandbox.name,
            "workspace": f"{sandbox.name}/workspace",
            "prompt": f"{sandbox.name}/PROMPT.md",
            "meta": f"{sandbox.name}/meta.json",
        })

    (out / "manifest.json").write_text(json.dumps(run_manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"created {len(tasks)} sandbox(es) under {out}")


if __name__ == "__main__":
    main()
