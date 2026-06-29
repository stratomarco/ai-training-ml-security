# BrokenPilot Prototype Student Lab Flow

This file defines how students should use the future runnable prototype.

## Lab sequence

Students should not start by randomly attacking the app. The lab should follow the same security engineering flow used throughout the course.

1. Understand the scenario.
2. Identify assets and trust boundaries.
3. Run the vulnerable behavior.
4. Capture evidence.
5. Explain the root cause.
6. Enable or design a control.
7. Compare vulnerable and hardened behavior.
8. Write a finding.
9. Add a remediation task.
10. Prepare a short readout.

## Student tasks

### Task 1 — Start the system

Start BrokenPilot locally and confirm the health check works.

Expected evidence:

- Screenshot or command output showing the app is running.
- Active mode: vulnerable or hardened.

### Task 2 — Map the architecture

Draw a minimal data-flow diagram with:

- User/browser
- Backend
- Retrieval service
- Documents
- Mock LLM
- Tools
- Memory
- Audit log
- Policy layer

Expected evidence:

- DFD with at least three trust boundaries.

### Task 3 — Trigger indirect prompt injection

Use a query that retrieves a poisoned document and observe whether the assistant follows document-supplied instructions.

Expected evidence:

- User input
- Retrieved document IDs
- Assistant output
- Any tool intent or policy decision

### Task 4 — Trigger cross-document retrieval

Use a lower-privileged user and attempt to retrieve documents outside that user's allowed role/team.

Expected evidence:

- Active user
- Retrieved document metadata
- Explanation of why the retrieval should or should not have been allowed

### Task 5 — Trigger tool confused deputy

Observe whether the assistant can cause a ticket update that the active user should not be allowed to perform.

Expected evidence:

- Ticket before/after state
- Requested tool action
- User permission
- Policy decision

### Task 6 — Test hardened mode

Enable one or more controls and repeat the relevant task.

Expected evidence:

- Control enabled
- New behavior
- Deny/approval/log output

### Task 7 — Write findings

For each finding, include:

- Title
- Impact
- Evidence
- Root cause
- Violated security property
- Recommended control
- Test case for the fix

## Success criteria

A good student submission explains both the failure and the fix.

A weak submission only says “the model was jailbroken” without explaining the violated trust boundary, missing authorization check, or required control.
