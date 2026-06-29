# BrokenPilot Scenario

## Business context

BrokenPilot is an internal AI assistant adopted by a fictional technology company called **Northwind Systems**.

Northwind has engineering, SRE, platform, security, and customer operations teams. The company runs several internal services and uses a ticketing system for incidents, change requests, customer escalations, and operational tasks.

Leadership wants BrokenPilot to reduce operational toil by helping teams summarize incidents, find documentation, draft postmortems, and create or update tickets.

## System purpose

BrokenPilot is intended to help authorized employees:

- Ask operational questions.
- Find relevant documentation.
- Summarize active incidents.
- Draft incident updates.
- Create new tickets.
- Update ticket priority and status.
- Query service configuration.
- Remember user preferences.

## Key business pressure

BrokenPilot was introduced quickly because teams were overwhelmed with operational load. The initial proof of concept was successful, so the system was promoted into wider internal use before all security controls were mature.

Engineering values speed and usability. Security must therefore propose controls that reduce risk without turning the assistant into a slow, unusable approval machine.

## Initial assumptions

For the capstone, assume:

- BrokenPilot is internal only.
- All data is fake.
- All users are simulated.
- All tools operate on fake local systems.
- There is no connection to real production infrastructure.
- Students must not test against external systems.
- The environment should be treated as a controlled security training lab.

## Student mission

You are part of the Product Security team reviewing BrokenPilot before a broader company rollout.

Your mission is to:

1. Understand the system architecture.
2. Identify assets, trust boundaries, and attacker goals.
3. Build a threat model.
4. Demonstrate representative vulnerabilities.
5. Explain root causes.
6. Propose practical mitigations.
7. Define residual risk.
8. Present the findings to engineering and leadership.

## Security questions to answer

Students should be able to answer:

- What can the model see?
- What can the model do?
- Which data sources are trusted?
- Which data sources are attacker-controlled?
- Where is authorization enforced?
- Which decisions are made by deterministic code?
- Which decisions are delegated to the model?
- Which actions require human approval?
- What is logged?
- What can be rolled back?
- What would an attacker try first?
- What could go wrong if the assistant is wrong but confident?

## Capstone framing

BrokenPilot should be treated as an AI-enabled application, not as a model-only problem.

The model is one component inside a larger system. The security review must include:

- Web application security.
- API security.
- Identity and access management.
- Data authorization.
- RAG architecture.
- Agent/tool permissions.
- Memory behavior.
- Logging and monitoring.
- Supply chain and model provenance.
- Privacy and data retention.
- Incident response and recovery.
