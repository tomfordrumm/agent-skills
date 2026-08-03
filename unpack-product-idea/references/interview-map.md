# Adaptive interview map

Use this map to choose questions, not as a questionnaire. Ask only about relevant uncertainty and phrase questions in the user's language.

## Completeness areas

### 1. Product essence

Determine:

- what the product enables someone to accomplish;
- why the owner wants to create it;
- whether it is a personal tool, internal tool, customer product, marketplace, community, or automation.

Useful question:

> Представьте, что приложение уже работает. Что человек теперь может сделать такого, что сегодня для него сложно или невозможно?

### 2. Problem and current alternative

Determine:

- what situation creates the problem;
- how people handle it today;
- what is slow, costly, confusing, risky, or impossible about the current method;
- why solving it matters.

Useful question:

> Как человек решает эту задачу сейчас и в какой момент понимает, что нынешний способ его не устраивает?

Do not require evidence of market demand. Capture claimed pain as the owner's hypothesis unless supported by supplied research.

### 3. Audience

Determine:

- who experiences the problem most acutely;
- their context, motivation, and relevant level of experience;
- who uses the product versus who buys or approves it.

If the answer is “everyone,” ask:

> Для кого эта проблема возникает чаще всего? Кому вы показали бы первую версию в первую очередь?

Do not invent demographic personas when behavior or context is more useful.

### 4. Product value and outcome

Determine:

- the result the user receives;
- why the result is better than the current alternative;
- what “success” looks like from the user's perspective.

Turn adjectives into observable change: less time, fewer errors, completed task, clearer decision, saved money, or access to something previously unavailable.

### 5. Main scenario

Reconstruct at least one end-to-end scenario:

1. Who acts?
2. What event or need starts the scenario?
3. What does the person do first?
4. What information do they provide or receive?
5. What does the product do in response?
6. What decisions, exceptions, or approvals occur?
7. What marks successful completion?
8. How often does this happen?

Ask through a story:

> Возьмём один реальный случай. Что произошло перед тем, как человек открыл приложение, что он делает дальше по шагам и с каким результатом уходит?

### 6. Users and roles

Explore roles only when more than one actor may create, review, approve, buy, sell, administer, or receive information.

Determine for each relevant role:

- what they want;
- what they can see or change;
- how their action affects another role.

Avoid technical permission matrices at this stage.

### 7. Core information

Identify the business objects handled by the scenario, such as a user, task, booking, request, payment, document, message, or result.

Ask what users create, receive, update, review, or retain. Describe meaning and lifecycle, not schemas or database fields.

### 8. First useful version

Classify capabilities into:

- **Must have** — without it, the main scenario cannot deliver its result;
- **Later** — valuable but unnecessary to prove the core outcome;
- **Explicitly out** — deliberately excluded to protect scope or avoid ambiguity.

Useful question:

> Если через неделю готова только самая простая законченная версия, что она обязана позволить человеку сделать, чтобы вы сказали: «Да, это уже решает проблему»?

When the list is large, ask which single complete journey should work first. Do not confuse “minimal” with a disconnected demo; the first version must deliver an end-to-end unit of value.

### 9. Business context

Ask only when relevant:

- who benefits and who pays;
- what is sold and when payment occurs;
- whether the goal is revenue, cost reduction, learning, lead generation, retention, or personal utility;
- how the owner expects the product to reach users.

Do not invent pricing or monetization. A project may intentionally have none.

### 10. Integrations and external actors

Explore services essential to the product outcome: payments, email, messaging, maps, calendars, AI models, files, import/export, company systems, or human operators.

Ask what information crosses the boundary and what happens when the external service fails. Do not select vendors unless an existing vendor is a confirmed constraint.

### 11. Constraints and risk

Ask only about constraints that can change product scope or experience:

- device or operating environment;
- language, geography, accessibility, or connectivity;
- deadline or budget boundary supplied by the user;
- sensitive personal, financial, health, child, or company data;
- legal, safety, moderation, or human-review needs known to the user.

Do not provide legal conclusions. Mark areas requiring specialist review.

### 12. Success signals

Determine what observable behavior or outcome would show the first version is useful. Examples include completing the main journey, returning to use it, reducing manual steps, or producing an acceptable result.

Do not invent target numbers. Record qualitative signals when no baseline or target exists.

## Adaptive branches

Use a branch only when the product matches it.

### Marketplace or two-sided product

Clarify supply and demand roles, discovery or matching, transaction flow, trust, disputes, cancellations, and what happens if one side does not respond.

### Internal tool

Clarify the current workflow, handoffs, source of truth, approvals, bottlenecks, exception handling, and who owns the result.

### AI-assisted product

Clarify input, context source, expected output, acceptable error, prohibited output, human review, feedback/correction, and fallback when the model is uncertain. Separate an essential AI capability from AI added only as a novelty.

### Social or user-generated content

Clarify who creates and sees content, visibility rules, identity, interaction, reporting, moderation, blocking, and harmful-content risks.

### Automation

Clarify trigger, input, rules or decisions, output, side effects, frequency, failure handling, retries, notification, and human override.

### Payments or subscriptions

Clarify payer, value purchased, timing, recurring versus one-time payment, trial or free tier if known, access after payment, cancellation, refund expectations, and failure states.

### Booking, logistics, or location

Clarify availability, time zones, capacity, confirmation, rescheduling, cancellation, no-shows, location accuracy, and which party updates status.

### Sensitive or high-stakes use

Clarify harm from an incorrect result, who verifies it, audit needs, consent, access, retention, deletion, and escalation. Preserve uncertainty and recommend expert review rather than making legal, medical, or financial claims.

## Question quality checks

Before sending a question, verify:

- The answer could change the concept, main flow, or first-version scope.
- The user has not already answered it implicitly or explicitly.
- It asks one understandable thing.
- It avoids professional jargon or explains it immediately.
- It does not push the user toward a feature or business model.
- It can be answered from the user's knowledge without outside research.

Prefer “What happens when…?” and “Walk me through…” over “Do you need feature X?”
