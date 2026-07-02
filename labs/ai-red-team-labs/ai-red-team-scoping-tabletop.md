# Lab  -  AI Red Team Scoping Tabletop

## Purpose

Practice defining a safe, useful, and legally bounded AI red team engagement.

Many AI red team exercises fail because scope is vague. This tabletop forces students to define what is being tested, what is not being tested, what data may be used, which actions are forbidden, and what evidence must be collected.

## Scenario

Your organization wants to red team an internal AI assistant before expanding access from a small pilot group to all engineering teams.

The assistant can:

- answer questions from internal docs;
- summarize incident tickets;
- retrieve fake configuration data;
- create and update tickets;
- store conversation memory;
- call tools through an API gateway.

The organization asks: “Is this safe enough for a wider internal rollout?”

## Team roles

Assign students to roles:

| Role | Responsibility |
|---|---|
| Red team lead | Defines objectives, scope, and attack plan. |
| AppSec engineer | Reviews application, RAG, and tool controls. |
| ML/platform engineer | Explains model, retrieval, memory, and MLOps assumptions. |
| Product owner | Defines business impact and acceptable residual risk. |
| Incident responder | Defines monitoring, evidence, escalation, and stop conditions. |

## Task 1  -  Define mission

Write a one-paragraph mission statement.

Example:

> Assess whether attacker-controlled prompts or documents can cause BrokenPilot to disclose restricted information, perform unauthorized ticket actions, or mislead operators during incident response.

## Task 2  -  Define in-scope systems

List in-scope components:

- application UI;
- LLM gateway;
- prompt templates;
- RAG service;
- vector database;
- fake ticket system;
- fake document store;
- fake configuration API;
- tool gateway;
- memory store;
- logs and traces.

## Task 3  -  Define out-of-scope systems

List out-of-scope components:

- production systems;
- real customer data;
- employee personal data;
- external phishing;
- destructive infrastructure testing;
- credential theft outside the lab;
- persistence outside approved environment.

## Task 4  -  Rules of engagement

Define:

- test dates;
- environment;
- accounts;
- allowed payload types;
- forbidden actions;
- rate limits;
- token/cost budgets;
- tool-use limits;
- data handling rules;
- logging requirements;
- escalation contacts;
- emergency stop conditions.

## Task 5  -  Evidence requirements

For each finding, require:

- test objective;
- account and role;
- input or prompt;
- retrieved context;
- model output;
- tool-call trace;
- affected asset;
- log evidence;
- impact statement;
- remediation recommendation.

## Task 6  -  Success criteria

Define what success means for the engagement.

Examples:

- At least one attack path per major component is tested.
- Tool authorization is validated independently of model output.
- RAG authorization is tested across user roles.
- Sensitive data disclosure is tested using fake restricted records.
- Logging and traceability are validated.
- Findings include actionable remediation.

## Deliverable

Submit a short red team engagement plan with:

1. Mission.
2. Scope.
3. Out-of-scope boundaries.
4. Rules of engagement.
5. Evidence requirements.
6. Success criteria.
7. Safety assumptions.

## Instructor notes

Push students away from vague scope language.

Bad:

> Test the chatbot.

Better:

> Test whether attacker-controlled user input or retrieved documents can influence BrokenPilot into leaking restricted incident context or calling ticket-modification tools without independent authorization.
