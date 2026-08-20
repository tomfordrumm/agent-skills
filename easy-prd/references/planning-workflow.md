# Planning workflow

Use this workflow for every Easy PRD run. Keep a private working model until the product, scope, architecture, and slices agree. Templates must follow the analysis, not shape it.

## 1. Find the evidence

Look for product intent in this order:

1. the path named by the user;
2. `PROJECT_BRIEF.md` at the project root;
3. `docs/BRIEF.md` or `BRIEF.md`;
4. another clear discovery artifact or existing PRD;
5. a sufficiently complete brief in the conversation.

If sources conflict and authority is unclear, ask which one controls. Keep the original brief as evidence even when working documents later refine it.

Inspect the repository before asking questions. Read the instructions, manifests, entry points, tests, data contracts, deployment files, and existing project documents that could affect the plan. Do not treat found code as verified behavior.

Classify the starting point as new, scaffold-only, implemented but poorly documented, or implemented with maintained documents. The classification affects how much evidence must be reconciled, not which template to use.

## 2. Build a working model

Record only facts needed to decide scope and implementation:

```yaml
product:
  problem:
  users: []
  primary_outcome:
  primary_journey: []
  must_have: []
  later: []
  out_of_scope: []

behavior:
  roles: []
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

delivery:
  intended_use:
  profile: prototype | lean | production
  timebox:
  timebox_covers:
  non_negotiable_quality: []
  accepted_compromises: []

evidence:
  confirmed: []
  assumptions: []
  open_questions: []
  contradictions: []
  verified_implementation: []
```

Mark the source of every material claim as user, brief, repository evidence, agent proposal, or unknown.

## 3. Select the delivery profile and timebox

Read `delivery-profiles.md`. Choose `prototype`, `lean`, or `production` from the intended use and risk, not from the presence of authentication, a database, an SDK, or deployment.

Treat a timebox as a separate constraint. State what it covers, such as idea through publication or implementation only. If the intended result cannot fit safely, narrow the first-version journey, split delivery, or ask the user to resolve the conflict. Do not silently downgrade a real integration, privacy boundary, or other non-negotiable quality.

Report the proposed profile and its practical consequences when the brief does not make them obvious. Ask only when another profile would materially change scope, fidelity, or release checks.

## 4. Decide how much documentation is warranted

Complexity grows when the product has several roles or journeys, sensitive data, payments, irreversible actions, external integrations, offline or background behavior, non-trivial data lifecycles, or existing behavior that must remain compatible.

Use this judgment to control question depth and documentation size. It does not force a package. A small product can need a separate security section, while a larger content site may still fit the Compact package. The delivery profile also does not force a package.

## 5. Resolve material questions

Ask only when the answer could change:

- who can use, own, or see data;
- the main journey or promised outcome;
- first-version scope;
- intended use or a timebox conflict that would change the first version;
- privacy, retention, payment, or destructive behavior;
- a required integration or platform capability;
- a major architecture component;
- compatibility with existing behavior.

Use product language. Do not ask a non-technical user to choose databases, API styles, state managers, or folder structures.

If the user asks to proceed without questions, choose conservative defaults and label material inferences as assumptions. Stop only when continuing would misrepresent safety or feasibility.

When confirmation is needed, show a short synthesis of the first-version outcome, must-have scope, exclusions, roles, proposed system shape, and unresolved decisions.

## 6. Match needs to components

Translate confirmed requirements into technical needs before naming providers:

```yaml
project_needs:
  - id: NEED-001
    capability: data.persistent_storage
    reason: Tasks must survive reloads and devices.
    criticality: required
```

For Y-Hub, follow `yhub-adapter.md`. For another platform, use current authoritative documentation and record any unverified capability.

Capability support is not proof of a runtime response shape. For every material external SDK or API boundary, plan the earliest cheap contract probe that can verify actual method names, identifiers, wrappers, pagination, and error behavior. Base fixtures and mocks on that evidence. A lean or production plan must include a real happy-path smoke test before publication.

Choose frontend, server logic, data, authentication, files, integrations, background processing, and deployment separately. Select the simplest combination that satisfies every first-version need. A friendly preset name may summarize the result but must not replace the component list.

## 7. Set the MVP boundary

Place each candidate capability in `must_have`, `later`, or `out_of_scope`.

A capability belongs in `must_have` only when the main journey cannot produce its result without it, the product would be unsafe without it, or a confirmed business rule requires it. Keep decoration, speculative scale work, optional social mechanics, and analytics without a decision use outside the MVP.

Write one observable boundary sentence. Example:

> The first version is useful when a user can save a task, see it after returning, and mark it complete without exposing it to another user.

## 8. Define behavior and contracts

Create stable IDs only for items referenced by slices or tests:

- `FR-###` for functional behavior;
- `BR-###` for business rules;
- `NFR-###` for material quality, privacy, compatibility, or operational requirements;
- `D-###` for significant decisions.

For each important action, describe only relevant loading, empty, success, validation, permission, server-error, offline, or conflict states.

Describe data twice only when both views are useful. Product documents cover meaning, ownership, visibility, lifecycle, and relationships. Technical documents cover storage, identifiers, validation authority, and failure behavior.

Record significant decisions with their source, context, rationale, consequences, and status. Never present an agent inference as a user decision.

## 9. Create vertical slices

Map every must-have requirement to a slice before writing slice prose:

```text
FR-001 -> S002
BR-001 -> S002
NFR-001 -> S001, S002
```

Each slice must end in an observable user result or necessary infrastructure result. A slice may cross UI, server, and data layers. Avoid separate table, API, and frontend slices that provide no result alone.

One small foundation slice is acceptable when it produces a running, testable path. Do not let setup grow into a separate infrastructure project.

Scale the slice plan to the delivery profile. Prototype plans usually need one or two slices. Lean plans usually need two to four. Production plans have no fixed count because risk and independent outcomes control the shape.

For lean and production work, make the first slice prove the highest-risk real external contract and the deployment path while delivering the smallest observable value. Do not plan a disposable fixture-only shell unless the interface itself is the prototype hypothesis. Combine setup, data, API, and UI work when separating them would create handoffs without an independently useful result.

A ready slice states:

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
acceptance_criteria: []
verification: []
```

Keep one cohesive outcome per slice. Split a slice when its criteria describe independent results or cannot fit one focused implementation session.

Use automated checks for anything the agent can run or inspect. Reserve human checks for perception, physical hardware, a real external account, OS-level behavior, or another runtime the agent cannot observe. State each human check as setup, action, and expected result.

Plan verification at meaningful evidence points, not after every document or layer. Use focused checks during implementation and a full build or suite when a complete path or release candidate exists. Repeat a full gate only when a relevant change could invalidate its result. For lean work, default to one final independent review at most; do not create an automatic review-fix-review loop for lower-impact findings.

Use these statuses:

- `planned` when details or dependencies remain;
- `ready` when the slice is specified and unblocked;
- `in_progress` when implementation has started;
- `blocked` when a named blocker exists;
- `needs_verification` when code may exist but criteria are unproven;
- `done` when every required check passed.

Detail all slices in a small plan. For a long roadmap, fully detail the first milestone and nearest ready work. Expand a planned slice before implementation.

## 10. Package the documents

Read `documentation-model.md` and choose Compact, Standard, or Extended from actual complexity and existing conventions.

Preserve the source brief. If it exists only in the conversation, save a faithful snapshot as `docs/BRIEF.md` when provenance will matter.

## 11. Validate before writing

Check these invariants:

- every MVP capability is confirmed or visibly assumed;
- the delivery profile, intended use, timebox boundary, and accepted compromises agree;
- the primary journey reaches the promised outcome;
- roles, ownership, permissions, and success signals agree;
- every required need has a supported component;
- material external contracts have an early evidence step and a real smoke test when required by the profile;
- private secrets do not enter browser code;
- every must-have requirement maps to a slice;
- slice dependencies are acyclic and at least one slice is ready;
- slice count and verification cadence are proportionate to the delivery profile;
- human checks cover only behavior the agent cannot verify;
- links and paths resolve;
- each fact and status has one owner;
- existing human instructions remain intact.

Fix failures before writing or claiming completion.

## 12. Write and report

Re-read every existing destination, preserve unrelated content, then create or update the selected documents. Replace only the marked Easy PRD block in `AGENTS.md`. Re-read the result, inspect the diff, and validate against actual paths.

Do not silently delete old documentation. When consolidation is needed, preserve useful facts, update inbound links, and report what moved.

Report the delivery profile and timebox, chosen document set, changed files, MVP boundary, first ready slice, assumptions, blockers, platform source, and existing behavior that still needs verification. Do not begin implementation unless the user separately requests it.
