# Documentation model

Every project needs clear product intent, a technical approach, ordered work, current state, and recorded decisions. The project does not need a separate file for each category.

Choose the document package from information complexity and maintenance needs, not from the delivery profile. Record the selected `prototype`, `lean`, or `production` profile and any timebox inside the chosen package. Authentication, a database, an integration, or deployment does not by itself require Standard documentation.

## Compact

Use Compact for a small product with one main journey, few roles, limited independent decisions, and roughly one to five slices. A known authentication or integration contract can remain Compact when it does not need a separate owner or lifecycle.

```text
AGENTS.md
docs/
  PROJECT.md
  PLAN.md
```

`PROJECT.md` owns the product summary, delivery profile and timebox, scope, journey, requirements, business rules, data ownership, technical approach, constraints, assumptions, and decisions.

`PLAN.md` owns milestones, slices, dependencies, status, acceptance criteria, verification cadence, release checks, blockers, and implementation reports.

Do not add empty status, decision, or slice files to imitate a larger project.

## Standard

Use Standard when the product has several journeys or roles, independently changing technical contracts, a meaningful data lifecycle, enough decisions to need their own log, or roughly six to fifteen slices. Do not choose it for authentication or one integration alone.

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

Keep an existing brief at its original path. Add `docs/BRIEF.md` only when the source existed solely in chat or a preserved copy has clear value.

### PRODUCT.md

This file owns product behavior:

- goals, exclusions, users, roles, and journeys;
- intended use, delivery profile, timebox, and accepted compromises;
- the MVP boundary;
- functional requirements and business rules;
- material quality and privacy requirements;
- permissions, interface states, errors, and edge cases;
- success signals, assumptions, and open product questions.

### TECHNICAL.md

This file owns implementation constraints:

- selected stack and component responsibilities;
- useful source-layout guidance without prescribing every file;
- data storage, ownership enforcement, and lifecycle;
- authentication and authorization;
- integrations, configuration, secrets, and failure handling;
- test and deployment strategy;
- evidence and recheck points for material external contracts;
- platform contract and recheck points.

Leave local class boundaries and helper structure to the implementation agent unless a confirmed contract depends on them.

### PLAN.md and STATE.md

`PLAN.md` owns milestones, slice order, dependency summaries, requirement coverage, and the profile-appropriate verification and release gates.

`STATE.md` is the only operational status source. It names the current milestone, active or first ready slice, slice statuses, blockers, last verified behavior, and exact next action.

### DECISIONS.md

For each significant decision, record its ID, status, date, source, context, choice, rationale, consequences, and any decision it replaces. Keep decisions, proposals, assumptions, and open questions distinct.

### Slice files

Use frontmatter for fields that agents need to scan:

```yaml
---
id: S002
title: Create and view a task
status: ready
depends_on:
  - S001
covers:
  - FR-001
  - BR-001
---
```

The body should contain only the sections needed to implement and verify the slice:

```markdown
# S002: Create and view a task

## User outcome
## Scope
## Expected behavior
## Interface states
## Data and contracts
## Acceptance criteria
## Verification
## Implementation report
```

Acceptance criteria are binding. Implementation suggestions may change when behavior and contracts remain correct and the change is recorded when significant.

Omit human verification when the agent can run every required check. Never assign an automatable check to the user.

## Extended

Start with Standard. Add a domain file such as `DATA.md`, `SECURITY.md`, or `INTEGRATIONS.md` only when the domain has its own owner or lifecycle, affects several slices, changes independently, or carries material security, privacy, payment, migration, or operational risk.

Move the detail rather than duplicating it. Leave a short summary and link in the original file.

## Managed AGENTS.md block

Create or update one marked block and preserve everything outside it:

```markdown
<!-- BEGIN EASY PRD WORKFLOW -->
## Project documentation

### Document map

- `actual/path.md`: what this file owns.

### Delivery approach

- Profile: `prototype | lean | production`.
- Timebox: [duration and what it covers, or `not specified`].
- Preserve the documented quality floor and accepted compromises when reducing scope.
- For implementation of an existing slice, follow the current state and slice. Do not invoke Easy PRD again unless product scope, a material contract, architecture, or the plan changes.
- Run focused checks while working and full gates only at the milestones defined in the plan or after a change that invalidates prior evidence.

### Load only relevant context

- For a code question or local fix, read the affected code and tests. Read product documents only when expected behavior is unclear.
- For planned implementation, read current state, the selected slice, and documents linked from that slice.
- For a new feature, read product scope, relevant decisions, and related slices. Create or update a slice before implementation.
- For data, architecture, integration, authentication, or deployment changes, read the matching technical contract and decisions.
- For an unplanned bug, update documents only when behavior, a contract, architecture, data shape, or the plan changes.

### Complete a slice

Do not mark a slice `done` until its acceptance criteria and verification pass, its implementation report is filled, state is updated, and significant new decisions are recorded.

### Human verification

Keep the slice at `needs_verification` while required human checks remain. Give the user only checks the agent cannot perform, with setup, action, and expected result. Record the result as confirmed, failed, skipped, unavailable, or accepted as a deviation.

### Grow documents carefully

Add a section to an existing file first. Extract a separate domain only when it has a reason to change independently. Update the document map after moving content.

<!-- END EASY PRD WORKFLOW -->
```

Adapt paths and instructions to the real project. Do not mention files that do not exist.

When Y-Hub is part of the project, add the refresh subsection from `yhub-adapter.md`. Omit it otherwise.

## Status ownership

In Compact, `PLAN.md` owns status. In Standard and Extended, `STATE.md` owns it. Other files may show summaries but must link to the owner when a conflict appears.

New slices start as `ready` only when specified and unblocked. Later slices start as `planned`. Existing behavior starts as `needs_verification` until its criteria are checked.
