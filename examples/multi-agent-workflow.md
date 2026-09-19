# Multi-Agent Workflow Example

**Question:** How do the Orchestrator, Sage, and Reviewer work together to process a user request?

---

**Scenario:** A high-school student asks, "Why does ice float on water if solids are usually heavier than liquids?"

**Step 1: Orchestrator Routing (Intake)**
- **User Input:** "Why does ice float on water if solids are usually heavier than liquids?"
- **Action:** The Orchestrator receives the prompt. It detects the domain (Chemistry/Physics) and the implied audience level (School/General).
- **Routing:** Orchestrator assigns the task to the **Sage (Maker)** sub-agent, passing the context: `Domain: Chemistry, Audience: High School`.

**Step 2: Sage Generates Draft (Maker Step)**
- **Action:** Sage uses its `concept-breakdown` skill.
- **Draft Output:** 
  > **Plain Language:** Usually, when things freeze, their pieces pack tightly together, making them heavier. Water is weird. When it freezes, its molecules form a rigid, open structure like a honeycomb, leaving lots of empty space. This makes ice lighter (less dense) than liquid water, so it floats.
  > **Steps:** 1. Density dictates floating... 2. Hydrogen bonding in $H_2O$ causes crystal lattice formation...

**Step 3: Reviewer Verification (Checker Step)**
- **Action:** The Orchestrator intercepts the draft and sends it to the **Reviewer (Checker)** sub-agent.
- **Verification Process:** 
  - Checks if "Hydrogen bonding" is accurately described.
  - Verifies the claim that the crystal lattice has more empty space.
  - Ensures no advanced college-level thermodynamics were unnecessarily introduced (verifying Audience constraint).
- **Reviewer Output:** `Status: APPROVED. Feedback: Conceptual logic is sound. Audience level appropriate.`

**Step 4: Orchestrator Delivery**
- **Action:** The Orchestrator formats the final approved draft. (If the user had requested Hindi, it would route to a Translator sub-agent here).
- **Final Result Delivered to User.**

**Takeaway:**
This maker-checker pipeline ensures that Sage remains focused on clear, empathetic explanations, while the Reviewer acts as a strict guardrail against logical errors or hallucinations before the user ever sees the output.
