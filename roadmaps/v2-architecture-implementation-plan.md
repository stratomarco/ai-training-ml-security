# v2 Architecture Implementation Plan

This document is the first implementation-planning artifact for the v2 development branch.

v1.1.0 remains the stable teaching release. v2 work happens on a separate development branch and should not rewrite the v1 learning path until a v2 release candidate exists.

## v2.0 scope

v2.0 focuses on the risk surface that appears when a single-agent application becomes an agentic system:

- an orchestrator delegating to sub-agents
- an explicit tool broker
- an MCP-like server boundary
- agent identity and descriptor trust
- inter-agent message integrity
- cascading failure across delegation
- rogue or spoofed agent behavior
- audit evidence across a multi-agent workflow

This is not a new course. It is an extension of the v1 security-engineering spine.

## Phasing

### Phase A: architecture and threat model

Create the BrokenPilot v2 architecture specification, message envelope, trust-boundary model, control matrix, and failure chains before writing code.

### Phase B: minimal runnable skeleton

Add a deterministic multi-agent skeleton with no external model dependency:

- orchestrator agent
- retrieval/documentation agent
- ticket/action agent
- tool broker
- MCP-like descriptor registry
- audit trace

### Phase C: vulnerable flows

Add intentionally vulnerable flows:

- unsigned descriptor acceptance
- spoofed capability advertisement
- message replay
- delegation-chain poisoning
- rogue peer impersonation

### Phase D: controls and tests

Add controls one at a time:

- signed descriptors
- descriptor pinning
- agent identity
- message authentication
- replay prevention
- broker allowlist
- approval on descriptor change
- audit correlation across agents

Every control must have a failing baseline test and a passing control-on test.

## v2 lab quality bar

Every v2 lab must have:

- an observable failure
- a control that changes the outcome
- a naive fix that still fails
- a defense-in-depth discussion
- a graded artifact
- deterministic reset behavior
- an instructor debrief path
- a validation or test artifact
