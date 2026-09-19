import argparse
import yaml
import os

def migrate_agent(agent_name, agent_config, output_dir):
    agent_dir = os.path.join(output_dir, agent_name)
    os.makedirs(agent_dir, exist_ok=True)
    
    role = agent_config.get("role", "Specialized Agent")
    goal = agent_config.get("goal", "Perform specialized tasks effectively")
    backstory = agent_config.get("backstory", "Dedicated domain assistant.")
    
    # 1. agent.yaml conforming to OpenGAP 0.1.0
    agent_yaml = {
        "spec_version": "0.1.0",
        "name": agent_name,
        "version": "0.1.0",
        "description": f"{role}: {goal}",
        "identity": {
            "soul": "SOUL.md",
            "rules": "RULES.md",
            "duties": "DUTIES.md"
        },
        "model": {
            "preferred": "llama-3.3-70b-versatile"
        }
    }
    
    with open(os.path.join(agent_dir, "agent.yaml"), "w", encoding="utf-8") as f:
        yaml.dump(agent_yaml, f, default_flow_style=False)
        
    # 2. SOUL.md
    soul_content = f"""# SOUL

## Identity
{agent_name} is an autonomous agent operating with the role of {role}.

## Goal & Mission
{goal}

## Personality & Backstory
{backstory}
"""
    with open(os.path.join(agent_dir, "SOUL.md"), "w", encoding="utf-8") as f:
        f.write(soul_content)
        
    # 3. RULES.md
    rules_content = f"""# Rules

These constraints represent mandatory behavioral boundaries for {agent_name}:

1. Always adhere to the role and persona defined in SOUL.md.
2. Verify all inputs before executing automated actions.
3. Reject hazardous, unsafe, or destructive tasks.
4. Flag uncertainties clearly rather than speculating.
"""
    with open(os.path.join(agent_dir, "RULES.md"), "w", encoding="utf-8") as f:
        f.write(rules_content)

    # 4. DUTIES.md
    duties_content = f"""# Duties

## Role: {role}
- Primary objective: {goal}
- Execute tasks in compliance with the assigned mission.
- Produce structured, verifiable responses for consumers and peer agents.
"""
    with open(os.path.join(agent_dir, "DUTIES.md"), "w", encoding="utf-8") as f:
        f.write(duties_content)

    print(f"Migrated agent '{agent_name}' to {agent_dir}")

def main():
    parser = argparse.ArgumentParser(description="Migrate CrewAI agents to OpenGAP format.")
    parser.add_argument("--input", required=True, help="Path to CrewAI agents.yaml file")
    parser.add_argument("--output", required=True, help="Path to output directory for OpenGAP agents")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        
    agents_data = data.get("agents", data) if "agents" in data else data
    
    for agent_name, agent_config in agents_data.items():
        migrate_agent(agent_name, agent_config, args.output)

if __name__ == "__main__":
    main()
