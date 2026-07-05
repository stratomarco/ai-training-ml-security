# Module 11 Checklist  -  AI Red Team Methodology

Use this checklist before, during, and after an AI red team engagement.

## 1. Mission and scope

- [ ] Engagement objective is defined.
- [ ] Business questions are clear.
- [ ] In-scope systems are listed.
- [ ] Out-of-scope systems are listed.
- [ ] Test environment is approved.
- [ ] Allowed accounts and roles are defined.
- [ ] Allowed data types are defined.
- [ ] Forbidden actions are defined.
- [ ] Emergency stop process is defined.
- [ ] Legal and policy approvals are complete.

## 2. System understanding

- [ ] Architecture is documented.
- [ ] Data flows are documented.
- [ ] Trust boundaries are identified.
- [ ] User roles are documented.
- [ ] Model role is understood.
- [ ] RAG sources are documented.
- [ ] Tools and permissions are documented.
- [ ] Memory behavior is documented.
- [ ] Logs and traces are understood.
- [ ] Monitoring and alerting are understood.

## 3. Threat model

- [ ] Assets are identified.
- [ ] Attacker personas are defined.
- [ ] Entry points are listed.
- [ ] Abuse cases are written.
- [ ] Attack paths are planned.
- [ ] Safety boundaries are included.
- [ ] Known assumptions are documented.

## 4. Test coverage

- [ ] Direct prompt injection tested.
- [ ] Indirect prompt injection tested.
- [ ] RAG authorization tested.
- [ ] Source trust and provenance tested.
- [ ] Tool authorization tested.
- [ ] Approval gates tested.
- [ ] Memory poisoning tested.
- [ ] Sensitive disclosure tested.
- [ ] Model DoS/cost abuse tested.
- [ ] Overreliance scenarios tested.
- [ ] Model extraction or abuse testing considered.
- [ ] Supply chain and MLOps review considered.
- [ ] Robustness and adversarial input testing considered.
- [ ] Infrastructure controls reviewed.

## 5. Evidence

- [ ] Test objective captured.
- [ ] Account and role captured.
- [ ] Input/prompt captured.
- [ ] Retrieved context captured.
- [ ] Model output captured.
- [ ] Tool-call trace captured.
- [ ] Logs or monitoring evidence captured.
- [ ] Impact captured.
- [ ] Reproduction steps captured.
- [ ] Sensitive data handled according to rules.

## 6. Finding quality

- [ ] Title is clear.
- [ ] Affected component is identified.
- [ ] Security property violated is stated.
- [ ] Preconditions are described.
- [ ] Attack path is clear.
- [ ] Evidence supports the claim.
- [ ] Impact is concrete.
- [ ] Root cause is identified.
- [ ] Severity is justified.
- [ ] Remediation is actionable.
- [ ] Detection opportunity is included.
- [ ] Residual risk is explained.

## 7. Remediation

- [ ] Fixes are mapped to owners.
- [ ] Quick wins are separated from architectural changes.
- [ ] Controls are placed outside the model where appropriate.
- [ ] Trade-offs are described.
- [ ] Regression tests are proposed.
- [ ] Monitoring improvements are proposed.
- [ ] Retest plan is defined.

## 8. Executive readout

- [ ] Scope is summarized.
- [ ] Most important risks are prioritized.
- [ ] Business impact is clear.
- [ ] Required decisions are stated.
- [ ] Residual risk is explained.
- [ ] Next steps are actionable.
