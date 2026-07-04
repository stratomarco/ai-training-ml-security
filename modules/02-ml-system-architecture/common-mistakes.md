# Common Mistakes: ML System Architecture

## Mistake 1: Drawing the model but not the system

A model box alone hides data sources, retrieval filters, tool permissions, logs, and deployment paths.

Better approach: draw the data flow and control flow around the model.

## Mistake 2: Treating retrieval as a search problem only

Vector search quality matters, but retrieval is also an access-control problem. A relevant restricted document is still restricted.

Better approach: enforce authorization before content is added to context.

## Mistake 3: Giving the agent the application's full privilege

A broad service account turns model mistakes into broad system actions.

Better approach: scope tool permissions by user, action, target object, tenant, and approval state.

## Mistake 4: Ignoring output sinks

Teams often review prompts and tools but forget that model output may be rendered, stored, parsed, or used as an argument.

Better approach: validate output for the sink where it is used.

## Mistake 5: Leaving logs out of the architecture

Logs can contain the most sensitive copy of the system: prompt, context, output, tool arguments, and error traces.

Better approach: include logs in the data-flow diagram and review their access, retention, and redaction.

## Mistake 6: Reviewing only the runtime path

ML systems also have training, evaluation, promotion, monitoring, feedback, and rollback paths.

Better approach: review the full lifecycle, especially artifact promotion and feedback loops.
