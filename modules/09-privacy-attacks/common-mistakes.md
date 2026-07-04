# Common mistakes: Privacy attacks and data protection

## Mistake 1: Treating privacy as only PII

Secrets, credentials, customer strategy, internal contacts, incident reports, and tenant-specific business data can all be privacy or confidentiality concerns. The course uses fake tokens and fake contacts because they are safe training examples, not because privacy risk is limited to tokens.

## Mistake 2: Filtering after retrieval

If unauthorized content enters the model context, the main boundary already failed. Output filtering may reduce harm, but it does not repair the architecture.

## Mistake 3: Ignoring internal viewers

Logs, traces, support tools, analytics exports, and evaluation dashboards can leak sensitive data to internal users. Internal does not mean authorized.

## Mistake 4: Confusing redaction with minimization

Redaction removes or masks selected content. Minimization avoids collecting or processing unnecessary content in the first place. Strong systems use both.

## Mistake 5: Overclaiming privacy from synthetic tests

Synthetic tests are useful for safe regression testing. They do not prove that production data has no privacy risk. They prove that specific control paths behave as expected.

## Mistake 6: Forgetting retention

A chat system may not leak data in the moment but may retain sensitive prompts and retrieved context for months. Retention is part of the privacy boundary.

## How to correct these mistakes in class

When a student says "the model leaked private data," push for the exact system path. Was the data retrieved without authorization? Was it summarized from authorized context but shown to the wrong user? Was it stored in logs? Was it inferred from repeated queries? Each path has a different control.

When a student proposes output redaction as the main fix, ask whether the model should have seen the data at all. In most cross-tenant cases, the primary fix is authorization before retrieval. Redaction and logging controls are defense in depth, not permission to send restricted data into context.

The expected correction is a data-flow answer: protect retrieval, output, logs, traces, retention, and support access as one privacy boundary.
