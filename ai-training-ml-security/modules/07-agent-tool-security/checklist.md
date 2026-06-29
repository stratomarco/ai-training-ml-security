# Agent and Tool Security Checklist

Use this checklist when reviewing an LLM agent, tool-using assistant, workflow agent, or autonomous AI system.

## 1. Agent purpose and scope

- [ ] The agent has a clearly defined purpose.
- [ ] The agent has documented non-goals.
- [ ] The agent's allowed actions are explicitly listed.
- [ ] The agent's prohibited actions are explicitly listed.
- [ ] There is a documented owner for the agent.
- [ ] The agent has a support and incident-response contact.

## 2. Identity and authorization

- [ ] The agent has a distinct identity.
- [ ] The user identity is preserved through tool calls where appropriate.
- [ ] Shared broad service accounts are avoided.
- [ ] Credentials are short-lived where possible.
- [ ] Tool access is scoped by task and role.
- [ ] Object-level authorization is enforced.
- [ ] Authorization happens at tool execution time.
- [ ] Authorization is enforced outside the model.

## 3. Tool design

- [ ] Tools are narrow and purpose-specific.
- [ ] Broad tools such as shell, raw SQL, arbitrary HTTP, and arbitrary email are avoided or heavily sandboxed.
- [ ] Tool schemas are strict.
- [ ] Tool arguments are validated.
- [ ] Tool targets are allowlisted or policy-checked.
- [ ] Read and write tools are separated.
- [ ] Destructive actions have rollback paths.
- [ ] Tool results are treated as untrusted input.

## 4. Approval gates

- [ ] Sensitive actions require human approval.
- [ ] Destructive actions require approval.
- [ ] Externally visible actions require approval or strict allowlisting.
- [ ] Expensive actions have budget controls.
- [ ] Approval prompts show exact action, target, arguments, evidence, and risk tier.
- [ ] The model cannot bypass approval by rephrasing the action.
- [ ] Approval decisions are logged.

## 5. Memory and context

- [ ] Memory has a clear purpose.
- [ ] Memory writes are controlled.
- [ ] Memory items include provenance.
- [ ] Memory items include owner and scope.
- [ ] Memory items have expiry where appropriate.
- [ ] Users/admins can inspect and delete memory.
- [ ] Retrieved documents cannot silently create durable memory.
- [ ] Memory is separated by tenant, user, team, or project as required.

## 6. Retrieval and indirect input

- [ ] Retrieved content is labeled as untrusted data.
- [ ] Retrieved instructions are not automatically treated as commands.
- [ ] Tool calls cannot be triggered solely by untrusted retrieved content.
- [ ] Source trust and provenance are visible.
- [ ] Cross-tenant retrieval is prevented.
- [ ] Sensitive retrieved content is filtered by authorization.

## 7. Sandboxing and execution

- [ ] Code execution tools are sandboxed.
- [ ] Shell-like tools are avoided or replaced with allowlisted diagnostics.
- [ ] Filesystem access is restricted.
- [ ] Network egress is restricted.
- [ ] Secrets are not available inside execution sandboxes.
- [ ] Execution has time, CPU, memory, and cost limits.
- [ ] Sandboxes are reset between runs.

## 8. Logging and audit

- [ ] User requests are traceable.
- [ ] Tool calls are logged.
- [ ] Tool arguments are logged safely.
- [ ] Policy decisions are logged.
- [ ] Approval decisions are logged.
- [ ] Tool results are logged or summarized safely.
- [ ] Correlation IDs connect conversation, retrieval, tool calls, and approvals.
- [ ] Logs avoid unnecessary sensitive data.

## 9. Monitoring and detection

- [ ] Unusual tool sequences are monitored.
- [ ] Repeated denied actions are monitored.
- [ ] Unexpected recipients or targets are monitored.
- [ ] High-volume retrieval is monitored.
- [ ] Memory write spikes are monitored.
- [ ] Cost and token spikes are monitored.
- [ ] Looping or runaway execution is detected.
- [ ] Security events are routed to the right team.

## 10. Incident response

- [ ] There is a kill switch for the agent.
- [ ] Individual tools can be disabled.
- [ ] Agent credentials can be revoked quickly.
- [ ] Memory writes can be frozen.
- [ ] Scheduled actions can be stopped.
- [ ] Agent-created changes can be identified.
- [ ] Rollback is possible for high-impact actions.
- [ ] Forensic logs are preserved.

## 11. Human factors

- [ ] The agent shows uncertainty when relevant.
- [ ] The agent provides evidence for recommended actions.
- [ ] Approval screens are clear and not manipulative.
- [ ] Operators are trained not to blindly trust agent recommendations.
- [ ] High-risk actions show diffs or previews.

## 12. Residual risk

- [ ] Remaining risks are documented.
- [ ] Risk acceptance has an owner.
- [ ] Monitoring is linked to residual risk.
- [ ] The design is reviewed after incidents, major model changes, new tools, and new data sources.
