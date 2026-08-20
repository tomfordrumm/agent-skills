# Delivery profiles

Use a delivery profile to scale the plan to the result the user expects. Keep schedule pressure separate. A profile answers "what standard must the result meet?" A timebox answers "how much time is available?"

Record both in the project documentation. If the timebox cannot support the intended result, reduce scope, split delivery, or expose the conflict. Do not silently lower safety, privacy, data integrity, or a required real integration.

## Common quality floor

Every profile must:

- complete the declared user journey at the fidelity promised to the user;
- make temporary data, mocks, missing persistence, and unsupported states visible;
- avoid fabricated integration behavior or claims of verification;
- keep secrets out of client code and avoid unsafe handling of sensitive data;
- leave the repository runnable and the next action clear.

## Prototype

Choose `prototype` when the first result exists to explain, explore, or test an idea and is not intended to be relied on as a working service.

- Temporary data, fixtures, mocks, and local-only behavior are allowed when clearly declared.
- Prefer one complete demonstration path over broad feature coverage.
- Usually plan one or two vertical slices.
- Verify that the demonstration path runs and that declared limitations are accurate.
- Deployment is optional unless sharing the prototype is part of the outcome.
- Do not add production hardening, generalized architecture, or exhaustive edge-case coverage without a specific reason.

## Lean

Choose `lean` for a small product intended for real use by its owner, a small group, or early users, where speed and scope discipline matter more than broad operational maturity.

- The main journey must work end to end with real required persistence, identity, integrations, and deployment.
- Use temporary substitutes only outside the promised journey or when the user explicitly accepts them.
- Usually plan two to four vertical slices. Combine work when another slice would create only a handoff, setup layer, or repeated verification cycle.
- Make the first slice prove the highest-risk real external boundary and a deployable path while delivering the smallest observable value. Do not build a disposable fixture shell unless the user is testing the interface itself.
- Use focused checks while implementing, then one final build and required-journey smoke test. Add another full pass only after a change that could invalidate the previous result.
- Use at most one independent final review by default. Fix release blockers in the required journey, safety, privacy, data integrity, or deployment. Batch lower-impact improvements instead of starting repeated review loops.

Lean does not mean fake, fragile, or undocumented. It means the smallest real result with compact handoff documentation and proportionate verification.

## Production

Choose `production` when the product is public or commercial, handles sensitive or high-impact actions, supports important operations, or will be relied on beyond a controlled early-use context.

- Plan the main journey plus material failure, recovery, access, data lifecycle, observability, and operational behavior.
- Use deeper contract, security, migration, compatibility, and deployment checks where the risk requires them.
- Let the number of slices follow independent outcomes and risk. Do not impose a fixed count.
- Use targeted checks during implementation and full release gates at meaningful milestones. Repeat a gate only when relevant changes invalidate its evidence.
- Record ownership of remaining operational risks and any manual release checks.

Production does not require speculative enterprise architecture. Add controls only for a confirmed requirement or credible failure mode.

## Classification

Prefer the user's stated intended use. When it is unclear, infer a proposal from the brief and ask only if a different choice would materially change scope or verification.

Signals for `prototype` include "show the idea," "clickable demo," "test the concept," or explicit acceptance of temporary data.

Signals for `lean` include personal use, a small internal tool, a workshop result intended to keep working, or a small application expected to be usable and published quickly.

Signals for `production` include public launch, paying users, sensitive data, irreversible or high-impact actions, service commitments, regulated use, or operational dependence.

Authentication, a database, an SDK, or deployment alone does not force `production`. A lean product can need all four.

## Timebox

Record an explicit timebox when the brief supplies one or schedule pressure changes the plan. It may cover discovery through publication or only implementation, so state the boundary.

Use the timebox to:

- narrow the first-version journey and exclusions;
- prefer proven components and existing project conventions;
- combine documentation and slices that do not need separate ownership;
- schedule the highest-risk contract and deployment proof early;
- reserve time for a real happy-path smoke test and publication.

Do not convert the timebox into a promise based only on slice count. If the required profile cannot fit, present the smallest safe scope that can and name what moves later.

## What the profile controls

The profile controls implementation fidelity, slice shape, verification depth, review cadence, and release expectations. It does not directly choose the documentation package. Choose Compact, Standard, or Extended from information complexity and maintenance needs.
