# Multi-Agent Patterns in OpenGAP

OpenGAP thrives in multi-agent environments. By standardizing agent interfaces and roles, OpenGAP enables robust enterprise architectures.

## The Maker-Checker Pattern (Segregation of Duties)

The Maker-Checker pattern involves two distinct agents:
1. **Maker (Creator):** Generates content, code, or data.
2. **Checker (Reviewer):** Validates the Maker's output against defined constraints.

### OpenGAP Implementation
- Define two agents in the `agents/` directory (e.g., `agents/maker/` and `agents/checker/`).
- Use `DUTIES.md` to strictly isolate capabilities (Maker has `write` tools, Checker only has `read` tools).

## Socratic Tutoring & Adaptive Scaffolding

This pattern involves an Orchestrator and specialized Tutors. The Orchestrator assesses the user's level and delegates to the appropriate Tutor (Beginner, Intermediate, Advanced).

### OpenGAP Implementation
- The Orchestrator's `DUTIES.md` includes routing logic.
- Each Tutor has a specialized `SOUL.md` tailored to their target audience.

## Hierarchical Delegation & Orchestrator Routing

In complex workflows, a Manager agent breaks down a goal into subtasks and delegates them to Worker agents.

### OpenGAP Implementation
- Manager agent has access to a `delegate_task` tool.
- Sub-agents are completely isolated and only return results to the Manager, maintaining a clean state.

## Immutable Audit Trails with Git

Every action and state change in an OpenGAP multi-agent system should be version-controlled. Agent interactions, decisions, and tool executions can be logged as commits, providing an immutable audit trail for enterprise compliance.
