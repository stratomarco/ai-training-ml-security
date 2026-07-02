# Lab  -  BrokenPilot Attack-Chain Red Team

## Purpose

Practice turning AI vulnerabilities into structured attack chains, findings, mitigations, and residual-risk statements.

This lab uses the BrokenPilot capstone paper design as the target system.

## Prerequisites

Read:

- [`../brokenpilot/scenario.md`](../brokenpilot/scenario.md)
- [`../brokenpilot/architecture.md`](../brokenpilot/architecture.md)
- [`../brokenpilot/roles.md`](../brokenpilot/roles.md)
- [`../brokenpilot/tools.md`](../brokenpilot/tools.md)
- [`../brokenpilot/vulnerabilities.md`](../brokenpilot/vulnerabilities.md)
- [`../brokenpilot/attack-paths.md`](../brokenpilot/attack-paths.md)

## Scenario

BrokenPilot is an internal AI operations assistant.

It helps engineers and operations staff summarize incidents, search internal runbooks, retrieve fake configuration data, and create or update tickets.

The red team must assess whether BrokenPilot can be abused to:

- leak restricted information;
- follow malicious retrieved instructions;
- perform unauthorized ticket actions;
- misuse tools;
- persist malicious instructions in memory;
- mislead operators during incident response;
- operate without adequate audit evidence.

## Attack-chain format

Each team must define at least one full attack chain:

```text
attacker entry point
  -> model or retrieval behavior
  -> failed control
  -> unauthorized data access or action
  -> impact
  -> evidence
  -> remediation
```

## Suggested attack chains

### Chain 1  -  Indirect prompt injection to tool misuse

```text
attacker creates malicious runbook
  -> RAG retrieves runbook
  -> model follows hidden instruction
  -> model calls ticket update tool
  -> tool gateway lacks per-action authorization
  -> restricted ticket is modified
```

Security properties:

- integrity;
- authorization;
- workflow control;
- auditability.

### Chain 2  -  Cross-role retrieval leakage

```text
low-privilege user asks about incident pattern
  -> retrieval fetches restricted incident notes
  -> model summarizes restricted content
  -> application fails to enforce document-level authorization
  -> sensitive incident context leaks
```

Security properties:

- confidentiality;
- least privilege;
- tenant or role isolation.

### Chain 3  -  Memory poisoning

```text
attacker plants preference in memory
  -> later session retrieves memory
  -> model treats memory as trusted instruction
  -> future answer or tool call is influenced
```

Security properties:

- persistence integrity;
- trust separation;
- auditability.

### Chain 4  -  Overreliance during incident response

```text
assistant produces confident but wrong remediation
  -> operator follows recommendation
  -> incident impact increases
  -> UI does not indicate uncertainty or source limitations
```

Security properties:

- safety;
- reliability;
- decision support integrity.

## Student tasks

### Task 1  -  Choose an attack chain

Pick one chain or create your own.

### Task 2  -  Define prerequisites

Document:

- attacker role;
- required access;
- required data/control point;
- system assumptions;
- constraints.

### Task 3  -  Define test steps

Write safe, lab-only steps.

Do not use real secrets, real customer data, real production systems, or uncontrolled destructive actions.

### Task 4  -  Define expected evidence

Capture:

- input;
- retrieved content;
- model output;
- tool call;
- authorization decision;
- logs;
- final impact.

### Task 5  -  Write the finding

Use [`../../course-templates/ai-red-team-report-template.md`](../../course-templates/ai-red-team-report-template.md) or [`../../course-templates/red-team-report-template.md`](../../course-templates/red-team-report-template.md).

### Task 6  -  Recommend mitigations

Include:

- one quick mitigation;
- one architectural mitigation;
- one detection/monitoring improvement;
- one residual-risk statement.

## Deliverable

Submit:

1. Attack chain diagram.
2. Test plan.
3. Evidence plan.
4. Finding.
5. Remediation plan.
6. Executive summary.

## Success criteria

A strong submission:

- ties the issue to architecture;
- explains the failed control;
- collects relevant evidence;
- recommends controls outside the model;
- explains detectability;
- communicates residual risk.
