---
name: concept-breakdown
description: Turn a STEM question into a sequence of understandable, checkable steps, from restating the goal through a plain-language intuition, a justified step chain, and a sanity check.
---

# Skill: Concept Breakdown

## Purpose
Turn a learner's STEM question into a sequence of understandable, checkable
steps. This skill is framework-neutral: a host may implement it as a prompt,
a workflow, or a tool-calling policy.

## Procedure
1. Restate the question and identify the learner's likely target: definition,
   intuition, derivation, calculation, comparison, or application.
2. List the minimum prerequisite ideas. Mark any assumption that may need to be
   confirmed instead of silently inventing background knowledge.
3. State the core idea in plain language before introducing symbols.
4. Build an ordered chain: premise, transformation or observation, and result.
   Every non-obvious transition gets a short justification.
5. Introduce notation, equations, units, or diagrams only when they reduce
   ambiguity; define each symbol at first use.
6. Add a small sanity check: units, limiting case, example, or counterexample.
7. End with a concise takeaway and one optional follow-up question.

## Output Contract
Return these headings when appropriate:
- **Goal**
- **Prerequisites**
- **Step 1**, **Step 2**, ...
- **Check**
- **Takeaway**

If the question is underspecified, ask one focused clarification question or
state the assumption explicitly. Do not present an unchecked calculation as
certain.

## Language
Use plain English first and support Hindi when requested. Preserve technical
terms in English alongside a Hindi explanation when translation could introduce
ambiguity.
