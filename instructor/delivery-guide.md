# Delivery Guide

## Teaching stance

Teach AI security as security engineering.

Avoid making the course only about clever prompts. Prompts are useful demonstrations, but the learning objective is architecture and risk judgment.

## Recommended module rhythm

1. Start with a realistic scenario.
2. Draw the architecture.
3. Identify assets and trust boundaries.
4. Explain the vulnerability.
5. Demonstrate the lab.
6. Explain root cause.
7. Discuss mitigations.
8. Discuss trade-offs.
9. Capture residual risk.

## Common student mistakes

- Treating the prompt as the security boundary
- Ignoring IAM and authorization
- Ignoring logs and monitoring
- Ignoring data provenance
- Assuming the model can reliably identify trusted instructions
- Treating all failures as jailbreaks
- Missing supply chain risks
- Missing privacy risks
- Overfocusing on blocking instead of workflow design

## Instructor reminders

Always ask:

- What is the asset?
- Who is the attacker?
- What is the trust boundary?
- What can the model see?
- What can the model do?
- What should happen when the model is uncertain?
- What requires human approval?
- What should be logged?
- What risk remains?
