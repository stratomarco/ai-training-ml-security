# Module 04 Student Handout  -  BIML and Architectural Risk Analysis

## One-sentence summary

Architectural risk analysis is a structured way to find AI security risks before they become production vulnerabilities.

## Core idea

AI security is not only about model behavior. It is about the system around the model.

A model response becomes dangerous when the surrounding architecture gives it access to:

- sensitive data
- privileged tools
- unsafe rendering paths
- business workflows
- memory
- feedback loops
- cross-tenant context
- production decisions

## What BIML contributes

BIML provides a security engineering lens for ML systems.

Instead of starting with exploit strings, start with the architecture:

- components
- data flows
- trust boundaries
- assumptions
- attacker goals
- design risks
- security requirements
- residual risk

## Design-level risk

A design-level risk exists because of how the system is built, not because of one coding mistake.

Examples:

| Design choice | Risk |
|---|---|
| Model decides whether a user is allowed to update a record | Authorization depends on probabilistic output |
| Retrieved documents are inserted into context without access checks | Cross-user or cross-tenant data exposure |
| Model output is rendered as trusted HTML | Insecure output handling |
| Agent has broad tool credentials | Prompt injection can become privileged action |
| Memory stores model-generated instructions | Persistent attacker influence |
| Logs store full prompts and retrieved data | Sensitive data leakage |

## Architecture review questions

Use these questions for every AI system:

### 1. What are we building?

Describe the system in plain language.

### 2. What are the assets?

Examples:

- user data
- customer records
- internal documents
- prompts
- model outputs
- embeddings
- model artifacts
- tool credentials
- logs
- business decisions

### 3. Who are the users and attackers?

Examples:

- normal user
- malicious user
- low-privilege internal user
- compromised account
- external attacker
- malicious document author
- supply chain attacker

### 4. Where are the trust boundaries?

Examples:

- browser to application
- application to model provider
- retrieved document to model context
- model output to application logic
- model-generated tool arguments to tool broker
- user identity to document retrieval
- tenant data to shared vector database

### 5. What can the model do?

Ask:

- Can it only answer?
- Can it retrieve documents?
- Can it use tools?
- Can it write data?
- Can it send messages?
- Can it execute code?
- Can it store memory?
- Can it trigger workflows?

### 6. What does the model know?

Ask:

- What is included in the prompt?
- What is retrieved?
- What user data is included?
- What system instructions are included?
- What previous memory is included?
- What logs are retained?

### 7. What assumptions are unsafe?

Common unsafe assumptions:

- users will not attack the system
- internal documents are safe
- model output is safe
- the model can enforce policy
- the model can keep secrets
- the model knows the user’s permissions
- a guardrail catches everything
- logs are harmless
- feedback is honest

## Abuse cases

A use case describes expected behavior.

An abuse case describes intentional misuse.

Example:

| Use case | Abuse case |
|---|---|
| User asks assistant to summarize an incident | User hides instructions in the incident to make the assistant leak confidential context |
| Assistant retrieves related docs | Malicious document injects instructions into the model context |
| Assistant updates a ticket | Prompt injection causes unauthorized ticket update |

## Security requirements

Architecture review should produce requirements, not just risks.

Examples:

- The model must not make authorization decisions.
- Retrieval must enforce user-level document permissions.
- Retrieved text must be treated as untrusted data.
- Model output must be encoded before rendering.
- Tool calls must be authorized per user and action.
- Destructive actions require human approval.
- Tool credentials must be scoped.
- Sensitive prompt and retrieval data must be redacted from logs.
- Memory writes must be controlled and auditable.
- All tool calls must be logged.

## Residual risk

After mitigation, ask:

- What can still go wrong?
- How likely is it?
- What is the impact?
- What is monitored?
- Who owns the risk?
- When should the risk be reviewed again?

## Deliverable checklist

Your architecture risk review should include:

- [ ] System summary
- [ ] Architecture diagram or component list
- [ ] Asset list
- [ ] Data flows
- [ ] Trust boundaries
- [ ] Assumptions
- [ ] Abuse cases
- [ ] Prioritized risks
- [ ] Security requirements
- [ ] Mitigations
- [ ] Residual risk statement
