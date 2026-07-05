# Module 02 Slides  -  ML System Architecture

These slides are written in Markdown so they can be used directly in GitHub, converted with tools such as Marp, or copied into a presentation later.

---

# 1. ML System Architecture

## Core idea

Before we can secure ML systems, we need to understand how they are built.

ML security is not only about attacking the model.

**Speaker notes:**
Open by connecting back to Module 01. We established that AI security starts with security engineering. Now we look at the system architecture that creates, serves, and changes model behavior.

---

# 2. The central claim

> In ML systems, data, models, prompts, and feedback loops become part of the attack surface.

**Speaker notes:**
This is the module’s equivalent of “the model is not the security boundary.” The model is important, but it is only one component in a lifecycle.

---

# 3. Traditional application architecture

A simplified application may include:

- User interface
- API layer
- Authentication
- Authorization
- Business logic
- Database
- Logs
- Background jobs
- Third-party services

**Speaker notes:**
Students already know this world. AppSec has mature ways to reason about these components: DFDs, STRIDE, abuse cases, code review, API testing, logging, and IAM review.

---

# 4. ML adds a lifecycle

An ML system also includes:

- Data collection
- Labeling
- Data cleaning
- Feature engineering
- Training
- Evaluation
- Model registry
- Deployment
- Inference
- Monitoring
- Feedback and retraining

**Speaker notes:**
The security problem expands from the running application into the full lifecycle that created and maintains model behavior.

---

# 5. Why lifecycle matters

A model can be compromised without changing application code.

Examples:

- Poisoned training data
- Manipulated labels
- Backdoored model artifact
- Unsafe dependency in training pipeline
- Benchmark leakage
- Compromised vector index
- Abusive feedback loop

**Speaker notes:**
This is the mindset shift. Source code is not the only place where behavior lives.

---

# 6. Data is a security asset

Data affects:

- What the model learns
- What the model predicts
- What the model reveals
- Which groups are affected
- Which errors become likely
- Which attacks become possible

**Speaker notes:**
In ML security, data governance is security. Data lineage, provenance, access control, retention, and quality are security-relevant controls.

---

# 7. Data collection risks

Questions to ask:

- Where does the data come from?
- Is it trusted?
- Who can submit it?
- Can attackers influence it?
- Does it contain sensitive information?
- Is consent or retention defined?
- Is provenance tracked?

**Speaker notes:**
Data collection is often treated as a business or data science problem. In ML systems, it is also an attack surface.

---

# 8. Labeling risks

Labels can be created by:

- Employees
- Contractors
- Vendors
- Crowdsourcing platforms
- Automated systems
- User feedback

Labeling failures include:

- Malicious labeling
- Low-quality labels
- Biased labels
- Unreviewed automation
- Insider manipulation

**Speaker notes:**
A label is often treated as ground truth. But if labels are manipulated, the model learns manipulated reality.

---

# 9. Feature engineering risks

Features can leak sensitive information or encode fragile assumptions.

Examples:

- Hidden proxy for protected data
- Feature computed from future data
- Feature vulnerable to manipulation
- Feature transformation not reproduced in production
- Feature extraction dependency compromise

**Speaker notes:**
For classical ML systems, feature engineering is often where the security and privacy story becomes subtle.

---

# 10. Training pipeline risks

Training pipelines include:

- Code
- Notebooks
- Dependencies
- Containers
- Secrets
- Compute resources
- Data access
- Experiment tracking
- Artifact generation

**Speaker notes:**
This is DevSecOps plus data science. A compromised notebook or dependency can alter the model, leak data, or steal credentials.

---

# 11. Model artifact risks

A model artifact can be:

- Stolen
- Tampered with
- Replaced
- Backdoored
- Loaded unsafely
- Deployed without review
- Used outside its intended context

**Speaker notes:**
Treat model artifacts like deployable software artifacts. They need integrity, provenance, access control, and safe loading.

---

# 12. Evaluation risks

Evaluation can fail when:

- Test data leaks into training
- Benchmarks do not reflect adversarial use
- Metrics hide minority failure modes
- Robustness is not tested
- Privacy leakage is not tested
- Humans overtrust model scores

**Speaker notes:**
A model can have strong average performance and still be insecure under adversarial use.

---

# 13. Inference risks

At inference time, attackers may:

- Send adversarial inputs
- Probe model boundaries
- Extract model behavior
- Cause high-cost requests
- Trigger unsafe outputs
- Abuse authenticated access
- Infer sensitive training data

**Speaker notes:**
Inference APIs are public or semi-public attack surfaces. Rate limits, monitoring, output handling, and abuse detection matter.

---

# 14. Monitoring risks

Monitoring should cover:

- Performance drift
- Data drift
- Abuse patterns
- Model extraction attempts
- Privacy leakage
- Unexpected outputs
- Tool-call failures
- High-cost usage
- Feedback manipulation

**Speaker notes:**
ML monitoring is not only about accuracy. It must include security and abuse signals.

---

# 15. Feedback loops

Feedback can improve a system.

Feedback can also poison a system.

Questions:

- What feedback is collected?
- Who can provide it?
- Is it trusted automatically?
- Does it affect future training?
- Is there review before promotion?
- Can attackers create many feedback events?

**Speaker notes:**
Feedback loops are where small abuses can become persistent behavior changes.

---

# 16. LLM systems extend the lifecycle

LLM applications add:

- System prompts
- Prompt templates
- Retrieved context
- Vector databases
- Embeddings
- Tool calls
- Agent memory
- Conversation logs
- Model provider APIs

**Speaker notes:**
For many organizations, they are not training foundation models. But they are still building AI systems through prompts, retrieval, tools, memory, and provider integrations.

---

# 17. RAG architecture

A RAG system usually includes:

- Document ingestion
- Chunking
- Embedding generation
- Vector database
- Retrieval service
- Prompt construction
- LLM completion
- Source rendering

**Speaker notes:**
Every step is security relevant. RAG is not just “search plus LLM.” It is a data access and authorization problem.

---

# 18. RAG trust boundaries

Retrieved content may be:

- Internal but untrusted
- External and attacker-controlled
- Stale
- Unauthorized for the user
- Cross-tenant
- Prompt-injection-bearing
- Sensitive
- Misleading

**Speaker notes:**
The model sees retrieved content as text. The system must preserve authorization, provenance, and instruction/data separation outside the model.

---

# 19. Agent architecture

An agent may include:

- Planner
- LLM
- Tool registry
- Tool executor
- Memory
- Task queue
- Approval workflow
- Audit log
- External APIs

**Speaker notes:**
An agent architecture should immediately trigger authorization thinking. What can the model cause the system to do?

---

# 20. Tool-use trust boundary

Tool calls need deterministic controls:

- Tool allowlist
- Schema validation
- User authorization
- Argument validation
- Risk classification
- Human approval
- Rate limits
- Audit logs

**Speaker notes:**
The model may propose a tool call. The system must decide whether that call is allowed.

---

# 21. Architecture-level attack paths

Examples:

- Attacker poisons user feedback used for retraining
- Insider modifies labels to alter model behavior
- User extracts a model through repeated API queries
- Malicious document changes RAG output
- Compromised model artifact is deployed
- Agent uses broad service account to perform unauthorized action

**Speaker notes:**
These are architecture problems. Individual payloads matter later, but the root cause is often the system design.

---

# 22. Security controls by lifecycle stage

| Stage | Example controls |
|---|---|
| Data collection | provenance, validation, consent, access control |
| Labeling | quality review, separation of duties, vendor controls |
| Training | CI/CD controls, secrets management, dependency scanning |
| Model registry | signing, access control, approval workflow |
| Deployment | rollback, environment separation, change management |
| Inference | authz, rate limits, monitoring, output validation |
| Feedback | review gates, abuse detection, provenance |

**Speaker notes:**
This slide helps students see that there is no single ML security control. Controls are distributed across the lifecycle.

---

# 23. What to diagram

When threat modeling ML systems, diagram:

- Users and roles
- Data sources
- Data stores
- Training pipeline
- Model artifact flow
- Evaluation gates
- Serving path
- Model outputs
- Logs
- Feedback loops
- Tools and external APIs

**Speaker notes:**
A diagram that only shows “user -> model -> response” is almost always insufficient.

---

# 24. Key questions for architecture review

Ask:

1. What behavior depends on data?
2. Who can influence that data?
3. Who can modify the model artifact?
4. How is deployment approved?
5. What does the model see at inference time?
6. Can users repeatedly probe the model?
7. Can outputs affect future training?
8. Can the system explain and roll back decisions?

**Speaker notes:**
These questions prepare students for the exercise.

---

# 25. Exercise: LoanAssist ML

Students review a fictional ML-enabled loan triage system.

Tasks:

- Draw the lifecycle DFD
- Identify assets
- Mark trust boundaries
- Find attack paths
- Map controls to lifecycle stages
- Write residual risk

**Speaker notes:**
Emphasize that the exercise is not about whether the loan model is fair or accurate in an abstract sense. The goal is to identify security-relevant architecture risks.

---

# 26. What good looks like

A good ML architecture has:

- Clear data provenance
- Controlled write paths
- Reviewed labels
- Reproducible training
- Signed model artifacts
- Secure model registry
- Evaluation gates
- Scoped inference APIs
- Abuse monitoring
- Controlled feedback loops
- Rollback and incident response

**Speaker notes:**
This is the transition from attack surface to design pattern.

---

# 27. Main takeaway

ML security is lifecycle security.

To secure an ML system, protect:

- The data
- The pipeline
- The model
- The serving path
- The outputs
- The feedback loop
- The humans relying on it

**Speaker notes:**
Close by connecting to Module 03: once students understand the architecture, OWASP ML Top 10 risks become easier to place.
