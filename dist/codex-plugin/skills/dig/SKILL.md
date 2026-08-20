---
name: dig
description: Investigate bugs, features, or system behavior without making changes. Use when the user asks to investigate, debug, analyze, or understand something before editing it.
---

# Dig

Stay in investigation mode until the user ends it. Read files, inspect code, run read-only diagnostics, and ask focused questions. Do not edit files or run write operations.

If the investigation points to a change, explain the proposed change and its reason. Ask for permission before making it. Permission covers only that specific change.

## Investigation workflow

1. Establish the question, scope, and constraints.
2. Read the relevant files, logs, configuration, and command output.
3. Fill evidence gaps with targeted questions or read-only checks.
4. Separate confirmed facts from hypotheses and name the likely cause when evidence supports it.
5. Report what is known, what remains uncertain, and the next useful check.

## Leaving investigation mode

Leave this mode only when the user explicitly ends the investigation or authorizes a specific change. If the request is unclear, keep investigating rather than assuming permission to edit.
