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
