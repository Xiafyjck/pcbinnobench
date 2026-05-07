# PCBInnoBench

PCBInnoBench is an executable PCB design benchmark for LLM agents. This release contains a curated 35-task subset packaged for Forge runs. Each task asks an agent to modify a KiCad project in place and is evaluated against hidden task validators.

## Repository Layout

- `tasks/`: 35 agent-visible task packages. Each task contains `workspace/`, `prompt.md`, `prompt_with_guidance.md`, and `task.json`; original component PDFs remain under each task workspace when available.
- `evaluation/ground_truths/`: hidden golden KiCad projects used only by validators. Do not copy this directory into an agent sandbox.
- `validators/common/`: shared validator implementation.
- `validators/tasks/`: thin per-task validators that call the shared validator with task-specific file expectations.
- `scripts/create_sandboxes.py`: creates isolated Forge sandboxes.
- `scripts/run_forge.py`: runs Forge on prepared sandboxes.
- `scripts/validate.py`: scores completed sandboxes.

## Run With Forge

Create base-prompt sandboxes:

```bash
uv run python scripts/create_sandboxes.py --variant base --tasks all --out runs/forge_base_35
```

Create guided-prompt sandboxes:

```bash
uv run python scripts/create_sandboxes.py --variant guidance --tasks all --out runs/forge_guidance_35
```

Run Forge:

```bash
uv run python scripts/run_forge.py --root runs/forge_guidance_35 --workers 8 --timeout 5400
```

Score the run:

```bash
uv run python scripts/validate.py --run runs/forge_guidance_35 --write
```

Forge model/provider selection is intentionally left to your Forge configuration. The runner records the selected model label if you pass `--model`, but it does not call Codex CLI or Claude Code.

## Task Format

A task directory has this shape:

```text
tasks/<task_id>/
├── workspace/
├── prompt.md
├── prompt_with_guidance.md
└── task.json
```

`workspace/` is the only directory the evaluated agent should edit. The `prompt_with_guidance.md` file is the guided condition described in the benchmark paper.

## Validator Boundary

The public validator code is split into a maintained common layer and small task-specific wrappers. The hidden golden projects live under `evaluation/ground_truths/` and are intentionally excluded from sandboxes produced by `create_sandboxes.py`.
