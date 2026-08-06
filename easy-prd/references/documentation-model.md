# Adaptive documentation model

Stable information domains do not require a stable number of files. Every project needs clear product intent, implementation approach, work sequence, current state, and decisions; package those domains according to complexity.

## Compact package

Use for a small product with one main role, one primary journey, few entities, little security or integration risk, and roughly two to five slices.

```text
AGENTS.md
docs/
  PROJECT.md
  PLAN.md
```

`PROJECT.md` contains:

- product summary, users, problem, and first-version outcome;
- must-have, later, and out-of-scope lists;
- main journey and important states;
- functional requirements and business rules;
- data ownership and visibility;
- technical approach and platform contract;
- constraints, assumptions, open questions, and decisions.

`PLAN.md` is the sole source of truth for operational state and contains:

- milestones and ordered slices;
- statuses and dependencies;
- active or next ready slice;
- detailed acceptance criteria and verification for each near-term slice;
- blockers and last verified state;
- implementation reports.

Do not create empty `STATE.md`, `DECISIONS.md`, or `slices/` merely to resemble a larger project.

## Standard package

Use for most full web applications: several journeys, authentication, multiple roles, meaningful data, integrations, or approximately six to fifteen slices.

```text
AGENTS.md
docs/
  PRODUCT.md
  TECHNICAL.md
  PLAN.md
  STATE.md
  DECISIONS.md
  slices/
    S001-foundation.md
    S002-first-user-value.md
```

Retain an existing brief at its original path. Add `docs/BRIEF.md` only when the source brief existed solely in conversation or consolidation is explicitly useful.

### PRODUCT.md

Make this the product behavior contract:

- goals and non-goals;
- users and roles;
- primary and secondary journeys;
- MVP boundary;
- functional requirements (`FR-###`);
- business rules (`BR-###`);
- material non-functional requirements (`NFR-###`);
- permissions, interface states, errors, and edge cases;
- observable product success signals;
- assumptions and open product questions.

### TECHNICAL.md

Make this the implementation contract:

- application type and selected stack;
- architecture components and responsibilities;
- source layout at a useful, non-prescriptive level;
- data storage, ownership enforcement, and lifecycle;
- authentication and authorization;
- integrations, secrets, configuration, and failure handling;
- security constraints;
- test strategy;
- deployment approach and platform contract;
- technical assumptions and recheck points.

Do not prescribe low-level structure that the implementation agent should choose from evidence.

### PLAN.md

Contain milestones, slice ordering, dependency summaries, and requirements coverage. Do not duplicate operational status details beyond a concise derived summary when `STATE.md` exists.

### STATE.md

Make this the only operational status source of truth:

- current milestone;
- active slice, or first ready slice when work has not begun;
- one status table for all slices;
- concrete blockers;
- last verified build, tests, and behavior;
- exact next action.

### DECISIONS.md

Keep a lightweight decision log. For each `D-###`, record:

- status and date;
- source: user, existing system, or agent proposal;
- context;
- decision;
- rationale;
- consequences;
- superseded decision when applicable.

Distinguish accepted decisions, proposals, assumptions, and open questions.

### Slice files

Use frontmatter for stable machine-scannable metadata:

```yaml
---
id: S002
title: Create and view a task
status: ready
depends_on:
  - S001
covers:
  - FR-001
  - FR-002
  - BR-001
---
```

Then include:

```markdown
# S002 — Create and view a task

## User outcome

## In scope

## Out of scope

## Preconditions

## Expected behavior

## Interface states

## Data and contracts

## Acceptance criteria

- [ ] ...

## Verification

- [ ] ...

## Definition of Done

- [ ] All acceptance criteria pass.
- [ ] Required automated and manual checks pass.
- [ ] The application builds without a new regression.
- [ ] Operational state is updated.
- [ ] New significant decisions are recorded.
- [ ] The implementation report below is complete.

## Implementation report

### Implemented

### Files changed

### Verification performed

### Deviations from plan

### Remaining issues
```

Acceptance criteria are binding. Implementation suggestions may change if the final behavior and contracts remain correct and any significant decision is recorded.

## Extended package

Start with Standard. Add only independently useful documents such as:

```text
docs/
  DATA.md
  UI.md
  API.md
  INTEGRATIONS.md
  SECURITY.md
  DEPLOYMENT.md
  TESTING.md
  PLATFORM.md
```

Extract a domain into its own document when at least one is true:

- three or more slices reference it;
- it contains five or more substantial requirements or contracts;
- it has an independent lifecycle or owner;
- it carries material security, privacy, money, migration, or operational risk;
- it changes frequently without the rest of the technical contract;
- leaving it embedded makes information meaningfully hard to find.

Do not duplicate the extracted content. Replace the old section with a concise summary and link.

## AGENTS.md managed block

Create or update exactly one marked block, preserving all content outside it:

```markdown
<!-- BEGIN EASY PRD WORKFLOW -->
## Project documentation workflow

### Document map

- `actual/path.md` — its real source-of-truth purpose.

### Choose context by task

Do not load all project documentation automatically.

- **Question about code:** read relevant code and tests. Read product documentation only when expected behavior is in question. Current project state is optional.
- **Local visual, copy, or technical edit:** read affected code, styles, and tests. Documentation is optional when product behavior and contracts do not change.
- **Continue planned implementation:** read the current state, selected slice, and only the documents and requirements linked by that slice.
- **New feature:** read product scope, plan, relevant technical decisions, and related slices. Create or update a slice before implementation.
- **Data, architecture, integration, auth, or deployment change:** read the relevant technical contract, decisions, and affected slices. Refresh platform context when required.
- **Unplanned bug fix:** work outside the active slice when appropriate. Update documentation only if behavior, a contract, data shape, architecture, or plan changes.

### Completing a slice

Do not mark a slice `done` until every acceptance criterion and verification step passes, the implementation report is filled, operational state is updated, and significant new decisions are recorded.

### Growing documentation

Add a section to an existing document first. Extract it only when it becomes an independent domain. Keep one source of truth and update the document map and links after extraction.

When the project depends on Y-Hub, insert the refresh subsection defined in `yhub-adapter.md`. Omit it otherwise.
<!-- END EASY PRD WORKFLOW -->
```

Adapt the example to real paths and project-specific rules. Do not mention nonexistent documents.

For a Compact package, route planned implementation to the current/next slice in `docs/PLAN.md`. For Standard or Extended, route it through `docs/STATE.md` and the selected file in `docs/slices/`.

## Status consistency

In Compact, `PLAN.md` owns statuses. In Standard and Extended, `STATE.md` owns statuses; `PLAN.md` and slice frontmatter may display synchronized summaries but must point readers to `STATE.md` when a conflict appears.

Never use `done` as a planning default. New-project slices begin as `ready` only when fully specified and unblocked; later concise slices begin as `planned`. Existing behavior begins as `needs_verification` unless its criteria were actually checked.
