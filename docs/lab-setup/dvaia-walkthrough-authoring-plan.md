# Next Step: Turn Validated DVAIA Labs into Guided Walkthroughs

DVAIA is now locally validated as an external lab dependency. The next course-quality task is to convert that validation into precise student/instructor lab guides.

## Goal

Move each DVAIA-backed lab from "validated environment" to "repeatable teaching exercise."

## Work order

1. Module 05 — Direct Prompt Injection guided walkthrough
2. Module 06 — Indirect Prompt Injection / RAG guided walkthrough
3. Module 07 — Agent and Tool Misuse walkthrough where supported
4. Module 11 — DVAIA attack-chain exercise

## Required structure for each walkthrough

Each validated lab walkthrough should include:

- Lab goal
- Course module mapping
- OWASP / BIML / NIST / MITRE mapping where relevant
- DVAIA commit tested
- Setup command
- Initial state
- Student task
- Expected observation
- Evidence to collect
- Root cause explanation
- Mitigation discussion
- Concrete control exercise
- Cleanup/reset step
- Instructor notes

## Do not overclaim

Only document exact behavior observed in the validated DVAIA environment. If a concept is taught as a tabletop extension rather than directly reproduced in DVAIA, label it as a tabletop extension.

## Next milestone after DVAIA walkthroughs

After the DVAIA walkthroughs are repeatable, the next major priority is the BrokenPilot minimal runnable prototype.
