# Module 04 Slides  -  BIML and Architectural Risk Analysis

## Slide 1  -  Title

# BIML and Architectural Risk Analysis

Security design review for systems that contain machine learning.

---

## Slide 2  -  Why this module exists

Most AI security discussions start too late.

They start with:

- jailbreak payloads
- prompt injection examples
- red-team screenshots
- model behavior tricks

But many AI security failures are created earlier:

- during architecture
- during data-flow design
- during permission design
- during tool integration
- during deployment planning
- during monitoring design

---

## Slide 3  -  Key message

# Architecture determines which failures become possible.

A model can make a bad prediction.

A prompt can be injected.

A retrieved document can be malicious.

A tool call can be dangerous.

But the architecture decides whether those failures become business impact.

---

## Slide 4  -  From exploit to root cause

Weak analysis:

> The model was jailbroken.

Better analysis:

> Untrusted user input was allowed to override task instructions.

Stronger analysis:

> The system trusted model output as authorization for a privileged workflow action.

Best analysis:

> A missing trust boundary and missing per-action authorization allowed untrusted natural-language input to influence a privileged tool call.

---

## Slide 5  -  What is architectural risk analysis?

Architectural risk analysis is a security review of system design.

It asks:

- What are we building?
- What are the valuable assets?
- Who are the attackers?
- Where are the trust boundaries?
- What assumptions are we making?
- What can go wrong?
- What controls should exist?
- What residual risk remains?

---

## Slide 6  -  Building security in

Gary McGraw-style software security emphasizes that security cannot be bolted on at the end.

The same is true for ML systems.

You cannot fix every AI risk with:

- one prompt
- one classifier
- one guardrail
- one filter
- one moderation API
- one policy statement

Security must be built into architecture, workflow, permissions, and operations.

---

## Slide 7  -  Why BIML fits this course

BIML is useful because it treats ML security as security engineering.

It emphasizes:

- architectural risk
- ML process models
- component-level risks
- system-wide risks
- design-time analysis
- building security in

This is exactly the mindset we want.

---

## Slide 8  -  BIML-78

BIML-78 is a set of 78 risks associated with a generic ML process model.

The important lesson is not memorizing all 78.

The important lesson is using the process model to ask better questions:

- Where can data be manipulated?
- Where can labels be corrupted?
- Where can model artifacts be stolen or tampered with?
- Where can sensitive information leak?
- Where can feedback loops be abused?

---

## Slide 9  -  BIML and LLMs

LLM systems add new components and risks:

- prompts
- system instructions
- retrieval context
- embeddings
- vector databases
- tools
- memory
- agents
- plugin ecosystems
- model gateways
- policy layers
- human approval workflows

The architecture becomes more than model inference.

---

## Slide 10  -  ML architecture risk components

Classical ML components:

```text
data collection -> labeling -> features -> training -> evaluation -> registry -> deployment -> inference -> monitoring -> feedback
```

Each component creates risks.

The job is to ask:

> What can an attacker influence here?

---

## Slide 11  -  LLM architecture risk components

LLM application components:

```text
user -> app -> prompt builder -> model gateway -> output handler
              |                 |
              v                 v
          retrieval          tools/actions
              |                 |
              v                 v
       vector database       business APIs
```

Each arrow may cross a trust boundary.

---

## Slide 12  -  Component risk examples

| Component | Risk |
|---|---|
| Prompt builder | Confuses instruction and data |
| Retrieval service | Returns unauthorized documents |
| Vector DB | Cross-tenant leakage |
| Tool broker | Allows unsafe action |
| Memory service | Stores attacker instructions |
| Output renderer | Renders unsafe HTML or code |
| Feedback loop | Reinforces attacker-controlled behavior |
| Model registry | Serves tampered model artifact |

---

## Slide 13  -  System-wide risks

Some risks do not belong to only one component.

Examples:

- unclear ownership
- weak governance
- missing auditability
- excessive model authority
- weak human oversight
- no incident response plan
- no rollback path
- hidden data dependencies
- unclear privacy boundaries
- overreliance on model output

Architectural review must look across the whole system.

---

## Slide 14  -  Design-level risk vs implementation bug

Implementation bug:

> The API endpoint forgot to validate one parameter.

Design-level risk:

> The system design allows the model to decide whether a privileged API action is authorized.

Implementation bug:

> The markdown renderer allows unsafe HTML.

Design-level risk:

> The system treats model output as trusted presentation content.

---

## Slide 15  -  Risk review question 1: What are the assets?

AI system assets may include:

- source code
- prompts
- system instructions
- user data
- business records
- training data
- labels
- embeddings
- model weights
- model API keys
- tool credentials
- workflow state
- logs
- user trust
- operational decisions

---

## Slide 16  -  Risk review question 2: What are the trust boundaries?

Common AI trust boundaries:

- user input to app
- app to model provider
- model output to application
- retrieved document to prompt
- prompt to tool call
- tool call to business API
- tenant A data to tenant B context
- offline training data to production model
- model registry to deployment environment
- feedback to future training

---

## Slide 17  -  Risk review question 3: What can the model do?

A model that can only answer questions has limited impact.

A model that can use tools can create real-world impact.

Ask:

- Can it read sensitive data?
- Can it write records?
- Can it create tickets?
- Can it send emails?
- Can it execute code?
- Can it access the internet?
- Can it call internal APIs?
- Can it store memory?
- Can it trigger workflows?

---

## Slide 18  -  Risk review question 4: What does the model know?

Ask:

- What user data enters the prompt?
- What documents are retrieved?
- What system messages are exposed?
- What previous conversation is included?
- What secrets or credentials are reachable?
- What logs are stored?
- What training data may be memorized?
- What tenant boundaries exist?

---

## Slide 19  -  Risk review question 5: What assumptions are unsafe?

Unsafe assumptions:

- users will not attack the prompt
- retrieved documents are trustworthy
- model output is safe to render
- model output is safe to execute
- the model understands authorization
- the model can keep secrets reliably
- internal users are always benign
- logs never contain sensitive data
- feedback is always honest
- one guardrail catches everything

---

## Slide 20  -  Abuse cases

A normal use case says:

> A user asks the assistant to summarize an incident.

An abuse case says:

> A user hides instructions in an incident comment so the assistant leaks confidential documents during summarization.

Abuse cases make attacker intent visible.

---

## Slide 21  -  Example abuse cases

For an internal AI operations assistant:

- malicious user injects instructions into a ticket
- compromised document poisons retrieval context
- low-privilege user retrieves high-privilege docs
- model calls update-ticket tool without authorization
- attacker poisons memory for future users
- assistant renders unsafe output in the browser
- model summarizes incorrect recovery steps during incident response

---

## Slide 22  -  Security requirements

Architectural risk analysis should produce requirements.

Examples:

- The model must not make authorization decisions.
- Tool calls must be authorized per action.
- Retrieved documents must be filtered by user identity.
- Model output must be treated as untrusted.
- Destructive actions require human approval.
- Tool credentials must be scoped.
- Sensitive data must be redacted from logs.
- All tool calls must be auditable.

---

## Slide 23  -  Defensive architecture patterns

Useful design patterns:

- policy outside the model
- least-privilege tool broker
- retrieval authorization
- context labeling
- output encoding
- human approval gates
- sandboxed execution
- egress restrictions
- model gateway
- rate limits and budgets
- audit logging
- monitoring for abuse

---

## Slide 24  -  Where controls should live

Do not put all security inside the prompt.

| Control | Better location |
|---|---|
| Authorization | Application / policy engine |
| Tool permission | Tool broker |
| Output encoding | Rendering layer |
| Retrieval access | Retrieval service |
| Secrets handling | Secrets manager |
| Rate limiting | Gateway/API layer |
| Audit logs | Platform layer |
| Approval | Workflow layer |

---

## Slide 25  -  Residual risk

Mitigation does not mean zero risk.

Residual risk should explain:

- what remains possible
- why it is acceptable or not
- what compensating controls exist
- what is monitored
- who owns the risk
- what triggers re-review

AI systems change quickly, so residual risk must be revisited.

---

## Slide 26  -  Practical architecture review workflow

1. System summary
2. Component diagram
3. Asset list
4. Data-flow diagram
5. Trust boundaries
6. Assumption list
7. Abuse cases
8. Risk list
9. Security requirements
10. Mitigation plan
11. Residual risk statement

---

## Slide 27  -  Student exercise

Review the DocOps Assistant architecture.

Find design-level risks before exploit payloads.

You must produce:

- assets
- trust boundaries
- assumptions
- abuse cases
- prioritized risks
- security requirements
- mitigation plan
- residual risk

---

## Slide 28  -  What good looks like

A good review does not say only:

> Prompt injection is possible.

A good review says:

> Indirect prompt injection is possible because untrusted document content is inserted into the model context without source labeling, retrieval authorization, or policy separation. The impact is high because model output can trigger privileged ticket updates through a broadly scoped tool token.

---

## Slide 29  -  Instructor discussion

Ask students:

- Which control must be outside the model?
- Which risk is highest impact?
- Which risk is easiest to fix?
- Which mitigation improves developer velocity?
- Which mitigation adds friction?
- What would you accept for v1?
- What must be fixed before production?

---

## Slide 30  -  Closing

Architectural risk analysis turns AI security from tricks into engineering.

The goal is not to memorize every risk.

The goal is to ask better questions earlier:

- What can go wrong?
- Why would it matter?
- Where should the control live?
- What risk remains?
