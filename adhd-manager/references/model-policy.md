# Model policy

Choose a worker model and reasoning effort for each dispatch. Optimize the managed project for reliable completion, not for using the strongest model everywhere.

## Runtime discovery

Before the first dispatch, inspect the current subagent spawn tool metadata:

1. List the model overrides it actually accepts.
2. List the reasoning-effort values accepted for each model.
3. Treat this runtime list as authoritative for what can be spawned now.
4. Never attempt a documented model that the current tool does not expose.
5. Use `inherit` when no override is available or deliberate inheritance is the best choice.

Model catalogs change. Apply the named defaults below only when those models are available; otherwise use the fallback rules.

## Balanced default policy

| Worker task | Preferred selection | Escalate when |
|---|---|---|
| Narrow read-only discovery | `gpt-5.6-terra` / `medium` | The evidence spans many subsystems or remains contradictory |
| Ordinary diagnosis | `gpt-5.6-terra` / `high` | The bug is cross-system, intermittent, or survives one sound attempt |
| Routine implementation | `gpt-5.6-terra` / `high` | It changes architecture, shared contracts, or a broad critical path |
| Complex refactor or architecture | `gpt-5.6-sol` / `high` | The design remains underdetermined or verification is unusually difficult |
| Security, authentication, authorization, payments, privacy, or migrations | `gpt-5.6-sol` / `xhigh` | Use `max` only for the hardest unresolved quality-first case |
| Independent verification | `gpt-5.6-terra` / `high` | The change is high-risk, broad, or earlier evidence conflicts |
| Multi-batch integration | `gpt-5.6-sol` / `high` | Semantic conflicts or stale revisions require deeper repair reasoning |
| Difficult repair or merge conflict | `gpt-5.6-sol` / `xhigh` | Use `max` after a well-scoped `xhigh` attempt is insufficient |

Use `medium` as the lowest normal starting point for tool-using project work. Use `low` only for tightly bounded, latency-sensitive mechanical inspection. Reserve `max` for exceptional tasks where quality dominates latency and cost; do not select it merely because a task is important.

## Selection procedure

For each ready task:

1. Determine whether the task is read-only, routine code work, complex reasoning, high-risk domain work, independent verification, or integration.
2. Evaluate scope breadth, contract impact, reversibility, safety risk, uncertainty, and prior failed attempts.
3. Select the lowest tier and effort that responsibly covers those factors using the balanced table.
4. Confirm that both values are accepted by the current spawn tool.
5. Record `worker.model` and `worker.reasoning_effort` before dispatch.
6. Use `fork_turns: "none"` for a self-contained work order by default. Use a small positive bounded fork only when recent task-local context is required. A full-history fork must inherit the parent model when the runtime disallows overrides.

Do not change a running worker's model for a minor steering update. If new evidence materially raises complexity or risk, preserve its work, interrupt only when necessary, and dispatch a replacement or repair worker with the stronger selection.

## Fallbacks

If the preferred model is unavailable:

- Replace Sol with the strongest available coding/reasoning model.
- Replace Terra with the available balanced model; if no clear balanced tier exists, inherit the orchestrator model.
- Choose the nearest supported reasoning effort without exceeding the intended effort unless risk justifies escalation.
- Record the fallback and reason in `decisions.md`.
- Tell the user when the fallback materially changes expected quality, latency, cost, or the ability to execute safely.

Do not infer that a model is available because it appears in public documentation. Do not silently downgrade security-, payment-, privacy-, authentication-, or migration-sensitive work to a weak or unknown model; queue it or surface the constraint when no responsible fallback exists.

## User overrides

Honor explicit user preferences such as quality-first, cost-sensitive, a required model, or a reasoning cap when the runtime supports them. Treat the policy above as the default, not as permission to override the user.

If a user constraint makes a task unsafe or implausible, explain the mismatch and ask only for the smallest necessary decision while independent work continues.
