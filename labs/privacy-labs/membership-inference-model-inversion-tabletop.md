# Lab  -  Membership Inference and Model Inversion Tabletop

## Module

Module 09  -  Privacy Attacks and Data Protection

## Lab type

Tabletop exercise.

This lab is designed to teach reasoning about model privacy attacks without requiring students to run offensive tooling.

## Learning objectives

Students will learn to:

1. Explain membership inference risk.
2. Explain model inversion risk.
3. Identify when training data membership is sensitive.
4. Identify model behaviors that increase privacy leakage.
5. Propose privacy testing and mitigations.
6. Communicate residual risk to leadership.

## Scenario

A company builds a model to help prioritize employee well-being support cases.

The model is trained on historical support-case metadata and limited free-text summaries.

The model returns:

- risk category;
- confidence score;
- suggested support workflow;
- short explanation.

Users include HR specialists and a small analytics team.

## Sensitive data

The training dataset may include:

- mental health support categories;
- medical accommodation references;
- leave information;
- manager conflict details;
- performance concerns;
- location and department;
- age band;
- tenure;
- free-text notes.

## Review questions

### Membership inference

- Why might training membership be sensitive in this scenario?
- What model outputs might leak membership signals?
- Could repeated queries increase confidence in membership inference?
- Which users or attackers might attempt this?

### Model inversion

- What hidden attributes could be inferred?
- Could explanations reveal sensitive attributes?
- Could confidence scores reveal too much?
- Could small groups or rare cases increase re-identification risk?

### Training data extraction

- Does the model ever generate text based on free-text summaries?
- Could memorized phrases appear in output?
- Are rare or unique examples more likely to leak?
- Were sensitive notes deduplicated, filtered, or minimized?

## Student tasks

1. Create an attack hypothesis for membership inference.
2. Create an attack hypothesis for model inversion.
3. Identify design choices that increase leakage risk.
4. Propose mitigations.
5. Define privacy test cases.
6. Write residual risk.

## Mitigation ideas

Students may propose:

- remove unnecessary free text;
- aggregate or generalize features;
- reduce output confidence detail;
- avoid exposing explanations that reveal sensitive attributes;
- rate-limit repeated queries;
- monitor suspicious query patterns;
- use privacy-preserving training techniques where appropriate;
- evaluate differential privacy if the model and use case justify it;
- restrict model access by role and purpose;
- perform privacy testing before release;
- document residual risk.

## Discussion questions

1. Is it acceptable to train on this data at all?
2. Can the model meet the business need with less sensitive data?
3. How much explanation is useful versus risky?
4. Should confidence scores be shown to all users?
5. What is the release gate for privacy testing?
6. Who accepts residual privacy risk?

## Deliverable

Use:

- `course-templates/privacy-risk-assessment-template.md`
