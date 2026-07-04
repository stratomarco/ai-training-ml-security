# Toy ML Attack Labs

Toy ML labs teach classical adversarial ML concepts without requiring students to be ML researchers.

## Lab ideas

1. Evasion against a spam classifier
2. Poisoning a small training dataset
3. Model extraction by querying a simple prediction API
4. Membership inference on an overfit model
5. Output integrity failure through bad post-processing
6. Backdoor trigger in a small model

## Core lesson

A model can be accurate in normal testing and still fail under adversarial pressure.

<!-- toy-classifier-app-link -->

## Runnable toy-classifier app

The observable path for Modules 03 and 10 is now the shipped toy-classifier app:

```text
labs/toy-ml-attacks/toy-classifier-app/
```

Use it for evasion, poisoning, extraction, and output-integrity exercises. The dataset is synthetic, deterministic, local, and covered by pytest.

<!-- toy-classifier-instructor-debrief:start -->
## Toy-classifier teaching resources

The toy-classifier app now has instructor notes, a student debrief, strong and weak examples, and a grading rubric. Use these materials to keep the lab focused on engineering decisions rather than attack novelty.
<!-- toy-classifier-instructor-debrief:end -->
