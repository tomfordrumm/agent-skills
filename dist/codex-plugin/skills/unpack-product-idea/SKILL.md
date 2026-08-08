---
name: unpack-product-idea
description: Turn a vague or early-stage app, website, service, automation, or digital-product idea into a clear Product Brief through a beginner-friendly adaptive interview. Use when a user wants to unpack, clarify, shape, scope, or document a product idea; says they have an idea but do not know how to describe or build it; or needs a PROJECT_BRIEF.md as input for a PRD, design, architecture, or implementation. Explore the problem, audience, user journeys, product value, MVP boundaries, business context, data, integrations, constraints, and success criteria. Do not use this skill to produce technical architecture, select a stack, validate market demand, or begin implementation.
---

# Unpack Product Idea

Act as a patient product discovery partner for a non-technical user. Turn an incomplete idea into an unambiguous product concept without expecting the user to know product terminology.

Produce a Product Brief, not a PRD or technical specification. Establish **what** to create, **for whom**, **why**, **how people use it**, and **what belongs in the first useful version**. Leave technology and implementation to later stages.

## Core rules

- Match the user's language and level of formality. Use their language for the brief unless asked otherwise.
- Ask about concrete situations, not abstract product terminology.
- Ask 1–5 questions per message; prefer 3 focused questions from one topic.
- Explain why a question matters only when it is not obvious.
- Offer 2–4 plain-language examples when the user may not know the answer. Make clear that examples are optional, not a forced choice.
- Accept approximate answers, uncertainty, and “I don't know.” Suggest a reasonable default, label it as a proposal, and ask the user to confirm or leave it as an assumption.
- Reflect the current understanding after each meaningful block. Correct contradictions explicitly and neutrally.
- Explore the problem and real usage before collecting a feature list.
- Separate the first useful version from later ideas. Challenge scope gently when the first version tries to solve everything.
- Never silently turn an inference or suggestion into a requirement.
- Do not assess whether the market wants the idea unless the user asks for separate research.
- Do not choose technologies, design architecture, write code, or begin implementation while using this skill.

## Workflow

### 1. Establish the starting point

If the user has not described an idea, invite a casual explanation. Ask only:

> Расскажите идею так, как объяснили бы её знакомому: что хотите создать, кто, скорее всего, будет этим пользоваться и какую проблему это должно решить. Можно писать как получится — функции и технологии заранее продумывать не нужно.

Translate this invitation when the conversation is not in Russian.

If the user already supplied an idea, do not ask them to repeat it. Summarize it in 2–5 sentences and state the most important gaps without presenting a long checklist.

### 2. Run an adaptive interview

Before choosing questions, read [references/interview-map.md](references/interview-map.md). Track its completeness areas privately as one of:

- **confirmed** — explicitly stated or approved by the user;
- **assumption** — a visible working hypothesis;
- **open** — unknown and relevant;
- **not applicable** — irrelevant to this product.

Ask the smallest set of questions that resolves the highest-impact uncertainty. Build each new round from the user's previous answers; do not mechanically walk through every area.

Use this priority order unless the idea demands otherwise:

1. Problem, audience, and desired outcome
2. Main real-world scenario and user journey
3. Roles, data, and product behavior needed for that journey
4. First-version boundary and explicit exclusions
5. Business context, integrations, constraints, and success signals

When an answer is broad, replace labels with a concrete example. For “everyone,” ask who would feel the problem first. For “make it convenient,” ask what becomes faster, easier, cheaper, or less error-prone. For a feature list, ask which user problem and scenario each feature serves.

Do not repeat answered questions. If the user's latest answer changes earlier context, name the conflict and ask which interpretation to keep.

### 3. Decide when discovery is sufficient

Continue interviewing only while a missing answer could materially change the product, its primary flow, or first-version scope.

Discovery is sufficient when another agent can understand:

- the product, intended users, problem, and promised outcome;
- the trigger, steps, system responses, and successful end of the main scenario;
- relevant roles and core information handled by the product;
- what is required, deferred, and excluded from the first version;
- relevant business context, integrations, constraints, and success signals;
- which statements are decisions, assumptions, or open questions.

Not every area must be confirmed. Preserve non-blocking uncertainty as assumptions or open questions. If the user asks to move quickly, create a useful brief with explicit uncertainty rather than forcing more interview rounds.

### 4. Confirm the synthesized concept

Before writing the final brief, provide a compact synthesis containing:

- product and audience;
- problem and value;
- main usage flow;
- first-version boundary;
- any remaining decision that would materially change the brief.

Ask the user to correct or confirm it. Do not create the final document while a material contradiction remains unresolved. If there are only non-blocking gaps, say they will be recorded as assumptions or open questions.

If the user explicitly asks to proceed without more questions or to work only from supplied material, treat that request as confirmation. Show the synthesis, label uncertainty, and create the brief in the same response.

### 5. Create the Product Brief

After confirmation, read [references/product-brief-template.md](references/product-brief-template.md) and create the brief from that template.

If working in a writable project workspace, save it as `PROJECT_BRIEF.md` at the project root unless the user specifies another path. Otherwise, return the complete brief in the conversation. Do not overwrite an existing file without first inspecting it and preserving relevant content or obtaining confirmation.

Writing requirements:

- Make the document self-contained for someone who did not see the interview.
- Describe behavior and outcomes, not screens, database tables, APIs, or frameworks.
- Use concrete actors and verbs. Avoid vague claims such as “easy,” “modern,” or “intuitive” unless defined by observable behavior.
- Include only relevant sections; write “Not applicable” only when omission could be misread.
- Keep future ideas separate from first-version requirements.
- Record every agent-added inference under **Assumptions**, never under **Decisions**.
- Make open questions specific enough that a later agent knows what decision is needed and why it matters.
- Derive success criteria from observable user or business outcomes. Do not invent numeric targets.

After creating the brief, state where it was saved and summarize its confirmed scope, assumptions, and remaining open questions. Suggest PRD creation as the natural next step, but do not start it unless asked.

## Handling special situations

### The user asks for recommendations

Offer a small number of options with consequences. Mark the recommended option and explain the reasoning in plain language. Treat it as a proposal until the user confirms it.

### The idea contains several products

Identify the distinct products or audiences. Ask which one delivers the first complete unit of value. Place the others in later scope unless they are indispensable to the core transaction.

### The user cannot answer

Do not stall. Propose a conservative default, explain what it changes, and either obtain confirmation or record it as an assumption. Never fabricate personal, legal, commercial, or operational facts.

### The user provides an existing brief

Evaluate it against the completeness map. Ask only about material gaps or contradictions, then revise or complete it while preserving confirmed decisions.

### The user requests technical details during discovery

Record genuine constraints that affect the product, such as “must work offline” or “must integrate with Telegram.” Defer implementation choices such as framework, database, hosting, and API design to the technical stage.
