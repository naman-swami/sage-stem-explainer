#!/usr/bin/env python3
"""
OpenGAP Snippet Validator

Validates OpenGAP agent directories or snippets for compliance with the OpenGAP specification.
"""

import os
import sys
import yaml
import json
import argparse
from pathlib import Path

class OpenGAPValidator:
    def __init__(self, target_path):
        self.target_path = Path(target_path)
        self.errors = []
        self.warnings = []
        
    def validate(self):
        if self.target_path.is_file():
            self._validate_file(self.target_path)
        elif self.target_path.is_dir():
            self._validate_directory(self.target_path)
        else:
            self.errors.append(f"Target path does not exist: {self.target_path}")
            
        return {
            "status": "pass" if not self.errors else "fail",
            "errors": self.errors,
            "warnings": self.warnings
        }
        
    def _validate_file(self, file_path):
        if file_path.name == "agent.yaml":
            self._validate_agent_yaml(file_path)
        elif file_path.suffix in [".yaml", ".yml"] and "tools" in file_path.parts:
            self._validate_tool_yaml(file_path)
        elif file_path.name in ["SOUL.md", "RULES.md", "DUTIES.md"]:
            self._validate_core_markdown(file_path)
        elif file_path.name == "SKILL.md":
            self._validate_skill_markdown(file_path)
            
    def _validate_directory(self, dir_path):
        required_files = ["agent.yaml", "SOUL.md", "RULES.md", "DUTIES.md"]
        
        for req_file in required_files:
            if not (dir_path / req_file).exists():
                self.errors.append(f"Missing required file: {req_file} in {dir_path}")
            else:
                self._validate_file(dir_path / req_file)
                
        # Validate tools
        tools_dir = dir_path / "tools"
        if tools_dir.exists() and tools_dir.is_dir():
            for tool_file in tools_dir.glob("*.yaml"):
                self._validate_file(tool_file)
                
        # Validate skills
        skills_dir = dir_path / "skills"
        if skills_dir.exists() and skills_dir.is_dir():
            for skill_file in skills_dir.rglob("SKILL.md"):
                self._validate_file(skill_file)

    def _validate_agent_yaml(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                
            if not isinstance(data, dict):
                self.errors.append(f"{file_path} must be a YAML dictionary")
                return
                
            # Check spec version (spec_version or schema_version)
            if "spec_version" not in data and "schema_version" not in data:
                self.errors.append(f"{file_path} missing 'spec_version' or 'schema_version'")
                
            # Check agent name (top-level 'name' or data['agent']['name'])
            has_name = "name" in data or ("agent" in data and isinstance(data["agent"], dict) and "name" in data["agent"])
            if not has_name:
                self.errors.append(f"{file_path} missing agent 'name'")
                
        except Exception as e:
            self.errors.append(f"Failed to parse {file_path}: {str(e)}")

    def _validate_tool_yaml(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                
            if not isinstance(data, dict):
                self.errors.append(f"{file_path} must be a YAML dictionary")
                return
                
            if "name" not in data:
                self.errors.append(f"Tool {file_path} missing 'name'")
            if "description" not in data:
                self.errors.append(f"Tool {file_path} missing 'description'")
            if "input_schema" not in data:
                self.errors.append(f"Tool {file_path} missing 'input_schema'")
                
        except Exception as e:
            self.errors.append(f"Failed to parse {file_path}: {str(e)}")

    def _validate_core_markdown(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if not content:
                self.errors.append(f"{file_path} is empty")
            elif len(content) < 20:
                self.warnings.append(f"{file_path} is very short, please ensure it has meaningful content")
        except Exception as e:
            self.errors.append(f"Failed to read {file_path}: {str(e)}")

    def _validate_skill_markdown(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if not content.startswith('---'):
                self.errors.append(f"Skill {file_path} missing YAML frontmatter")
                return
                
            parts = content.split('---', 2)
            if len(parts) < 3:
                self.errors.append(f"Skill {file_path} has malformed YAML frontmatter")
                return
                
            frontmatter = yaml.safe_load(parts[1])
            if not frontmatter or not isinstance(frontmatter, dict):
                self.errors.append(f"Skill {file_path} has invalid YAML frontmatter")
                return
                
            if 'name' not in frontmatter:
                self.errors.append(f"Skill {file_path} frontmatter missing 'name'")
            if 'description' not in frontmatter:
                self.errors.append(f"Skill {file_path} frontmatter missing 'description'")
                
        except Exception as e:
            self.errors.append(f"Failed to validate skill {file_path}: {str(e)}")


def main():
    parser = argparse.ArgumentParser(description="OpenGAP Snippet Validator")
    parser.add_argument("target", help="Directory or file to validate")
    parser.add_argument("--format", choices=["json", "pretty"], default="pretty", help="Output format")
    args = parser.parse_args()
    
    validator = OpenGAPValidator(args.target)
    results = validator.validate()
    
    if args.format == "json":
        print(json.dumps(results, indent=2))
    else:
        print("\n=== OpenGAP Validation Report ===")
        print(f"Target: {args.target}")
        print(f"Status: {'PASS' if results['status'] == 'pass' else 'FAIL'}")
        
        if results['errors']:
            print("\nERRORS:")
            for err in results['errors']:
                print(f"  [ERROR] {err}")
                
        if results['warnings']:
            print("\nWARNINGS:")
            for warn in results['warnings']:
                print(f"  [WARN] {warn}")
                
        print("=================================\n")
        
    if results['status'] == 'fail':
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
