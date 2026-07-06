# BrokenPilot v2 Architecture Sketch

BrokenPilot v2 extends the single-agent v1 lab into a multi-agent system that exposes agentic-system trust boundaries without requiring a large production stack.

## Initial components

### User-facing orchestrator

Receives the user request, decides whether to answer directly or delegate to a specialist, and creates a delegation trace.

### Triage or planning agent

Classifies the task and proposes a route. This agent is a useful target for goal hijack and routing manipulation.

### Retrieval/documentation agent

Searches policy, runbook, and incident documents. This agent is a useful target for indirect prompt injection, retrieval authorization errors, and poisoned evidence.

### Ticket/action agent

Creates or updates tickets through the tool broker. This agent is a useful target for excessive agency, confused-deputy authorization, and unsafe action execution.

### Tool broker

Mediates access to tools and MCP-like servers. It should become the main enforcement point for identity, capability, policy, descriptor pinning, and approval gates.

### MCP-like server boundary

Represents an external tool or context server. It should expose descriptor metadata, capabilities, and tool schemas that can be trusted, pinned, spoofed, poisoned, or changed.

## Trust boundaries

- user to orchestrator
- orchestrator to sub-agent
- sub-agent to sub-agent
- agent to tool broker
- tool broker to MCP-like server
- retrieval agent to document store
- action agent to ticket system
- audit pipeline to evidence store

## New security properties

BrokenPilot v2 should make these properties visible:

- which agent made a decision
- which agent delegated the task
- which descriptor or capability was trusted
- which policy authorized the action
- which evidence crossed an agent boundary
- where a poisoned instruction entered
- where the cascade should have stopped

## Candidate control toggles

- enable agent identity verification
- enable signed descriptor verification
- enable descriptor pinning
- enable anti-replay checks
- enable tool-broker authorization
- enable delegation policy checks
- enable cross-agent audit correlation
- enable human approval for descriptor changes

## Design rule

Every control toggle should have:

- an unsafe baseline behavior
- a secure behavior
- a test
- a student-observable evidence trail
- a debrief question about residual risk
