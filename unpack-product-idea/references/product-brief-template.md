# Product Brief template

Use the user's language. Keep the core sections below. Add an optional section only when it contains information that can change the product, scope, or later planning.

```markdown
# [Project name]

## Summary

[What the product is, who it is for, and which result it provides.]

## Problem and current situation

[What prompts the need, how people handle it now, where that approach fails, and why the owner wants to solve it.]

## Intended users

### [Primary user or role]

- Goal: [what this person needs to accomplish]
- Context: [the relevant situation or experience]
- Key actions: [what this person does]

[Add another role only when it changes the main flow, access, payment, approval, or received result.]

## Main scenario

### [Outcome-oriented name]

- Actor: [role]
- Trigger: [event or need]
- Starting situation: [relevant context]
- Flow:
  1. [User action]
  2. [Product response]
  3. [Next action or decision]
- Successful result: [observable end state]
- Important exceptions: [only exceptions that change the product]

[Add another scenario only when the first version cannot be understood without it.]

## First-version scope

### Must have

- [Capability required for the complete main scenario]

### Later

- [Useful capability that is not required now]

### Out of scope

- [Deliberately excluded capability]

## Delivery expectations

- Intended use: [show an idea, use as a small working product, or release as a dependable public or operational product, in the user's terms]
- Time budget or deadline: [only when supplied or material]
- Non-negotiable quality: [real integration, deployment, privacy, reliability, or another expectation that must survive scope reduction]
- Acceptable temporary compromises: [only compromises the user explicitly accepted]

## Core information

### [Business object]

- Meaning: [what it represents]
- Created or supplied by: [role or external source]
- Used for: [role in the scenario]
- Ownership or lifecycle: [only when relevant]

## Constraints and dependencies

- [Confirmed platform, device, language, connectivity, privacy, accessibility, deadline, budget, integration, or specialist-review constraint]

## Success criteria

- [Observable user or owner outcome]

## Decisions

- [Only statements made or confirmed by the user]

## Assumptions

- [Unconfirmed working hypothesis]. Impact if wrong: [what would change]

## Open questions

- [Specific unresolved decision]. Why it matters: [affected scope, journey, risk, or business behavior]
```

Optional sections include business model, distribution, integrations, secondary journeys, accessibility, privacy, and specialist review. Add them when they carry real content. Do not keep an empty heading or write `Not applicable` unless omission could be misleading.

## Final check

Before delivery, confirm that:

- a reader can explain the product and audience in one sentence;
- at least one scenario runs from trigger to useful result;
- every must-have capability supports that scenario;
- later work and exclusions are distinct;
- intended use and any material timebox are visible without implying unapproved shortcuts;
- business objects are described without database design;
- constraints are confirmed or labeled as assumptions;
- success criteria are observable and contain no invented targets;
- decisions, assumptions, and open questions are not mixed;
- no frameworks, APIs, schemas, screens, or implementation plans entered the brief.
