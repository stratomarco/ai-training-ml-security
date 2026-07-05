# Weak Example  -  Executive Risk Memo

## Memo: AI assistant risk

The AI assistant has many risks. Prompt injection, data leakage, and supply chain attacks are possible. OWASP says these are important. We should implement guardrails and monitor the system. The team should be careful with data and make sure the model is secure.

I recommend delaying the launch until all AI risks are fixed.

## Why this is weak

This memo is weak because it does not support a leadership decision.

Problems:

- It does not explain the business value of the assistant.
- It does not distinguish launch blockers from lower-priority improvements.
- It uses broad phrases like “guardrails” without defining concrete controls.
- It references OWASP without explaining the actual risk to this system.
- It recommends delaying until “all AI risks are fixed,” which is not realistic.
- It does not define residual risk or pilot conditions.
- It gives leadership no actionable path forward.

## How to improve it

A better memo would say:

- Which risks matter most for this specific deployment.
- Which controls are required before a pilot.
- Which risks can be accepted temporarily.
- What evidence should be collected during the pilot.
- Whether the recommendation is launch, limited pilot, or delay.
