# Toy Classifier Debrief for Module 10

Module 10 uses the toy-classifier app to discuss robustness and the danger of hard-gate decisions.

## Core decision

The key question is not whether the model can be fooled. The key question is whether the system can safely depend on the model for the authority it has been given.

## Discussion prompts

1. Should the classifier automatically block a user, transaction, ticket, or message?
2. What happens when the classifier is uncertain?
3. What perturbations should be in the regression test set?
4. What data controls would reduce poisoning risk?
5. What monitoring would detect probing or drift?
6. What rollback path exists if the deployed model or threshold is wrong?

## Expected conclusion

For most high-impact decisions, the classifier should start as assisted triage or monitoring only. Automatic enforcement requires stronger evidence: robustness tests, fallback, threshold governance, abuse monitoring, and clear rollback.
