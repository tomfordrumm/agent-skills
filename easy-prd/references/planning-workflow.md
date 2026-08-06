# Planning workflow

Use this workflow for every Easy PRD run. Keep an internal model until the `WRITE` stage; do not let early file templates dictate analysis.

## 1. DISCOVER — locate evidence

Find the product input in this order:

1. A path explicitly named by the user.
2. `PROJECT_BRIEF.md` at the project root.
3. `docs/BRIEF.md`, then `BRIEF.md`.
4. Another obvious discovery artifact or PRD already in the repository.
5. A sufficiently complete brief supplied in the current conversation.

If several sources conflict and authority is unclear, ask which one controls. Preserve the original brief as intent evidence even when working documents later refine it.

Inspect the repository before asking questions. At minimum, inspect:

- `AGENTS.md` and other repository instructions;
- project manifests and lockfiles;
- source layout and primary entry points;
- tests and test configuration;
- data schemas, migrations, API contracts, and auth code when present;
- deployment and environment examples;
- existing product, technical, state, plan, decision, and slice documents.

Classify the starting state:

- `new` — no implementation exists;
- `existing-empty` — scaffolding exists without meaningful product behavior;
- `existing-implemented` — behavior exists but planning documents are absent or incomplete;
- `existing-documented` — implementation and a working documentation system exist.

Do not treat found code as verified behavior.

## 2. MODEL — normalize facts before decisions

Build a private working model with:

```yaml
product:
  problem:
  users: []
  primary_outcome:
  primary_journey: []
  roles: []
  must_have: []
  later: []
  out_of_scope: []
  success_signals: []

behavior:
  business_rules: []
  important_states: []
  failure_cases: []

data:
  entities: []
  ownership:
  visibility:
  sensitivity:
  lifecycle:

constraints:
  integrations: []
  platform:
  existing_stack:
  operational: []

evidence:
  confirmed: []
  assumptions: []
  open_questions: []
  contradictions: []
  verified_implementation: []
```

Record provenance for material claims: user-confirmed, brief, repository evidence, agent proposal, or unknown.

## 3. CLASSIFY — estimate documentation needs

Classify complexity provisionally. This classification guides interview depth and later packaging; it does not force a file structure.

Signals that increase complexity include:

- multiple roles or permission levels;
- several independent user journeys;
- authentication or cross-device identity;
- sensitive or regulated data;
- payments, billing, or irreversible operations;
- external integrations, webhooks, or private secrets;
- non-trivial data relationships or lifecycle rules;
- offline, realtime, background, file-processing, or migration behavior;
- more than roughly eight implementation slices;
- an existing system whose behavior must be reconciled.

A tiny app may still need a separate security or data section when risk justifies it. A larger but simple content site may remain Compact.

## 4. CLARIFY — ask only material questions

Ask only when the answer could change at least one of:

- who can use or see something;
- the primary user journey or promised outcome;
- must-have versus later scope;
- data ownership, privacy, retention, or sensitivity;
- payments or irreversible actions;
- a required integration or platform;
- technical feasibility or a major architecture component;
- whether existing behavior must remain compatible.

Use plain product language. Do not ask the user to choose implementation details the skill can responsibly decide.

If the user asks to proceed without questions, use conservative defaults, label every material inference as an assumption, and continue unless doing so would falsely claim safety or feasibility.

Before design, show a compact synthesis when user confirmation is needed:

- first-version outcome;
- must-have scope;
- explicit exclusions;
- roles and visibility;
- proposed platform and architecture shape;
- material assumptions or unresolved decisions.

## 5. RESOLVE PLATFORM — establish feasible components

Convert product requirements into technical needs before choosing providers:

```yaml
project_needs:
  - id: NEED-001
    capability: data.persistent_storage
    reason: Tasks must survive reloads and devices.
    criticality: required
```

For Y-Hub, follow `yhub-adapter.md`. For another platform, use its current authoritative documentation and the same status discipline.

Choose components, not a monolithic label:

```yaml
architecture:
  frontend:
    stack:
    delivery:
  server_logic:
    provider:
    purposes: []
  data:
    provider:
  authentication:
    provider:
  files:
    provider:
  integrations: []
  background_processing:
    provider:
  deployment:
    provider:
```

Select the simplest combination that fully satisfies first-version needs. Keep a friendly preset name only as a summary, never as the source of truth.

## 6. DEFINE MVP — normalize scope

Place every candidate function in exactly one group:

```yaml
must_have: []
later: []
out_of_scope: []
```

Keep a function in `must_have` only when it is necessary to:

- complete the primary journey;
- deliver the promised first-version value;
- use the product safely;
- preserve data required by that value;
- test the stated product hypothesis;
- satisfy a mandatory business rule.

Challenge decoration, premature automation, settings with only one choice, unmotivated admin tools, speculative scale work, analytics without a decision use, optional social mechanics, and features already deferred by the user.

Write one observable first-version statement, for example:

> The first version is useful when the user can capture a task, see it after returning, and mark it complete without exposing it to another user.

## 7. DESIGN — create coherent contracts

Create stable IDs only for items referenced by slices or tests:

- `FR-###` — functional behavior;
- `BR-###` — business rule;
- `NFR-###` — material quality, privacy, compatibility, or operational requirement;
- `D-###` — significant product or technical decision.

For each important user action, consider only relevant states:

- initial, loading, empty, success;
- validation error and server error;
- permission denied;
- offline or conflict states when applicable.

Describe data at two levels:

- product: entities, ownership, visibility, lifecycle, relationships;
- technical: storage, identifiers, critical fields, validation authority, failure behavior.

Do not prematurely design a large database schema. Document security boundaries, secret placement, destructive operations, and privacy rules when relevant.

Record significant decisions with context, decision, rationale, consequences, author/source, and status. Never label an agent inference as a user decision.

## 8. SLICE — create an executable roadmap

Build a coverage map before writing slice prose:

```text
FR-001 -> S002
FR-002 -> S002
BR-001 -> S002
NFR-001 -> S001, S002
```

Prefer vertical slices ending in an observable result. A slice may cross UI, data, and server layers. Avoid separate “create table,” “build API,” and “build frontend” slices that produce no value on their own.

Allow one small foundation slice when it produces a walking skeleton that runs, is testable, and can be deployed. Do not let setup become a multi-session infrastructure phase.

Each fully detailed slice must define:

```yaml
id:
title:
status:
outcome:
depends_on: []
covers: []
in_scope: []
out_of_scope: []
behavior: []
ui_states: []
data_changes: []
acceptance_criteria: []
verification: []
definition_of_done: []
implementation_report:
```

Keep each slice to one cohesive outcome and one focused implementation session. If it has more than roughly seven or eight independent acceptance criteria, consider splitting it.

Use these statuses:

- `planned` — known but not sufficiently detailed or still dependency-bound;
- `ready` — fully specified and unblocked;
- `in_progress` — implementation has started;
- `blocked` — a concrete blocker exists;
- `needs_verification` — implementation may exist but criteria are not proven;
- `done` — every criterion and verification step passed.

Apply progressive elaboration:

- Up to 8 slices: detail all slices.
- 9–15 slices: fully detail the first milestone and nearest ready slices; keep later slices concise.
- More than 15 slices: split into milestones, fully detail only the first, and leave later work at roadmap level.

Before implementation, a concise `planned` slice must be expanded and promoted to `ready`.

## 9. PACKAGE — choose files after content

Read `documentation-model.md` and select Compact, Standard, or Extended. Use actual project complexity and existing conventions, not arbitrary scoring.

Preserve an existing source brief. If the only brief exists in the conversation, save a faithful snapshot as `docs/BRIEF.md` when useful for provenance.

## 10. VALIDATE — audit the complete model

Before writing, check:

### Product

- Every MVP feature is confirmed or visibly assumed.
- No invented features or targets appear.
- `must_have`, `later`, and `out_of_scope` do not conflict.
- The primary journey reaches the promised outcome.
- Roles, ownership, permissions, and success signals agree.

### Technical

- Every project need is covered by an architecture component.
- No required component depends on a capability marked `unknown`.
- Private secrets never enter browser code.
- Storage matches ownership, visibility, sensitivity, and lifecycle.
- Infrastructure is proportional to the first version.

### Slices

- Every must-have requirement maps to a slice.
- Every slice has a real user or necessary infrastructure outcome.
- Dependencies are acyclic.
- At least one slice is `ready`.
- The first ready slice needs no unresolved product decision.
- Criteria are observable and deferred features have not leaked into MVP.

### Documents

- Links, anchors, and paths resolve.
- No empty or template-only documents exist.
- Each fact has one source of truth.
- Statuses agree everywhere they are summarized.
- `AGENTS.md` names only real files and preserves human instructions.

Fix validation failures before writing or reporting completion.

## 11. WRITE — save safely

1. List the intended created and changed files internally.
2. Re-read every destination that already exists.
3. Preserve unrelated content and repository-specific conventions.
4. Create or update the documentation files.
5. Create or replace only the marked Easy PRD block in `AGENTS.md`.
6. Re-read all written files and repeat validation against actual paths.
7. Inspect the diff when Git is available.

Do not delete obsolete documentation silently. If consolidation is necessary, retain relevant facts, update inbound links, and report the migration.

## 12. REPORT — hand off the first action

Report:

- chosen package and why;
- created and changed files;
- one-sentence MVP boundary;
- first `ready` slice;
- assumptions and open blockers;
- platform source and freshness;
- any existing behavior marked `needs_verification`.

Do not begin implementation unless the user separately requests it.
