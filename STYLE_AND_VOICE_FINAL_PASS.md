# Final Voice and Prose Cleanup Guide

This guide is for the final manual polish pass before v1.1 is tagged.

The goal is not to make the course sound casual. The goal is to make it sound like a senior security engineer teaching a practical professional course.

## Keep

- Direct explanations of security properties.
- Concrete evidence, controls, validation, and residual risk.
- Plain language about weak controls and tradeoffs.
- The distinction between runnable attack labs and reasoning review labs.
- The central rule: the model may propose, but the system must enforce.

## Reduce

- Repeated phrases such as "this package adds", "this pass creates", and "checked twice" in student-facing content.
- Long enumerations where a short paragraph would be clearer.
- Overly symmetrical sections that make every module sound machine-generated.
- Claims that something is complete, robust, or production-ready without evidence.
- Release-build notes in student-facing module and lab folders.

## Rewrite patterns

Instead of:

> This module provides a comprehensive overview of controls, risks, and remediation strategies.

Use:

> In this module, students decide where the control must live and how they would validate that it works.

Instead of:

> The lab demonstrates the vulnerability and the mitigation.

Use:

> Run the vulnerable path first, then enable the control and show which security property changed.

Instead of:

> Students should understand the importance of X.

Use:

> By the end, students should be able to decide whether X is enforceable, measurable, and safe enough for release.

## Manual pass order

1. README files in the root, modules, and labs.
2. Student reading guides.
3. Lab guides.
4. Worked examples and rubrics.
5. Instructor-only material.

Do not rewrite code comments or test names unless they are confusing.
