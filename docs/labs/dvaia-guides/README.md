# DVAIA Lab Guides

DVAIA is used as a validated external lab dependency for selected hands-on exercises in this course.

Validation baseline:

- DVAIA commit: `23c115252554caa445c0e6ba28641c1110c118e1`
- Run mode: Local mode
- Backend: Local / Ollama
- URL: `http://127.0.0.1:5000`
- Docker: `Docker version 29.5.3, build d1c06ef`
- Docker Compose: `Docker Compose version v5.1.4`

## Available guides

| Guide | Module | Purpose |
|---|---|---|
| `llm-application-security-lab.md` | Module 05 | Original DVAIA-style LLM application security lab guide |
| `module-05-direct-prompt-injection-walkthrough.md` | Module 05 | Validated direct prompt injection walkthrough |
| `module-06-rag-indirect-prompt-injection-walkthrough.md` | Module 06 | Validated indirect prompt injection / RAG trust-boundary walkthrough |
| `module-07-agent-tool-behavior-walkthrough.md` | Module 07 | Agent/tool behavior walkthrough or hybrid control-design exercise |
| `module-11-dvaia-red-team-mini-assessment.md` | Module 11 | Mini red-team assessment using DVAIA as the local target |
| `validated-lab-results.md` | Modules 05–07, 11 | Local validation summary |
| `dvaia-course-mapping.md` | Multiple | Course mapping to DVAIA-backed exercises |

## Important note

The course does not vendor DVAIA. Students and instructors should use the upstream DVAIA project and run it locally.

The course provides the learning path, lab framing, evidence expectations, mitigation guidance, and assessment structure.
