#!/bin/bash
# OpenGAP Local Validation Script
set -e

echo "Running OpenGAP Validation Suite..."

echo "1. Checking essential files..."
REQUIRED_FILES=("agent.yaml" "SOUL.md" "RULES.md" "DUTIES.md" "EXPLAINABILITY.md" "AGENTS.md")
for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -s "$file" ]; then
        echo "ERROR: Required file $file is missing or empty."
        exit 1
    fi
done
echo "✅ Essential files present."

echo "2. Installing test requirements..."
pip install -r tests/requirements.txt -q

echo "3. Running test suite..."
python -m pytest tests/ -v

echo "4. Checking python syntax in scripts and exports..."
python -m compileall -q scripts/ exports/ tests/

echo "✅ All validations passed successfully!"
