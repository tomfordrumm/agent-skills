---
name: unpack-product-idea
description: Turn an early product idea into a clear Product Brief through an adaptive interview. Use when a user needs help defining the problem, intended users, main journey, first-version scope, constraints, and success criteria before a PRD or implementation. Do not use for architecture, stack selection, market validation, or coding.
---

# Unpack product idea

Help a non-technical user explain what they want to create without requiring product vocabulary. The result is a Product Brief that defines the product, audience, problem, main use, first useful version, and delivery expectations. Technical design comes later.

## How to interview

- Match the user's language and level of formality.
- Ask about a concrete situation before asking for features.
- Ask only the questions needed for the largest current uncertainty. Keep a message to five questions or fewer.
- Give plain examples when the user may not know how to answer. Present them as examples, not fixed choices.
- Accept approximate answers and uncertainty. Offer a reasonable default when useful, label it as an assumption, and explain what would change if it is wrong.
- Reflect the current understanding after a meaningful block of answers. Name contradictions without blaming the user.
- Separate the first useful version from later ideas. Never turn an inference into a requirement.

Do not research market demand unless the user requests it separately. Do not choose technologies, design architecture, or begin implementation while using this skill.

## Start from what the user already provided

If no idea has been described, invite a casual explanation:

> Расскажите идею так, как объяснили бы ее знакомому. Что хотите создать, кто будет этим пользоваться и какую проблему это должно решить? Можно писать как получится, функции и технологии заранее продумывать не нужно.

Translate the invitation when the conversation is not in Russian.

If the user already described the idea, summarize it in a few sentences and ask about the most important gaps. Do not make them repeat it or present a full questionnaire.

## Run an adaptive interview

Read [references/interview-map.md](references/interview-map.md) before choosing questions. Use it as a private map, not as a sequence.

Track relevant areas as:

- `confirmed` when the user stated or approved the answer;
- `assumption` for a visible working hypothesis;
- `open` when an answer still matters;
- `not_applicable` when the area does not affect this product.

Start with the problem, audience, desired result, and one real usage story. Move to roles, information, integrations, constraints, business context, and delivery expectations only when they affect that story or the first-version boundary.

Before finalizing the first version, understand what the user expects to do with it. In plain language, distinguish a disposable demonstration, a small working product they intend to use, and a dependable public or operational release. Keep the desired result separate from an available time budget. Ask about either only when it remains unclear and the answer could change scope or acceptable tradeoffs.

When identity matters, distinguish one person, one shared account, separate private accounts, and people collaborating in the same workspace. Authentication by itself does not prove which model the product needs.

Replace broad labels with concrete cases. If the audience is "everyone," ask who feels the problem first. If the value is "convenience," ask what becomes faster, cheaper, safer, or less error-prone. If the input is a feature list, ask which problem and user action each feature supports.

Do not repeat answered questions. When a new answer conflicts with an earlier one, state both interpretations and ask which to keep.

## Know when to stop

Continue only while a missing answer could change the product, main flow, or first-version scope.

Discovery is sufficient when another agent can tell:

- who the product is for and which problem it addresses;
- what starts the main scenario and how the user reaches a useful result;
- which roles and information matter to that scenario;
- what belongs in the first version, later, and outside scope;
- which constraints or integrations can change the product;
- how the first version will be used and any material time budget;
- what is confirmed, assumed, or still open.

Not every area must be confirmed. If the user wants to move quickly, keep non-blocking gaps as explicit assumptions or open questions.

## Confirm and write the brief

Before writing, show a short synthesis of the product, audience, problem, main flow, MVP boundary, delivery expectations, and any unresolved choice that would materially change the brief. Ask for correction or confirmation.

If the user asks to proceed without more questions, that request counts as confirmation. Show the synthesis, label uncertainty, and create the brief in the same response.

After confirmation, read [references/product-brief-template.md](references/product-brief-template.md). Include only sections that carry useful information for this product.

Save the result as `PROJECT_BRIEF.md` at the project root when the workspace is writable, unless the user names another path. Inspect an existing file before updating it and preserve still-valid content.

The brief must stand on its own for a reader who did not see the interview. Describe actors, behavior, information, and observable outcomes. Keep future ideas separate from MVP requirements. Put agent-added inferences under Assumptions and user-confirmed statements under Decisions. Do not invent numeric targets.

After writing, report the path, confirmed scope, assumptions, and open questions. Mention PRD creation as the next likely step, but do not start it without a request.
