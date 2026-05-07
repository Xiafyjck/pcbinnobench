#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from validators.tasks import load_validator  # noqa: E402


def load_manifest() -> dict:
    return json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))


def task_ids() -> list[str]:
    return [task["task_id"] for task in load_manifest()["tasks"]]


def find_sandbox_workspaces(run_root: Path, task: str | None) -> list[tuple[str, Path, Path]]:
    workspaces: list[tuple[str, Path, Path]] = []
    for sandbox in sorted(path for path in run_root.iterdir() if path.is_dir()):
        meta_path = sandbox / "meta.json"
        if meta_path.is_file():
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            task_id = meta.get("task", sandbox.name.rsplit("__", 1)[0])
        else:
            task_id = sandbox.name.rsplit("__", 1)[0]
        if task is not None and task_id != task:
            continue
        workspace = sandbox / "workspace"
        if workspace.is_dir():
            workspaces.append((task_id, workspace, sandbox))
    return workspaces


def validate_one(task_id: str, workspace: Path) -> dict:
    validate = load_validator(task_id)
    result = validate(workspace, repo_root=ROOT)
    return result.to_dict()


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate PCBInnoBench submissions.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--run", type=Path, help="Run root containing sandboxes")
    source.add_argument("--workspace", type=Path, help="Single workspace to validate")
    parser.add_argument("--task", help="Task id for --workspace, or filter for --run")
    parser.add_argument("--write", action="store_true", help="Write validation.json under each sandbox logs directory")
    args = parser.parse_args()

    outputs = []
    if args.workspace:
        if not args.task:
            raise SystemExit("--task is required with --workspace")
        outputs.append({"workspace": str(args.workspace), "result": validate_one(args.task, args.workspace)})
    else:
        run_root = args.run if args.run.is_absolute() else ROOT / args.run
        for task_id, workspace, sandbox in find_sandbox_workspaces(run_root, args.task):
            result = validate_one(task_id, workspace)
            outputs.append({"sandbox": str(sandbox), "workspace": str(workspace), "result": result})
            if args.write:
                logs = sandbox / "logs"
                logs.mkdir(exist_ok=True)
                (logs / "validation.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    passed = sum(1 for item in outputs if item["result"].get("passed"))
    summary = {"count": len(outputs), "passed": passed, "failed": len(outputs) - passed, "results": outputs}
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    if outputs and passed != len(outputs):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
