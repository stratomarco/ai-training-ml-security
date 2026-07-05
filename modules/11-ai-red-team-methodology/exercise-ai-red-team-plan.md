# Exercise  -  AI Red Team Plan

## Purpose

Practice planning an AI red team engagement before testing.

Students will define scope, rules of engagement, threat model, attack paths, evidence requirements, and success criteria for an AI-enabled system.

## Scenario

You are asked to red team **BrokenPilot**, an internal AI operations assistant.

BrokenPilot can:

- summarize incident tickets;
- search internal runbooks;
- retrieve configuration data;
- create tickets;
- update tickets;
- store user preferences in memory;
- use tools through an API gateway.

The organization wants to know whether BrokenPilot can be safely piloted with engineering and operations teams.

## Student tasks

### Task 1  -  Define scope

Document:

- systems in scope;
- systems out of scope;
- allowed test environment;
- allowed accounts;
- allowed data;
- allowed payload classes;
- forbidden actions;
- stop conditions;
- escalation contacts.

### Task 2  -  Identify assets

List the assets that need protection:

- incident data;
- internal documents;
- configuration records;
- tool APIs;
- model prompts and hidden instructions;
- user memory;
- audit logs;
- model and provider credentials;
- business workflow integrity.

### Task 3  -  Identify trust boundaries

Draw or describe trust boundaries between:

- user and application;
- application and model provider;
- RAG service and document store;
- vector database and authorization layer;
- model and tools;
- tool gateway and backend systems;
- memory store and user sessions;
- logs and monitoring.

### Task 4  -  Create attack paths

Create at least three attack paths.

Each attack path should include:

- attacker goal;
- entry point;
- preconditions;
- steps;
- expected vulnerable behavior;
- expected impact;
- evidence to collect;
- mitigation to validate.

Suggested categories:

- prompt injection;
- indirect prompt injection through retrieved documents;
- unauthorized retrieval;
- excessive agency;
- tool misuse;
- memory poisoning;
- sensitive information disclosure;
- model DoS;
- overreliance.

### Task 5  -  Define evidence requirements

For each test, define what evidence must be captured:

- prompt or input;
- retrieved context;
- model output;
- tool-call trace;
- API response;
- logs;
- screenshot or transcript;
- affected asset;
- impact statement.

### Task 6  -  Write one finding

Choose one attack path and write a finding using the red-team report template.

The finding must include:

- title;
- summary;
- affected component;
- attack path;
- evidence;
- impact;
- root cause;
- severity;
- recommended fixes;
- residual risk.

## Deliverable

Submit:

1. Rules of engagement.
2. Threat model summary.
3. Three attack paths.
4. Evidence plan.
5. One complete finding.
6. Remediation recommendations.

## Success criteria

A strong submission:

- stays within scope;
- avoids real data;
- identifies realistic attack paths;
- connects failures to architecture;
- provides evidence requirements;
- recommends controls outside the model;
- explains residual risk.
