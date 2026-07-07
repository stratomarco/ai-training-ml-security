# v2 Module Draft: Agentic and MCP Security

This is a development-track module draft for the v2 branch. It is not part of the v1.1.0 stable teaching path.

## Learning goal

Students learn to secure agentic systems where multiple agents coordinate through shared tools, protocol descriptors, external capability servers, and delegated authority.

## Core security decision

When an agentic system accepts instructions, capabilities, or results from another agent or tool server, what evidence proves that the sender, descriptor, authority, and context are trustworthy enough to act on?

## Initial module shape

1. From single-agent to agentic systems
2. Agent identity and delegated authority
3. MCP-like tool-server trust boundaries
4. Descriptor poisoning and capability spoofing
5. Insecure inter-agent communication
6. Replay and rogue-agent behavior
7. Cascading failure across delegation chains
8. Controls: identity, signed descriptors, pinning, allowlists, approval gates, and audit correlation
9. Lab: BrokenPilot v2 multi-agent failure chain
10. Deliverable: agentic threat model and control validation report

## Required lab bar

This module should not ship until the lab has:

- a deterministic vulnerable baseline
- a deterministic control-on path
- tests for each control
- a student report template
- an instructor debrief
- a clear mapping to v2 failure chains
