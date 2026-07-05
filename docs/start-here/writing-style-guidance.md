# Writing style guidance

The course should read like professional security engineering material: clear, specific, and evidence-driven.

Prefer direct sentences. Avoid decorative punctuation and overly polished marketing language. Em dashes are a style preference, not a release blocker. When writing new prose, prefer commas, colons, semicolons, or shorter sentences if they make the material clearer.

The quality bar is not punctuation. The quality bar is whether a student can explain the issue, reproduce the evidence, identify the violated security property, propose an implementable control, validate the remediation, and communicate residual risk.

Use this checklist when adding or editing study material:

- Does the text explain why the issue matters, not only what happens?
- Does it connect the issue to a security principle or trust boundary?
- Does it separate weak controls from strong controls?
- Does it describe what an engineer should change?
- Does it describe how the fix should be validated?
- Does it avoid presenting toy filters or prompt wording as production controls?

Use this checklist when adding or editing labs:

- Can the student run it from a clean checkout?
- Is the vulnerable behavior deterministic enough for a classroom?
- Is the controlled behavior clear and testable?
- Are success criteria explicit?
- Does the lab teach root cause, not just payloads?
- Does the lab require evidence, remediation, and residual-risk discussion?
