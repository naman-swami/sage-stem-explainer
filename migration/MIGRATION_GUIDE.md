# OpenGAP Agent Migration Guide

## 1. Why Agent Migration is Necessary
As the AI agent ecosystem evolves, organizations often face framework lock-in. Agents built in early frameworks (like LangChain, CrewAI, or AutoGen) are tightly coupled to those runtimes, making it difficult to upgrade models, swap orchestration engines, or share agents across different parts of an organization.

**Open Git Agent Protocol (OpenGAP)** solves this by providing a standard, declarative, and framework-agnostic way to define agents. Migrating to OpenGAP ensures:
- **Portability**: Run your agent on any compatible orchestration engine.
- **Maintainability**: Separate concerns (identity, rules, tools) into version-controlled markdown and yaml.
- **Interoperability**: Connect tools via the Model Context Protocol (MCP) standard instead of proprietary python bindings.

## 2. Mapping Framework Concepts

### CrewAI to OpenGAP
CrewAI heavily relies on configuration properties that map directly to OpenGAP's core files:
- **`role` and `goal`** -> `agent.yaml` metadata.
- **`backstory`** -> `SOUL.md` (Identity and personality).
- **`allow_delegation`** -> Translated to workflow boundaries or `RULES.md`.

### LangChain to OpenGAP
LangChain uses functional pipelines and prompts. Migration focuses on extraction:
- **`SystemMessage` / `PromptTemplate`** -> `SOUL.md` (Identity) and `RULES.md` (Instructions).
- **`@tool` functions** -> Must be extracted into declarative YAML contracts in the `tools/` directory.

## 3. Handling Tools & MCP
In legacy frameworks, tools are Python functions or API calls directly bound to the agent. OpenGAP requires tool contracts to be defined in MCP-compatible YAML formats.

**Example Migration:**
*LangChain (Before)*:
```python
@tool
def search(query: str) -> str:
    "Searches the web"
    ...
```

*OpenGAP (After)* - `tools/search.yaml`:
```yaml
name: search
description: Searches the web
parameters:
  type: object
  properties:
    query:
      type: string
```

The underlying execution logic is handled by the framework runtime mapped to the tool interface.

## 4. Verifying Migrated Agents
Once an agent is migrated, you must validate the OpenGAP package:
1. **Schema Check**: Ensure `agent.yaml` and tool definitions comply with the OpenGAP schema.
2. **Completeness**: Verify `SOUL.md`, `RULES.md`, and `DUTIES.md` exist.
3. **Mock Run**: Use a test orchestrator to ensure the agent parses its identity and invokes tools correctly using the provided standard context.
