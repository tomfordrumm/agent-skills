---
name: easy-prd
description: Turn a Product Brief, project idea, or existing web application into an implementation-ready PRD, technical plan, vertical delivery slices, project state, decisions, and adaptive AGENTS.md documentation workflow. Use when the user asks to create or update a PRD, prepare a web app for implementation, convert PROJECT_BRIEF.md or equivalent discovery output into project documentation, plan an MVP, split work into executable slices, or establish durable agent handoff documents. Supports new and existing projects, compact through extended documentation, and a dynamic Y-Hub platform adapter. Do not use for initial product-idea discovery, market validation, or application implementation.
---

# Easy PRD

Convert confirmed product intent into the smallest coherent documentation system another coding agent can implement without relying on chat history.

Produce durable project files, not merely a PRD pasted into the conversation. Adapt the number of files and depth of detail to the project's real complexity.

## Boundaries

Do:

- inspect the brief, repository, existing documentation, and verified implementation state;
- clarify only decisions that materially change product behavior, MVP scope, privacy, access, feasibility, or architecture;
- define an explicit MVP and exclusions;
- choose the simplest architecture that covers confirmed requirements;
- create traceable requirements and vertical implementation slices;
- install a selective documentation workflow in `AGENTS.md`;
- preserve human instructions and existing verified facts.

Do not:

- rediscover an already adequate product brief;
- implement product code, install dependencies, deploy, or mutate infrastructure;
- invent features, business facts, credentials, legal requirements, or numeric success targets;
- ask a non-technical user to choose databases, API styles, state managers, or directory structures;
- mark existing behavior `done` merely because similar code exists;
- create every possible document just to fill a template.

If no usable brief or product description exists, stop and recommend `$unpack-product-idea`. A repository name or a feature list without a problem, user, primary outcome, or MVP boundary is not an adequate brief.

## Operating rules

- Match the user's language in all generated project documentation.
- Treat user-confirmed facts, agent assumptions, open questions, and verified implementation as distinct categories.
- Prefer reasonable, visible assumptions for reversible details. Ask when an answer would materially change the result.
- Ask no more than five focused questions at once. Do not repeat answers already present in the brief or codebase.
- Keep the source brief as a snapshot of intent. Do not silently rewrite it to match later implementation choices.
- Treat requirements and acceptance criteria as binding; treat suggested implementation details as revisable decisions.
- Use one source of truth for each kind of information, especially slice status.
- Preserve the existing stack and deployment target unless they create a demonstrated conflict with requirements.
- Never overwrite unrelated content in `AGENTS.md`; manage only the marked Easy PRD block.

## Required workflow

Read [references/planning-workflow.md](references/planning-workflow.md) completely before planning or writing files. Follow its state machine:

```text
DISCOVER -> MODEL -> CLASSIFY -> CLARIFY -> RESOLVE PLATFORM
-> DEFINE MVP -> DESIGN -> SLICE -> PACKAGE -> VALIDATE -> WRITE -> REPORT
```

Do not write partial project documents before the model, scope, architecture, and slice coverage agree. It is acceptable to show a compact proposed synthesis and file plan before writing.

## Documentation packaging

After modeling the content, read [references/documentation-model.md](references/documentation-model.md) completely. Select one adaptive package:

- **Compact** — a small product with few flows and decisions; use `PROJECT.md` and `PLAN.md`.
- **Standard** — most real web applications; separate product, technical, plan, state, decisions, and slice files.
- **Extended** — Standard plus only the independently useful domain documents justified by scale, risk, or reuse.

Packaging follows content; it must not drive product analysis. Prefer a section in an existing file until the topic deserves an independent lifecycle.

## Platform resolution

The initial product profile is `web-app`. Y-Hub is the supported dynamic platform adapter, not a frozen list of hosting presets.

When the project uses or is considering Y-Hub, read [references/yhub-adapter.md](references/yhub-adapter.md) completely. Resolve current capabilities from the live manifest and the current `yhub-deploy-site` skill. Normalize them to `supported`, `unsupported`, or `unknown`, map project needs to those capabilities, and only then select architecture components.

Do not migrate an existing project to Y-Hub automatically. Do not copy the complete Y-Hub feature catalog into project documentation; record only the capabilities and constraints the project actually depends on, their source, freshness, and recheck points.

For other deployment targets, preserve the target and apply the same needs-to-capabilities reasoning. Mark unverified platform assumptions explicitly.

## Frontend stack policy

Use this priority order:

1. Preserve a viable existing stack.
2. Use plain HTML/CSS/JavaScript for a small page or single-screen app with little state, navigation, modularity, or need for a build step.
3. Use Vite + TypeScript when there are several screens or substantial states, an API or platform SDK, authentication, reusable modules, tests, or expected continued development.
4. Add React, Vue, Svelte, or another framework only when the project already uses it, the UI is meaningfully component-heavy, a required library depends on it, or it clearly reduces implementation complexity.

Vite does not imply React. Avoid speculative enterprise architecture, microservices, queues, and infrastructure for hypothetical scale.

## Existing projects

Inspect source, tests, configuration, migrations or schemas, deployment files, and relevant history when available. Reconcile documentation with evidence:

- `done` — acceptance criteria have been verified;
- `needs_verification` — code appears to exist but behavior is not yet proven;
- `ready` — fully specified and unblocked;
- `planned`, `in_progress`, or `blocked` — use only when evidence supports the status.

Do not discard existing documentation. Repair contradictions, retain still-valid decisions, and explain material conflicts before resolving them.

## Completion contract

Finish only when:

- every MVP requirement is confirmed or visibly labeled as an assumption;
- every must-have requirement maps to at least one slice;
- no slice exists without a user outcome or necessary infrastructure outcome;
- dependencies are acyclic and at least one slice is `ready`;
- acceptance criteria are observable and testable;
- architecture covers every project need without relying on an unverified capability;
- statuses, links, terminology, roles, permissions, data ownership, and scope agree across files;
- `AGENTS.md` lists only files that actually exist and routes agents to the minimum relevant context;
- existing human content is preserved;
- the final response lists created or changed files, chosen package, MVP boundary, first ready slice, assumptions, blockers, and platform freshness.

If a critical platform capability remains unverified, complete independent documentation but mark affected decisions and slices `needs_verification` or `blocked`; never present feasibility as confirmed.
