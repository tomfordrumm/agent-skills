---
name: adhd-manager
description: Manage a changing software task queue with scoped subagents, dependencies, and durable status. Use when explicitly asked for an ADHD or SDVG manager or to resume that managed queue. Scale coordination to one bounded task or several independent tasks.
---

# ADHD Manager

Let the user add, correct, cancel, and reprioritize work without maintaining the queue. Keep this chat as the place for steering. Use collaboration subagents, not separate user-owned Codex tasks.

## Choose coordination depth

- **Bounded:** One cohesive outcome, one worker, one task branch for code. Keep diagnosis, implementation when authorized, and focused verification with that worker. A question about progress does not create another worker.
- **Managed:** Several independent outcomes or competing owners. Use the routing policy, exclusive scope ownership, and integration when branches must be combined.

Start bounded unless the accepted work needs a managed queue. These coordination choices are separate from the model budget modes. Preserve tasks and evidence when switching depth. Do not split one feature into discovery, implementation, testing, and integration agents merely to fill roles.

## Manager boundaries

The main chat may inspect evidence, answer questions supported by it, update manager records, prepare worktrees, and operate workers. Delegate product edits and substantial new product investigation. If collaboration is unavailable, continue local status and evidence explanations and mark only dependent worker tasks blocked; do not claim the whole objective is blocked when independent work remains.

An implementation request authorizes its necessary diagnosis and focused checks. A read-only request does not authorize repair. Carry accepted scope forward across steering messages without asking again for routine steps.

## Load relevant references

- Read [references/state-model.md](references/state-model.md) when initializing or recovering the queue, or when the state contract is unclear.
- Read [references/worker-contracts.md](references/worker-contracts.md) before the first worker dispatch. Apply only the sections needed for that worker's role.
- Read [references/model-policy.md](references/model-policy.md) before choosing the first worker's model; reuse the session capability map while runtime metadata is unchanged.
- Read [references/routing-policy.md](references/routing-policy.md) when multiple tasks need scheduling, ownership analysis, or a change of routing.

Use `scripts/ledger.py` without reading its source unless it fails or needs a change.

## Start or resume

Inspect project instructions and Git state. Initialize and validate records with:

```bash
python <skill-directory>/scripts/ledger.py init --project <project-root>
python <skill-directory>/scripts/ledger.py validate --project <project-root>
```

Resume existing tasks. Reconcile live workers, branches, and recorded revisions before treating stale work as complete. State the accepted outcome, coordination depth, and material assumptions. Use the balanced model budget unless the user selects another.

## Process steering

Match new intent to existing tasks before creating work. Record changed requirements, priorities, dependencies, exclusions, or cancellations and increment the affected revision. Update and validate the ledger before dispatching or steering a worker.

Send a compact current work order or revision delta with refreshed requirements. Reuse established evidence. Interrupt only when continued work violates new constraints or wastes substantial effort. Keep clarification local to the affected task and continue independent work.

Answer progress questions from the latest evidence. Do not launch workers or increment revisions for unchanged status requests.

## Ownership and integration

Give each code-writing worker an isolated worktree and task branch. Allow at most three active code-writing workers, or fewer when capacity is lower. One semantic area or shared contract has one active owner even across separate worktrees. Queue overlaps and batch work sharing one outcome and verification method.

For a single branch, the manager may inspect the diff, accepted revision, and worker verification and report that branch as the deliverable. Do not require a separate integrator merely to accept it. Record whether delivery means the verified branch or integration into a named target. If the user requested integration, that step remains required.

Use an integrator to combine multiple task branches or handle cross-task conflicts. An independent verifier is needed when explicitly requested or when risk, breadth, or weak evidence warrants it. One integrator can provide final cross-task verification; do not add another final reviewer without a distinct unresolved concern.

Never integrate into a dirty user worktree. Do not discard uncommitted or unintegrated changes. Check accepted-revision evidence before reusing stale results.

## Wait and finish

Prefer completion notifications or bounded event waits. Do not repeatedly fetch unchanged logs, diffs, or status. Recheck when work completes, requirements change, or evidence of failure appears.

Run required checks and repeat them only when a relevant change or unresolved concern invalidates prior evidence. Distinguish source checks, built artifacts, and deployed behavior. For any remaining required check, identify who can run it, the missing capability, and the expected result.

Before finishing, validate records and account for accepted tasks, including anything blocked, parked, or waiting. Report the delivered branch or integration target, completed revisions, verification evidence, and remaining gates. A stopped worker or clean cherry-pick does not prove acceptance.
