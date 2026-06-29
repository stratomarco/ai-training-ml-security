# BrokenPilot Capstone Checklist

Use this checklist to review student submissions or guide team work.

## System understanding

- [ ] Business purpose is clearly explained.
- [ ] Major components are identified.
- [ ] Data flows are described.
- [ ] Trust boundaries are identified.
- [ ] User roles and attacker personas are described.
- [ ] Tool capabilities are understood.
- [ ] RAG and memory behavior are considered.

## Asset review

- [ ] Incident data is considered.
- [ ] Ticket data is considered.
- [ ] Service configuration is considered.
- [ ] Internal documents and runbooks are considered.
- [ ] Vector DB content and metadata are considered.
- [ ] Prompts, traces, and logs are considered.
- [ ] Memory entries are considered.
- [ ] Tool tokens and service credentials are considered.
- [ ] Workflow integrity is considered.

## Threat model

- [ ] At least four attacker personas are defined.
- [ ] Entry points include prompts, documents, tickets, memory, tool output, and rendered output.
- [ ] Abuse cases are realistic.
- [ ] Abuse cases connect to business impact.
- [ ] Security requirements are mapped to abuse cases.
- [ ] Risks are prioritized.

## LLM application security

- [ ] Direct prompt injection is considered.
- [ ] Indirect prompt injection is considered.
- [ ] System prompt leakage is considered.
- [ ] Sensitive information disclosure is considered.
- [ ] Insecure output handling is considered.
- [ ] Model DoS or cost abuse is considered.
- [ ] Overreliance is considered.

## RAG security

- [ ] Retrieved content is treated as untrusted.
- [ ] Document-level authorization is enforced before context assembly.
- [ ] Metadata preservation is considered.
- [ ] Cross-team leakage is considered.
- [ ] Poisoned documents are considered.
- [ ] Source trust is represented in the output.
- [ ] Citations do not create false confidence.

## Agent and tool security

- [ ] Tool permissions are scoped.
- [ ] Tool arguments are validated.
- [ ] Per-action authorization is required.
- [ ] High-impact actions require approval.
- [ ] Tool output is treated as untrusted input.
- [ ] Tool calls are logged.
- [ ] The model is not the final policy authority.

## Memory security

- [ ] Memory scope is defined.
- [ ] Memory write rules are defined.
- [ ] Sensitive data is not stored unnecessarily.
- [ ] Memory entries are reviewable.
- [ ] Memory entries can expire.
- [ ] Memory poisoning is considered.

## Privacy and data protection

- [ ] Prompt and trace logging is reviewed.
- [ ] Sensitive fields are minimized or redacted.
- [ ] Retention is defined.
- [ ] Deletion is supported where required.
- [ ] Cross-tenant or cross-team leakage is considered.
- [ ] Embedding/vector DB leakage is considered.

## MLOps and supply chain

- [ ] Model, prompt, tool, and retrieval changes are versioned.
- [ ] Datasets and documents have provenance.
- [ ] Model and artifact promotion gates are defined.
- [ ] Dependency and container risks are considered.
- [ ] Rollback is possible.
- [ ] Evaluation includes security test cases.

## Evidence quality

- [ ] Evidence uses fake data only.
- [ ] The role/account used is documented.
- [ ] Inputs are documented.
- [ ] Retrieved context is documented where relevant.
- [ ] Tool calls are documented where relevant.
- [ ] Impact is clearly explained.
- [ ] Root cause is explained.

## Mitigation quality

- [ ] Controls are placed outside the model where needed.
- [ ] Mitigations are specific and implementable.
- [ ] Trade-offs are acknowledged.
- [ ] Developer velocity is considered.
- [ ] Residual risk is stated.
- [ ] Remediation is prioritized.
- [ ] Validation tests are proposed.

## Communication quality

- [ ] Executive summary is clear.
- [ ] Top risks are prioritized.
- [ ] Technical details support the conclusion.
- [ ] Recommendations are actionable.
- [ ] Leadership decision points are explicit.
- [ ] The report avoids hype and overclaiming.
