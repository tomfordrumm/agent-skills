# AgentSkills

Open skills that improve the quality of interaction with LLM CLI agents.

## Who this is for

People using CLI agents like Codex, Claude Code, or any LLM agent that supports the open skills format.

## Skills

- `dig` - Investigation-only mode for understanding bugs, features, or system behavior without making changes.
- `adr-logger` - Log an Architectural Decision Record (ADR) entry while the agent is working.
- `sviat-engineering` - Senior engineering thinking, development, debugging, and review process.
- `unpack-product-idea` - Turn a vague product idea into a clear Product Brief through a beginner-friendly adaptive interview.
- `easy-prd` - Turn a Product Brief into an implementation-ready PRD, adaptive documentation, and vertical delivery slices.
- `adhd-manager` - Orchestrate a changing stream of development tasks through isolated subagents while the main chat manages priorities, dependencies, and assumptions.

## Getting started

Install skills with your agent's installer and a GitHub URL:

- https://agentskills.io/integrate-skills
- https://developers.openai.com/codex/skills/
- https://code.claude.com/docs/en/skills

### Codex plugin

The curated Codex plugin is built from the allowlist in
`packaging/codex-plugin.json`:

```bash
python3 scripts/build_codex_plugin.py
python3 scripts/build_codex_plugin.py --check
```

To add this repository as a Codex plugin marketplace, run
`codex plugin marketplace add tomfordrumm/agent-skills`, then install the
plugin with `codex plugin add agent-skills@agent-skills`. Upgrade the
marketplace with `codex plugin marketplace upgrade agent-skills`.

The existing `dist/*.skill` archives remain available for individual skill
installation. Edit the allowlist when the Codex plugin should expose a
different subset of the repository.

## Repository structure

- Top-level skill directories contain the source skill definitions.
- `dist/` contains packaged `.skill` archives for distribution.
- `dist/codex-plugin/` contains the generated curated Codex plugin bundle.
- `.agents/plugins/marketplace.json` exposes that bundle through the repository marketplace.

## Contributing

Issues and pull requests are welcome. Please keep skill instructions concise and focused.

## License

MIT. See `LICENSE`.
