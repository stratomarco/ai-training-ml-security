# 40-Hour Course Dry-Run Plan

This plan is for a dry run before release cleanup. The goal is not to teach the course live. The goal is to verify that the week has a coherent flow, realistic timing, and clear deliverables.

## Dry-run method

For each day, walk through the instructor path, the student path, and the expected artifact. Record where a real cohort would need more guidance.

Use three questions repeatedly:

1. What decision is the student learning to make?
2. What evidence do they use to make it?
3. What artifact proves they understood it?

## Day 1: Foundations and architecture

### Modules

- Module 01: Security Engineering for AI
- Module 02: ML System Architecture
- Module 03 overview: OWASP ML categories as finding language

### Dry-run checks

- Can students explain why model behavior is not a security boundary?
- Can students identify trust boundaries in an ML-enabled system?
- Can students convert an OWASP ML category into a concrete finding?
- Does the day end with a useful architecture or risk artifact?

### Expected artifact

A short architecture risk review that identifies assets, trust boundaries, control points, and at least three abuse cases.

### Watch for timing risk

Do not spend too long on taxonomy. Use taxonomy only to improve finding language and control mapping.

## Day 2: LLM, RAG, and output handling

### Modules

- Module 05: LLM Application Security
- Module 06: RAG Security

### Dry-run checks

- Can students observe direct prompt injection in BrokenPilot?
- Can students observe indirect prompt injection or retrieval-driven instruction confusion?
- Can students explain why marker detection is not a production control?
- Can students observe insecure output handling and the effect of output encoding?
- Can students explain retrieval authorization as an application responsibility?

### Expected artifact

A lab journal entry with evidence, root cause, control recommendation, validation, and residual risk.

### Watch for timing risk

Students may focus too much on crafting payloads. Redirect them to the control question: where should the system enforce the boundary?

## Day 3: Agents, tools, memory, and MLOps

### Modules

- Module 07: Agent and Tool Security
- Module 08: Secure MLOps and AI Supply Chain

### Dry-run checks

- Can students observe tool confused-deputy behavior?
- Can students observe tool authorization blocking a cross-tenant update?
- Can students explain why poisoned memory can steer intent even when execution is blocked?
- Can students review the MLOps evidence pack and identify artifact integrity and promotion-gate weaknesses?

### Expected artifact

Either a tool permission matrix or an MLOps evidence-pack review with a launch recommendation.

### Watch for timing risk

The MLOps lab is a reasoning lab. Do not apologize for it not being runnable. The evidence-review artifact is the work.

## Day 4: Privacy, adversarial ML, and red-team method

### Modules

- Module 09: Privacy Attacks and Data Protection
- Module 10: Adversarial ML and Robustness
- Module 11: AI Red Team Methodology

### Dry-run checks

- Can students observe cross-tenant leakage in BrokenPilot?
- Can students explain what retrieval authorization fixes and what it does not fix?
- Can students run toy-classifier attacks and explain why the classifier should not be a hard authorization gate?
- Can students write a scoped red-team objective that is not just a list of tricks?

### Expected artifact

A rewritten strong finding or scoped red-team plan with evidence, validation, and residual risk.

### Watch for timing risk

Toy-classifier outputs should be used to teach robustness decisions, not to turn the course into an ML statistics class.

## Day 5: BrokenPilot capstone

### Modules

- Module 12: BrokenPilot Capstone

### Dry-run checks

- Does the capstone use the current evidence path?
- Can students connect multiple findings into an attack chain?
- Does the report include executive recommendation, remediation backlog, validation plan, and residual risk?
- Is the capstone graded on the quality of fix and reasoning, not number of payloads?

### Expected artifact

A final report and short presentation.

### Watch for timing risk

Students will want to keep testing. Force a transition from testing to decision: what should leadership do now?

## Dry-run output

At the end of the dry run, produce:

1. a list of timing changes
2. a list of unclear instructions
3. a list of labs that need better reset or troubleshooting notes
4. a list of pages that can be removed or moved to optional self-study
5. a decision on whether the course is ready for cleanup
