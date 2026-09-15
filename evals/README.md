# Skill behavior checks

Use `scenarios.json` when changing a relevant workflow or choosing a new model
baseline. Pick affected cases; do not run the whole set for every wording edit.

Create small fixture repositories in temporary directories from each case's setup.
Give the evaluated agent the request, fixture, and selected skill, without the scoring
checks. For negative invocation cases, expose the skill catalog but do not explicitly
load the skill. Score observable actions and artifacts against `checks`, not matching
phrases. A decision walkthrough can reveal contradictions but does not prove tool
execution, implicit selection, concurrency, or release behavior.

For a model or effort comparison, run the same fixtures and authorization on both
configurations. Keep skill revision, tools and context fixed when testing a model;
keep the model fixed when testing a skill revision. Repeat failures or ambiguous
outcomes before attributing them to the change. Use temporary branches and no live
services. Do not publish, send messages, or consume reset credits during evaluation.

Record case ID, skill revision, model and effort, outcome, artifact paths, missed
checks, user interventions, retries, tool/worker counts, and elapsed time. Record token
usage only when telemetry exposes it; otherwise use `unavailable`. Accept a cheaper
baseline only when the required behavior remains correct across the relevant cases.
Do not claim token savings from a shorter prompt or a lower effort label alone.
