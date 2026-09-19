# OpenAI Assistants SDK Export

This directory contains the export configuration for deploying Sage as an OpenAI Assistant via the OpenAI v2 Assistants API.

## Overview

The configuration in [`config.json`](config.json) specifies:
- Model selection: `gpt-4o` with low temperature for deterministic step-by-step reasoning
- Complete system instructions encapsulating Sage's `SOUL.md` persona, `RULES.md` behavioral constraints, and `DUTIES.md` maker-checker obligations
- Declarative JSON Schema definitions for all 7 tools:
  - `check_step_logic`
  - `lookup_reference`
  - `validate_math`
  - `generate_diagram`
  - `assess_understanding`
  - `translate_concept`
  - `fetch_reference`

## Quick Start

### 1. Install OpenAI SDK

```bash
pip install openai
```

### 2. Configure Environment

```bash
export OPENAI_API_KEY="your-api-key"
```

### 3. Deploy Assistant via Python

Use this script to create or update your Sage Assistant on OpenAI:

```python
import json
import os
from openai import OpenAI

client = OpenAI()

# Load the export configuration
with open("exports/openai-sdk/config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# Create the Assistant
assistant = client.beta.assistants.create(
    name=config["name"],
    instructions=config["instructions"],
    model=config["model"],
    tools=config["tools"],
)

print(f"Created Sage Assistant with ID: {assistant.id}")
```

### 4. Running a Conversation Thread

```python
# Create a thread
thread = client.beta.threads.create()

# Add a user question
client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Why does a spinning bicycle wheel resist falling over? Explain with angular momentum."
)

# Run the assistant
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id
)

# Retrieve messages
if run.status == "completed":
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    print(messages.data[0].content[0].text.value)
```