# CrewAI to OpenGAP Migration Guide

This directory contains tools and examples for migrating CrewAI agents to the OpenGAP specification.

## Before: CrewAI
In CrewAI, agents are typically defined in a `yaml` file mapped to Python objects:
```yaml
agents:
  researcher:
    role: Senior Data Researcher
    goal: Uncover cutting-edge developments in AI
    backstory: You're a seasoned researcher...
```

## After: OpenGAP
OpenGAP separates concerns into multiple markdown and yaml files for framework-agnostic portability:
- `agent.yaml`: Core metadata (role, goal)
- `SOUL.md`: Agent identity and personality (from backstory)
- `RULES.md`: Constraints and operational boundaries

## Usage

Run the automated migration tool to convert a CrewAI YAML configuration to OpenGAP:

```bash
python migrate_crewai.py --input sample_crew.yaml --output exported_agents/
```

This will create a structured directory for each agent in `exported_agents/`.
