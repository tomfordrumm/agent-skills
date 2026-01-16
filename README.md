# AgentSkills

Open skills that improve the quality of interaction with LLM CLI agents.

## Who this is for

People using CLI agents like Codex, Claude Code, or any LLM agent that supports the open skills format.

## Skills

- `dig` - Investigation-only mode for understanding bugs, features, or system behavior without making changes.
- `adr-logger` - Log an Architectural Decision Record (ADR) entry while the agent is working.

## Getting started

Install skills with your agent's installer and a GitHub URL:

- https://agentskills.io/integrate-skills
- https://developers.openai.com/codex/skills/
- https://code.claude.com/docs/en/skills

## Repository structure

- `dig/` and `adr-logger/` contain the source skill definitions (`SKILL.md`).
- `dist/` contains packaged `.skill` archives for distribution.

## Contributing

Issues and pull requests are welcome. Please keep skill instructions concise and focused.

## License

MIT. See `LICENSE`.
