---
name: adr-logger
description: Enforce Architectural Decision Records (ADR) logging for every task. Use when a user asks to create, update, or enforce ADRs, or when a workflow requires logging decisions in an ADR directory with daily files named adr_yyyy_mm_dd.md.
---

# ADR logger

Log one decision entry for each task in the daily file `ADR/adr_yyyy_mm_dd.md`.

## Workflow

1. Locate the project root in the current workspace.
2. Ensure an `ADR/` directory exists at the root; create it if missing.
3. Use today's local date to select the file name: `ADR/adr_yyyy_mm_dd.md`.
4. If the file exists, append a new entry; if not, create it with a header and the first entry.
5. Each task must produce exactly one entry.

## Entry format

Append this structure under the file header:

```
## HH:MM - <task title>

### Context
- <what prompted the decision or change>

### Decision
- <what was decided or done>

### Consequences
- <impact, tradeoffs, or follow-up>
```

Use local time for `HH:MM`. Keep the entry short and specific to the task. If the task has no architectural impact, write `No architectural impact` under Consequences.
