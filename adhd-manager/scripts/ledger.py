#!/usr/bin/env python3
"""Initialize, validate, and summarize ADHD Manager project state."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


TASK_STATUSES = {
    "inbox",
    "triaged",
    "ready",
    "blocked",
    "running",
    "verifying",
    "ready_to_integrate",
    "integrating",
    "done",
    "needs_user",
    "failed",
    "cancelled",
    "superseded",
    "parked",
}
TASK_TYPES = {"feature", "bug", "chore", "research", "repair", "integration", "question"}
PRIORITIES = {"urgent", "high", "normal", "low"}
MODES = {"discovery", "diagnosis", "implementation", "verification", "integration"}
ASSUMPTION_STATUSES = {"active", "confirmed", "rejected", "superseded"}
ACTIVE_OWNERSHIP_STATUSES = {
    "running",
    "verifying",
    "ready_to_integrate",
    "integrating",
}
ACTIVE_CODE_MODES = {"implementation", "verification", "integration"}
ACTIVE_AGENT_STATUSES = {"running", "verifying", "integrating"}
TASK_ID = re.compile(r"^TASK-(\d{3,})$")
ASSUMPTION_ID = re.compile(r"^ASSUMPTION-(\d{3,})$")
USER_ID = re.compile(r"^USER-(\d{3,})$")


def state_dir(project: str) -> Path:
    return Path(project).resolve() / ".codex" / "adhd-manager"


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"missing state file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object in {path}")
    return value


def load_inbox(path: Path) -> list[dict[str, Any]]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError as exc:
        raise ValueError(f"missing state file: {path}") from exc
    events: list[dict[str, Any]] = []
    for number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSON in {path} line {number}: {exc}") from exc
        if not isinstance(event, dict):
            raise ValueError(f"expected JSON object in {path} line {number}")
        events.append(event)
    return events


def initialize(project: str) -> Path:
    root = state_dir(project)
    root.mkdir(parents=True, exist_ok=True)
    defaults: dict[str, str | dict[str, Any]] = {
        "tasks.json": {"schema_version": 1, "next_task_number": 1, "tasks": []},
        "assumptions.json": {
            "schema_version": 1,
            "next_assumption_number": 1,
            "assumptions": [],
        },
        "inbox.jsonl": "",
        "decisions.md": "# ADHD Manager decisions\n\n",
    }
    for name, value in defaults.items():
        path = root / name
        if path.exists():
            continue
        if isinstance(value, dict):
            write_json(path, value)
        else:
            path.write_text(value, encoding="utf-8")
    sync_status(project)
    return root


def require_list(value: Any, label: str, errors: list[str]) -> list[Any]:
    if not isinstance(value, list):
        errors.append(f"{label} must be a list")
        return []
    return value


def validate(project: str) -> list[str]:
    root = state_dir(project)
    errors: list[str] = []
    try:
        task_doc = load_json(root / "tasks.json")
        assumption_doc = load_json(root / "assumptions.json")
        inbox_events = load_inbox(root / "inbox.jsonl")
    except ValueError as exc:
        return [str(exc)]
    if not (root / "decisions.md").is_file():
        errors.append(f"missing state file: {root / 'decisions.md'}")

    if task_doc.get("schema_version") != 1:
        errors.append("tasks.json schema_version must be 1")
    if assumption_doc.get("schema_version") != 1:
        errors.append("assumptions.json schema_version must be 1")

    tasks = require_list(task_doc.get("tasks"), "tasks.json tasks", errors)
    assumptions = require_list(
        assumption_doc.get("assumptions"), "assumptions.json assumptions", errors
    )
    task_ids: set[str] = set()
    task_numbers: list[int] = []
    assumption_ids: set[str] = set()
    assumption_numbers: list[int] = []

    for index, raw in enumerate(tasks):
        label = f"tasks[{index}]"
        if not isinstance(raw, dict):
            errors.append(f"{label} must be an object")
            continue
        task_id = raw.get("id")
        match = TASK_ID.match(task_id) if isinstance(task_id, str) else None
        if not match:
            errors.append(f"{label}.id must match TASK-NNN")
        elif task_id in task_ids:
            errors.append(f"duplicate task id {task_id}")
        else:
            task_ids.add(task_id)
            task_numbers.append(int(match.group(1)))
        if raw.get("type") not in TASK_TYPES:
            errors.append(f"{task_id or label} has invalid type {raw.get('type')!r}")
        if raw.get("priority") not in PRIORITIES:
            errors.append(f"{task_id or label} has invalid priority {raw.get('priority')!r}")
        if raw.get("status") not in TASK_STATUSES:
            errors.append(f"{task_id or label} has invalid status {raw.get('status')!r}")
        if raw.get("execution_mode") not in MODES:
            errors.append(
                f"{task_id or label} has invalid execution_mode {raw.get('execution_mode')!r}"
            )
        if not isinstance(raw.get("revision"), int) or raw.get("revision", 0) < 1:
            errors.append(f"{task_id or label} revision must be a positive integer")
        for key in (
            "depends_on",
            "conflicts_with",
            "requirements",
            "acceptance",
            "exclusions",
            "assumption_ids",
            "source_messages",
            "notes",
        ):
            require_list(raw.get(key), f"{task_id or label}.{key}", errors)
        scope = raw.get("scope")
        if not isinstance(scope, dict):
            errors.append(f"{task_id or label}.scope must be an object")
        else:
            require_list(scope.get("areas"), f"{task_id or label}.scope.areas", errors)
            require_list(
                scope.get("likely_files"), f"{task_id or label}.scope.likely_files", errors
            )
            if raw.get("status") in ACTIVE_OWNERSHIP_STATUSES and scope.get("areas"):
                if not scope.get("owner"):
                    errors.append(f"{task_id or label} has active scope but no scope.owner")
        worker = raw.get("worker")
        if not isinstance(worker, dict):
            errors.append(f"{task_id or label}.worker must be an object")
        elif raw.get("status") in {"running", "verifying", "integrating"}:
            if not worker.get("agent_id"):
                errors.append(f"{task_id or label} is active but has no worker.agent_id")
            if not isinstance(worker.get("model"), str) or not worker.get("model", "").strip():
                errors.append(f"{task_id or label} is active but has no worker.model")
            if not isinstance(worker.get("reasoning_effort"), str) or not worker.get(
                "reasoning_effort", ""
            ).strip():
                errors.append(
                    f"{task_id or label} is active but has no worker.reasoning_effort"
                )
            if raw.get("execution_mode") in ACTIVE_CODE_MODES and not worker.get("worktree"):
                errors.append(f"{task_id or label} is active code work but has no worktree")
        if raw.get("status") == "superseded" and not raw.get("superseded_by"):
            errors.append(f"{task_id or label} is superseded but superseded_by is empty")
        if raw.get("status") == "blocked" and not raw.get("depends_on") and not raw.get("notes"):
            errors.append(f"{task_id or label} is blocked without a dependency or blocker note")

    expected_next_task = max(task_numbers, default=0) + 1
    next_task = task_doc.get("next_task_number")
    if not isinstance(next_task, int) or next_task < expected_next_task:
        errors.append(f"next_task_number must be at least {expected_next_task}")

    for index, raw in enumerate(assumptions):
        label = f"assumptions[{index}]"
        if not isinstance(raw, dict):
            errors.append(f"{label} must be an object")
            continue
        assumption_id = raw.get("id")
        match = ASSUMPTION_ID.match(assumption_id) if isinstance(assumption_id, str) else None
        if not match:
            errors.append(f"{label}.id must match ASSUMPTION-NNN")
        elif assumption_id in assumption_ids:
            errors.append(f"duplicate assumption id {assumption_id}")
        else:
            assumption_ids.add(assumption_id)
            assumption_numbers.append(int(match.group(1)))
        if raw.get("task_id") not in task_ids:
            errors.append(f"{assumption_id or label} references unknown task {raw.get('task_id')!r}")
        if raw.get("status") not in ASSUMPTION_STATUSES:
            errors.append(f"{assumption_id or label} has invalid status {raw.get('status')!r}")
        if not isinstance(raw.get("reversible"), bool):
            errors.append(f"{assumption_id or label}.reversible must be boolean")
        if raw.get("status") == "superseded" and not raw.get("superseded_by"):
            errors.append(f"{assumption_id or label} is superseded but superseded_by is empty")

    expected_next_assumption = max(assumption_numbers, default=0) + 1
    next_assumption = assumption_doc.get("next_assumption_number")
    if not isinstance(next_assumption, int) or next_assumption < expected_next_assumption:
        errors.append(f"next_assumption_number must be at least {expected_next_assumption}")

    user_ids: set[str] = set()
    for index, event in enumerate(inbox_events):
        label = f"inbox event {index + 1}"
        user_id = event.get("id")
        if not isinstance(user_id, str) or not USER_ID.match(user_id):
            errors.append(f"{label}.id must match USER-NNN")
        elif user_id in user_ids:
            errors.append(f"duplicate inbox id {user_id}")
        else:
            user_ids.add(user_id)
        if not isinstance(event.get("summary"), str) or not event.get("summary", "").strip():
            errors.append(f"{user_id or label}.summary must be a non-empty string")
        for task_id in require_list(event.get("task_ids"), f"{user_id or label}.task_ids", errors):
            if task_id not in task_ids:
                errors.append(f"{user_id or label} references unknown task {task_id}")

    task_by_id = {
        raw["id"]: raw
        for raw in tasks
        if isinstance(raw, dict) and isinstance(raw.get("id"), str) and raw["id"] in task_ids
    }
    for task_id, raw in task_by_id.items():
        for dependency in raw.get("depends_on", []):
            if dependency not in task_ids:
                errors.append(f"{task_id} depends on unknown task {dependency}")
            if dependency == task_id:
                errors.append(f"{task_id} cannot depend on itself")
        for conflict in raw.get("conflicts_with", []):
            if conflict not in task_ids:
                errors.append(f"{task_id} conflicts with unknown task {conflict}")
            if conflict == task_id:
                errors.append(f"{task_id} cannot conflict with itself")
        for assumption_id in raw.get("assumption_ids", []):
            if assumption_id not in assumption_ids:
                errors.append(f"{task_id} references unknown assumption {assumption_id}")

    visit_state: dict[str, int] = {}

    def visit(task_id: str, trail: list[str]) -> None:
        state = visit_state.get(task_id, 0)
        if state == 1:
            cycle = trail[trail.index(task_id) :]
            errors.append("dependency cycle: " + " -> ".join(cycle))
            return
        if state == 2:
            return
        visit_state[task_id] = 1
        for dependency in task_by_id[task_id].get("depends_on", []):
            if dependency in task_by_id:
                visit(dependency, trail + [dependency])
        visit_state[task_id] = 2

    for task_id in task_by_id:
        if visit_state.get(task_id, 0) == 0:
            visit(task_id, [task_id])

    area_owners: dict[str, str] = {}
    active_code_agents: set[str] = set()
    for task_id, raw in task_by_id.items():
        if raw.get("status") not in ACTIVE_OWNERSHIP_STATUSES:
            continue
        scope = raw.get("scope") if isinstance(raw.get("scope"), dict) else {}
        worker = raw.get("worker") if isinstance(raw.get("worker"), dict) else {}
        if (
            raw.get("status") in ACTIVE_AGENT_STATUSES
            and raw.get("execution_mode") in ACTIVE_CODE_MODES
        ):
            agent_id = worker.get("agent_id")
            if agent_id:
                active_code_agents.add(agent_id)
        areas = scope.get("areas") if isinstance(scope.get("areas"), list) else []
        for area in areas:
            if not isinstance(area, str) or not area:
                errors.append(f"{task_id} has an invalid scope area")
                continue
            previous = area_owners.get(area)
            if previous:
                errors.append(f"scope area {area!r} is actively owned by {previous} and {task_id}")
            else:
                area_owners[area] = task_id
    if len(active_code_agents) > 3:
        errors.append(
            f"active code-writing agent count is {len(active_code_agents)}; maximum is 3"
        )

    return errors


def render_status(project: str) -> str:
    root = state_dir(project)
    task_doc = load_json(root / "tasks.json")
    assumption_doc = load_json(root / "assumptions.json")
    tasks = task_doc.get("tasks", [])
    assumptions = assumption_doc.get("assumptions", [])
    sections = [
        ("Active", {"running", "verifying", "ready_to_integrate", "integrating"}),
        ("Ready", {"ready"}),
        ("Waiting", {"blocked", "needs_user"}),
        ("Backlog", {"inbox", "triaged", "parked"}),
        ("Terminal", {"done", "failed", "cancelled", "superseded"}),
    ]
    lines = ["# ADHD Manager status", ""]
    for title, statuses in sections:
        selected = [task for task in tasks if isinstance(task, dict) and task.get("status") in statuses]
        lines.extend([f"## {title}", ""])
        if not selected:
            lines.extend(["- None", ""])
            continue
        for task in sorted(selected, key=lambda item: item.get("id", "")):
            mode = task.get("execution_mode", "unknown")
            worker = task.get("worker") if isinstance(task.get("worker"), dict) else {}
            model = worker.get("model") or "unassigned"
            effort = worker.get("reasoning_effort") or "unassigned"
            lines.append(
                f"- `{task.get('id', '?')}` r{task.get('revision', '?')} "
                f"[{task.get('status', '?')}/{mode}] {task.get('title', '')} "
                f": {model}/{effort}"
            )
        lines.append("")
    active_assumptions = [
        item for item in assumptions if isinstance(item, dict) and item.get("status") == "active"
    ]
    lines.extend(["## Active assumptions", ""])
    if not active_assumptions:
        lines.append("- None")
    else:
        for item in sorted(active_assumptions, key=lambda value: value.get("id", "")):
            lines.append(
                f"- `{item.get('id', '?')}` ({item.get('task_id', '?')}): "
                f"{item.get('statement', '')}"
            )
    lines.append("")
    return "\n".join(lines)


def sync_status(project: str) -> Path:
    root = state_dir(project)
    root.mkdir(parents=True, exist_ok=True)
    output = root / "status.md"
    temporary = root / ".status.md.tmp"
    temporary.write_text(render_status(project), encoding="utf-8")
    temporary.replace(output)
    return output


def next_id(project: str, kind: str) -> str:
    root = state_dir(project)
    if kind == "task":
        doc = load_json(root / "tasks.json")
        number = doc.get("next_task_number")
        if not isinstance(number, int) or number < 1:
            raise ValueError("next_task_number must be a positive integer")
        return f"TASK-{number:03d}"
    if kind == "assumption":
        doc = load_json(root / "assumptions.json")
        number = doc.get("next_assumption_number")
        if not isinstance(number, int) or number < 1:
            raise ValueError("next_assumption_number must be a positive integer")
        return f"ASSUMPTION-{number:03d}"
    numbers = []
    for event in load_inbox(root / "inbox.jsonl"):
        user_id = event.get("id")
        match = USER_ID.match(user_id) if isinstance(user_id, str) else None
        if match:
            numbers.append(int(match.group(1)))
    return f"USER-{max(numbers, default=0) + 1:03d}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("init", "validate", "status", "sync-status"):
        subparser = subparsers.add_parser(command)
        subparser.add_argument("--project", default=".")
    id_parser = subparsers.add_parser("next-id")
    id_parser.add_argument("kind", choices=("task", "assumption", "message"))
    id_parser.add_argument("--project", default=".")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "init":
            root = initialize(args.project)
            print(f"initialized {root}")
        elif args.command == "validate":
            errors = validate(args.project)
            if errors:
                for error in errors:
                    print(f"ERROR: {error}", file=sys.stderr)
                return 1
            print("ledger valid")
        elif args.command == "status":
            print(render_status(args.project), end="")
        elif args.command == "sync-status":
            output = sync_status(args.project)
            print(f"wrote {output}")
        elif args.command == "next-id":
            print(next_id(args.project, args.kind))
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
