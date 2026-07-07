# BrokenPilot v2 Agentic Architecture

BrokenPilot v2 extends the v1 single-agent lab into a small deterministic agentic system. The goal is not to simulate a production agent framework. The goal is to expose the trust boundaries, identity assumptions, delegation decisions, and control-plane failures that appear when multiple agents coordinate through tools and protocol descriptors.

## Architecture goals

BrokenPilot v2 should teach students to answer these questions:

- Which agent is allowed to decide?
- Which agent is allowed to act?
- Which server advertised the tool or capability?
- Which descriptor was trusted, and why?
- Which message caused the next delegation step?
- Which control would have stopped the unsafe action?
- Which evidence proves the control worked?

## Components

### Orchestrator agent

The orchestrator receives the user request, chooses a workflow, delegates to sub-agents, and decides whether a final action should be attempted.

Security responsibility:

- preserve user and tenant context
- avoid blindly trusting sub-agent outputs
- request approvals for high-risk transitions
- attach a correlation ID to the workflow
- maintain an audit trail across delegation

### Retrieval/documentation agent

The retrieval agent searches documents, summaries, runbooks, and incident notes.

Security responsibility:

- enforce retrieval authorization
- label provenance of retrieved content
- distinguish instructions from evidence
- avoid turning retrieved text into agent policy
- return structured evidence rather than free-form authority

### Ticket/action agent

The action agent proposes or performs ticket changes.

Security responsibility:

- enforce action authorization
- check tenant and role boundaries
- require approval for destructive state changes
- refuse actions that exceed delegated authority

### Tool broker

The tool broker exposes tools to agents and mediates tool invocation.

Security responsibility:

- map tool capability to policy
- enforce agent identity
- validate descriptors
- block unapproved tools
- record tool calls and policy decisions

### MCP-like server boundary

The MCP-like boundary models a third-party tool or context provider. It is intentionally local and deterministic, but it behaves like an external capability provider.

Security responsibility:

- advertise descriptors
- expose tools or resources
- provide signed or unsigned metadata
- demonstrate descriptor poisoning and capability spoofing
- support trust and pinning controls

## Trust boundaries

BrokenPilot v2 should make these boundaries explicit:

1. User to orchestrator
2. Orchestrator to sub-agent
3. Sub-agent to tool broker
4. Tool broker to MCP-like server
5. Retrieval content to agent reasoning
6. Agent output to action layer
7. Audit events to instructor/student evidence

## Non-goals

BrokenPilot v2 does not need to be a full MCP implementation in the first increment.

The first target is a local teaching model with MCP-like descriptors, identity, capability advertisement, and trust decisions. Protocol fidelity can increase later once the learning path is stable.
