# Dynamic Y-Hub platform adapter

Use this adapter only when a project already targets Y-Hub or Y-Hub is a candidate deployment platform. Treat `static`, `php`, `yhub-baas`, and `hybrid` as optional human-friendly summaries, never as a closed capability model.

## Source resolution

Use these sources in order:

1. Read the live Y-Hub agent manifest documented by the current `yhub-deploy-site` skill, currently `GET /api/v1/agent-manifest`.
2. Locate the installed `yhub-deploy-site` skill and determine its declared version.
3. Compare the installed version with the manifest's latest and minimum supported versions.
4. Use the manifest-provided download location to read the current skill package when the local copy is old or lacks the relevant capability.
5. Read only capability, constraint, SDK, auth, data, secret, runtime, and deployment sections needed for planning. Pairing, polling, and response-handling details are irrelevant until deployment.

Do not silently replace a globally installed skill during PRD creation. A current downloaded copy may be used read-only for this run.

Classify source freshness:

- `live`: the manifest and current supported skill were read successfully;
- `cached`: a supported local copy was used but live freshness was not established;
- `unverified`: only stale or incomplete information was available.

If the installed skill is below the manifest's minimum supported version, do not use it as authoritative. If the manifest is unavailable, do not assume a feature absent from the local skill is supported.

## Normalize capabilities

Build a private map before choosing architecture. Extend it when the live skill exposes new categories.

```yaml
platform:
  id: yhub
  source:
    skill_name: yhub-deploy-site
    skill_version: unknown
    api_version: unknown
    sdk_version: unknown
    checked_at: unknown
    freshness: live | cached | unverified

  frontend:
    static_assets: { status: unknown, constraints: [] }
    compiled_frontend: { status: unknown, constraints: [] }
    build_on_platform: { status: unknown, constraints: [] }

  server:
    runtimes: []
    secret_handling: { status: unknown, constraints: [] }
    custom_endpoints: { status: unknown, constraints: [] }
    background_jobs: { status: unknown, constraints: [] }

  data:
    browser_storage: { status: supported, constraints: [] }
    managed_database: { status: unknown, constraints: [] }
    owner_scoped_records: { status: unknown, constraints: [] }
    custom_database: { status: unknown, constraints: [] }

  authentication:
    methods: []
    app_users: { status: unknown, constraints: [] }

  files:
    upload: { status: unknown, constraints: [] }
    persistent_storage: { status: unknown, constraints: [] }

  integrations:
    outgoing_http: { status: unknown, constraints: [] }
    webhooks: { status: unknown, constraints: [] }

  deployment:
    methods: []
    custom_domains: { status: unknown, constraints: [] }
    https: { status: unknown, constraints: [] }
```

Use exactly these evidence states:

- `supported`: a current source confirms the capability;
- `unsupported`: a current source explicitly rules it out;
- `unknown`: information is absent, stale, ambiguous, or inaccessible.

Absence of documentation is not evidence of lack of support.

## Separate capability evidence from contract evidence

A supported Y-Hub capability proves that a need can be covered. It does not prove the exact runtime shape an implementation will receive.

For each material SDK, authentication, managed-database, or deployment boundary, identify the smallest contract probe needed before building dependent behavior. Verify only the fields the project uses, including:

- current method and argument names;
- identifier types and ownership fields;
- success wrappers, collection shapes, and pagination;
- empty, unauthorized, validation, and server-error behavior;
- deployment output or status used by release verification.

Use current official examples as a starting point, then require a live read-only call, a captured real response, or an existing verified test before treating the response shape as confirmed. Base fixtures and mocks on that evidence. Never invent a convenient response shape from the capability description.

Easy PRD must not mutate live infrastructure to perform the probe. Put the probe in the earliest slice that depends on the contract. For a lean or production project, include a real main-journey smoke test against the deployed application before completion.

## Map project needs

Derive needs from the product and technical model:

```yaml
project_needs:
  - id: NEED-001
    capability: frontend.compiled_frontend
    reason: The selected Vite and TypeScript app must be delivered.
    criticality: required

  - id: NEED-002
    capability: authentication.app_users
    reason: A user must access private records across devices.
    criticality: required
```

Create a coverage matrix:

```yaml
capability_match:
  - need: NEED-001
    status: satisfied
    provider: yhub
    evidence: current yhub-deploy-site skill

  - need: NEED-002
    status: unverified
    provider: yhub
    evidence: live manifest unavailable
```

Use these match statuses:

- `satisfied`;
- `partially_satisfied`;
- `unsupported`;
- `unverified`.

Do not choose a Y-Hub component for a required need until the match is `satisfied`. For `partially_satisfied`, either narrow the MVP, add an external provider, or expose the tradeoff to the user. For `unsupported`, redesign or use another platform. For `unverified`, mark affected decisions and slices `needs_verification` or `blocked`.

## Record only the project contract

In Compact projects, put the platform contract in `docs/PROJECT.md`. In Standard projects, put it in `docs/TECHNICAL.md`. Create `docs/PLATFORM.md` only when platform dependencies meet the Extended extraction rules.

Record:

```markdown
## Platform contract

### Platform

Y-Hub.

### Verified from

- Skill: `yhub-deploy-site`
- Skill version: ...
- API version: ...
- SDK version: ...
- Checked at: YYYY-MM-DD
- Freshness: live | cached | unverified

### Required capabilities

- Only capabilities this project actually depends on.

### External providers

- Any need not supplied by Y-Hub.

### Architecture decision

- Selected components and why they are the simplest complete fit.

### Recheck before

- The first slice using each material platform capability.
- Creating fixtures or adapters that depend on an external response shape.
- The first production deployment.
- Any change to data, auth, server logic, secrets, SDK use, or deployment shape.
```

Do not copy all current Y-Hub features or API routes into the PRD.

## Add selective refresh rules to AGENTS.md

Insert this adapted subsection inside the Easy PRD managed block when the project depends on Y-Hub:

```markdown
### Refresh Y-Hub context when relevant

Project documentation records the Y-Hub capabilities this project depends on; it is not a complete or permanently current platform reference.

Do not refresh Y-Hub context for code questions, copy or style edits, local UI changes, or refactors and bug fixes that do not change platform dependencies.

Refresh current Y-Hub context before assessing a new feature's feasibility; changing storage, authentication, permissions, server-side logic, secrets, SDK usage, integrations, or deployment; implementing the first slice that depends on a platform capability; creating fixtures or adapters for an external response shape; and performing the first production deployment.

To refresh, read the live agent manifest, obtain a current supported `yhub-deploy-site` skill when necessary, inspect only relevant sections, compare them with the project's platform contract, and update documentation only when an actual dependency or constraint changed. Do not change architecture merely because an optional new capability appeared.
```

## React to platform change

- New optional capability: leave the architecture unchanged unless it solves a confirmed need better enough to justify a decision change.
- Required capability changed but remains supported: update constraints and affected verification steps.
- Required capability became unsupported or materially incompatible: mark affected slices `blocked`, document the impact, and propose the smallest viable alternative.
- Source freshness cannot be established: retain prior decisions as provisional and use `needs_verification`; never claim live support.
