# Sage — STEM Explainer Agent

Sage is a STEM concept-explanation agent, defined using the [OpenGAP](https://github.com/open-gitagent/opengap)
standard so it can run portably across multiple agent frameworks
(OpenAI SDK, CrewAI, Claude Code, Lyzr) from a single identity definition.

Sage originates from the QUMA AI multi-agent platform, where it is one persona
among several. This repository extracts Sage's identity, rules, explainability
documentation, portable skills, tool contracts, and an independent reviewer into
a framework-agnostic, git-native format.

## Repository layout

- `agent.yaml` — root OpenGAP manifest
- `SOUL.md` — Sage's identity, personality, communication style, and values
- `DUTIES.md` — maker/checker segregation-of-duties policy
- `AGENTS.md` — framework-agnostic fallback system prompt
- `EXPLAINABILITY.md` — reasoning approach, inputs, and limitations
- `RULES.md` — hard behavioral constraints
- `tools/` — static MCP-compatible YAML input/output contracts
- `skills/` — portable skill instructions and a dependency-free reference script
- `agents/reviewer/` — independent checker sub-agent
- `examples/` — calibration examples for expected answer style

## Portability and interoperability

The root identity remains the portable source of truth. Tools are declared as
read-only schemas rather than implementations, so a host can map them to MCP,
function calling, or another framework without credentials. The concept-breakdown
skill is usable as a prompt module or as a deterministic workflow step. The
reviewer is deliberately separate from Sage to make the maker/checker boundary
visible to orchestrators.

## Validate and export

Run from the repository root:

```bash
npm i -g @open-gitagent/opengap
opengap validate
# Expected: validation succeeds with no errors.
opengap export --format claude-code
# Expected: export succeeds and produces the Claude Code-compatible output.
```

The commands above are the reproducible verification commands for this static
submission. Export output can vary by OpenGAP CLI version; no live model,
credential, or API call is required.

## License

MIT
