import subprocess
import json
import sys
import os
import pytest

@pytest.mark.execution
def test_concept_breakdown_script(project_root):
    script_path = os.path.join(project_root, 'skills', 'concept-breakdown', 'breakdown.py')
    res = subprocess.run([sys.executable, script_path, '--concept', 'calculus'], capture_output=True, text=True)
    assert res.returncode == 0, f"Script failed: {res.stderr}"
    data = json.loads(res.stdout)
    assert 'concept' in data
    assert 'sub_components' in data

@pytest.mark.execution
def test_problem_solving_script(project_root):
    script_path = os.path.join(project_root, 'skills', 'problem-solving', 'solve.py')
    res = subprocess.run([sys.executable, script_path, '--problem', 'Find velocity'], capture_output=True, text=True)
    assert res.returncode == 0, f"Script failed: {res.stderr}"
    data = json.loads(res.stdout)
    assert 'solution_steps' in data
    assert len(data['solution_steps']) == 4

@pytest.mark.execution
def test_prerequisite_check_script(project_root):
    script_path = os.path.join(project_root, 'skills', 'prerequisite-check', 'check.py')
    res = subprocess.run([sys.executable, script_path, '--target', 'calculus'], capture_output=True, text=True)
    assert res.returncode == 0, f"Script failed: {res.stderr}"
    data = json.loads(res.stdout)
    assert 'target_concept' in data
    assert 'ready_to_learn' in data

@pytest.mark.execution
def test_practice_generation_script(project_root):
    script_path = os.path.join(project_root, 'skills', 'practice-generation', 'generate.py')
    res = subprocess.run([sys.executable, script_path, '--topic', 'physics', '--difficulty', '3'], capture_output=True, text=True)
    assert res.returncode == 0, f"Script failed: {res.stderr}"
    data = json.loads(res.stdout)
    assert 'problems' in data
    assert len(data['problems']) > 0
