# Module 12 Instructor Notes — BrokenPilot Capstone

## Instructor objective

The instructor's job is to keep students focused on system-level security reasoning.

Students will naturally gravitate toward prompt payloads. Redirect them toward:

- assets;
- trust boundaries;
- authorization;
- tool permissions;
- retrieved context;
- memory scope;
- workflow impact;
- evidence;
- remediation;
- residual risk.

## Recommended prerequisites

Students should have completed or reviewed:

- Module 1 — Security Engineering for AI
- Module 5 — LLM Application Security
- Module 6 — RAG Security
- Module 7 — Agent and Tool Security
- Module 8 — Secure MLOps and AI Supply Chain
- Module 9 — Privacy Attacks and Data Protection
- Module 11 — AI Red Team Methodology

For shorter workshops, provide a 20-minute recap of the concepts above.

## Delivery options

### Option A — Short tabletop, 2–3 hours

Use when the audience is leadership, architects, or security champions.

| Phase | Time | Activity |
|---|---:|---|
| Context | 20 min | Introduce BrokenPilot and architecture. |
| Threat model | 40 min | Students identify assets, trust boundaries, and abuse cases. |
| Attack path review | 40 min | Teams analyze two selected attack paths. |
| Mitigation design | 30 min | Teams propose controls and trade-offs. |
| Debrief | 20 min | Instructor compares results to expected findings. |

### Option B — Half-day workshop, 4 hours

Use for AppSec, platform, ML, and product security teams.

| Phase | Time | Activity |
|---|---:|---|
| Context and architecture | 25 min | Introduce scenario, architecture, tools, and roles. |
| Threat modeling | 50 min | Teams fill the threat model template. |
| Red team planning | 35 min | Teams select attack paths and evidence plans. |
| Finding analysis | 45 min | Teams document findings and root causes. |
| Mitigation design | 45 min | Teams design target-state controls. |
| Presentation | 30 min | Teams present top risks. |
| Debrief | 10 min | Instructor closes with common patterns. |

### Option C — Full-day capstone, 6–7 hours

Use for the complete practitioner experience.

| Phase | Time | Activity |
|---|---:|---|
| Briefing | 30 min | Scenario, goals, scope, safety boundaries. |
| Architecture review | 45 min | Data flows, trust boundaries, tool inventory. |
| Threat modeling | 60 min | STRIDE/abuse-case review. |
| Red team planning | 45 min | Attack paths, test cases, evidence plan. |
| Controlled testing/tabletop | 75 min | Teams work through selected attack paths. |
| Mitigation design | 60 min | Secure architecture, policy, monitoring, roadmap. |
| Report prep | 45 min | Findings, risk register, executive summary. |
| Presentations | 45 min | Team readouts. |
| Debrief | 30 min | Instructor solution and lessons learned. |

## Materials to provide

Student-facing:

- `student-handout.md`
- `exercise-capstone-threat-model.md`
- `exercise-capstone-red-team-review.md`
- `../../labs/brokenpilot/student-brief.md`
- `../../labs/brokenpilot/scenario.md`
- `../../labs/brokenpilot/architecture.md`
- `../../labs/brokenpilot/roles.md`
- `../../labs/brokenpilot/tools.md`
- `../../templates/brokenpilot-final-report-template.md`
- `../../templates/brokenpilot-risk-register-template.md`
- `../../templates/brokenpilot-evidence-log-template.md`

Instructor-only:

- `../../labs/brokenpilot/instructor-solution.md`
- `../../labs/brokenpilot/vulnerabilities.md`
- `../../labs/brokenpilot/attack-paths.md`
- `../../labs/brokenpilot/grading-rubric.md`
- `../../assessments/brokenpilot-capstone-final-rubric.md`

## Expected high-quality findings

Students do not need to find every issue. They should find enough representative issues to show system-level reasoning.

Expected strong findings include:

| Area | Expected finding |
|---|---|
| RAG authorization | Retrieved documents are not filtered according to user permissions before context assembly. |
| Indirect prompt injection | Untrusted document content can influence model behavior and tool decisions. |
| Tool authorization | Tool execution trusts model intent instead of enforcing per-action authorization. |
| Excessive agency | The agent can update operational tickets without sufficient approval or confidence gates. |
| Memory poisoning | User-controlled memory persists instructions across unrelated tasks. |
| Sensitive disclosure | Prompt traces, retrieved context, or summaries may expose restricted incident details. |
| Insecure output handling | Model-generated Markdown/HTML may be rendered without safe handling. |
| Auditability | Logs do not sufficiently reconstruct retrieval, authorization, tool calls, approvals, and model decisions. |
| Overreliance | Users may treat model-generated operational recommendations as authoritative. |
| Supply chain | Prompts, embeddings, model artifacts, or tool definitions are not controlled as deployable artifacts. |

## Common student mistakes

### Mistake 1 — Treating prompt injection as the whole finding

Redirect with:

> What security property was violated? Which control should have prevented the outcome?

### Mistake 2 — Recommending only “better prompting”

Redirect with:

> What control outside the model would enforce this even if the model is manipulated?

### Mistake 3 — Ignoring authorization at retrieval time

Redirect with:

> Should the document have entered the context window for this user at all?

### Mistake 4 — Treating the model as the actor

Redirect with:

> The application executed the action. Where should the application have checked policy?

### Mistake 5 — Over-securing the system until it is useless

Redirect with:

> Which controls reduce risk while preserving the productivity goal?

## Discussion prompts

Use these when teams get stuck:

1. What can BrokenPilot see that the current user cannot normally see?
2. What can BrokenPilot do that the current user cannot normally do?
3. What data reaches the model before authorization is checked?
4. What action can happen without human approval?
5. What is stored in memory and who can influence it?
6. Could a document author influence a later user session?
7. What would you need in logs after an incident?
8. Which control would block the attack even if the prompt injection works?
9. Which mitigation creates the most developer friction?
10. Which residual risk should leadership explicitly accept or reject?

## Suggested grading emphasis

| Criterion | Weight |
|---|---:|
| Threat model quality | 20% |
| Finding quality and evidence | 25% |
| Mitigation design | 25% |
| Residual-risk reasoning | 15% |
| Communication quality | 15% |

## Instructor debrief structure

Close with this sequence:

1. BrokenPilot is not unrealistic; it mirrors how internal AI assistants are actually assembled.
2. The model is not the only risk source.
3. RAG changes data exposure and trust assumptions.
4. Agents turn model output into action.
5. Memory creates persistence.
6. Security decisions belong outside the model.
7. The correct target state is not “disable AI.”
8. The correct target state is scoped, observable, least-privilege automation.

## Final instructor message

The point of the capstone is to show that AI security is not a separate universe.

It is security engineering under new conditions:

- probabilistic behavior;
- natural-language interfaces;
- untrusted context;
- model-mediated decisions;
- autonomous or semi-autonomous actions;
- new privacy and monitoring challenges.

Students who understand that are ready to help real teams build safer AI systems.
