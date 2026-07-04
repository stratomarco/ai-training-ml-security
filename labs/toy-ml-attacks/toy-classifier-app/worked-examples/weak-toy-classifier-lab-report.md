# Weak Example: Toy Classifier Lab Report

The model can be tricked by changing words. This means it is vulnerable. The fix is to train it with more data and block bad words. The poisoning script also showed problems, so the team should protect the dataset. Extraction can be stopped by hiding the model. The threshold should not be changed.

I recommend improving the model and adding guardrails. After that it should be safe to deploy.

## Why this is weak

This report lists observations but does not make a clear deployment decision. It does not explain what authority the classifier has, what security property changed, how the proposed controls would be validated, or what residual risk remains. It also recommends broad fixes like more data and guardrails without specifying provenance, approval, monitoring, fallback, or rollback.
