#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import signal
import subprocess
import time
import uuid
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def find_sandboxes(root: Path) -> list[Path]:
    if not root.is_dir():
        raise SystemExit(f"run root not found: {root}")
    return sorted(path for path in root.iterdir() if path.is_dir() and (path / "workspace").is_dir() and (path / "PROMPT.md").is_file())


def is_done(sandbox: Path) -> bool:
    status_path = sandbox / "logs" / "status.json"
    if not status_path.is_file():
        return False
    try:
        return json.loads(status_path.read_text(encoding="utf-8")).get("status") == "done"
    except (OSError, json.JSONDecodeError):
        return False


def capture(name: str, cmd: list[str], logs_dir: Path, cwd: Path, timeout: int = 120) -> int:
    stdout_path = logs_dir / f"{name}.stdout"
    stderr_path = logs_dir / f"{name}.stderr"
    with stdout_path.open("wb") as stdout_file, stderr_path.open("wb") as stderr_file:
        try:
            result = subprocess.run(cmd, cwd=cwd, stdout=stdout_file, stderr=stderr_file, timeout=timeout)
            return result.returncode
        except subprocess.TimeoutExpired as exc:
            stdout_file.write(exc.stdout or b"")
            stderr_file.write(exc.stderr or b"")
            stderr_file.write(b"\ncommand timed out\n")
            return -124
        except FileNotFoundError:
            stderr_file.write((cmd[0] + " not found\n").encode("utf-8"))
            return -1


def parse_stats(path: Path) -> dict[str, str]:
    stats: dict[str, str] = {}
    if not path.exists():
        return stats
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        parts = line.split()
        if len(parts) >= 3:
            stats[f"{parts[0]}.{parts[1]}"] = parts[2]
    return stats


def move_latest_dump(sandbox: Path, logs_dir: Path, before: set[Path]) -> bool:
    after = set(sandbox.glob("*dump.json"))
    new_dumps = sorted(after - before, key=lambda path: path.stat().st_mtime)
    if not new_dumps:
        return False
    target = logs_dir / "conversation.json"
    if target.exists():
        target.unlink()
    shutil.move(str(new_dumps[-1]), target)
    return True


def run_one(sandbox_text: str, timeout: int, model: str, keep_conversation: str) -> dict:
    sandbox = Path(sandbox_text)
    logs_dir = sandbox / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    stdout_path = logs_dir / "stdout.log"
    stderr_path = logs_dir / "stderr.log"
    status_path = logs_dir / "status.json"
    last_message_path = logs_dir / "last_message.txt"
    prompt_snapshot = logs_dir / "prompt.snapshot.md"

    meta = {}
    if (sandbox / "meta.json").is_file():
        meta = json.loads((sandbox / "meta.json").read_text(encoding="utf-8"))
    task_id = meta.get("task", sandbox.name.rsplit("__", 1)[0])
    prompt_text = (sandbox / "PROMPT.md").read_text(encoding="utf-8")
    shutil.copyfile(sandbox / "PROMPT.md", prompt_snapshot)

    conversation_id = str(uuid.uuid4())
    cmd = [
        "forge",
        "--verbose",
        "--conversation-id",
        conversation_id,
        "-C",
        str(sandbox),
        "-p",
        prompt_text,
    ]

    started_at = now_utc()
    started = time.monotonic()
    status = "done"
    exit_code: int | None = None

    with stdout_path.open("wb") as stdout_file, stderr_path.open("wb") as stderr_file:
        try:
            proc = subprocess.Popen(cmd, cwd=sandbox, stdout=stdout_file, stderr=stderr_file, start_new_session=True)
            try:
                proc.wait(timeout=timeout)
                exit_code = proc.returncode
                if exit_code != 0:
                    status = "failed"
            except subprocess.TimeoutExpired:
                status = "timeout"
                try:
                    os.killpg(proc.pid, signal.SIGTERM)
                    proc.wait(timeout=5)
                except (ProcessLookupError, subprocess.TimeoutExpired):
                    try:
                        os.killpg(proc.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                    proc.wait()
                exit_code = proc.returncode
        except FileNotFoundError:
            status = "failed"
            exit_code = -1
            stderr_file.write(b"forge CLI not found\n")

    show_exit = capture("last_message", ["forge", "conversation", "show", conversation_id], logs_dir, sandbox)
    stats_exit = capture("stats", ["forge", "conversation", "stats", "--porcelain", conversation_id], logs_dir, sandbox)
    if (logs_dir / "last_message.stdout").exists():
        shutil.copyfile(logs_dir / "last_message.stdout", last_message_path)

    dump_exit: int | None = None
    conversation_json_exists = False
    if keep_conversation in {"always", "failed"} and (keep_conversation == "always" or status != "done"):
        before = set(sandbox.glob("*dump.json"))
        dump_exit = capture("dump", ["forge", "conversation", "dump", conversation_id], logs_dir, sandbox)
        conversation_json_exists = move_latest_dump(sandbox, logs_dir, before)

    stats = parse_stats(logs_dir / "stats.stdout")
    payload = {
        "task": task_id,
        "status": status,
        "exit_code": exit_code,
        "started_at": started_at,
        "ended_at": now_utc(),
        "duration_s": round(time.monotonic() - started, 3),
        "agent": "forge",
        "model": model,
        "conversation_id": conversation_id,
        "sandbox": str(sandbox),
        "show_exit": show_exit,
        "stats_exit": stats_exit,
        "dump_exit": dump_exit,
        "conversation_json_exists": conversation_json_exists,
        "tokens": {
            "prompt_tokens": stats.get("token.prompt_tokens"),
            "completion_tokens": stats.get("token.completion_tokens"),
            "total_tokens": stats.get("token.total_tokens"),
        },
        "stats": stats,
        "cmd": cmd[:5] + ["-C", str(sandbox), "-p", "<prompt text>"],
    }
    status_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Forge over prepared PCBInnoBench sandboxes.")
    parser.add_argument("--root", required=True, type=Path, help="Run root created by create_sandboxes.py")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=5400)
    parser.add_argument("--model", default="forge-config", help="Recorded in status; configure Forge separately")
    parser.add_argument("--task", help="Run one task id")
    parser.add_argument("--include-done", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--keep-conversation", choices=["never", "failed", "always"], default="failed")
    args = parser.parse_args()

    sandboxes = find_sandboxes(args.root)
    if args.task:
        sandboxes = [sandbox for sandbox in sandboxes if sandbox.name.startswith(args.task + "__")]
        if not sandboxes:
            raise SystemExit(f"task not found under {args.root}: {args.task}")
    if not args.include_done:
        sandboxes = [sandbox for sandbox in sandboxes if not is_done(sandbox)]

    if args.dry_run:
        print(f"{len(sandboxes)} sandbox(es) would run")
        for sandbox in sandboxes:
            print(sandbox.name)
        return
    if not sandboxes:
        print("No pending sandboxes.")
        return

    print(f"running {len(sandboxes)} sandbox(es), workers={args.workers}, timeout={args.timeout}s, agent=forge")
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(run_one, str(sandbox), args.timeout, args.model, args.keep_conversation) for sandbox in sandboxes]
        for future in as_completed(futures):
            result = future.result()
            tokens = result.get("tokens", {})
            print(f"[{result['status']}] {result['task']} exit={result['exit_code']} duration={result['duration_s']}s tokens={tokens.get('total_tokens')}")


if __name__ == "__main__":
    main()
