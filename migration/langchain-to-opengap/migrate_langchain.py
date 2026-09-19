import argparse
import ast
import os
import yaml

def extract_system_messages(node):
    messages = []
    for child in ast.walk(node):
        if isinstance(child, ast.Assign) and len(child.targets) == 1:
            if isinstance(child.targets[0], ast.Name) and child.targets[0].id == "system_message":
                if isinstance(child.value, ast.Constant):
                    messages.append(child.value.value)
    return messages

def extract_tools(node):
    tools = []
    for child in ast.walk(node):
        if isinstance(child, ast.FunctionDef):
            is_tool = False
            for dec in child.decorator_list:
                if isinstance(dec, ast.Name) and dec.id == "tool":
                    is_tool = True
                elif isinstance(dec, ast.Call) and isinstance(dec.func, ast.Name) and dec.func.id == "tool":
                    is_tool = True
            if is_tool:
                docstring = ast.get_docstring(child) or "No description provided."
                args = {}
                required_args = []
                for arg in child.args.args:
                    arg_type = "string"
                    if arg.annotation and isinstance(arg.annotation, ast.Name):
                        if arg.annotation.id == "float": arg_type = "number"
                        elif arg.annotation.id == "int": arg_type = "integer"
                        elif arg.annotation.id == "bool": arg_type = "boolean"
                    args[arg.arg] = {"type": arg_type}
                    required_args.append(arg.arg)
                
                tools.append({
                    "name": child.name,
                    "description": docstring,
                    "input_schema": {
                        "type": "object",
                        "properties": args,
                        "required": required_args
                    },
                    "output_schema": {
                        "type": "object",
                        "properties": {
                            "result": {
                                "type": "string"
                            }
                        }
                    },
                    "annotations": {
                        "requires_confirmation": False,
                        "read_only": True,
                        "cost": "none"
                    }
                })
    return tools

def migrate_langchain(input_file, output_dir):
    with open(input_file, 'r', encoding='utf-8') as f:
        source_code = f.read()

    tree = ast.parse(source_code)
    
    system_messages = extract_system_messages(tree)
    tools = extract_tools(tree)

    os.makedirs(output_dir, exist_ok=True)
    
    # 1. agent.yaml conforming to OpenGAP 0.1.0
    agent_yaml = {
        "spec_version": "0.1.0",
        "name": "migrated-langchain-agent",
        "version": "0.1.0",
        "description": "Agent migrated from LangChain framework to OpenGAP standard.",
        "identity": {
            "soul": "SOUL.md",
            "rules": "RULES.md",
            "duties": "DUTIES.md"
        },
        "model": {
            "preferred": "llama-3.3-70b-versatile"
        },
        "tools": [t["name"] for t in tools]
    }
    with open(os.path.join(output_dir, "agent.yaml"), "w", encoding="utf-8") as f:
        yaml.dump(agent_yaml, f, default_flow_style=False)

    # 2. SOUL.md
    soul_content = "# SOUL\n\n## Identity\n"
    if system_messages:
        soul_content += system_messages[0] + "\n"
    else:
        soul_content += "Autonomous STEM explainer agent migrated from LangChain.\n"
        
    with open(os.path.join(output_dir, "SOUL.md"), "w", encoding="utf-8") as f:
        f.write(soul_content)

    # 3. RULES.md
    rules_content = """# Rules

1. Always preserve the persona defined in SOUL.md.
2. Validate inputs before tool execution.
3. State assumptions and caveats on uncertain calculations.
"""
    with open(os.path.join(output_dir, "RULES.md"), "w", encoding="utf-8") as f:
        f.write(rules_content)

    # 4. DUTIES.md
    duties_content = """# Duties

## Role: Migrated LangChain Worker
- Execute tool calls as orchestrated by the system.
- Format responses clearly and accurately.
"""
    with open(os.path.join(output_dir, "DUTIES.md"), "w", encoding="utf-8") as f:
        f.write(duties_content)

    # 5. Tools directory with MCP-compatible YAML schemas
    tools_dir = os.path.join(output_dir, "tools")
    os.makedirs(tools_dir, exist_ok=True)
    for t in tools:
        with open(os.path.join(tools_dir, f"{t['name']}.yaml"), "w", encoding="utf-8") as f:
            yaml.dump(t, f, default_flow_style=False)

    print(f"Migrated LangChain agent to {output_dir}")

def main():
    parser = argparse.ArgumentParser(description="Migrate LangChain agents to OpenGAP format.")
    parser.add_argument("--input", required=True, help="Path to LangChain Python script")
    parser.add_argument("--output", required=True, help="Path to output directory for OpenGAP agents")
    args = parser.parse_args()

    migrate_langchain(args.input, args.output)

if __name__ == "__main__":
    main()
