# Explainability

## Decision Reasoning
Sage decides how to structure an explanation by first identifying the
core concept behind the learner's question, then building a sequence
of smaller logical steps toward it. It reorders or simplifies steps
based on the apparent difficulty level of the question.

## Data Sources and Inputs Used
Sage's explanations are grounded in curated STEM reference material
and the learner's own question text as input. It does not browse the
live web; all reasoning happens over its trained knowledge and any
reference notes provided in context.

## Known Limitations
Sage can misjudge a learner's existing background and pitch an
explanation too high or too low. It does not verify numerical
calculations independently, so multi-step derivations should be
spot-checked, especially for advanced topics outside core STEM syllabi.
