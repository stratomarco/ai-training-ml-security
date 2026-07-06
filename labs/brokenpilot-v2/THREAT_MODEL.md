# BrokenPilot v2 Threat Model Draft

This draft captures the first threat-modeling scope for the v2 multi-agent and MCP security track.

## System under consideration

A small internal support agent system where an orchestrator delegates work to specialist agents that retrieve documents and update tickets through a tool broker and MCP-like server boundary.

## Assets

- tenant-specific documents
- incident and support tickets
- tool credentials
- agent descriptors
- tool descriptors
- delegation messages
- memory and context stores
- audit logs
- approval decisions

## Actors

- normal internal user
- user from another tenant or business unit
- malicious insider
- compromised MCP-like server
- rogue or spoofed agent
- compromised document source
- over-trusting human approver

## Threats to model first

### Spoofed tool descriptor

A malicious or compromised server advertises a capability that looks equivalent to a trusted internal tool but routes data to an unsafe endpoint.

### Rogue peer agent

A rogue agent clones a legitimate schema or role name and intercepts coordination traffic.

### Insecure inter-agent message

A poisoned instruction crosses from one agent to another as if it were trusted coordination data.

### Cascading failure

One bad retrieval result or poisoned agent response causes downstream planning, routing, and action decisions to fail.

### Replay of delegated action

A previously valid delegation request is replayed to trigger a tool call outside its intended context.

### Descriptor drift

A trusted MCP-like server changes its descriptor or tool schema after approval, expanding capabilities without a matching review.

## Controls to explore

- signed agent identity
- signed or pinned tool descriptors
- descriptor-change approval
- tool-broker allowlists
- audience-bound delegation tokens
- nonces and timestamps
- policy checks at delegation and action time
- audit trace correlation
- blast-radius limits for sub-agents

## First lab candidate

A fake MCP-like endpoint advertises a spoofed ticket-update capability. With controls disabled, the orchestrator routes sensitive task context through the endpoint. With descriptor pinning and broker policy enabled, the route is blocked or requires approval.

## Second lab candidate

A poisoned retrieval result causes the retrieval agent to instruct the action agent to close a ticket. With controls disabled, the action cascades. With delegation policy, tool authorization, and approval enabled, the chain is stopped and the audit trail shows where.
