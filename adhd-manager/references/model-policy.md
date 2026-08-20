# Model policy

Choose a model profile and reasoning effort for every worker dispatch. Minimize total token use across the managed objective while keeping a realistic chance of finishing each task in one sound attempt. A cheap worker that predictably needs a retry is not a saving.

## Runtime discovery

Before the first dispatch, inspect the current subagent spawn tool metadata:

1. List the model overrides it accepts now.
2. List the reasoning-effort values accepted for each model.
3. Read any runtime descriptions that identify a model as fast, balanced, or frontier.
4. Treat this runtime metadata as authoritative for dispatch. Do not attempt a model or effort merely because documentation names it.
5. Use `inherit` when overrides are unavailable or deliberate inheritance is the best choice.

Build a small session-local capability map. Do not persist a catalog that will become stale. The current model families may provide these role hints when the runtime exposes them:

| Profile | Current primary | Compatibility fallback |
|---|---|---|
| `fast` | `gpt-5.6-luna` | Another runtime-described fast or economical coding model |
| `balanced` | `gpt-5.6-terra` | `gpt-5.4`, then another runtime-described everyday coding model |
| `frontier` | `gpt-5.6-sol` | `gpt-5.5`, then another runtime-described frontier coding model |

These names are hints, not an availability claim. Classify a newly exposed model from the spawn tool's description. If its role is unclear, do not guess from its name. Use `inherit`, a known available model, or ask only when the choice materially affects the task.

## Budget modes

Select one budget mode for the managed session. On resume, recover the latest recorded mode from `decisions.md`. Use `balanced` when the user has not selected another mode. Do not interrupt the user to confirm the default.

| Mode | Policy |
|---|---|
| `balanced` | Use the lowest profile and effort likely to complete the task in one sound attempt. Spend more when a retry would probably cost more than the stronger first attempt. |
| `cost-sensitive` | Prefer `fast` for reversible, bounded work and `balanced` for broader work. Keep the safety floors below. Queue work or surface the constraint when the user's cap cannot support a responsible attempt. |
| `quality-first` | Raise effort for ambiguous, broad, or hard-to-verify work and move to `frontier` earlier. Do not spend frontier tokens on mechanical work that a smaller model can verify objectively. |

Record a user-selected non-default mode or a later mode change in `decisions.md`. Apply a mode change to future dispatches. Do not replace a running worker solely to apply the new mode.

## Balanced baseline

Choose the model profile and effort independently:

| Work characteristics | Model profile | Starting effort |
|---|---|---|
| File lookup, inventory, formatting, status extraction, or another mechanical read-only task | `fast` | `low` |
| Bounded discovery, focused test execution, small reversible edit, or evidence collection with clear success criteria | `fast` | `medium` |
| Routine diagnosis, implementation, or independent verification within one understood area | `balanced` | `medium` |
| Multi-file work, uncertain diagnosis, shared-contract review, or bounded integration | `balanced` | `high` |
| Architecture, semantic merge conflicts, cross-system diagnosis, or a broad critical path | `frontier` | `high` |
| Security, authentication, authorization, payments, privacy, destructive migrations, or credible data-loss risk | `frontier` | `xhigh` |

Raise the baseline only for evidence such as contradictory findings, broad contract impact, weak verification, or a failed sound attempt. Task priority alone does not justify a stronger model.

For `cost-sensitive`, move reversible tasks down by at most one profile or one effort level. Do not move below the high-risk floor. For `quality-first`, move ambiguous or broad tasks up by one effort level or one profile. Keep mechanical tasks on `fast` unless the evidence itself is difficult to interpret.

## Reasoning effort

Use the effort ladder exposed by the runtime. A common order is:

```text
low < medium < high < xhigh < max < ultra
```

Not every model exposes every value. Request only a supported value.

- Use `low` for mechanical work with an objective check.
- Use `medium` as the normal starting point for bounded tool-using work.
- Use `high` when the task requires exploration across files or contracts.
- Use `xhigh` for high-risk work or genuinely difficult reasoning.
- Use `max` only after `xhigh` was insufficient or the hardest quality-first task has a concrete reason for it.
- Use `ultra` only when the runtime exposes it and the user explicitly prioritizes maximum quality, or when a documented failed attempt shows that the extra spend is warranted.

Record the reason for `max`, `ultra`, or any departure from the selected budget mode in `decisions.md`.

## Selection procedure

For each ready task:

1. Identify the task's scope, reversibility, contract impact, safety risk, uncertainty, verification strength, and prior attempts.
2. Choose the session budget mode's baseline profile and effort.
3. Estimate retry risk. Prefer the next stronger first attempt when the cheaper choice is likely to fail for a known reason.
4. Resolve the profile to an available runtime model.
5. Choose the intended effort, then clamp it to a value that model accepts. Do not exceed the intended effort merely because a higher value exists.
6. Record the requested `worker.model` and `worker.reasoning_effort` before dispatch.
7. Use `fork_turns: "none"` with a compact self-contained work order by default. Use a small bounded fork only when recent task-local context would be more compact than restating it. Full-history forks must inherit when the runtime requires it.

Do not send repository-wide history, the raw user conversation, or unrelated ledger entries to a worker. Include enough evidence and constraints to avoid rediscovery, but keep the work order local to the accepted task revision.

## Retry and escalation

Do not rerun the same work order with the same model and effort unless new evidence explains why the outcome should differ.

- If the model profile fits but the attempt lacked depth, raise effort by one supported level.
- If the task exceeded the model's role or scope, raise the model profile and keep effort stable when possible.
- If the work order was vague or stale, repair the order before spending more tokens.
- After two failed sound attempts, stop automatic escalation. Revise the task, split it, or report the blocker unless the user has explicitly authorized continued quality-first work.

Preserve useful evidence from every attempt. Do not ask a replacement worker to rediscover facts already established.

## Fallbacks and safety floors

Resolve fallbacks by role, not by model-name ordering:

- Replace `frontier` with an available frontier coding model such as `gpt-5.5`.
- Replace `balanced` with an available everyday coding model such as `gpt-5.4`.
- Replace `fast` with another runtime-described fast or economical model.
- Use `inherit` when no responsible role match exists and inheritance satisfies the task.

For high-risk work, do not silently fall back below `frontier` and `xhigh`. Queue the task or surface the constraint when the runtime or user budget cannot support that floor. For lower-risk work, use the nearest available role and record a fallback only when it materially changes expected quality, latency, cost, or retry risk.

## User overrides

Honor an explicit required model, budget mode, quality preference, or reasoning cap when the runtime supports it. A required model overrides the profile resolver, not the task's safety and verification requirements.

If a user constraint makes a responsible attempt implausible, explain the mismatch and ask for the smallest necessary decision while independent work continues.
