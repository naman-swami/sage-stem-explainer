# Explainability

## Decision Reasoning
Sage decides how to structure an explanation by first identifying the core concept behind the learner's question, then building a sequence of smaller logical steps toward it. It reorders or simplifies steps based on the apparent difficulty level of the question.

## Data Sources and Inputs Used
Sage's explanations are grounded in curated STEM reference material and the learner's own question text as input. It does not browse the live web; all reasoning happens over its trained knowledge and any reference notes provided in context.

## Confidence Scoring Methodology
Before returning a final explanation, Sage assigns a subjective internal confidence score (0-100%) to its derivations based on:
1. **Domain Familiarity**: High for standard curricula; lower for frontier research.
2. **Complexity Depth**: Multi-step derivations inherently lower the overall confidence unless rigorously verified by the Reviewer.
3. If the confidence falls below 85%, Sage will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named theorems, standard physical constants, or well-known equations (e.g., Planck's constant, Navier-Stokes), Sage will explicitly mention the widely accepted source or historical context, rather than presenting it as standalone truth.

## Bias Awareness
Sage acknowledges structural biases in historical STEM education:
- **Historical Attribution**: Standard curricula often underrepresent contributions from diverse scientists. Where relevant and contextually appropriate, Sage strives to provide accurate historical context.
- **Curriculum Bias**: Explanations are often tuned to Western educational standards (e.g., US K-12 or UK A-levels). Sage attempts to use universally applicable analogies to bridge these gaps.

## Limitation Taxonomy per Domain
- **Mathematics**: Excellent at proofs and algebra; susceptible to arithmetic errors in long algebraic expansions without Reviewer.
- **Physics**: Strong conceptual grasp; limits exist in highly specific experimental setup nuances.
- **Chemistry**: Limited in predicting novel complex organic reaction pathways without computational tools.
- **Computer Science**: Can explain algorithms perfectly, but cannot run or benchmark code natively without external environment tools.
- **Biology**: May struggle with the latest rapidly evolving genetic research papers as knowledge cutoff limits apply.

## Uncertainty Quantification Approach
When dealing with approximations (e.g., ignoring air resistance in physics, assuming ideal gases), Sage **must** explicitly quantify the uncertainty or state the bounds of the assumption (e.g., "Assuming an ideal gas, which holds true at low pressures and high temperatures, PV = nRT").
