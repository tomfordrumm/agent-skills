# Interview map

Use this map to find the next useful question. It is not a questionnaire. Skip any area that cannot change the product or first-version scope.

## Product and problem

Establish what the product lets someone accomplish, why the owner wants it, and what situation creates the need.

Ask how people handle the situation today and where that approach fails. Capture the problem as the owner's hypothesis unless supplied research supports it. Market validation is separate work.

Useful question:

> Представьте, что продукт уже работает. Что человек теперь может сделать такого, что сегодня для него сложно или невозможно?

Turn broad value claims into observable change. Replace "easy" or "convenient" with time saved, errors avoided, a completed task, a clearer decision, or access that did not exist before.

## Audience and roles

Find the people who encounter the problem first or most often. Behavior and context matter more than invented demographic personas.

If the answer is "everyone," ask:

> Для кого эта проблема возникает чаще всего? Кому вы показали бы первую версию в первую очередь?

Separate the user from the buyer, approver, administrator, provider, or recipient only when those roles change the flow. For each relevant role, establish what they want, what they can see or change, and how their action affects someone else.

When accounts or authentication appear, identify the actual isolation model:

- one person uses the product;
- several people share one account or one common data space;
- each person has a separate private account and data;
- people collaborate inside a shared workspace with different permissions.

Do not turn "users need to sign in" into a multi-user or collaboration requirement without this distinction.

## Main scenario

Reconstruct at least one real case from trigger to useful result:

1. who acts;
2. what starts the situation;
3. what the person does and what information they provide;
4. how the product responds;
5. which decisions or exceptions matter;
6. what successful completion looks like.

Ask through a story:

> Возьмем один реальный случай. Что произошло перед тем, как человек открыл приложение, что он делает дальше и с каким результатом уходит?

Identify the business objects that appear in this scenario, such as a task, booking, request, payment, document, message, or result. Describe their meaning, ownership, visibility, and lifecycle. Do not design tables or fields.

## First useful version

Classify candidate capabilities as:

- `must_have` when the main scenario cannot produce its result without them;
- `later` when they add value but are unnecessary for the first complete result;
- `out_of_scope` when exclusion protects the first version from ambiguity or expansion.

Useful question:

> Если через неделю готова только самая простая законченная версия, что она обязана позволить человеку сделать, чтобы вы сказали: "Да, это уже решает проблему"?

When the feature list is large, choose the first complete journey. A disconnected demo is not an MVP.

## Delivery expectations

Clarify what the owner expects to do with the first version when the answer could change scope or quality. Ask in ordinary language, for example:

> После первой версии вы хотите только показать идею, начать пользоваться приложением сами или выпустить его для людей, которые будут на него полагаться?

Useful distinctions are:

- a demonstration used to explain or test an idea, where visible temporary substitutes may be acceptable;
- a small working product intended for real use, with the main journey, real required integrations, and deployment working;
- a dependable public, commercial, sensitive, or operational product that needs deeper release checks and support considerations.

Do not assign a technical delivery profile during discovery. Record the user's intended use, required quality, and any acceptable temporary compromise in their own terms.

Treat time as a separate constraint. If urgency, a workshop, a deadline, or an expectation of a very small build is mentioned but no usable limit is known, ask how much time is available from planning through a usable result. Do not ask for a time budget when it cannot change the first-version boundary. Never infer that a short timebox permits fake integrations, unsafe handling, or hidden limitations.

## Business context and success

Ask about money, distribution, or organizational value only when it affects product behavior or scope. Useful facts may include who pays, when payment happens, whether the goal is revenue or saved labor, and how the first users will reach the product.

Do not invent pricing, monetization, or target numbers.

Define success through observable behavior or outcome. Examples include completing the main journey, returning to use the product, reducing manual steps, or producing an acceptable result.

## Integrations, constraints, and risk

Explore an external service only when the product depends on it. Ask what crosses the boundary and what happens when the service fails. Keep a confirmed vendor as a constraint, but do not select one during discovery.

Ask about constraints that can change the product:

- device, connectivity, language, geography, or accessibility;
- a deadline, timebox, or budget that can change the first version;
- sensitive personal, financial, health, child, or company data;
- legal, safety, moderation, consent, retention, or human-review needs known to the user.

Do not make legal, medical, or financial conclusions. Record the need for specialist review.

## Conditional branches

Use only the branch that matches the idea.

### Marketplace

Clarify both sides, discovery or matching, the transaction, trust, disputes, cancellation, and what happens when one side does not respond.

### Internal tool or automation

Clarify the current workflow, source of truth, handoffs, approvals, exceptions, trigger, output, side effects, failure handling, and human override.

### AI-assisted product

Clarify input, context source, expected output, acceptable error, prohibited output, human review, correction, and fallback. Check whether AI is necessary to the outcome or merely a proposed implementation detail.

### User-generated or social content

Clarify identity, visibility, interaction, reporting, moderation, blocking, and harmful-content risk.

### Payments, bookings, or logistics

Clarify payer or participant, timing, confirmation, capacity or availability, cancellation, refunds when relevant, failure states, and who updates status.

### High-stakes use

Clarify the harm from a wrong result, who verifies it, audit needs, consent, access, retention, deletion, and escalation. Preserve uncertainty and recommend expert review.

## Check each question

Before asking, confirm that the answer can change the concept, main flow, or first-version scope. Do not ask for information the user already supplied, push a feature, or require outside research.

Prefer "What happens when...?" and "Walk me through..." to "Do you need feature X?"
