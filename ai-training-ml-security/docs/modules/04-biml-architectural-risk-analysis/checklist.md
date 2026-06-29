# Checklist — BIML-Style AI Architecture Risk Review

Use this checklist during design review of ML, LLM, RAG, and agent systems.

## 1. System definition

- [ ] The system purpose is clearly described.
- [ ] The AI/ML components are identified.
- [ ] The non-AI components are identified.
- [ ] Human users and roles are identified.
- [ ] Automated actors and agents are identified.
- [ ] External providers and dependencies are identified.
- [ ] Production impact is understood.

## 2. Asset identification

- [ ] User data is identified.
- [ ] Customer or employee data is identified.
- [ ] Internal documents are identified.
- [ ] Training data is identified.
- [ ] Labels or annotations are identified.
- [ ] Embeddings are identified.
- [ ] Vector database contents are identified.
- [ ] Model artifacts are identified.
- [ ] Prompts and system instructions are identified.
- [ ] Tool credentials are identified.
- [ ] Logs and traces are identified.
- [ ] Memory and feedback stores are identified.
- [ ] Business decisions or workflow actions are identified.

## 3. Trust boundaries

- [ ] User input to application boundary is identified.
- [ ] Application to model boundary is identified.
- [ ] Application to retrieval service boundary is identified.
- [ ] Retrieval to prompt context boundary is identified.
- [ ] Model output to application logic boundary is identified.
- [ ] Model output to rendering boundary is identified.
- [ ] Model output to tool call boundary is identified.
- [ ] Tenant/team/user data boundaries are identified.
- [ ] Training-to-production boundaries are identified.
- [ ] Feedback-to-training boundaries are identified.
- [ ] Model registry to deployment boundary is identified.

## 4. Assumptions

- [ ] System assumptions are documented.
- [ ] Trust assumptions are documented.
- [ ] Data quality assumptions are documented.
- [ ] Model behavior assumptions are documented.
- [ ] Authorization assumptions are documented.
- [ ] Privacy assumptions are documented.
- [ ] Logging assumptions are documented.
- [ ] Monitoring assumptions are documented.
- [ ] Each assumption has been challenged.

## 5. Abuse cases

- [ ] Malicious user abuse cases are included.
- [ ] Compromised account abuse cases are included.
- [ ] Malicious document/content abuse cases are included.
- [ ] Supply chain abuse cases are included.
- [ ] Insider misuse abuse cases are included.
- [ ] Privacy abuse cases are included.
- [ ] Tool misuse abuse cases are included.
- [ ] Feedback or memory poisoning abuse cases are included.

## 6. RAG-specific review

- [ ] Retrieval is authorized before context insertion.
- [ ] Retrieved content is treated as untrusted data.
- [ ] Source metadata is preserved.
- [ ] Tenant and user boundaries are enforced.
- [ ] Vector database access is controlled.
- [ ] Sensitive content is filtered or redacted where needed.
- [ ] Retrieval events are logged.
- [ ] Poisoned document scenarios are considered.

## 7. Agent/tool-specific review

- [ ] Tool list is documented.
- [ ] Tool permissions are scoped.
- [ ] Tool credentials are not shared broadly.
- [ ] Tool arguments are validated.
- [ ] Tool calls are authorized per user and action.
- [ ] High-impact actions require approval.
- [ ] Destructive actions have rollback.
- [ ] Tool calls are logged.
- [ ] Egress is controlled.
- [ ] Code execution, if any, is sandboxed.

## 8. Model/prompt-specific review

- [ ] System prompts are not treated as secrets or hard controls.
- [ ] Prompt construction is deterministic and reviewable.
- [ ] Instruction and data context are separated where possible.
- [ ] Model output is treated as untrusted.
- [ ] Output is encoded before rendering.
- [ ] Model confidence and uncertainty are considered.
- [ ] Failure modes are defined.
- [ ] Fallback behavior is safe.

## 9. MLOps and supply chain

- [ ] Dataset provenance is documented.
- [ ] Model artifact provenance is documented.
- [ ] Model registry access is controlled.
- [ ] Unsafe deserialization is avoided.
- [ ] Dependencies are reviewed.
- [ ] Secrets are not stored in notebooks or prompts.
- [ ] CI/CD permissions are scoped.
- [ ] Deployment rollback exists.
- [ ] Changes to prompts, models, tools, and retrieval are versioned.

## 10. Logging, monitoring, and response

- [ ] Security-relevant events are logged.
- [ ] Sensitive data is redacted from logs.
- [ ] Retrieval events are logged.
- [ ] Tool calls are logged.
- [ ] Denied actions are logged.
- [ ] Prompt injection indicators are monitored.
- [ ] Abnormal tool usage is monitored.
- [ ] Model DoS or high-cost usage is monitored.
- [ ] Incident response playbooks exist.
- [ ] Risk owners are identified.

## 11. Security requirements

- [ ] Requirements are specific.
- [ ] Requirements have owners.
- [ ] Requirements map to risks.
- [ ] Requirements are testable.
- [ ] Requirements distinguish prevention, detection, response, and recovery.
- [ ] Requirements include operational monitoring.
- [ ] Requirements include residual risk.

## 12. Residual risk

- [ ] Residual risk is documented.
- [ ] Risk acceptance owner is identified.
- [ ] Review triggers are defined.
- [ ] Monitoring is defined.
- [ ] Known limitations are stated.
- [ ] Assumptions requiring revalidation are listed.
