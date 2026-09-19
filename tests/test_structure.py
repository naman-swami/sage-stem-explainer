import os
import pytest

@pytest.mark.structure
def test_root_agent_yaml_exists(project_root, load_yaml):
    agent_yaml_path = os.path.join(project_root, 'agent.yaml')
    assert os.path.exists(agent_yaml_path), "agent.yaml is missing"
    
    data = load_yaml(agent_yaml_path)
    assert 'spec_version' in data, "agent.yaml missing spec_version"
    assert 'name' in data, "agent.yaml missing name"
    assert 'version' in data, "agent.yaml missing version"
    assert 'description' in data, "agent.yaml missing description"

@pytest.mark.structure
def test_root_markdown_files_exist_and_populated(project_root):
    required_files = ['SOUL.md', 'RULES.md', 'DUTIES.md', 'EXPLAINABILITY.md', 'AGENTS.md']
    for filename in required_files:
        filepath = os.path.join(project_root, filename)
        assert os.path.exists(filepath), f"{filename} is missing"
        assert os.path.getsize(filepath) > 0, f"{filename} is empty"

@pytest.mark.structure
def test_subagents_structure(project_root):
    agents_dir = os.path.join(project_root, 'agents')
    if not os.path.exists(agents_dir):
        return # No subagents to test
        
    for item in os.listdir(agents_dir):
        agent_path = os.path.join(agents_dir, item)
        if os.path.isdir(agent_path):
            assert os.path.exists(os.path.join(agent_path, 'agent.yaml')), f"Subagent {item} missing agent.yaml"
            assert os.path.exists(os.path.join(agent_path, 'SOUL.md')), f"Subagent {item} missing SOUL.md"
            assert os.path.exists(os.path.join(agent_path, 'DUTIES.md')), f"Subagent {item} missing DUTIES.md"

@pytest.mark.structure
def test_skills_structure(project_root):
    skills_dir = os.path.join(project_root, 'skills')
    if not os.path.exists(skills_dir):
        return
        
    for item in os.listdir(skills_dir):
        skill_path = os.path.join(skills_dir, item)
        if os.path.isdir(skill_path):
            skill_md = os.path.join(skill_path, 'SKILL.md')
            assert os.path.exists(skill_md), f"Skill {item} missing SKILL.md"
            
            with open(skill_md, 'r', encoding='utf-8') as f:
                content = f.read()
                assert content.startswith('---'), f"Skill {item} SKILL.md missing frontmatter"
