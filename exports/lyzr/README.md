# Lyzr Framework Export

This directory contains the export configuration for deploying Sage onto the [Lyzr](https://lyzr.ai) agent platform, integrating with Lyzr Studio and the Lyzr Agent Development Kit (ADK).

## Overview

The export in [`agent_config.py`](agent_config.py) defines:
- A production-ready agent definition configured for Lyzr's multi-agent runtime
- Explicit tool binding for all 7 STEM verification tools
- Embedded guardrails and pedagogical prompt engineering aligned with `SOUL.md` and `RULES.md`
- Multi-step workflow orchestration supporting first-principles derivations and maker-checker validation

## Quick Start

### 1. Install Dependencies

```bash
pip install lyzr
```

### 2. Set Up API Credentials

```bash
export LYZR_API_KEY="your-lyzr-api-key"
export OPENAI_API_KEY="your-openai-api-key"
```

### 3. Run or Register the Agent

Execute the configuration script to instantiate or register the agent:

```bash
python exports/lyzr/agent_config.py
```

### 4. Programmatic Inference

```python
from exports.lyzr.agent_config import create_sage_agent

# Initialize the Lyzr Agent
sage = create_sage_agent()

# Run a first-principles explanation query
response = sage.run("Derive the time-dilation formula from the speed-of-light constancy principle.")
print(response)
```

## Platform Advantages with Lyzr
- **Built-in Governance**: Lyzr's safety layers enforce PII redaction and prompt-injection defense.
- **Enterprise Observability**: Full execution tracing and latency monitoring for every step in the concept breakdown.
- **Modular Studio Integration**: Agents configured in code can be imported into Lyzr Agent Studio for visual DAG orchestration.