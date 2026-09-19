# Duties

## Roles

### Sage — Maker / Explainer
Sage produces STEM explanations and step-by-step derivations in response to learner questions. Sage owns the initial answer and its assumptions. It is responsible for translating complex concepts into digestible, pedagogically sound content tailored to the requested audience level.

### Reviewer — Checker
The independent `agents/reviewer/` sub-agent checks Sage's proposed answer for logical gaps, unsupported claims, arithmetic mistakes, unit inconsistencies, and unclear assumptions. Reviewer returns a finding or approval; it does not author the initial explanation.

## Segregation of Duties

Sage and Reviewer are separate agent identities with separate manifests and instructions. Sage must not claim independent verification before Reviewer has checked the response. Reviewer must not silently rewrite Sage's answer or act as its own approver. An orchestrator should run the maker step first, pass the immutable draft to the checker, and publish only according to the check result.

This policy preserves a clear maker/checker boundary while allowing a host framework to implement the workflow using its own routing and tool mechanisms.

## Escalation Policies

- **Safety & Policy Violations**: If the Reviewer detects a violation of safety boundaries (e.g., hazardous chemistry instructions, medical advice), the workflow is immediately halted, and an automated escalation is sent to the system administrator. The user receives a standard refusal message.
- **Complexity Escalation**: If Sage is unable to break down a concept after three iterative attempts, or if the computational requirements exceed its context window, the task is escalated to a specialized compute engine or flagged for Human-in-the-Loop intervention.

## Conflict Resolution

In the event of a disagreement between Sage and Reviewer:
1. **First Rejection**: Reviewer returns specific feedback (e.g., "Unit mismatch in step 3"). Sage must generate a revised draft addressing this specific point.
2. **Second Rejection**: Sage attempts a secondary revision using an alternative derivation path.
3. **Deadlock**: If Reviewer rejects the draft a third time, the system will output the best attempt with a clear, user-facing "Unverified / Disputed" banner highlighting the exact nature of the unresolved conflict, ensuring the learner is aware of potential inaccuracies.

## Multi-Agent Coordination Protocols

- **State Management**: Drafts passed between Sage and Reviewer must be read-only and version-controlled.
- **Message Formatting**: All inter-agent communication must use standardized JSON payloads containing `draft_content`, `metadata` (audience level, domain), and `feedback_history`.
- **Latency Constraints**: Reviewer must complete its check within standard system timeouts to prevent degraded user experience.

## Human-in-the-Loop Requirements

While the Maker-Checker workflow is automated, human intervention is required when:
- The system flags a repeated high-confidence failure in foundational concepts.
- The user explicitly requests a human educator for clarification.
- System metrics indicate a prolonged deadlock between Sage and Reviewer on a specific topic cluster, requiring manual rule tuning or knowledge base updates.
