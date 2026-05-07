from __future__ import annotations

import hashlib
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def has_balanced_parentheses(path: Path) -> bool:
    depth = 0
    in_string = False
    escaped = False
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    for char in text:
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
            if depth < 0:
                return False
    return depth == 0 and not in_string


def contains_forbidden_hidden_path(workspace_dir: Path) -> bool:
    forbidden = {"ground_truth", "ground_truths", "evaluation"}
    for path in workspace_dir.rglob("*"):
        parts = {part.lower() for part in path.relative_to(workspace_dir).parts}
        if parts & forbidden:
            return True
    return False
