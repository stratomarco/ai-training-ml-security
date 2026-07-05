# Course storyline

This course has one through-line: AI security is security engineering for systems that contain models. The model matters, but the model is not the whole system and should not be treated as the only boundary.

The course starts with foundations, then moves through architecture, taxonomy, and design risk. It then turns those foundations into hands-on work across LLM applications, RAG, agents, supply chain, privacy, adversarial robustness, and red team reporting. The capstone asks students to combine these threads into a decision-grade review of BrokenPilot with validation evidence and residual risk.

## The course arc

1. Establish the security engineering lens.
2. Map the AI system as a set of data, authority, artifact, and output flows.
3. Classify risks with OWASP ML and related frameworks without becoming checklist-driven.
4. Use BIML-style architectural risk analysis to find assumptions before implementation.
5. Observe LLM application failures and learn why prompts are not security boundaries.
6. Observe RAG failures and learn why retrieval authorization is part of access control.
7. Observe agent failures and learn why action authorization must live outside the model.
8. Review MLOps evidence and learn why model promotion is a supply-chain decision.
9. Observe privacy leakage and learn to reason about disclosure, inference, reconstruction, and logging.
10. Observe classical ML robustness failures and learn why accuracy is not enough.
11. Convert tests into decision-grade red team evidence.
12. Integrate the course in the BrokenPilot capstone.

## Repeated message

Every module should return to the same question: What can the model influence, and where must the system enforce the boundary?

## What students should stop saying

- The model was tricked, so we need a stronger prompt.
- The answer was wrong, so the model is insecure.
- We found an attack, so the system cannot launch.
- The tool called the API, so the model was authorized.

## What students should start saying

- This text crossed a trust boundary and was treated as instruction.
- This retrieval result bypassed an authorization decision.
- This action needs target-object authorization outside the model.
- This artifact lacks enough provenance and integrity evidence for promotion.
- This finding changes the launch decision because the control is missing or unvalidated.
