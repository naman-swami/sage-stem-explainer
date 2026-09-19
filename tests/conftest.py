import pytest
import yaml
import os
import glob

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "structure: marks tests checking the project structure"
    )
    config.addinivalue_line(
        "markers", "schema: marks tests checking the yaml schemas"
    )

@pytest.fixture(scope="session")
def project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

@pytest.fixture
def load_yaml():
    def _load_yaml(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return _load_yaml

@pytest.fixture
def get_all_yaml_files(project_root):
    pattern = os.path.join(project_root, '**', '*.yaml')
    return glob.glob(pattern, recursive=True)

@pytest.fixture
def get_all_md_files(project_root):
    pattern = os.path.join(project_root, '**', '*.md')
    return glob.glob(pattern, recursive=True)
