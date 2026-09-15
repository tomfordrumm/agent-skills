---
name: dig
description: Investigate a bug, feature, or system behavior without changing it. Use for diagnosis, explanation, or review before deciding on a change. Do not select for a request that already asks to find and fix a problem; diagnosis is part of that implementation.
---

# Dig

Investigate the requested question without editing product files or mutating live systems. Read relevant files and run diagnostics whose side effects fit the investigation. Do not add temporary instrumentation without authorization.

## Investigation workflow

1. Establish the question from the request and existing context.
2. Read relevant code, logs, configuration, and runtime evidence.
3. Use targeted checks to distinguish the plausible causes. Ask only when an unanswered question could change the conclusion or scope.
4. Separate confirmed facts from hypotheses. Report the cause when supported, its impact, and the smallest useful change or remaining check.

Stop investigating when the question is answered or further progress requires unavailable evidence. Do not broaden the audit merely because adjacent issues exist.

## Transition to implementation

An investigation request alone does not authorize changes. A later request to fix the problem authorizes the necessary edits and verification within that problem's scope. Follow it without requiring a separate exit command or approval for each file or step.

Carry forward the evidence and constraints already established. Ask again only when a proposed action needs new authorization, such as a material scope expansion or an external action not covered by the request. Do not turn this skill into a persistent restriction on unrelated later tasks.
