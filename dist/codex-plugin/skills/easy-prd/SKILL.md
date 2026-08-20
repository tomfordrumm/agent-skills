---
name: easy-prd
description: Turn a confirmed Product Brief or an existing web application into implementation-ready product documentation and vertical delivery slices, scaled for a prototype, lean working product, or production release. Use for PRDs, MVP plans, durable agent handoffs, or reconciling project documents with existing code. Do not use for initial idea discovery, market research, or implementation.
---

# Easy PRD

Create the smallest set of project files another coding agent can use without the chat history. The documents must state what to build, what is out of scope, how the system should behave, and which slice is ready first.

## Boundaries

Inspect the brief, repository, existing documentation, and verifiable behavior. Preserve confirmed facts and human instructions.

Do not implement product code, install dependencies, deploy, or change infrastructure. Do not invent features, credentials, legal requirements, business facts, or numeric targets. Choose internal technical details yourself when the product requirements already determine a safe answer.

Do not invoke Easy PRD again merely to implement an already planned slice. The implementation agent should follow the project's `AGENTS.md`, current state, and selected slice. Re-run this skill only when product scope, a material contract, architecture, or the delivery plan needs to change.

If the input does not identify the problem, intended user, primary outcome, and first-version boundary, stop and recommend `$unpack-product-idea`. Do not repeat product discovery when an adequate brief already exists.

## Working rules

- Match the user's language in generated documents.
- Separate confirmed facts, assumptions, open questions, and verified implementation.
- Ask only about choices that would change product behavior, MVP scope, access, privacy, feasibility, or architecture. Ask no more than five questions at once.
- Keep the source brief as evidence of intent. Do not rewrite it to justify later choices.
- Treat requirements and acceptance criteria as binding. Implementation suggestions may change when the resulting behavior and contracts stay correct.
- Preserve the existing stack and deployment target unless they conflict with a confirmed requirement.
- Keep one source of truth for each fact, especially slice status.
- Edit only the marked Easy PRD block in `AGENTS.md`.

## Workflow

Read [references/planning-workflow.md](references/planning-workflow.md) before planning. It covers evidence gathering, scope, architecture, slices, validation, and safe writes.

Read [references/delivery-profiles.md](references/delivery-profiles.md) when choosing how much implementation, verification, and release work the plan requires. Select `prototype`, `lean`, or `production`, and treat any timebox as a separate constraint. State the choice and its consequences before writing documents when it is not already explicit in the brief.

Do not start writing project files until the requirements, MVP boundary, architecture, and slice coverage agree. A short synthesis and proposed file list may be shown first when confirmation is needed.

## Choose the document set

Read [references/documentation-model.md](references/documentation-model.md) when packaging the result. Use one of these shapes:

- `Compact` for a small product with few flows and decisions. Use `PROJECT.md` and `PLAN.md`.
- `Standard` for most applications. Separate product, technical, plan, state, decisions, and slice files.
- `Extended` only when a domain such as security, data, or integrations needs its own maintained document.

Start with a section in an existing file. Extract a new file only when the topic has separate owners, risks, reuse, or change cadence.

## Platform and frontend choices

When Y-Hub is in use or under consideration, read [references/yhub-adapter.md](references/yhub-adapter.md). Check current capabilities before choosing components. Record only the capabilities this project depends on and whether the source was live, cached, or unverified. Never migrate an existing project to Y-Hub automatically.

For other platforms, preserve the current target and verify any capability needed by the MVP.

Keep a viable existing frontend stack. For a new frontend, use plain HTML, CSS, and JavaScript when the product is a small page with little state. Use Vite and TypeScript when it has several screens, authentication, an API or SDK, reusable modules, or ongoing development. Add a framework only when existing code, UI complexity, or a required library justifies it.

## Existing projects

Inspect relevant source, tests, configuration, schemas, migrations, deployment files, and history. Use these statuses:

- `done` only when the acceptance criteria were checked;
- `needs_verification` when code appears to exist but behavior was not proven;
- `ready` when a slice is fully specified and unblocked;
- `planned`, `in_progress`, or `blocked` only when evidence supports the label.

Repair contradictions without discarding still-valid documentation. Explain a material conflict before resolving it.

## Finish

Before reporting completion, confirm that every MVP requirement maps to a slice, acceptance criteria are observable, dependencies are acyclic, and at least one slice is ready. The architecture must cover every required capability without presenting an unverified platform feature as available.

Check links, paths, terminology, roles, permissions, data ownership, status summaries, and the managed `AGENTS.md` block against the files that actually exist.

Report the files changed, delivery profile and timebox, chosen document set, MVP boundary, first ready slice, assumptions, blockers, and platform-source freshness. If a required capability remains unverified, mark the affected decision and slice `needs_verification` or `blocked`.
