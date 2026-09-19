---
name: concept-breakdown
description: Deconstructs a high-level concept into fundamental building blocks.
---

# Concept Breakdown Skill

## Procedure
1. **Define the Boundary**: Determine the scope of the requested concept.
2. **Identify Prerequisites**: List what must be known *before* learning this concept.
3. **Deconstruct**: Break the core concept into 2-5 sub-components.
4. **Order Sequentially**: Arrange the sub-components in a logical learning progression.
5. **Format Output**: Generate the structured JSON output.

## Output Contract
Returns a JSON object matching the schema output of `breakdown.py`.
Keys must include `concept`, `definition`, `sub_components`, and `recommended_learning_order`.

## Edge Cases
- **Circular dependencies**: Resolve by picking the most intuitive entry point.
- **Overly broad concepts (e.g., "Physics")**: Ask the user to narrow down the scope rather than attempting to break down the entire field.

## Language
- Output keys must remain in English. Content values should match the user's preferred language.

## Integration Notes
- This is the first skill invoked by the `Orchestrator` when a new topic is introduced.
- The output dictates the workflow execution path for the `Tutor`.
