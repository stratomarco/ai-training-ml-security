# AI Training — ML Security

**Security engineering for systems that contain machine learning.**

This repository contains a GitHub-ready curriculum for practical ML, LLM, RAG, and agent security training. The goal is not to reinvent software security. The goal is to apply strong security engineering foundations to systems where models, datasets, prompts, retrieval pipelines, tools, and autonomous workflows become part of the attack surface.

This training is designed for security engineers, AppSec teams, ML engineers, platform engineers, architects, security champions, red teams, and engineering leaders.

## Core idea

ML Security is not separate from software security. It is software security, data security, cloud security, identity security, privacy engineering, supply chain security, and adversarial ML applied to systems that contain machine learning.

AI systems fail through:

- Normal software flaws
- Normal infrastructure flaws
- Normal identity and access-control flaws
- Normal cryptographic mistakes
- Normal supply chain compromises
- New ML-specific failure modes
- New LLM, RAG, and agent-specific failure modes

The course therefore teaches students to reason about the whole system: code, model, data, users, tools, permissions, business workflows, logs, monitoring, and residual risk.

## What this course is not

This is not only prompt injection training.

This is not generic AI safety.

This is not a collection of jailbreak screenshots.

This is not a replacement for secure software engineering.

## What this course is

This is practical security engineering for AI-enabled systems.

Students learn how to:

- Threat model AI systems
- Understand ML, LLM, RAG, and agent attack surfaces
- Use OWASP, BIML, NIST, MITRE ATLAS, and classic security literature
- Perform hands-on labs using existing vulnerable environments such as DVAIA
- Design mitigations that balance security, usability, and developer velocity
- Produce useful engineering deliverables: threat models, risk registers, red-team reports, secure architecture reviews, and residual-risk statements

## Repository structure

```text
ai-training-ml-security/
├── README.md
├── syllabus.md
├── course-map.md
├── references.md
├── modules/
│   ├── 01-security-engineering-for-ai/
│   ├── 02-ml-system-architecture/
│   ├── 03-owasp-ml-top-10/
│   ├── 04-biml-architectural-risk-analysis/
│   ├── 05-llm-application-security/
│   ├── 06-rag-security/
│   ├── 07-agent-tool-security/
│   ├── 08-secure-mlops-supply-chain/
│   ├── 09-privacy-attacks/
│   ├── 10-adversarial-ml-robustness/
│   ├── 11-ai-red-team-methodology/
│   └── 12-capstone-brokenpilot/
├── labs/
│   ├── dvaia-guides/
│   ├── rag-labs/
│   ├── agent-labs/
│   ├── toy-ml-attacks/
│   └── brokenpilot/
├── templates/
├── instructor/
└── assessments/
```

## Recommended first build order

1. Finalize the syllabus.
2. Complete Module 1 as the reference module.
3. Build the reusable module template.
4. Map DVAIA labs to OWASP and course modules.
5. Design the BrokenPilot capstone.
6. Expand one module at a time.

## Lab philosophy

Existing vulnerable projects should be used where possible. The course value is in the structure, explanations, lab guides, architecture discussions, mitigation design, and assessment material.

DVAIA and similar projects can provide the hands-on substrate. This curriculum provides the learning path.

## License

Choose a license before publishing. A practical default for training content is Creative Commons Attribution 4.0 for course material and Apache 2.0 or MIT for any code you later add.


## Course status

Current working version: **v0.5 draft**. Module 01, Module 02, Module 03, and Module 04 have complete teaching packages.


## v0.6 update

Module 5 — LLM Application Security is now complete.

Added:

- OWASP LLM/GenAI risk framing
- LLM application architecture slides
- Instructor notes
- Student handout
- LLM application security review exercise
- LLM security checklist
- Quiz and answer key
- DVAIA-style LLM application security lab guide
- LLM application security review template
