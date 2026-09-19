---
name: difficulty-adaptation
description: Scales the complexity of an explanation up or down based on user feedback.
---

# Difficulty Adaptation Skill

## Procedure
1. **Analyze Feedback**: Review the user's response or performance on practice questions.
2. **Determine Direction**: Decide if the difficulty needs to increase, decrease, or stay the same.
3. **Identify Levers**: Select which aspects to change (e.g., vocabulary, math rigor, analogy complexity).
4. **Apply Transformation**: Rewrite the explanation applying the chosen levers.

## Output Contract
- Returns a revised explanation string.
- Includes a metadata block noting the new difficulty level (1-5) and the specific levers adjusted.

## Edge Cases
- **User is completely lost (Level 1 isn't enough)**: Pivot entirely to a prerequisite concept.
- **User finds Level 5 too easy**: Acknowledge mastery and suggest tangential advanced topics.

## Language
- Ensure the tone remains supportive, especially when decreasing difficulty. Do not sound condescending.

## Integration Notes
- Used by the `Tutor` during interactive sessions.
- Heavily relies on the `SessionLog` memory schema to track historical performance.
