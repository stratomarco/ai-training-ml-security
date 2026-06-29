# Security Policy

This repository contains security training material. It is intended for lawful, controlled learning environments.

## Scope

This policy covers:

- Course material
- Lab wrappers
- Templates
- Capstone design
- Future code or lab infrastructure added to this repository

Third-party labs linked from this repository keep their own security policies and licenses.

## Reporting security issues

If this repository becomes public and you find a security issue in original code, lab infrastructure, or documentation that could cause harm, report it privately to the repository owner instead of opening a public issue.

If private reporting is not configured yet, open a minimal public issue saying:

```text
Security issue found. Please provide a private contact path.
```

Do not include exploit details in the public issue.

## Training safety rules

All labs should use:

- Local environments
- Fake data
- Systems owned by the student or instructor
- Clear rules of engagement
- No real customer data
- No third-party targets
- No credential theft
- No persistence outside the lab
- No exfiltration outside the lab

## AI security lab boundaries

The course may discuss prompt injection, RAG poisoning, model extraction, adversarial examples, and agent abuse. These topics are included for defensive education and controlled testing.

Students should not use these techniques against systems they do not own or have explicit permission to test.

## Supported versions

| Version | Status |
|---|---|
| v1.0.0-rc | Active release candidate |
| v0.x | Draft build history |
