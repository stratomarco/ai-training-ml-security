# Module Template

Use this template for every module in the course.

Each module should teach one security idea deeply, connect it to classic security engineering, then show what changes when ML, LLMs, RAG, or agents are involved.

## Status

Draft / Ready for review / Ready to teach

## Purpose

Explain why this module exists and what problem it solves.

Good module purpose statements should answer:

- What security problem are we teaching?
- Why does this matter in real systems?
- What will students be able to do after this module?

## Core message

Write one sentence students should remember.

Example:

> Retrieved content is untrusted input.

## Learning objectives

By the end of this module, students should be able to:

1. Explain the security problem.
2. Identify relevant assets and trust boundaries.
3. Describe the AI/ML-specific failure mode.
4. Demonstrate or analyze the issue in a lab.
5. Propose practical mitigations.
6. Discuss trade-offs and residual risk.

## Audience

Specify primary and secondary audiences.

## Required background

List what students should already know.

## Recommended duration

| Format | Duration | Notes |
|---|---:|---|
| Awareness session | 60 minutes | Lecture/discussion |
| Practitioner session | 90 minutes | Includes exercise |
| Workshop | 2–3 hours | Includes group work |

## Module files

Each module should eventually contain:

| File | Purpose |
|---|---|
| `README.md` | Main module overview |
| `slides.md` | Markdown slide deck |
| `instructor-notes.md` | Facilitation guidance |
| `student-handout.md` | Student-facing summary |
| `exercise-*.md` | Exercise or lab instructions |
| `checklist.md` | Practical review checklist |
| `quiz.md` | Review questions and answer key |
| `references.md` | Module-specific references |

## Core concepts

List the concepts that must be taught.

- Concept one
- Concept two
- Concept three

## Security engineering connection

Explain how this topic maps back to classic security engineering.

Potential principles:

- Least privilege
- Complete mediation
- Fail-safe defaults
- Defense in depth
- Separation of duty
- Economy of mechanism
- Open design
- Secure defaults
- Input validation
- Output encoding
- Auditability
- Supply chain integrity
- Privacy by design
- Resilience and recovery

## AI-specific risk

Explain what changes when the system includes machine learning, LLMs, RAG, agents, tools, memory, or model-driven behavior.

Use this structure:

```text
In normal software, the risk looks like [...].
In AI-enabled systems, the risk changes because [...].
The security consequence is [...].
```

## Reference architecture

Include a simple diagram.

```text
user / attacker
  |
  v
application
  |
  +-- identity layer
  +-- model gateway
  +-- retrieval service
  +-- tool service
  +-- data store
  +-- logs and monitoring
```

## Threat model prompts

Ask students:

1. What are the assets?
2. Who are the users?
3. Who are the attackers?
4. What are the trust boundaries?
5. What data is trusted?
6. What data is untrusted?
7. What can the model access?
8. What can the model do?
9. What happens when the model is wrong?
10. What needs human approval?
11. What should be logged?
12. What residual risk remains?

## Lab or exercise

### Goal

Describe what the lab teaches.

### Scenario

Describe the application or system.

### Student task

Students must:

1. Understand the system.
2. Identify the vulnerable behavior or design flaw.
3. Explain the root cause.
4. Propose a mitigation.
5. Discuss residual risk.

### Safety boundary

Labs must be performed only in intentionally vulnerable local or approved training environments. Do not instruct students to test real systems without authorization.

## Mitigations

List practical mitigations.

Prioritize controls that are:

- Enforced outside the model
- Testable
- Auditable
- Fail-closed
- Reasonable for developer velocity

## Discussion questions

1. What would you fix first?
2. What would you monitor?
3. What would you block?
4. What would you allow with approval?
5. What would you accept as residual risk?
6. How would you explain this to leadership?

## Deliverable

Describe what students must submit.

Examples:

- Threat model
- Abuse cases
- Lab report
- Red team report
- Architecture review
- Risk register
- Residual risk statement

## Instructor notes

Include:

- Timing
- Teaching tips
- Common mistakes
- Expected answers
- How to steer discussion
- How to evaluate submissions

## Quiz

Include:

- Multiple-choice questions
- Short-answer questions
- Answer key

## References

Use official and primary sources where possible.

Examples:

- OWASP
- BIML
- NIST
- MITRE ATLAS
- Classic security engineering books and papers
