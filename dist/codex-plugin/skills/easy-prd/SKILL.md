---
name: easy-prd
description: Create or revise implementation-ready product documentation and delivery slices from a brief or existing application. Use for PRDs and plan reconciliation, not product implementation or open-ended idea discovery.
---

# Easy PRD

Create the smallest maintained document set another coding agent can use without the chat history. State the intended behavior, exclusions, contracts, acceptance criteria, and next actionable work.

## Shared boundaries

Preserve confirmed intent, existing stack, and deployment target unless a confirmed requirement conflicts with them. Separate facts, assumptions, open questions, and verified implementation. Do not invent features, credentials, legal requirements, business facts, or numeric targets.

This workflow edits planning documents, not product code or infrastructure. A request to create or update the plan authorizes those document edits. Ask only about unresolved choices that materially change behavior, scope, access, privacy, feasibility, or architecture. Decide internal technical details from evidence.

Use the brief, conversation, and relevant repository evidence before asking for missing information. Resolve a small gap directly. Recommend `$unpack-product-idea` when substantial discovery remains, while preserving useful planning work that does not depend on the answer.

Match the user's language. Keep the source brief as evidence of intent and one owner for each mutable fact. Preserve still-valid content and edit only the marked Easy PRD block in an existing `AGENTS.md`.

## Choose the workflow

- **New plan or broad revision:** Read [planning-workflow.md](references/planning-workflow.md). Use it when product or architecture assumptions must be established or reconsidered across the plan.
- **Bounded update:** Read [plan-updates.md](references/plan-updates.md) for affected slices, deferrals, status reconciliation, or a local contract revision. Reuse established intent and document layout.
- **Delivery expectations:** Read [delivery-profiles.md](references/delivery-profiles.md) when choosing or changing implementation fidelity, verification, or release expectations. A timebox is a separate constraint.
- **Document structure:** Read [documentation-model.md](references/documentation-model.md) when creating the document set or changing its ownership or layout. Start with existing sections; extract files only when maintenance needs justify them.
- **Y-Hub dependency:** Read [yhub-adapter.md](references/yhub-adapter.md) when choosing or changing that dependency. Verify only capabilities and contracts needed by the project; record whether evidence is live, cached, or unverified. Never migrate a project automatically.

Implementation of an already planned slice follows the project's current state and slice. Do not invoke Easy PRD again unless scope, a material contract, architecture, or the plan needs to change.

## Finish

Complete the selected workflow's document edits and consistency checks. Acceptance criteria are binding; implementation suggestions can change when behavior and contracts remain correct.

For a new plan, report the document set, delivery expectations, MVP boundary, first ready slice, and material uncertainty. For a bounded update, report changed scope or status, affected dependencies, and the next action or blocker. Mention profile, timebox, or platform freshness only when relevant to the change.
