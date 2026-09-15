# Bounded plan updates

Read the status owner, affected slices and decisions, and direct dependencies. Trace only code or contracts needed to understand the requested change. Reuse established product intent, delivery profile, stack, and document layout.

Update affected scope, acceptance criteria, requirement coverage, and dependency links. Move deferred work to the existing backlog or mark it deferred in the status owner, preserving IDs and still-valid content. Do not reset completed slices or repeat discovery for unchanged requirements.

## Status and evidence

Keep mutable status in one owner: `PLAN.md` for Compact, `STATE.md` for Standard and Extended. Replace touched duplicate statuses with links without migrating unrelated documents. Resolve conflicting statuses from acceptance evidence or record the uncertainty.

- `done`: acceptance criteria were checked.
- `needs_verification`: implementation appears to exist but behavior is not proven.
- `ready`: specified and unblocked.
- `planned`, `in_progress`, or `blocked`: supported by current evidence.
- `deferred`: accepted work moved out of current delivery, following the existing backlog convention.

## Completion

Check affected dependencies, coverage, links, paths, terminology, permissions, data ownership, and any touched managed `AGENTS.md` instructions. Identify the next ready slice or actual blocker. A deferral-only request does not require inventing a ready slice.

Continue through authorized document edits without a second approval. If a material choice remains unresolved, prepare unaffected content and ask about that choice. Load additional references only when the update needs their guidance.
