import os
import subprocess
import sys
import json
import pytest

@pytest.mark.execution
def test_claw_worker_health(project_root):
    worker_script = os.path.join(project_root, 'claw-worker', 'worker.py')
    res = subprocess.run([sys.executable, worker_script, '--health'], capture_output=True, text=True)
    assert res.returncode == 0, f"Worker health check failed: {res.stderr}"
    data = json.loads(res.stdout)
    assert data.get('status') == 'ok'

@pytest.mark.execution
def test_snippet_validator_on_root(project_root):
    validator_script = os.path.join(project_root, 'validator', 'snippet_validator.py')
    res = subprocess.run([sys.executable, validator_script, project_root, '--format', 'json'], capture_output=True, text=True)
    assert res.returncode == 0, f"Validator failed on root repository: {res.stderr}"
    data = json.loads(res.stdout)
    assert data.get('status') == 'pass'
    assert len(data.get('errors', [])) == 0

@pytest.mark.execution
def test_migration_crewai(project_root, tmp_path):
    migrator = os.path.join(project_root, 'migration', 'crewai-to-opengap', 'migrate_crewai.py')
    sample = os.path.join(project_root, 'migration', 'crewai-to-opengap', 'sample_crew.yaml')
    out_dir = str(tmp_path / 'crew_out')
    
    res = subprocess.run([sys.executable, migrator, '--input', sample, '--output', out_dir], capture_output=True, text=True)
    assert res.returncode == 0, f"CrewAI migration failed: {res.stderr}"
    assert os.path.exists(os.path.join(out_dir, 'researcher', 'agent.yaml'))
    assert os.path.exists(os.path.join(out_dir, 'researcher', 'SOUL.md'))

@pytest.mark.execution
def test_migration_langchain(project_root, tmp_path):
    migrator = os.path.join(project_root, 'migration', 'langchain-to-opengap', 'migrate_langchain.py')
    sample = os.path.join(project_root, 'migration', 'langchain-to-opengap', 'sample_langchain_agent.py')
    out_dir = str(tmp_path / 'lc_out')
    
    res = subprocess.run([sys.executable, migrator, '--input', sample, '--output', out_dir], capture_output=True, text=True)
    assert res.returncode == 0, f"LangChain migration failed: {res.stderr}"
    assert os.path.exists(os.path.join(out_dir, 'agent.yaml'))
    assert os.path.exists(os.path.join(out_dir, 'SOUL.md'))
    assert os.path.exists(os.path.join(out_dir, 'tools', 'calculate_trajectory.yaml'))

@pytest.mark.execution
def test_adapters_compilation(project_root, tmp_path):
    lyzr_adapter = os.path.join(project_root, 'adapters', 'lyzr_adapter.py')
    langgraph_adapter = os.path.join(project_root, 'adapters', 'langgraph_adapter.py')
    
    lyzr_out = str(tmp_path / 'lyzr_dist')
    lg_out = str(tmp_path / 'lg_dist')
    
    res1 = subprocess.run([sys.executable, lyzr_adapter, '--repo', project_root, '--out', lyzr_out], capture_output=True, text=True)
    assert res1.returncode == 0, f"Lyzr adapter failed: {res1.stderr}"
    
    res2 = subprocess.run([sys.executable, langgraph_adapter, '--repo', project_root, '--out', lg_out], capture_output=True, text=True)
    assert res2.returncode == 0, f"LangGraph adapter failed: {res2.stderr}"
