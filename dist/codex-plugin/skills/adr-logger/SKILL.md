---
name: adr-logger
description: Record significant architecture, contract, operational, or technical-debt decisions in the project's existing decision log. Use when asked to document decisions or when the project requires ADRs. Log every task only when explicitly required.
---

# ADR logger

Record decisions a future maintainer needs to understand: a changed architecture or public contract, an operational tradeoff, or accepted technical debt with a condition for revisiting it. Routine implementation, status updates, and investigations with no accepted decision do not need an ADR.

## Choose the destination

Inspect project instructions and existing records first. Use the existing ADR convention or decision log, including an Easy PRD `DECISIONS.md` or decisions section. Do not create a second owner for the same decision.

If a significant decision needs recording and no convention exists, use `ADR/adr_yyyy_mm_dd.md` with the local date. Preserve existing content. Append a new decision or update a proposal's status without rewriting the history of an accepted decision.

Recording a decision does not authorize implementation. In a read-only task, return a proposed entry unless the user also requested a documentation update.

## Entry contents

Use the existing format. Otherwise include:

- Local date/time and a concrete title.
- Context and the constraint that required a choice.
- Decision, its source, and whether it is proposed or accepted.
- Consequences, tradeoffs, and any condition for revisiting it.

Distinguish an agent recommendation from a user-confirmed decision. Link to supporting evidence when it will help a later reader. Keep the entry proportional to the decision.

## Explicit per-task logging

When the user or project explicitly requires a daily entry for every task, append exactly one entry per task, using the established daily log. For a task without architectural impact, record that fact briefly. This mode is optional and does not apply to other projects or override a read-only boundary.
