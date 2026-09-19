# OpenGAP Framework Export Adapters

OpenGAP provides a standardized way to define AI agents. To run these agents in different orchestration frameworks, we use **Export Adapters**.

This directory contains adapters for building your OpenGAP repository into framework-specific deployable artifacts.

## Architecture

All adapters inherit from `BaseAdapter` defined in `base_adapter.py`. An adapter's primary responsibilities are:
1. `parse_opengap_repo()`: Reads `agent.yaml`, `SOUL.md`, `RULES.md`, tools, and skills from the source repository.
2. `compile_tools()`: Maps OpenGAP YAML tools to framework-specific tool registries.
3. `compile_persona()`: Compiles identity and rules into the framework's prompt format.
4. `emit_artifacts()`: Generates executable code and configuration.

## Included Adapters

### Lyzr Adapter
Compiles the OpenGAP definition into a Lyzr ADK/Studio compatible format.
```bash
python lyzr_adapter.py --repo ../ --out ../exports/lyzr
```

### LangGraph Adapter
Compiles the OpenGAP definition into a LangGraph ReAct agent.
```bash
python langgraph_adapter.py --repo ../ --out ../exports/langgraph
```

## Contributing a New Adapter

To write a new framework adapter for OpenGAP:
1. Create a new Python file `myframework_adapter.py`.
2. Subclass `BaseAdapter`.
3. Implement `compile_tools()`, `compile_persona()`, and `compile_agent()`.
4. Ensure it has a standard CLI `python myframework_adapter.py --repo <path> --out <path>`.
5. Submit a Pull Request upstream to the OpenGAP community!
