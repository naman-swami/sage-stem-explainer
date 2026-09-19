# Claude Code Export

This directory contains the export configuration for running **Sage STEM Explainer** within Claude Code or Anthropic Claude environments.

## Overview

The export packages Sage's unified system prompt into [`system-prompt.md`](system-prompt.md), consolidating:
- Core identity, pedagogical philosophy (first-principles reasoning), and personality from `SOUL.md`
- Hard constraints and behavioral guardrails (15 mandatory rules) from `RULES.md`
- Maker-checker segregation of duties from `DUTIES.md`
- Decision rationale, confidence quantification, and limitations from `EXPLAINABILITY.md`

## Usage with Claude Code

### Option 1: Claude Code System Instructions (`CLAUDE.md`)
You can symlink or copy `system-prompt.md` to your project root or user configuration:

```bash
# In your target workspace
cp exports/claude-code/system-prompt.md ./CLAUDE.md
```

### Option 2: Project-Specific Memory
To use Sage as a dedicated STEM tutor persona in any workspace:

```bash
claude --prompt "$(cat exports/claude-code/system-prompt.md)"
```

### Option 3: Anthropic Python SDK Integration

```python
import anthropic

client = anthropic.Anthropic()

with open("exports/claude-code/system-prompt.md", "r", encoding="utf-8") as f:
    system_prompt = f.read()

response = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=2048,
    system=system_prompt,
    messages=[
        {"role": "user", "content": "Explain why Newton's second law is F=ma from first principles."}
    ]
)

print(response.content[0].text)
```

## Features Supported
- **First-Principles Derivation**: Steps through definitions, physical intuition, mathematical transformations, and checks.
- **Bilingual STEM Mode**: Seamless explanation in English or Hindi (preserving technical nomenclature).
- **Maker-Checker Boundary**: Includes verification guidelines to ensure logical rigor before finalizing responses.