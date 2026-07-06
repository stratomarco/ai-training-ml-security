# v2 Module Outline: Agentic and MCP Security

This is a planning outline for a future v2 module or module pair. It is not part of the v1.1.0 release path.

## Core security decision

How do we trust, constrain, observe, and safely compose agents, tools, and MCP-like servers when work is delegated across a system rather than performed by one agent?

## Learning objectives

Students should be able to:

- identify agentic-system trust boundaries
- distinguish single-agent risks from multi-agent risks
- threat model inter-agent communication
- evaluate tool and server descriptors as supply-chain artifacts
- reason about agent identity and privilege
- explain cascading failure paths
- design controls for tool brokers and delegation chains
- produce evidence that a control stopped an unsafe chain

## Proposed lesson sequence

1. From single agent to agentic system
2. Agent identity, role, and delegation
3. Tool broker as enforcement point
4. MCP-like descriptor and server trust boundary
5. Insecure inter-agent communication
6. Cascading failures and blast radius
7. Rogue agents and spoofed capabilities
8. Controls: signed descriptors, pinning, mTLS-style trust, anti-replay, policy gates, approval, audit
9. Lab: spoofed MCP-like endpoint
10. Lab: cascading failure across agents

## Lab dependency

This module depends on BrokenPilot v2 or another small multi-agent target. It should not ship as a reading-only module.

## Relationship to v1 modules

- Extends Module 05 LLM Application Security
- Extends Module 06 RAG Security
- Extends Module 07 Agent and Tool Security
- Extends Module 08 Secure MLOps and Supply Chain
- Extends Module 11 AI Red Team Methodology
- Feeds a future v2 capstone
