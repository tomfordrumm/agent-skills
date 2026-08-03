# Product Brief template

Use the user's language. Keep headings even when brief content underneath is concise. Omit a section only when it is genuinely irrelevant and its omission cannot create ambiguity.

```markdown
# [Project name]

## 1. Summary

[One or two sentences: what the product is, who it serves, and what result it provides.]

## 2. Project goal

[Why the owner wants to create this product and what outcome the project should produce.]

## 3. Problem and current situation

[The user's situation, current alternative, pain or limitation, and why it matters.]

## 4. Target audience

### Primary audience

[Who experiences the problem first or most strongly, including relevant context and needs.]

### Secondary audience

[Only if relevant.]

## 5. Users and roles

### [Role]

- Goal: [what this role wants]
- Key actions: [what this role does]
- Relationship to other roles: [only if relevant]

## 6. Product value

[The concrete result and why it is better than the current alternative.]

## 7. Main usage scenarios

### Scenario 1: [Outcome-oriented name]

- Actor: [role]
- Trigger: [event or need]
- Starting situation: [relevant context]
- Steps:
  1. [User action]
  2. [Product response]
  3. [Next action or decision]
- Successful result: [observable end state]
- Important exceptions: [only material exceptions]

### Scenario 2: [Name]

[Add only when another scenario is necessary to understand the first version.]

## 8. Primary user journey

1. [From first contact or opening]
2. [Setup or required input]
3. [Core action]
4. [Product response]
5. [Moment the user receives value]

## 9. First version scope

### Must have

- [Capability required for the complete primary journey]

### Later

- [Useful future capability that is not required now]

### Explicitly out of scope

- [Deliberately excluded capability]

## 10. Core information

### [Business object]

- Meaning: [what it represents]
- Created or supplied by: [role or external source]
- Used for: [role in the scenario]
- Important lifecycle note: [only if relevant]

## 11. Integrations and external participants

- [Service or participant]: [why it is needed and what information or action crosses the boundary]

## 12. Business model and owner value

[Who pays and for what, or another owner outcome such as saved time, reduced cost, learning, or personal utility. State when monetization is intentionally undecided or absent.]

## 13. Constraints and considerations

- Platforms and devices: [confirmed constraint or assumption]
- Language and geography: [if relevant]
- Privacy and sensitive data: [if relevant]
- Accessibility and connectivity: [if relevant]
- Time or budget: [only user-supplied constraints]
- Specialist review: [legal, safety, medical, financial, or other review if needed]

## 14. Success criteria

- [Observable user outcome or behavior]
- [Observable owner or operational outcome]

## 15. Decisions

- [Only statements explicitly made or confirmed by the user]

## 16. Assumptions

- [Unconfirmed working hypothesis] — Impact if wrong: [what would change]

## 17. Open questions

- [Specific unresolved decision] — Why it matters: [affected scope, journey, risk, or business behavior]
```

## Final quality check

Before delivery, verify:

- A reader can explain the product in one sentence.
- The primary audience is narrower than “everyone.”
- At least one scenario runs from trigger to user value.
- Every must-have capability supports that scenario.
- Later and out-of-scope items are distinct.
- Core information is described without database design.
- Constraints are confirmed or clearly labeled assumptions.
- Success criteria are observable and contain no invented targets.
- Decisions, assumptions, and open questions are not mixed.
- No frameworks, APIs, schemas, screen designs, or implementation plans slipped into the brief.
