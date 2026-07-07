# BrokenPilot v2

BrokenPilot v2 is the future agentic and MCP security track for the course.

v1 remains the stable teaching release. v2 work happens on a development branch and should not change the released v1 path until a v2 release candidate exists.

## Current status

The v2 track currently has:

- architecture notes
- threat-model notes
- a lab quality bar
- a minimal runnable skeleton in [`prototype-app/`](prototype-app/README.md)

The skeleton is not yet a student lab. It provides the executable base for future multi-agent and MCP failure-chain labs.

## Intended v2 direction

BrokenPilot v2 extends the v1 single-agent target into an agentic system with:

- orchestrator and sub-agent delegation
- explicit message envelopes
- an MCP-like descriptor registry
- a shared tool broker
- signed-descriptor and trust-boundary controls
- audit traces across multi-agent delegation
- future failure chains for descriptor spoofing, rogue agents, insecure inter-agent communication, and cascading agent failures
