# DVAIA Guides

This folder maps DVAIA exercises to the course modules.

DVAIA should be used as the initial DVWA-like hands-on environment for LLM application security topics.

## Initial mapping

| Topic | Course module | Notes |
|---|---|---|
| Direct prompt injection | Module 05 | Teach why prompts are not hard security boundaries |
| Indirect prompt injection | Module 06 | Use retrieved or external content as attacker-controlled input |
| RAG abuse | Module 06 | Focus on retrieval authorization and poisoned documents |
| Insecure output handling | Module 05 | Treat model output as untrusted data |
| Agent testing | Module 07 | Connect tool access to authorization and workflow risk |
| Payload generation | Module 11 | Use as part of AI red-team methodology |

## Instructor guidance

Do not teach DVAIA as a bag of tricks. Teach each exercise as:

1. System design weakness
2. Exploit path
3. Root cause
4. Mitigation
5. Residual risk


## Validated local environment

DVAIA has been validated locally as an external lab dependency for this course.

Baseline:

- Validation date: 2026-06-29
- Host OS: Windows / PowerShell
- DVAIA commit: `23c115252554caa445c0e6ba28641c1110c118e1`
- Docker: `Docker version 29.5.3, build d1c06ef`
- Docker Compose: `Docker Compose version v5.1.4`
- Run mode: Local mode
- Backend: Local / Ollama
- URL: `http://127.0.0.1:5000`

See [`validated-lab-results.md`](validated-lab-results.md) for the validation summary.
