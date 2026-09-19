---
name: practice-generation
description: Generates custom practice problems to test understanding.
---

# Practice Generation Skill

## Procedure
1. **Identify Target Concept**: Determine exactly what needs to be tested.
2. **Read Difficulty Level**: Check the current difficulty level from the session state.
3. **Generate Problems**: Create N problems that isolate the target concept.
4. **Generate Solutions**: Create step-by-step solutions for each problem.
5. **Format Output**: Return the structured problem set.

## Output Contract
Returns a JSON object matching the schema output of `generate.py`.
Keys must include `topic`, `requested_difficulty`, `problem_count`, and an array of `problems` (with `id`, `question`, `type`, `difficulty_level`).

## Edge Cases
- **Calculation vs. Conceptual**: Ensure a mix of both types unless the topic is purely one or the other.
- **Unsolvable Problems**: Must include a validation step to ensure generated numbers don't lead to complex roots unless intended.

## Language
- Problem statements should be clear and unambiguous.

## Integration Notes
- Invoked by the `Tutor` after delivering an explanation.
- Can be triggered by the `Orchestrator` if the user explicitly requests a quiz.
