# Contributing

This project is an educational ML Security training repository.

## Contribution principles

Contributions should:

- Teach security engineering, not only tricks.
- Prefer official and primary references.
- Connect labs to real engineering decisions.
- Include defensive guidance and residual risk discussion.
- Keep hands-on content limited to intentionally vulnerable, local, or authorized environments.
- Avoid instructions that encourage testing real systems without permission.

## Content structure

New modules should follow [`modules/module-template.md`](modules/module-template.md).

New labs should follow [`course-templates/lab-guide-template.md`](course-templates/lab-guide-template.md).

## Style

Use clear Markdown.

Prefer:

- Short sections
- Tables for mappings
- Practical examples
- Explicit assumptions
- Clear defensive controls

Avoid:

- Hype
- Vendor marketing
- Unattributed claims
- Payload collections without learning context
- Offensive-only material without mitigation

## Review checklist

Before submitting content, check:

- [ ] Does it identify the asset at risk?
- [ ] Does it identify trust boundaries?
- [ ] Does it explain root cause?
- [ ] Does it include mitigation guidance?
- [ ] Does it discuss residual risk?
- [ ] Does it cite useful references?
- [ ] Is the lab clearly limited to authorized environments?
