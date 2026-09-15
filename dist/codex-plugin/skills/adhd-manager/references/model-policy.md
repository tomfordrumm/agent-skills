# Model policy

Choose a model profile and reasoning effort for every worker dispatch. Minimize total token use across the managed objective while keeping a realistic chance of finishing each task in one sound attempt. A cheap worker that predictably needs a retry is not a saving.

## Runtime discovery

Before the first dispatch, inspect the current subagent spawn tool metadata:

1. List the model overrides it accepts now.
2. List the reasoning-effort values accepted for each model.
3. Read any runtime descriptions that identify a model as fast, balanced, or frontier.
4. Treat this runtime metadata as authoritative for dispatch. Do not attempt a model or effort merely because documentation names it.
5. Use `inherit` in records when overrides are unavailable or deliberate inheritance is the best choice. Omit the corresponding spawn argument; `inherit` is a ledger value, not a model ID or effort to pass to the tool.

Build a session-local capability map from runtime descriptions, not model-name ordering. Do not persist a catalog or probe unavailable models.

| Profile | Resolve from current runtime metadata |
|---|---|
| `fast` | Fast or economical model suitable for objectively verifiable, bounded work |
| `balanced` | Everyday coding model suitable for the task's implementation scope |
| `frontier` | Most capable available model described as suitable for complex or demanding work |

Do not pin a family as the permanent primary or fallback. Use inheritance when it fits or when overrides are unavailable. If the role is unclear, use a known available fit; ask only when the uncertainty materially affects the task.

## Budget modes

Select one budget mode for the managed session. On resume, recover the latest recorded mode from `decisions.md`. Use `balanced` when the user has not selected another mode. Do not interrupt the user to confirm the default.

| Mode | Policy |
|---|---|
| `balanced` | Use the lowest profile and effort likely to complete the task in one sound attempt. Spend more when a retry would probably cost more than the stronger first attempt. |
| `cost-sensitive` | Prefer `fast` for reversible, bounded work and `balanced` for broader work. Preserve the verification requirements below. Queue work or surface the constraint when the user's cap cannot support a responsible attempt. |
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
| A change to security boundaries, payment rules, sensitive-data handling, or destructive behavior with broad impact or difficult verification | `frontier` | `high`, escalating to `xhigh` when uncertainty warrants it |

Raise the baseline only for evidence such as contradictory findings, broad contract impact, weak verification, or a failed sound attempt. Task priority or a security-related filename alone does not justify a stronger model. A copy edit on a login screen does not change authentication. A permission enforcement change does, and requires explicit checks of allowed and denied behavior.

For `cost-sensitive`, move reversible tasks down by at most one profile or one effort level. Do not reduce required authorization, isolation, rollback, or behavioral verification. For `quality-first`, move ambiguous or broad tasks up by one effort level or one profile. Keep mechanical tasks on `fast` unless the evidence itself is difficult to interpret.

## Dispatch selection

Use the baseline above as a starting point, then adjust for uncertainty, verification strength, and prior attempts. Resolve the profile and effort from current runtime metadata; request only supported values. Prefer a stronger first attempt when known retry risk outweighs its cost.

Use `max` or `ultra` only when available and difficult work or a failed sound attempt warrants the extra effort. Record the reason for these settings or a departure from the selected budget mode in `decisions.md`.

Record `worker.model` and `worker.reasoning_effort` before dispatch. Use `inherit` when inheritance is selected, omitting the corresponding spawn arguments.

Use `fork_turns: "none"` with a compact self-contained work order by default. A bounded fork may be useful when recent task-local context is shorter than restating it. Full-history forks must inherit when the runtime requires it. Send only evidence and constraints needed for the accepted task revision.

## Retry and escalation

Do not rerun the same work order with the same model and effort unless new evidence explains why the outcome should differ.

- If the model profile fits but the attempt lacked depth, raise effort by one supported level.
- If the task exceeded the model's role or scope, raise the model profile and keep effort stable when possible.
- If the work order was vague or stale, repair the order before spending more tokens.
- After two failed sound attempts, stop automatic escalation. Revise the task, split it, or report the blocker unless the user has explicitly authorized continued quality-first work.

Preserve useful evidence from every attempt. Do not ask a replacement worker to rediscover facts already established.

## Fallbacks and verification

Resolve fallbacks by the runtime-described role and supported effort. Do not select an older named model from a static list. Use inheritance when it is a responsible fit.

Model size and reasoning effort are not safety guarantees. Preserve checks for changed trust boundaries, ownership, payments, privacy, and destructive behavior regardless of the selected model. Prefer independent review when the impact or weak evidence warrants it. If available models or access cannot support a responsible attempt, explain the concrete limitation and continue unaffected work.

When changing a previously effective model or lowering effort, compare outcomes on representative requests with the same acceptance checks before adopting the cheaper setting as the new baseline. Record task completion, retries, user interventions, latency, and token usage when exposed. Do not infer savings from effort labels or claim usage numbers that the runtime does not report.

## User overrides

Honor an explicit required model, budget mode, quality preference, or reasoning cap when the runtime supports it. A required model overrides the profile resolver, not the task's safety and verification requirements.

If a user constraint makes a responsible attempt implausible, explain the mismatch and ask for the smallest necessary decision while independent work continues.
