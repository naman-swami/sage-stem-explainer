# LangChain to OpenGAP Migration Guide

This directory contains tools to extract LangChain ReAct agents and export them to OpenGAP format.

## Before: LangChain
LangChain agents tightly couple prompts, model configurations, and python function tools inside python scripts. The logic is often bound to a specific runtime execution.

## After: OpenGAP
OpenGAP decouples the agent's identity, role, and tools from the runtime logic:
- The system prompt maps to `SOUL.md` and `RULES.md`.
- Python `@tool` functions are extracted into standardized JSON Schema / MCP-compatible YAML tools in a `tools/` directory.

## Usage

Run the migration script against a Python file containing LangChain agents:

```bash
python migrate_langchain.py --input sample_langchain_agent.py --output exported_agent/
```

This will extract the system message into `SOUL.md` and generate YAML contracts for each discovered tool.
