# State model

Use this reference as the durable state contract for ADHD Manager.

## Contents

- Project files
- Task schema
- Worker model assignment
- Assumption schema
- State transitions
- Revision rules
- Recovery and reconciliation

## Project files

Store manager-owned state under `.codex/adhd-manager/`:

```text
.codex/adhd-manager/
├── tasks.json
├── assumptions.json
├── inbox.jsonl
├── decisions.md
└── status.md
```

- `tasks.json`: source of truth for tasks, dependencies, ownership, workers, and integration.
- `assumptions.json`: important assumptions and their resolution history.
- `inbox.jsonl`: append-only normalized user-message events. Store concise intent summaries, not secrets or unnecessary raw chat.
- `decisions.md`: durable explanations for routing, architecture constraints, cancellations, and significant priority changes.
- `status.md`: generated human-readable snapshot, not a source of truth.

Do not place product specifications or worker scratch notes here when they belong in normal project documentation.

## Task schema

Keep `tasks.json` in this shape:

```json
{
  "schema_version": 1,
  "next_task_number": 2,
  "tasks": [
    {
      "id": "TASK-001",
      "title": "Manage access keys",
      "type": "feature",
      "priority": "normal",
      "status": "ready",
      "revision": 2,
      "execution_mode": "implementation",
      "depends_on": [],
      "conflicts_with": [],
      "scope": {
        "areas": ["access-key-domain"],
        "likely_files": [],
        "owner": null
      },
      "requirements": [
        "List active keys",
        "Revoke an existing key",
        "Reduce an existing key's permissions"
      ],
      "acceptance": [
        "A user can revoke a key and it can no longer authenticate"
      ],
      "exclusions": [
        "Do not increase permissions on an existing key"
      ],
      "assumption_ids": ["ASSUMPTION-001"],
      "source_messages": ["USER-001", "USER-005"],
      "worker": {
        "agent_id": null,
        "model": null,
        "reasoning_effort": null,
        "worktree": null,
        "branch": null,
        "base_commit": null,
        "result_commit": null
      },
      "superseded_by": null,
      "notes": []
    }
  ]
}
```

Allowed task types:

```text
feature bug chore research repair integration question
```

Allowed priorities:

```text
urgent high normal low
```

Allowed execution modes:

```text
discovery diagnosis implementation verification integration
```

Use lowercase values in state files even when displaying uppercase labels to the user.

## Worker model assignment

Set `worker.model` and `worker.reasoning_effort` immediately before dispatch:

```json
"worker": {
  "agent_id": "agent-a1",
  "model": "gpt-5.6-sol",
  "reasoning_effort": "xhigh",
  "worktree": "/absolute/project-specific/worktree",
  "branch": "codex/adhd/task-001-r2",
  "base_commit": "abc123",
  "result_commit": null
}
```

This example uses the high-risk floor because the task changes authentication credentials. Resolve every assignment through `model-policy.md`; do not copy this model and effort as general defaults.

Use `"inherit"` when the runtime does not expose an override or deliberate inheritance is selected. Record the effective requested values, not a model guessed from documentation. A ready or blocked task may keep these fields `null` until it is assigned.

Changing the worker model does not increment the product-task revision. Record a meaningful escalation or fallback in `decisions.md`, replace the worker assignment, and preserve evidence from the earlier attempt.

## Assumption schema

Keep `assumptions.json` in this shape:

```json
{
  "schema_version": 1,
  "next_assumption_number": 2,
  "assumptions": [
    {
      "id": "ASSUMPTION-001",
      "task_id": "TASK-001",
      "statement": "Existing key permissions may only be reduced",
      "reason": "Safer default for credential management",
      "risk": "User may require permission increases",
      "reversible": true,
      "status": "active",
      "source_message": "USER-005",
      "superseded_by": null
    }
  ]
}
```

Allowed assumption states:

```text
active confirmed rejected superseded
```

Announce each material `active` assumption when it is created. When the user corrects it, change its state, record the replacement if any, revise the task, and steer or stop stale work.

## Inbox events

Append one JSON object per user message or meaningful correction:

```json
{"id":"USER-005","at":"2026-08-08T14:30:00Z","summary":"Allow reducing access-key permissions","task_ids":["TASK-001"]}
```

Use monotonically increasing `USER-NNN` identifiers within the manager session. Omit secrets, credentials, personal data, and large pasted content. Reference an external or project artifact instead.

Use `ledger.py next-id message` to obtain the next message ID; use `next-id task` and `next-id assumption` for the other ledgers. Increment the corresponding `next_*_number` value when adding a task or assumption.

## State transitions

Use these normal transitions:

```text
inbox -> triaged -> ready -> running -> verifying
       -> blocked <- ready
verifying -> ready_to_integrate -> integrating -> done
```

Use these side states when justified:

```text
needs_user failed cancelled superseded parked
```

Rules:

- `blocked` requires an explicit dependency or blocker in `notes`.
- `needs_user` requires a question whose answer materially changes the task.
- `failed` requires attempted work and failure evidence; retry by revising or creating a repair task.
- `superseded` requires `superseded_by` to identify a task or source message.
- `parked` is accepted backlog, not silently discarded work.
- `done` requires accepted-revision evidence and integration, except a discovery-only task whose deliverable is a decision or work order.
- Keep scope ownership until integration, cancellation, supersession, or an explicit handoff releases it.

## Revision rules

Increment `revision` when any accepted property changes:

- requirements or exclusions;
- acceptance criteria;
- scope or ownership boundaries;
- dependencies or priority;
- user-approved assumption;
- execution mode when it changes the deliverable.

Do not increment for progress notes, timestamps, worker IDs, model assignment, test output, or result commits.

Before accepting a worker result, compare its revision with the current task revision. If stale, identify the delta. Reuse the result only when a verifier or integrator proves the delta cannot affect it.

## Recovery and reconciliation

At activation or after interruption:

1. Validate JSON and graph integrity with `ledger.py validate`.
2. Inspect live agent state, known worktrees, branch heads, and result commits.
3. Treat `running`, `verifying`, and `integrating` entries without a live worker as uncertain.
4. Inspect evidence before changing uncertain work to `ready`, `failed`, or `ready_to_integrate`.
5. Do not create a duplicate task solely because the worker identity was lost.
6. Regenerate `status.md` after reconciliation.

The ledger records managerial truth; Git and test artifacts provide product-work evidence. Reconcile them instead of trusting either blindly.
