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
