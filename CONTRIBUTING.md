# Contributing to Sage

We welcome contributions to expand Sage's capabilities, add new skills, and improve explanation quality. Follow these guidelines to contribute effectively.

## Adding New Skills

Skills are modular capabilities that Sage can use. To add a new skill:
1. Create a new directory in `skills/` (e.g., `skills/visual-analogies/`).
2. Include a `SKILL.md` containing the YAML frontmatter (name, description, required context) and detailed instructions for the LLM on how to execute the skill.
3. Ensure the skill adheres to the OpenGAP specification.

## Adding New Tools

Tools provide external capabilities via MCP (Model Context Protocol).
1. Add the tool definition to `tools/`.
2. Provide standard JSON schema for inputs and outputs.
3. Document the tool in a corresponding Markdown file, clearly stating its limitations and error handling procedures.

## Adding New Sub-Agents

If introducing a new sub-agent (e.g., a dedicated `Translator` or `MathSolver`):
1. Create a directory in `agents/`.
2. Must include `agent.yaml`, `SOUL.md`, and `DUTIES.md`.
3. Update `ARCHITECTURE.md` to reflect the new workflow.

## Testing Requirements

All changes must be validated against existing calibration examples.
- **Regression Testing**: Ensure the `Reviewer` agent still correctly identifies errors injected into test prompts.
- **Example Updates**: If changing the core output format, update all `examples/*.md` files to reflect the new structure.

## Code Style Guide

- Markdown files should be formatted cleanly. Use 80-character line limits where possible.
- Use explicit headings and avoid deep nesting (no deeper than H4).
- Adhere strictly to the Maker/Checker segregation rules in all implementations.

## Pull Request Process

1. Fork the repository and create a feature branch.
2. Submit a PR outlining the change, the reasoning, and a test run log.
3. At least one core maintainer must review and approve the PR.
