# Common Mistakes: OWASP ML Security Top 10

## Mistake 1: Treating the list as a checklist

A checklist can help coverage, but it does not replace system analysis.

Better approach: map each relevant category to an entry point, component, security property, impact, control, and validation.

## Mistake 2: Assigning every category to every system

Not every ML system has every risk. Forcing all categories onto a system creates noise and weakens credibility.

Better approach: focus on categories that match the system's data, model, deployment, and decision role.

## Mistake 3: Reporting category names as findings

"ML01 input manipulation" is not a finding. It is a mapping.

Better approach: write the actual failure path and evidence.

## Mistake 4: Ignoring system impact

A model failure is not always a security incident. The impact depends on what the system does with the output.

Better approach: describe the downstream decision or action.

## Mistake 5: Over-focusing on exotic attacks

Some teams jump to advanced adversarial examples while ignoring basic authorization, logging, artifact integrity, and privacy failures.

Better approach: cover practical controls first, then evaluate advanced attacks in context.

## Mistake 6: Treating model robustness as the only defense

Robustness helps, but critical systems also need fallback, review, authorization, monitoring, and recovery.

Better approach: combine model-level and system-level controls.
