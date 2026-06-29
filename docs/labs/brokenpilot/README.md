# BrokenPilot Capstone

BrokenPilot is the final capstone scenario for **AI Training — ML Security**.

It is intentionally designed as a realistic internal AI assistant rather than a toy chatbot. The goal is to force students to combine classic security engineering, ML system architecture, LLM application security, RAG security, agent/tool security, privacy, MLOps, red teaming, and residual-risk communication.

## Scenario summary

BrokenPilot is an internal AI assistant used by engineering and operations teams.

It can:

- Summarize incidents.
- Search internal documentation.
- Read tickets.
- Create tickets.
- Update ticket status and priority.
- Query fake IT and service configuration data.
- Retrieve context from a vector database.
- Use tools through an API.
- Store user and workspace memory.
- Generate incident summaries and postmortem drafts.

The system is intentionally flawed. Students must identify what can go wrong, demonstrate representative failures in a safe lab setting, and propose a secure reference architecture.

## Learning goals

By completing the capstone, students should be able to:

1. Build a system-level threat model for an AI-enabled internal operations assistant.
2. Identify assets, trust boundaries, assumptions, and attacker goals.
3. Explain why prompts are not security boundaries.
4. Demonstrate direct prompt injection, indirect prompt injection, RAG poisoning, tool misuse, excessive agency, and memory poisoning.
5. Explain how normal AppSec, identity, cloud, data, and supply-chain risks show up in AI systems.
6. Design practical mitigations that preserve developer velocity.
7. Produce a red-team report, risk register, secure architecture proposal, and residual-risk statement.
8. Communicate findings to both engineering and leadership audiences.

## Capstone files

| File | Purpose |
|---|---|
| [`scenario.md`](scenario.md) | Business context, system purpose, assumptions, and student mission. |
| [`architecture.md`](architecture.md) | Component model, data flows, trust boundaries, and architecture diagrams. |
| [`roles.md`](roles.md) | Users, attacker personas, permissions, and abuse assumptions. |
| [`data-model.md`](data-model.md) | Fake datasets, document collections, tickets, config records, memories, and logs. |
| [`tools.md`](tools.md) | Tool inventory, intended permissions, risky operations, and required controls. |
| [`vulnerabilities.md`](vulnerabilities.md) | Intentional vulnerability list mapped to course modules. |
| [`attack-paths.md`](attack-paths.md) | Suggested attack chains for student and instructor use. |
| [`student-brief.md`](student-brief.md) | Student-facing assignment brief. |
| [`instructor-solution.md`](instructor-solution.md) | Instructor-only guide with expected findings and discussion prompts. |
| [`secure-reference-architecture.md`](secure-reference-architecture.md) | Target-state control design and secure architecture. |
| [`grading-rubric.md`](grading-rubric.md) | BrokenPilot-specific grading rubric. |
| [`implementation-notes.md`](implementation-notes.md) | Guidance for later converting the paper design into a local lab app. |
| [`module-mapping.md`](module-mapping.md) | Mapping from BrokenPilot tasks to course modules and deliverables. |

## Expected vulnerability classes

- Direct prompt injection.
- Indirect prompt injection.
- RAG poisoning.
- Sensitive data disclosure.
- Cross-document authorization failure.
- Tool misuse.
- Excessive agency.
- Memory poisoning.
- Insecure output handling.
- Weak audit logging.
- Overreliance.
- Missing human approval.
- Weak rate limiting.
- Poor secret handling.
- Unsafe feedback loops.
- Weak model/data provenance.

## Student deliverables

Students must produce:

1. System context diagram.
2. Data-flow diagram with trust boundaries.
3. Threat model.
4. Abuse cases.
5. Attack narrative with evidence.
6. Risk register.
7. Mitigation plan.
8. Secure reference architecture.
9. Residual-risk statement.
10. Executive summary.

## Instructor principle

Do not let the capstone become a prompt-hacking contest.

The expected outcome is not only that students can break the assistant. The expected outcome is that students can explain **why the architecture allowed the failure**, what should be changed, what remains risky, and how to communicate the decision to engineering and leadership.


## v0.14 teaching support guides

| File | Purpose |
|---|---|
| `final-presentation-guide.md` | Helps students prepare the final leadership and engineering readout. |
| `evidence-log-guide.md` | Defines safe, useful evidence handling for capstone findings. |
| `remediation-backlog-guide.md` | Converts findings into actionable engineering work. |
