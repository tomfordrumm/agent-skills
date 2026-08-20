# Routing policy

Apply this policy to every atomic intent after reconciling it with the current ledger.

## Contents

- Routing decisions
- Execution modes
- Relationship and conflict analysis
- Batching and ownership
- Priority and preemption
- Scheduling loop
- Worked scenario

## Routing decisions

Choose exactly one primary routing decision:

| Decision | Use when | Required action |
|---|---|---|
| `STEER` | New input changes an active task | Increment revision, update the task, send the delta and current requirements to its worker |
| `SPAWN` | Work is ready, independent, non-conflicting, and a slot exists | Assign scope, prepare a worktree if writing code, and dispatch the current work order |
| `QUEUE` | Work is accepted but waiting for capacity, evidence, dependency, or ownership | Record the reason and launch condition |
| `SUPERSEDE` | New input cancels or replaces accepted work | Preserve history, mark the old task or requirement superseded, stop invalid work if necessary |
| `PARK` | The idea is valid backlog but intentionally outside current focus | Record it with enough context to recover later; do not spend a worker slot |
| `CLARIFY` | No safe reversible interpretation exists | Ask one focused question for that task; continue independent work |

`STEER` is not a casual message to a worker. Update the ledger first, then send a precise revision delta. `QUEUE` is not neglect: always record why it waits and what will unblock it.

## Execution modes

Choose execution mode independently of routing:

| Mode | Deliverable |
|---|---|
| `DISCOVERY` | Evidence, affected scope, risks, options, and an implementation-ready recommendation; no product edits |
| `DIAGNOSIS` | Reproduction, root cause, impact, and a bounded repair order; do not implement unless the work order explicitly includes a later implementation phase |
| `IMPLEMENTATION` | Product changes and focused verification in an isolated worktree |
| `VERIFICATION` | Independent review or test evidence against acceptance criteria; change product code only through a separate repair task |
| `INTEGRATION` | Revision check, commit integration, conflict handling, cross-task verification, and final branch evidence |

Examples:

```text
SPAWN + DISCOVERY
STEER + IMPLEMENTATION
QUEUE + INTEGRATION
CLARIFY + DIAGNOSIS
```

## Relationship and conflict analysis

Check more than likely files. Two tasks conflict or depend on each other when they share or alter:

- product behavior or an invariant;
- modules, packages, generated code, or build configuration;
- routes, global navigation, layouts, or shared components;
- database schema, migrations, fixtures, or serialization;
- public APIs, events, types, or authentication and authorization contracts;
- external-provider configuration or environment variables;
- deployment, release, or observability behavior;
- the same acceptance test or user flow.

Create a dependency when one task needs the other task's accepted contract or output. Create a conflict when simultaneous work could produce incompatible decisions or overlapping edits. A task can have both.

When scope is uncertain, use a read-only discovery worker before granting write ownership.

## Batching and ownership

Batch intents when they share all or most of:

- one product outcome;
- one owner for the affected behavior or contract;
- compatible implementation order;
- the same inputs and assumptions;
- one verification strategy.

Split work when it has different risk, root-cause uncertainty, ownership, verification, or independent delivery value.

Grant one active owner per semantic area. Represent cross-owner needs as explicit handoff tasks. For example, an access-key worker may build the access-key screen while a navigation worker owns the global menu; adding the new screen to navigation becomes a queued integration or handoff task.

Do not treat separate worktrees as permission to make conflicting decisions concurrently.

## Priority and preemption

Use these defaults:

```text
urgent: credible active production outage, security exposure, privacy breach, or data loss
high: user-blocking bug or clear regression
normal: accepted feature or ordinary defect
low: polish, speculative improvement, or distant backlog
```

Newness and user excitement do not raise priority by themselves.

Preempt a worker only when:

1. the incoming task is urgent;
2. continuing creates meaningful safety risk or avoidable waste;
3. the interrupted state can be preserved or cleanly abandoned;
4. the user is told what changed and what is deferred.

Prefer the next free slot for ordinary regressions. Fold cosmetic issues into the compatible UI batch.

## Scheduling loop

After every ledger update or worker event:

1. Recompute dependencies and conflicts.
2. Release ownership from terminal or explicitly handed-off tasks.
3. Rank ready work by safety, user impact, dependency unblocking, age, and batching efficiency.
4. Reserve slots for integrators when completed code is waiting; unfinished integration is work in progress.
5. Spawn only tasks with an available slot and exclusive scope.
6. If nothing can start, report the smallest real blocker rather than asking broad questions.
7. Validate state and sync the status snapshot.

## Worked scenario

Given a stream about access keys, Stripe, a broken header, a shorter menu, reduced key permissions, an MCP server, and broken email layout:

- `Access keys` -> `SPAWN + IMPLEMENTATION`.
- `Stripe with future providers` -> `SPAWN + DISCOVERY`; assume a minimal provider adapter, not a speculative universal framework.
- `Broken header` -> `SPAWN + DIAGNOSIS`, then implementation when the cause is confirmed.
- `Shorter menu` -> `STEER` the header/navigation owner; group secondary items without deleting functionality unless corrected.
- `Reduce key permissions` -> `STEER` the access-key task and increment its revision; default to reduction only.
- `MCP server` -> `SPAWN + DISCOVERY`; depend on the access-key authentication contract and prefer an adapter over the existing API, not direct database access.
- `Broken email layout` -> high-priority diagnosis in the next non-conflicting slot; inspect the latest changed template first.

The access-key worker must not edit global navigation while another worker owns it. Queue that connection as a handoff or integration task.
