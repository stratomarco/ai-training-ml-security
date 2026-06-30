# Common Mistakes — Agent and Tool Security

This page lists mistakes that repeatedly appear in agent designs. Students should use it as a review checklist during architecture review, lab work, and capstone preparation.

## 1. Treating the model as the authorization layer

Bad assumption:

```text
The system prompt says the agent may only act on authorized records, so it is safe.
```

Why it is wrong:

The model can be influenced by user input, retrieved content, memory, or tool output. Authorization must be enforced by deterministic application logic.

Better pattern:

```text
The model proposes an action. The tool broker authorizes the action using user, agent, tenant, target, action, and risk context.
```

## 2. Giving the agent broad tools

Bad tools:

```text
run_shell(command)
query_database(sql)
update_record(table, id, fields)
send_email(to, subject, body)
```

These are hard to validate safely because they expose broad power through flexible arguments.

Better tools:

```text
run_approved_diagnostic(check_name, target_id)
search_authorized_docs(query, scope)
add_ticket_comment(ticket_id, comment)
request_ticket_status_change(ticket_id, status, reason)
```

Narrow tools reduce blast radius.

## 3. Missing target-object authorization

Many systems check whether the user can use the tool but forget to check whether the user can act on the specific target.

Bad check:

```text
Alice is ops, so she can update tickets.
```

Better check:

```text
Alice is ops, the ticket belongs to Alice's tenant, the action is allowed for her role, and this status change does not require additional approval.
```

BrokenPilot demonstrates this mistake directly.

## 4. No approval gate for state-changing actions

Agents often start with read-only tasks and gradually gain write actions. The approval model is forgotten.

Ask:

- Does this action change persistent state?
- Is it externally visible?
- Is it irreversible or expensive to reverse?
- Does it affect another tenant, customer, or production system?
- Should a human approve it?

## 5. Trusting memory too much

Bad assumption:

```text
Memory is previous context, so it is helpful and safe.
```

Why it is wrong:

Memory may be stale, malicious, false, out of scope, cross-tenant, or created by an attacker.

Better pattern:

- memory has owner and scope;
- memory has trust level;
- memory has review status;
- memory has expiry;
- memory cannot directly trigger sensitive tool calls without policy checks.

## 6. Letting retrieved content become instruction

Agent systems often combine RAG and tools. That creates a dangerous path:

```text
poisoned document -> model plan -> tool call -> business action
```

Retrieved content should be labeled and handled as untrusted data. It may help answer a question, but it should not become authority to perform an action.

## 7. Missing audit context

Bad log:

```text
update_ticket succeeded
```

Useful log:

```text
user=alice
agent=ops-agent
tool=update_ticket
target=TCK-2001
target_tenant=beta
action=close
authorization_decision=denied
reason=cross_tenant
correlation_id=...
```

Without useful logs, the system cannot support incident response, grading, debugging, or control validation.

## 8. No dry-run mode

A safe agent should often be able to say:

```text
Here is what I would do, but I have not executed it.
```

Dry-run mode is useful for:

- training;
- high-risk workflows;
- debugging;
- approvals;
- red team assessment;
- preventing accidental damage.

## 9. Letting agent loops run without limits

Agent loops can create cost, spam, repeated tool calls, or repeated failed actions.

Controls:

- max steps;
- max tool calls;
- max cost;
- max retries;
- timeout;
- repeated-denial stop condition;
- escalation to human.

## 10. Grading only the exploit

In a training context, it is easy to reward students only for finding a clever exploit.

This course should reward:

- correct root cause;
- security principle violated;
- concrete control design;
- validation of the fix;
- residual risk;
- clear communication.

Finding is not enough. Fixing and validating matter.
