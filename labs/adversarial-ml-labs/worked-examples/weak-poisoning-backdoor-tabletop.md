# Weak Example: Poisoning and Backdoor Tabletop Review

Attackers could poison the model, so the team should clean the data and use a secure model. They should check accuracy and retrain if it is bad.

## Why this is weak

- It does not describe how poisoned data enters the pipeline.
- It treats "clean the data" as a control without ownership or validation.
- It relies on aggregate accuracy only.
- It has no promotion gate, no rollback plan, and no residual-risk statement.
