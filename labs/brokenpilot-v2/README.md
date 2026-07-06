# BrokenPilot v2 Planning Area

This folder is the planning area for the v2 multi-agent and MCP security track.

It is not part of the v1.1.0 stable teaching path yet. Do not wire this folder into the v1 module sequence or capstone until the v2 labs have runnable targets, tests, instructor guidance, and graded deliverables.

Start with:

1. [`ARCHITECTURE.md`](ARCHITECTURE.md)
2. [`THREAT_MODEL.md`](THREAT_MODEL.md)
3. [`LAB_QUALITY_BAR.md`](LAB_QUALITY_BAR.md)

## Target direction

BrokenPilot v2 should extend the existing BrokenPilot model from a single agent into a small multi-agent system with:

- orchestrator agent
- specialist sub-agents
- shared tool broker
- MCP-like server boundary
- explicit agent identity
- signed or pinned tool descriptors
- cross-agent audit traces
- failure and control toggles suitable for labs

## Release rule

This folder can evolve on the dev branch. It should not be treated as released course content until a future v2 release candidate.
