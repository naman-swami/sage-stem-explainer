import abc
import os
import yaml
import json
from pathlib import Path
from typing import Dict, Any, List

class BaseAdapter(abc.ABC):
    """
    Abstract base class for OpenGAP export adapters.
    """
    
    def __init__(self, repo_path: str, out_dir: str):
        self.repo_path = Path(repo_path)
        self.out_dir = Path(out_dir)
        self.opengap_data = {}
        self.compiled_artifacts = {}
        
    def parse_opengap_repo(self) -> None:
        """
        Parses the standard OpenGAP repository structure.
        """
        agent_yaml_path = self.repo_path / "agent.yaml"
        if agent_yaml_path.exists():
            with open(agent_yaml_path, 'r', encoding='utf-8') as f:
                self.opengap_data['agent'] = yaml.safe_load(f)
        else:
            print(f"Warning: Missing agent.yaml in {self.repo_path}")
            self.opengap_data['agent'] = {}
            
        soul_md_path = self.repo_path / "SOUL.md"
        if soul_md_path.exists():
            with open(soul_md_path, 'r', encoding='utf-8') as f:
                self.opengap_data['soul'] = f.read()
                
        rules_md_path = self.repo_path / "RULES.md"
        if rules_md_path.exists():
            with open(rules_md_path, 'r', encoding='utf-8') as f:
                self.opengap_data['rules'] = f.read()
                
        tools_dir = self.repo_path / "tools"
        self.opengap_data['tools'] = []
        if tools_dir.exists() and tools_dir.is_dir():
            for tool_file in tools_dir.glob("*.yaml"):
                with open(tool_file, 'r', encoding='utf-8') as f:
                    self.opengap_data['tools'].append(yaml.safe_load(f))

    @abc.abstractmethod
    def compile_tools(self) -> Any:
        """
        Compile OpenGAP tools into framework-specific tools.
        """
        pass

    @abc.abstractmethod
    def compile_persona(self) -> Any:
        """
        Compile SOUL.md, RULES.md, etc. into framework-specific persona/system prompt.
        """
        pass

    @abc.abstractmethod
    def compile_agent(self) -> Any:
        """
        Compile the full agent definition into framework artifacts.
        """
        pass
        
    def emit_artifacts(self) -> None:
        """
        Writes compiled artifacts to the output directory.
        """
        self.out_dir.mkdir(parents=True, exist_ok=True)
        for filename, content in self.compiled_artifacts.items():
            filepath = self.out_dir / filename
            if isinstance(content, dict) or isinstance(content, list):
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(content, f, indent=2)
            else:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
        print(f"Successfully generated artifacts in {self.out_dir}")

    def run(self) -> None:
        self.parse_opengap_repo()
        self.compile_tools()
        self.compile_persona()
        self.compile_agent()
        self.emit_artifacts()
