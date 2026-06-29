# AI Red Team Grading Rubric

Use this rubric for Module 11 deliverables and BrokenPilot red team reports.

## Scoring summary

| Area | Points |
|---|---:|
| Scope and rules of engagement | 15 |
| System understanding and threat model | 15 |
| Attack-path quality | 15 |
| Evidence quality | 15 |
| Impact and severity analysis | 15 |
| Remediation and residual risk | 15 |
| Communication quality | 10 |
| **Total** | **100** |

## 1. Scope and rules of engagement — 15 points

| Score | Criteria |
|---:|---|
| 0–5 | Scope is vague or unsafe. |
| 6–10 | Scope is mostly clear but lacks safety boundaries or evidence rules. |
| 11–15 | Scope, boundaries, allowed actions, forbidden actions, evidence rules, and stop conditions are clear. |

## 2. System understanding and threat model — 15 points

| Score | Criteria |
|---:|---|
| 0–5 | Little understanding of architecture or trust boundaries. |
| 6–10 | Identifies major components but misses key data/tool/memory flows. |
| 11–15 | Clearly maps assets, trust boundaries, roles, model, RAG, tools, memory, logs, and assumptions. |

## 3. Attack-path quality — 15 points

| Score | Criteria |
|---:|---|
| 0–5 | Isolated prompt tricks with unclear impact. |
| 6–10 | Plausible attacks but incomplete chaining or prerequisites. |
| 11–15 | Realistic attack chains with entry point, failed controls, impact, and safety constraints. |

## 4. Evidence quality — 15 points

| Score | Criteria |
|---:|---|
| 0–5 | Evidence is missing, unsafe, or not reproducible. |
| 6–10 | Some evidence exists but lacks logs, traces, or context. |
| 11–15 | Evidence includes input, retrieved context, model output, tool traces, logs, impact, and reproduction notes. |

## 5. Impact and severity analysis — 15 points

| Score | Criteria |
|---:|---|
| 0–5 | Severity is asserted without rationale. |
| 6–10 | Impact is reasonable but lacks blast radius, privilege, or compensating-control analysis. |
| 11–15 | Severity is clearly justified using asset sensitivity, exposure, privilege, reproducibility, detectability, and business impact. |

## 6. Remediation and residual risk — 15 points

| Score | Criteria |
|---:|---|
| 0–5 | Recommends vague prompt changes only. |
| 6–10 | Provides useful fixes but misses architectural controls or residual risk. |
| 11–15 | Provides quick fixes, architectural fixes, detection improvements, regression tests, and residual-risk statement. |

## 7. Communication quality — 10 points

| Score | Criteria |
|---:|---|
| 0–3 | Report is hard to follow. |
| 4–7 | Report is understandable but not well tailored to audience. |
| 8–10 | Report is clear for developers, architects, and leadership; avoids hype and minimization. |
