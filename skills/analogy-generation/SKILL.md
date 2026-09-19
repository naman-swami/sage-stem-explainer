---
name: analogy-generation
description: Generates relatable analogies for complex STEM concepts.
---

# Analogy Generation Skill

## Procedure
1. **Identify Core Mechanism**: Extract the fundamental mechanism of the target concept.
2. **Determine Audience Context**: Look at the learner profile to find relatable domains (e.g., sports, cooking, video games).
3. **Map Properties**: Create a 1:1 mapping between the abstract concept's components and the analogy's components.
4. **Identify Breaking Points**: Determine where the analogy fails or becomes inaccurate.
5. **Draft Analogy**: Write the explanation using the mapped properties.

## Output Contract
The output must be formatted as follows:
### Analogy: [Title]
**The Mapping:**
- [Abstract Concept A] is like [Everyday Object A]
- [Abstract Concept B] is like [Everyday Object B]

**The Explanation:**
[Paragraph describing the analogy]

**Where this breaks down:**
[Explanation of the limitations of the analogy]

## Edge Cases
- **Highly abstract math (e.g., n-dimensional spaces)**: Fall back to 2D/3D projections instead of physical analogies.
- **Quantum Mechanics**: Warn the user explicitly that macro-world analogies for quantum phenomena are inherently flawed.

## Language Support
- Translate cultural references appropriately. A baseball analogy in English might need to be a cricket analogy in Hindi.

## Integration Notes
- Used heavily by the `Tutor` agent during the initial explanation phase.
- Reviewed by the `Reviewer` to ensure the mapping does not introduce fundamental misconceptions.
