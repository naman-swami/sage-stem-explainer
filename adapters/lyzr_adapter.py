import argparse
import os
from pathlib import Path
from base_adapter import BaseAdapter

class LyzrAdapter(BaseAdapter):
    """
    OpenGAP Adapter for Lyzr ADK / Studio.
    """
    
    def compile_tools(self):
        lyzr_tools = []
        for tool in self.opengap_data.get('tools', []):
            lyzr_tools.append({
                "name": tool.get("name", "UnknownTool"),
                "description": tool.get("description", ""),
                "parameters": tool.get("input_schema", {})
            })
        self.compiled_artifacts['lyzr_tools.json'] = lyzr_tools
        return lyzr_tools

    def compile_persona(self):
        system_prompt = f"IDENTITY:\n{self.opengap_data.get('soul', '')}\n\nRULES:\n{self.opengap_data.get('rules', '')}"
        self.compiled_artifacts['lyzr_system_prompt.txt'] = system_prompt
        return system_prompt

    def compile_agent(self):
        agent_name = self.opengap_data.get('agent', {}).get('name', 'OpenGAP Agent')
        python_code = f'''
from lyzr import Agent

def get_lyzr_agent():
    with open("lyzr_system_prompt.txt", "r") as f:
        system_prompt = f.read()
        
    agent = Agent(
        name="{agent_name}",
        system_prompt=system_prompt
    )
    return agent
'''
        self.compiled_artifacts['agent.py'] = python_code.strip()

def main():
    parser = argparse.ArgumentParser(description="Lyzr OpenGAP Adapter")
    parser.add_argument("--repo", required=True, help="Path to OpenGAP repository")
    parser.add_argument("--out", required=True, help="Output directory for Lyzr artifacts")
    args = parser.parse_args()
    
    adapter = LyzrAdapter(args.repo, args.out)
    adapter.run()

if __name__ == "__main__":
    main()
