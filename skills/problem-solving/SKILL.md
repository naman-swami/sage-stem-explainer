---
name: problem-solving
description: Solves STEM problems step-by-step using Polya's framework.
---

# Problem Solving Skill

## Procedure
1. **Understand Phase**: State the given variables and the goal.
2. **Plan Phase**: Identify the relevant formulas and outline the steps.
3. **Execute Phase**: Perform the mathematical or logical operations.
4. **Review Phase**: Verify the answer using dimensional analysis or logic checks.
5. **Format Output**: Compile into a structured step-by-step guide.

## Output Contract
Returns a JSON object matching the schema output of `solve.py`.
Keys must include `original_problem`, `framework_used`, `solution_steps`, and `final_verification`.

## Edge Cases
- **Missing Information**: Identify exactly what is missing and state that the problem cannot be solved as written.
- **Multiple Solutions**: If applicable (e.g., quadratic equations), clearly state and explain both solutions.

## Language
- Use clear transitions between phases.

## Integration Notes
- Used by the `Tutor` when demonstrating an example.
- Used by the `Reviewer` (via `check-step-logic`) to verify derivations.
