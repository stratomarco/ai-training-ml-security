# Module 01 Instructor Notes  -  Security Engineering for AI

## Instructor goal

Your job in this module is to prevent two bad outcomes:

1. Students think AI security is only prompt injection and jailbreaks.
2. Students think AI security is completely separate from software security.

The correct framing is:

> AI security is security engineering for systems that contain probabilistic components, model-driven behavior, data-driven behavior, retrieval, tools, and sometimes autonomous workflows.

## Recommended delivery formats

### 60-minute awareness session

| Time | Segment |
|---:|---|
| 0–5 min | Introduce the course philosophy |
| 5–20 min | Explain classic security principles for AI |
| 20–35 min | AI-specific attack surface |
| 35–50 min | Walk through DocAssist threat model as a group |
| 50–60 min | Discussion and wrap-up |

### 90-minute practitioner session

| Time | Segment |
|---:|---|
| 0–10 min | Opening and course philosophy |
| 10–30 min | Security engineering principles |
| 30–45 min | AI-specific architecture and trust boundaries |
| 45–70 min | Group exercise: DocAssist threat model |
| 70–85 min | Group review and mitigations |
| 85–90 min | Wrap-up and next module preview |

### 3-hour workshop

| Time | Segment |
|---:|---|
| 0–20 min | Opening lecture |
| 20–45 min | Security principles applied to AI |
| 45–65 min | AI-specific attack surface |
| 65–75 min | Break |
| 75–120 min | Group exercise |
| 120–150 min | Group presentations |
| 150–170 min | Instructor solution walkthrough |
| 170–180 min | Quiz and wrap-up |

## Key messages to repeat

- The model is not the security boundary.
- Prompts are not authorization.
- Retrieved content is untrusted input.
- Model output is untrusted output.
- Tool use is an authorization and workflow problem.
- Agents require least privilege, approval gates, and auditability.
- AI security should produce engineering decisions, not just interesting screenshots.

## Common student mistakes

### Mistake 1  -  Jumping straight to jailbreaks

Students may immediately propose payloads such as “ignore previous instructions.” Redirect them:

- What asset is at risk?
- Which trust boundary is crossed?
- Why did the system allow the model to see or do this?
- Which deterministic control would prevent impact?

### Mistake 2  -  Treating the model as the policy engine

Students may suggest “make the prompt stricter.” Acknowledge that prompt hardening helps, then ask:

- What if the prompt fails?
- Where is authorization enforced?
- What prevents unauthorized retrieval?
- What prevents unauthorized tool execution?

### Mistake 3  -  Ignoring logs and operations

Students often focus on prevention only. Ask:

- How would we detect abuse?
- What should be logged?
- Who reviews suspicious behavior?
- How do we recover after data exposure?

### Mistake 4  -  Overcorrecting with unusable controls

Some students will suggest blocking all useful AI behavior. Ask:

- What is the business use case?
- Which operations are low risk?
- Which operations need approval?
- How can we keep developer velocity while reducing high-impact risk?

## Expected exercise outcomes

A good student answer for DocAssist should include:

### Assets

- Internal documents
- Confidential project information
- Customer or employee data inside documents
- User identity and session context
- Chat history
- Prompt and response logs
- Embeddings and vector index
- Access tokens used by the app

### Actors

- Normal employee
- Employee with limited document access
- Privileged employee
- External attacker with compromised account
- Malicious insider
- Admin/operator
- Model provider or infrastructure dependency

### Trust boundaries

- Browser to application
- Application to identity provider
- Application to document store
- Application to vector database
- Application to model provider or model gateway
- Model output to browser
- Logs to monitoring or analytics systems

### Abuse cases

- User asks the assistant to reveal documents they cannot access.
- User injects instructions to override system behavior.
- Malicious document influences answers through indirect prompt injection.
- Assistant summarizes confidential content into logs.
- Assistant reveals hidden prompt or retrieved context.
- Cross-tenant or cross-department documents are retrieved.
- Model output is rendered unsafely in the browser.
- Logs contain sensitive prompts and are broadly accessible.

### Mitigations

- Enforce authorization before retrieval.
- Filter retrieval results by user permissions.
- Treat retrieved content as untrusted data.
- Keep policy enforcement outside the model.
- Validate and encode model output before rendering.
- Redact sensitive data in logs where appropriate.
- Use scoped service accounts.
- Add monitoring for unusual access patterns.
- Use rate limits and cost controls.
- Define retention rules for prompts, responses, and retrieved context.

## Instructor solution framing

When reviewing the exercise, group findings into four categories:

1. **Prevent**  -  authorization, scoping, policy, validation.
2. **Limit blast radius**  -  least privilege, segmentation, scoped tokens, tenant isolation.
3. **Detect**  -  logs, anomaly detection, audit trails, alerting.
4. **Recover**  -  incident response, rollback, deletion, key rotation, user notification.

This helps students see that security is more than blocking one attack.

## Discussion prompts

Use these if the room is quiet:

1. Should the assistant use the user’s permissions or a broad service account?
2. Should prompts and responses be logged? If yes, who can read them?
3. Is the vector database an authorization boundary?
4. What is the difference between “the model refused” and “the system prevented”?
5. Which actions require human approval?
6. What would you ship in v1 if the product team wants this live in four weeks?

## Grading guidance

Strong submissions:

- Identify concrete assets and trust boundaries.
- Explain root cause, not just symptoms.
- Separate model behavior from system enforcement.
- Include operational controls and residual risk.
- Discuss trade-offs honestly.

Weak submissions:

- Only list prompt injection payloads.
- Assume a stricter prompt solves the problem.
- Ignore data authorization.
- Ignore logging and monitoring.
- Recommend controls that make the system unusable.

## Transition to Module 2

End by saying:

> Now that we have the security engineering lens, we need to understand how ML systems are built: data collection, training, evaluation, deployment, inference, monitoring, and feedback. That lifecycle creates attack surfaces that do not exist in normal web applications.
