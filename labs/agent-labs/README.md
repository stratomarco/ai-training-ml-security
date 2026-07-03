# Agent Labs

This folder contains controlled, fake-data labs for agent and tool security.

These labs should be run only in local or dedicated training environments. They are designed to teach secure design, threat modeling, and defensive controls for AI agents. They are not intended for attacking real systems.

## Labs

- `agent-tool-misuse-lab.md`  -  tool misuse, excessive agency, tool permission matrix, approval gates.
- `memory-poisoning-approval-gates-lab.md`  -  persistent memory risk, provenance, review, expiry, and approval workflow.

## Lab philosophy

Each agent lab should teach the same pattern:

1. What can the agent do?
2. What identity does it use?
3. What data can influence it?
4. What tools can it call?
5. What can go wrong?
6. What controls should exist outside the model?
7. What should be logged, approved, monitored, and reversible?

<!-- LAB_QUALITY_STANDARD_AGENT_CONSOLIDATION:START -->
## Runnable path

The runnable agent-security path is BrokenPilot, not this paper folder.

Use these labs for hands-on work:

- `../brokenpilot/prototype-app/TOOL_CALLING_LAB.md`
- `../brokenpilot/prototype-app/MEMORY_POISONING_LAB.md`
- `../brokenpilot/STANDALONE_CORE_LAB_PATH.md`
- `../../modules/07-agent-tool-security/brokenpilot-tool-validation.md`
- `../../modules/07-agent-tool-security/brokenpilot-memory-validation.md`

This folder remains as a scenario and discussion index only. Do not maintain a second paper version of the same agent lab when BrokenPilot can demonstrate the behavior directly.

## Required deliverable

Students should produce a tool permission matrix or approval policy that includes user role, tenant or object scope, permitted action, denied action, approval requirement, audit requirement, and validation request.

The graded artifact is the control design and validation, not the fact that the model can be tricked.
<!-- LAB_QUALITY_STANDARD_AGENT_CONSOLIDATION:END -->
