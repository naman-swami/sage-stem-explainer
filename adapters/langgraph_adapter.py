import argparse
import os
from pathlib import Path
from base_adapter import BaseAdapter

class LangGraphAdapter(BaseAdapter):
    """
    OpenGAP Adapter for LangGraph ReAct Agent.
    """
    
    def compile_tools(self):
        tool_names = []
        for tool in self.opengap_data.get('tools', []):
            tool_names.append(tool.get("name", "UnknownTool"))
        self.compiled_artifacts['langgraph_tools.json'] = {"tool_names": tool_names}
        return tool_names

    def compile_persona(self):
        system_prompt = f"{self.opengap_data.get('soul', '')}\n\n{self.opengap_data.get('rules', '')}"
        self.compiled_artifacts['system_message.txt'] = system_prompt
        return system_prompt

    def compile_agent(self):
        agent_name = self.opengap_data.get('agent', {}).get('name', 'LangGraph Agent')
        python_code = f'''
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage

def create_agent(llm, tools):
    with open("system_message.txt", "r") as f:
        system_prompt = f.read()
        
    system_message = SystemMessage(content=system_prompt)
    
    agent_executor = create_react_agent(
        llm, 
        tools, 
        state_modifier=system_message
    )
    return agent_executor
'''
        self.compiled_artifacts['graph.py'] = python_code.strip()

def main():
    parser = argparse.ArgumentParser(description="LangGraph OpenGAP Adapter")
    parser.add_argument("--repo", required=True, help="Path to OpenGAP repository")
    parser.add_argument("--out", required=True, help="Output directory for LangGraph artifacts")
    args = parser.parse_args()
    
    adapter = LangGraphAdapter(args.repo, args.out)
    adapter.run()

if __name__ == "__main__":
    main()
