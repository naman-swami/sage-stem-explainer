---
name: visual-explanation
description: Maps textual concepts to appropriate visual formats.
---

# Visual Explanation Skill

## Procedure
1. **Extract Core Structures**: Parse text to find relationships (hierarchies, sequences, comparisons).
2. **Select Format**: Apply the Visualizer's format selection logic (Mermaid vs ASCII).
3. **Draft Diagram**: Write the syntax for the chosen format.
4. **Validate Syntax**: Ensure there are no syntax errors (e.g., unescaped characters in Mermaid).
5. **Embed Context**: Add a caption explaining how to read the diagram.

## Output Contract
Returns a string containing the markdown-formatted diagram blocks.

## Edge Cases
- **Graph too large**: If a flowchart has >20 nodes, break it down into smaller, linked sub-graphs.
- **Unsupported syntax**: Stick to standard Mermaid features to ensure cross-platform rendering.

## Language
- Keep node labels concise. Use the surrounding text for detailed explanations.

## Integration Notes
- Core skill of the `Visualizer` agent.
