# OpenGAP Snippet Validator

A standalone CLI tool for validating OpenGAP agent directories or individual file snippets.

## Features
- Validates `agent.yaml` syntax and required fields
- Validates `SOUL.md`, `RULES.md`, `DUTIES.md` completeness
- Validates tool YAML contracts against OpenGAP JSON Schema rules
- Validates skills frontmatter in `SKILL.md`
- Outputs clear terminal reports or JSON formats for CI/CD integrations

## Requirements
- Python 3.8+
- PyYAML

```bash
pip install pyyaml
```

## Usage

### Basic Usage (Pretty Print)
```bash
python snippet_validator.py /path/to/agent/directory
```

### JSON Output (For Automation)
```bash
python snippet_validator.py /path/to/agent/directory --format json
```

### Validating a Single File
```bash
python snippet_validator.py /path/to/agent/directory/agent.yaml
```

## Exit Codes
- `0`: Validation passed successfully.
- `1`: Validation failed (errors were found).
