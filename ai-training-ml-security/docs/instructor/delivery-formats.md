# Delivery Formats

This guide helps instructors adapt the course to different teaching windows. The full course is modular, but every module cannot be delivered in every format.

## Format overview

| Format | Goal | What to emphasize |
|---|---|---|
| 2-hour lunch-and-learn | Awareness and executive/developer framing | Core ideas, examples, one mini exercise |
| Half-day workshop | Practical introduction | Modules 1, 5, 6, 7 highlights + one lab/tabletop |
| 1-day workshop | Practitioner overview | Security foundations, LLM/RAG/agent risks, DVAIA lab, mini readout |
| 2-day intensive | Hands-on practitioner training | Modules 1–8 highlights, validated labs, BrokenPilot tabletop |
| 12-week course | Full curriculum | All modules, labs, capstone, assessments |

## 2-hour lunch-and-learn

### Keep

- Course thesis: the model is not the security boundary
- One AI architecture diagram
- Prompt injection as an architectural problem
- RAG trust boundary example
- Agent tool abuse example
- One executive risk discussion

### Cut

- Detailed OWASP taxonomy walkthrough
- Full quizzes
- Most templates
- Deep MLOps material
- Full capstone

### Suggested agenda

| Time | Activity |
|---:|---|
| 0–10 min | Why ML Security is security engineering |
| 10–30 min | LLM/RAG/agent architecture overview |
| 30–55 min | Three failure modes: prompt injection, RAG leakage, tool misuse |
| 55–75 min | Mini tabletop: vulnerable assistant |
| 75–100 min | Mitigation patterns |
| 100–120 min | Leadership discussion and Q&A |

## Half-day workshop

### Keep

- Modules 1, 5, 6, 7
- One DVAIA demonstration if validated
- One threat modeling exercise
- One mitigation design exercise

### Cut

- Module 3 details
- Module 8 details
- Module 9/10 details unless audience is ML-heavy
- Full BrokenPilot capstone

### Suggested agenda

| Time | Activity |
|---:|---|
| 0–30 min | Security engineering for AI |
| 30–70 min | LLM app security |
| 70–110 min | RAG security |
| 110–150 min | Agent/tool security |
| 150–200 min | Guided lab or tabletop |
| 200–240 min | Controls and risk memo |

## 1-day workshop

### Keep

- Modules 1, 2, 5, 6, 7, 8, 11
- DVAIA lab if validated
- Mini BrokenPilot attack path
- Executive readout exercise

### Cut or assign as pre-read

- Module 3 details
- Module 9 details
- Module 10 details
- Full capstone grading

## 2-day intensive

### Keep

- Modules 1–8
- Module 11
- BrokenPilot tabletop
- DVAIA validated labs
- Concrete control deliverables

### Add

- Student teams
- Report writing
- Instructor debrief
- Risk register review
- Executive readout

## 12-week course

### Keep

Everything.

### Weekly cadence

| Week | Focus |
|---:|---|
| 1 | Security Engineering for AI |
| 2 | ML System Architecture |
| 3 | OWASP ML Security Top 10 |
| 4 | BIML Architectural Risk Analysis |
| 5 | LLM Application Security |
| 6 | RAG Security |
| 7 | Agent and Tool Security |
| 8 | Secure MLOps and AI Supply Chain |
| 9 | Privacy Attacks |
| 10 | Adversarial ML and Robustness |
| 11 | AI Red Team Methodology |
| 12 | BrokenPilot Capstone |

## Instructor rule of thumb

When time is short, cut taxonomy before cutting architecture. Students remember attack paths and design principles better than category numbers.
