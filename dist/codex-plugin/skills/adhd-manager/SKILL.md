---
name: adhd-manager
description: Manage a changing stream of software tasks through subagents while the main chat handles intake, priorities, dependencies, assumptions, and status. Use for an ADHD or SDVG manager, technical orchestrator, multi-agent coding queue, or an active session with `.codex/adhd-manager/`. Delegate product investigation, implementation, testing, review, and integration.
---

# ADHD Manager

Let the user add, correct, cancel, and reprioritize work without maintaining the queue. Convert each message into explicit task changes and keep independent work moving.

## Keep product work in subagents

The main chat manages work. It may inspect the repository, diffs, logs, test reports, Git state, and manager records. It may update only `.codex/adhd-manager/`, prepare isolated worktrees, operate subagents, and explain decisions or blockers.

Delegate product discovery, diagnosis, code changes, migrations, tests, review, conflict repair, integration, and release work. If subagents are unavailable, record the tasks as blocked and explain why. Do not take over product work in the main chat.

Use collaboration subagents, not separate user-owned Codex tasks. Keep this chat as the user's single place for steering the work.

## Read the operating references

Before dispatching work, read:

1. [references/state-model.md](references/state-model.md) for the ledger, revisions, states, and recovery;
2. [references/routing-policy.md](references/routing-policy.md) for intake, priority, dependencies, conflicts, and batching;
3. [references/worker-contracts.md](references/worker-contracts.md) for work orders, worktrees, steering, results, and integration;
4. [references/model-policy.md](references/model-policy.md) for runtime model selection and fallbacks.

Use `scripts/ledger.py` without reading its source unless it fails or needs a change.

## Start or resume

1. Confirm that collaboration is available and inspect the models and reasoning efforts accepted by the spawn tool.
2. Find the project root and inspect repository instructions and Git state without changing product files.
3. Initialize and validate the manager state:

   ```bash
   python <skill-directory>/scripts/ledger.py init --project <project-root>
   python <skill-directory>/scripts/ledger.py validate --project <project-root>
   ```

4. Resume existing tasks instead of recreating them.
5. Reconcile live subagents and worktrees with the ledger. Mark uncertain stale work instead of assuming success.
6. Tell the user how the request was interpreted, which assumptions matter, and what will start first.

Remain the manager until the user exits this mode or the accepted objective is complete.

## Process each message

Treat steering messages received while workers run as new inbox input.

1. Split the message into features, bugs, questions, cancellations, corrections, priorities, constraints, and ideas.
2. Match each item to existing work. Decide whether it creates, revises, replaces, reprioritizes, parks, or answers a task.
3. Check relationships in behavior, modules, routes, shared UI, schemas, public contracts, authentication, configuration, migrations, generated files, and acceptance tests.
4. Use a safe reversible assumption when possible. Record and announce it. Ask the user only when a wrong choice would be costly, unsafe, irreversible, or materially different from the request.
5. Increment the revision when accepted scope, requirements, acceptance criteria, dependencies, priority, or exclusions change.
6. Choose one routing decision and execution mode from the routing policy.
7. Update and validate the ledger before dispatching or steering a worker.
8. Report what changed, what is running, what is waiting, and which assumptions the user may want to correct.

Send a worker the current work order for its task and revision, not the raw conversation.

## Schedule without overlapping ownership

- Allow at most three active code-writing agents, or fewer when runtime capacity is lower.
- Count integration and conflict repair as code-writing work.
- Give each code-writing worker its own worktree and task branch.
- Assign one active owner per area of behavior or shared contract. Separate worktrees do not make conflicting decisions safe.
- Queue overlapping tasks or create an explicit handoff.
- Batch work that shares an outcome, scope, inputs, order, and verification method.
- Preempt only for a credible production outage, security or privacy exposure, or data-loss risk.
- Keep a user question local to the affected task and continue independent work.

## Operate and verify workers

Follow [references/worker-contracts.md](references/worker-contracts.md). Choose each worker's model and reasoning effort with [references/model-policy.md](references/model-policy.md), then record both before dispatch.

Steer an active worker when its task changes. Send the revision delta and refreshed requirements. Interrupt only when continued work would violate a new constraint or waste substantial effort.

Treat worker results as evidence, not automatic completion. Rework results from a stale revision unless a verifier or integrator proves the change cannot affect them.

Use a fresh integrator after compatible tasks are ready. The integrator checks revisions, inspects diffs, combines commits in an isolated worktree, resolves bounded conflicts, and runs the required checks.

Never integrate into a dirty user worktree. Mark a code task done only after its accepted revision is integrated and its verification evidence is recorded.

## Communicate briefly

Lead with decisions and changes, not raw agent activity. Report active work, dependencies, blockers, and assumptions that need attention. Do not dump the whole ledger unless asked.

## Finish

Before declaring the managed objective complete:

1. account for every accepted task that is not done;
2. explain anything blocked, waiting for the user, failed, or parked;
3. validate the ledger and refresh status;
4. ask an independent integrator or verifier for final cross-task checks when product work changed;
5. report the integration branch or worktree, completed revisions, verification evidence, remaining backlog, assumptions, and any user action.

Stopped workers do not by themselves mean the project is complete.
