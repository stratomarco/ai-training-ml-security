# Lab debrief language guide

A lab debrief should not celebrate the exploit. It should convert the observation into an engineering decision.

## Use this sequence

1. What failed?
2. Which boundary was crossed?
3. Why did the naive fix fail?
4. Which control changed the security property?
5. How did the student validate the control?
6. What residual risk remains?
7. What would you tell an engineering lead?

## For attack labs

Attack labs need observable failure and observable fix. Students should show vulnerable behavior, enable or propose the control, and show the security property changes.

## For reasoning labs

Reasoning labs need a graded artifact. Students should produce a review, memo, scope, rubric, or remediation plan that can be assessed against anchors.

## Common debrief correction

If a student says, "the model was tricked," ask: which component accepted untrusted output as authority?
