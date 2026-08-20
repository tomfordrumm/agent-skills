# Worker contracts

Use current work orders so workers receive accepted intent instead of the user's raw message stream.

## Contents

- Universal contract
- Discovery and diagnosis orders
- Implementation order
- Steering
- Result contract
- Verification and integration
- Worktree policy

## Universal contract

Every work order must state:

```text
Task and revision
Role and execution mode
Selected model and reasoning effort
Objective
Current accepted requirements
Acceptance criteria or deliverable
Owned scope and likely files
Explicit exclusions
Dependencies and inputs
Active assumptions
Required verification
Result format
```

Tell every worker:

- Work only on the specified task revision and scope.
- Preserve unrelated user changes.
- Inspect project instructions before acting.
- Report newly discovered conflicts, scope expansion, or unsafe ambiguity instead of silently deciding beyond the order.
- Do not delegate user communication; report to the orchestrator.
- Return evidence, not only a success claim.

Prefer a self-contained work order with no inherited chat history when selecting a model override. Use a bounded context fork only when the worker genuinely needs recent task-local turns. Do not request a model override with a full-history fork when the runtime requires full-history forks to inherit the parent model.

## Discovery and diagnosis orders

Use a read-only order:

```text
Investigate TASK-005 revision 1 in DISCOVERY mode.

Objective:
Define the smallest useful MCP server over the existing service API.

Questions to answer:
- Which API operations map to useful MCP tools?
- How should existing access keys authenticate it?
- Which modules and public contracts would implementation touch?

Constraints:
- Do not edit product files.
- Do not design direct database access.
- Distinguish evidence, inference, and recommendation.

Return:
- evidence with file paths or command output;
- recommended boundary and alternatives rejected;
- dependencies, conflicts, risks, and open questions;
- implementation-ready work order and verification plan.
```

Diagnosis may include reproducing and running diagnostics when safe, but it must not repair the product unless the order explicitly authorizes a subsequent implementation phase in an isolated worktree.

## Implementation order

Use this form:

```text
Implement TASK-019 revision 2 in the assigned worktree.

Runtime:
- model: gpt-5.6-terra
- reasoning effort: high

Objective:
Fix the mobile placement of the registration submit button.

Accepted requirements:
- Keep the button full-width.
- Do not use sticky positioning.
- Preserve the desktop layout.

Owned scope:
- registration-ui
- registration page and directly related styles

Do not:
- refactor the whole form;
- change validation or authentication behavior;
- edit global navigation.

Dependencies and assumptions:
- none

Verification:
- verify 320px, 375px, and desktop layouts;
- run relevant frontend tests.

Return:
- task ID and revision;
- summary and changed files;
- commands and exact results;
- risks or follow-up work;
- commit SHA on the assigned task branch.
```

Give a code-writing worker a task branch and absolute worktree path. Instruct it to commit only its scoped product changes. Manager-state files belong to the orchestrator and must not be committed from worker worktrees.

## Steering

Update the ledger before steering. Send both the delta and the refreshed task state:

```text
TASK-001 is now revision 3; revision 2 is stale.

Delta:
- Add permission reduction for existing keys.
- Existing keys still cannot gain permissions.

Current requirements:
- list keys;
- revoke a key;
- reduce permissions.

Re-evaluate work already performed. Confirm whether the delta invalidates your approach,
tests, or changed files before continuing.
```

Interrupt instead of steering when the new revision removes the worker's objective, revokes its scope ownership, introduces a safety constraint already violated, or makes continued work meaningfully wasteful.

## Result contract

Require structured results:

```text
Task: TASK-NNN
Revision: N
Outcome: completed | partial | blocked | failed
Requested model and reasoning effort:
Summary:
Changed files or inspected evidence:
Verification commands and results:
Commit:
Assumptions made:
New risks or discovered tasks:
Scope deviations:
```

The orchestrator must reconcile newly discovered tasks without silently adding them to the worker's scope.

## Verification and integration

Use an independent verifier when risk, breadth, or weak worker evidence warrants it. The verifier receives acceptance criteria and artifacts, not the implementer's confidence or desired verdict.

Give the integrator:

- target integration branch and worktree;
- base commit and ordered task commits;
- accepted revision and acceptance criteria for every task;
- known dependencies, ownership boundaries, and active assumptions;
- required focused and cross-task checks;
- instructions to preserve unrelated changes and stop on unexplained scope.

Require the integrator to:

1. confirm each result commit belongs to the accepted revision;
2. inspect diffs before combining them;
3. integrate in dependency order;
4. resolve only bounded, well-understood conflicts;
5. create a repair task for semantic conflicts or stale requirements;
6. run focused checks and the appropriate broader suite;
7. return the final commit, exact test results, residual risks, and rejected or deferred commits.

Do not mark tasks done merely because commits cherry-picked cleanly.

## Worktree policy

- Inspect the base repository and current branch before creating worktrees.
- Use explicit task branches such as `codex/adhd/task-019-r2` and an integration branch such as `codex/adhd/integration-001`.
- Place worktrees in a narrow, project-specific temporary or sibling directory, never a broad system path.
- Record branch, absolute worktree path, and base commit in the task before code work starts.
- Never delete a worktree with uncommitted or unintegrated changes.
- Do not reuse a worktree concurrently across tasks.
- Clean up only after integration evidence exists and the operation is safe and authorized.
- If the repository is not Git-backed or worktrees cannot be created, block code-writing tasks and explain the constraint. Do not silently fall back to shared concurrent editing.
