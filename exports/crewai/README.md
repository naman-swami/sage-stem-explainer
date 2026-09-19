# CrewAI Multi-Agent Export

This directory contains the declarative multi-agent hierarchy definition for running Sage and its sub-agents within the [CrewAI](https://crewai.com) framework.

## Overview

The export definition in [`crew.yaml`](crew.yaml) maps the OpenGAP agent architecture directly into CrewAI's declarative schema:
- **`sage`**: Primary STEM concept explainer (First-principles reasoning)
- **`reviewer`**: Independent fact-checker and pedagogical evaluator
- **`tutor`**: Adaptive tutor managing learner progression and practice problem generation
- **`researcher`**: Grounding and reference verification agent
- **`visualizer`**: Diagram, Mermaid chart, and LaTeX equation generator
- **`translator`**: Bilingual translation specialist (English ↔ Hindi)

## Quick Start

### 1. Install CrewAI

```bash
pip install crewai crewai-tools
```

### 2. Set Up API Credentials

```bash
export OPENAI_API_KEY="your-api-key"
# or export GROQ_API_KEY / ANTHROPIC_API_KEY
```

### 3. Execution Example

You can load and run the crew using the following Python runner:

```python
import yaml
from crewai import Agent, Task, Crew, Process

# Load agents and tasks configuration
with open("exports/crewai/crew.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# Instantiate Agents
agents_dict = {}
for agent_id, agent_cfg in config["agents"].items():
    agents_dict[agent_id] = Agent(
        role=agent_cfg["role"],
        goal=agent_cfg["goal"],
        backstory=agent_cfg["backstory"],
        verbose=agent_cfg.get("verbose", True),
        allow_delegation=agent_cfg.get("allow_delegation", False),
    )

# Instantiate Tasks
tasks_list = []
for task_id, task_cfg in config["tasks"].items():
    assigned_agent = agents_dict[task_cfg["agent"]]
    tasks_list.append(
        Task(
            description=task_cfg["description"],
            expected_output=task_cfg["expected_output"],
            agent=assigned_agent,
        )
    )

# Form the Crew with sequential maker-checker process
stem_crew = Crew(
    agents=list(agents_dict.values()),
    tasks=tasks_list,
    process=Process.sequential,
    verbose=True,
)

# Kick off the workflow
result = stem_crew.kickoff(inputs={"topic": "Quantum Tunneling in Semiconductors"})
print(result)
```

## Architecture Alignment

The workflow enforces Sage's strict **maker-checker policy**:
1. `sage` breaks down the topic and derives the explanation.
2. `reviewer` scrutinizes the draft for logic gaps, unit consistency, and pedagogical clarity.
3. Only verified outputs are approved for final presentation.