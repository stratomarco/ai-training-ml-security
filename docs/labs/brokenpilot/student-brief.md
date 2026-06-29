# BrokenPilot Student Brief

## Assignment

You are reviewing BrokenPilot, an internal AI assistant used by engineering and operations teams at Northwind Systems.

BrokenPilot can search documents, summarize incidents, read and update tickets, query fake service configuration, use tools, and store memory.

Your job is to perform a security review before the system is rolled out more broadly.

## What you are given

You receive:

- System scenario.
- Architecture overview.
- Role descriptions.
- Data model.
- Tool inventory.
- Sample documents, tickets, and incidents if running as a hands-on lab.
- Course templates for threat modeling, abuse cases, risk register, and red-team reporting.

## Your tasks

### 1. Understand the system

Create a short architecture summary that explains:

- What BrokenPilot does.
- Who uses it.
- What data it can access.
- What actions it can perform.
- Which components are inside and outside major trust boundaries.

### 2. Identify assets

At minimum, consider:

- Internal documents.
- Tickets.
- Incident timelines.
- Service configuration.
- User/team memory.
- Model prompts and policy text.
- Tool permissions.
- Audit logs.
- Model and retrieval index versions.

### 3. Build a threat model

Your threat model should include:

- System context diagram.
- Data-flow diagram.
- Trust boundaries.
- Attacker personas.
- Abuse cases.
- Security assumptions.
- Initial risk list.

### 4. Demonstrate representative vulnerabilities

Demonstrate at least three different classes of vulnerability.

Good combinations include:

- Direct prompt injection.
- Indirect prompt injection through retrieved content.
- RAG authorization bypass.
- Tool misuse or confused deputy.
- Memory poisoning.
- Sensitive information disclosure.
- Insecure output handling.
- Weak auditability.

You do not need to exploit every issue. Depth is better than a long shallow list.

### 5. Explain root cause

For each finding, explain:

- What happened.
- Why it happened.
- Which trust boundary failed.
- Which assumption was unsafe.
- Which classic security principle applies.
- What makes the AI version different.

### 6. Propose mitigations

Your mitigation plan should include:

- Short-term controls.
- Long-term design changes.
- Detection and monitoring.
- Approval gates.
- Data and retrieval controls.
- Tool authorization controls.
- Memory controls.
- Logging and audit improvements.

### 7. Communicate residual risk

Explain what remains risky even after mitigations.

Examples:

- Prompt injection cannot be fully eliminated.
- RAG can still retrieve stale or incomplete content.
- Human approval can become rubber-stamping.
- Logs can create privacy risk.
- Strong controls may reduce usability or speed.

## Required deliverables

Submit:

1. Executive summary.
2. Architecture and trust-boundary summary.
3. Threat model.
4. Abuse cases.
5. Findings with evidence.
6. Risk register.
7. Mitigation plan.
8. Secure reference architecture.
9. Residual-risk statement.
10. Leadership talking points.

## Expected tone

Write like a security engineer helping a product team ship safely.

Avoid:

- Hype.
- Fearmongering.
- Prompt-hacking screenshots without explanation.
- Unrealistic recommendations that block all useful AI behavior.

Prefer:

- Clear engineering reasoning.
- Practical mitigations.
- Explicit trade-offs.
- Prioritized risk reduction.
- Clear ownership.
