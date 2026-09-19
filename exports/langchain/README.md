# LangChain / LangGraph Export

This directory contains the export implementation for running Sage as a stateful, tool-calling ReAct agent using **LangChain** and **LangGraph**.

## Overview

The export in [`agent.py`](agent.py) features:
- Implementation of modern `langgraph.prebuilt.create_react_agent`
- Full mapping of Sage's 7 MCP tool contracts into LangChain `@tool` definitions:
  1. `check_step_logic`: Formal reasoning and invariant checker
  2. `lookup_reference`: STEM reference text search
  3. `validate_math`: Numerical, algebraic, and calculus verification
  4. `generate_diagram`: Diagram specification generator (Mermaid / LaTeX / ASCII)
  5. `assess_understanding`: Targeted comprehension query builder
  6. `translate_concept`: Bilingual terminology-preserving translator
  7. `fetch_reference`: High-confidence academic citation retrieval
- Embedded system persona reflecting Sage's `SOUL.md` and `RULES.md`

## Quick Start

### 1. Install Dependencies

```bash
pip install langchain-openai langgraph langchain-core
```

### 2. Configure Environment

```bash
export OPENAI_API_KEY="your-api-key"
```

### 3. Run the Agent

You can test the agent locally using:

```bash
python exports/langchain/agent.py
```

### 4. Interactive Programmatic Usage

```python
from exports.langchain.agent import get_sage_agent

app = get_sage_agent()

# Execute a STEM explanation query
query = "Explain how eigenvalues and eigenvectors relate to principal component analysis."
inputs = {"messages": [("user", query)]}

for chunk in app.stream(inputs, stream_mode="values"):
    message = chunk["messages"][-1]
    print(f"[{message.type}]: {message.content}\n")
```

## Production Notes
- Uses LangGraph's state graph architecture, allowing persistence, human-in-the-loop checkpoints, and time-travel debugging.
- Tools adhere strictly to the parameter schemas specified in `tools/*.yaml`.