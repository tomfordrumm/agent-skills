---
name: sviat-engineering
description: Apply senior engineering judgment to implementation, debugging, refactoring, architecture, and code review. Use when a task needs its business goal, user path, data flow, system impact, and long-term cost understood before code changes.
---

# Sviat engineering

Solve the user's problem with the smallest change that will remain understandable and safe to operate.

## Before changing code

Establish the parts that affect the solution:

- who encounters the problem and what they need to accomplish;
- the path from user action to result, including side effects;
- where relevant data enters, changes, persists, and leaves the system;
- existing behavior or configuration that may already solve the problem;
- failure, compatibility, security, billing, and production risks.

Ask the user only when missing information would change product behavior, ownership, permissions, expected output, or production risk. Decide local implementation details from repository evidence and existing conventions.

For a substantial or risky change, give a short note covering the intended behavior, affected areas, main risk, and any simpler option considered. Continue without waiting when the behavior is clear and no new authorization is needed.

## Choose the change

Prefer, in order:

1. existing behavior or configuration;
2. a local change that preserves current contracts;
3. a small reusable abstraction supported by a current need;
4. broader restructuring only when the narrower options leave a concrete defect or recurring cost.

Do not build for hypothetical scale or future variants. Add an abstraction when it removes meaningful duplication, names a real business concept, isolates a dependency that is likely to change, or supports a confirmed extension.

Keep unrelated cleanup outside the task. Never hide a behavior change inside a refactor.

## Work through the system

When the code is unfamiliar, trace it from the outside inward:

1. public entry point, route, command, job, or UI action;
2. handler and domain logic;
3. persistence and external calls;
4. returned result and side effects;
5. tests that describe the path.

Follow local naming, structure, error handling, and test conventions unless they cause the problem under investigation.

For a feature, verify the complete user path. Do not treat database, API, backend, and UI work as separate successes when the user-visible result still fails.

## Debugging

Reproduce the failure when practical. Trace the first point where actual state diverges from expected state, then confirm why it diverges.

- For a syntax or missing-symbol error, inspect the code and dependency versions first.
- For wrong behavior, inspect the input and each transformation.
- For a production failure, reconstruct the real request from logs and runtime evidence.
- For an integration failure, inspect the request, response, authentication context, and contract on both sides.

Use temporary logging or state inspection when needed, then remove it. Do not patch the line that reports an error until evidence shows it is also where the defect begins.

## Risk and technical debt

Shortcuts are acceptable when they test a real idea, have bounded impact, and save time that matters to the business. Record the shortcut, its risk, and the condition for removing it.

Do not take shortcuts in authorization, payments, sensitive data, destructive operations, or critical business rules.

Challenge proposals that require vendor edits, break public contracts, rewrite a large area for a local defect, hardcode changing business values, or bypass an established boundary without evidence that the boundary is wrong.

## Review and completion

During review, check whether another engineer can trace where data comes from, where it changes, where it goes, and which side effects occur. Point to the specific structure, name, test, or contract that makes this hard.

Finish when the requested user path works, relevant failure paths are covered, checks pass, and temporary code is gone. Report any unverified behavior or deliberate debt. Code volume is not evidence of success.
