---
name: sviat-engineering
description: Evaluate engineering tradeoffs for consequential behavior changes, cross-system diagnosis, or architecture reviews. Use when contracts, ownership, or operational risks shape the solution; skip routine local edits.
---

# Sviat engineering

Solve the user's problem with the smallest change that remains understandable and safe to operate.

## Decisions that matter

Establish the user-visible outcome and the affected data, contracts, ownership, and side effects. Inspect only the paths needed to resolve the task. Use existing behavior or configuration when it already solves the problem.

Prefer a local change that preserves contracts. Add an abstraction when it removes meaningful duplication, names a real business concept, isolates a changing dependency, or supports a confirmed extension. Broader restructuring needs a concrete defect or recurring cost that narrower options cannot address.

Ask only when missing information changes product behavior, ownership, permissions, expected output, or production risk. Decide local implementation details from repository evidence. For substantial or risky changes, briefly explain the intended behavior, affected areas, main risk, and any useful simpler option. Continue within established authorization.

Keep unrelated cleanup outside the task. Never hide a behavior change inside a refactor. Challenge vendor edits, broken public contracts, hardcoded changing business values, and bypassed boundaries unless evidence justifies them.

## Evidence and tradeoffs

For diagnosis, distinguish the point where an error is reported from the cause. Use evidence from the actual failing path; a local reproduction does not establish production behavior. Remove temporary instrumentation after use.

Shortcuts may be appropriate for a bounded experiment. Record the tradeoff and condition for removing it. Do not compromise authorization, payments, sensitive data, destructive operations, or critical business rules.

During review, identify specific structures, names, tests, or contracts that obscure data flow and side effects. Tie recommendations to the resulting maintenance or operational cost.

## Completion

Verify the requested user path and material failure paths with proportionate checks. Add regression tests for distinct failures, not tests that repeat a reversible, low-impact implementation. Repeat or broaden successful checks only when changed code, a failure, or unresolved uncertainty invalidates the evidence. Honor requested independent review; otherwise use it when risk, breadth, or weak evidence warrants it.

Distinguish source checks, the built application, and the published release. A passing build or active deployment does not prove the user path works in that artifact.

Complete all authorized work and runnable required checks before returning. Reuse user-confirmed checks unless a relevant change invalidates them. For unavailable required evidence, report the exact remaining check, who can perform it, missing access or capability, and expected result. Do not assign a runnable script to the user or claim full acceptance while required evidence is missing.
