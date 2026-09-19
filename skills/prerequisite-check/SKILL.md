---
name: prerequisite-check
description: Verifies if the learner has the necessary foundational knowledge.
---

# Prerequisite Check Skill

## Procedure
1. **Identify Target**: Determine the concept the user wants to learn.
2. **Query Learner Profile**: Retrieve the `knowledge_base` from the user's profile.
3. **Build Graph Path**: Traverse the prerequisite graph from the target concept backwards.
4. **Find Gaps**: Compare the required path against the learner's known concepts.
5. **Generate Report**: Output the missing prerequisites.

## Output Contract
Returns a JSON object matching the schema output of `check.py`.
Keys must include `target_concept`, `known_concepts`, `missing_prerequisites`, and a boolean `ready_to_learn`.

## Edge Cases
- **Unknown Concept**: If the target concept is not in the graph, attempt to infer prerequisites using an LLM call or default to assuming basic algebra/logic.
- **Stale Knowledge**: If a known concept hasn't been reviewed in >6 months, flag it as a potential gap.

## Language
- Outputs are technical JSON, but missing concepts should be formatted as human-readable strings.

## Integration Notes
- Runs as a pre-flight check in the `Orchestrator` before starting a new lesson.
