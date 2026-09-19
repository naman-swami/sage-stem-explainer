# Sage — STEM Explainer Agent

Sage is a STEM concept-explanation agent, defined using the [OpenGAP](https://github.com/open-gitagent/opengap)
standard so it can run portably across multiple agent frameworks
(OpenAI SDK, CrewAI, Claude Code, Lyzr) from a single identity
definition.

Sage originates from the QUMA AI multi-agent platform, where it is
one persona among several (alongside agents focused on research,
practice problems, and content generation). This repository extracts
Sage's identity, rules, and explainability documentation into a
framework-agnostic, git-native format.

## Files

- `agent.yaml` — manifest: name, version, model preference
- `SOUL.md` — identity, personality, communication style, values
- `DUTIES.md` — role definition
- `AGENTS.md` — framework-agnostic fallback system prompt
- `EXPLAINABILITY.md` — how Sage decides, what data it uses, its
  known limitations

## Validate & Export

```bash
npm i -g @open-gitagent/opengap
opengap validate
opengap export --format claude-code
```

## License

MIT
