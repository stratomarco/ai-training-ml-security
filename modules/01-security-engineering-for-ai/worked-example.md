# Worked Example: Reviewing an Internal AI Ticket Assistant

## Scenario

A team wants to deploy an internal AI assistant for operations teams. The assistant can summarize incident tickets, search internal runbooks, suggest next steps, and draft ticket updates. A later release may allow the assistant to close duplicate tickets automatically.

## Step 1: Classify the feature

The first version is decision support. It reads tickets and documents, then drafts text for humans. The later version becomes a control-plane feature because it can change ticket state.

This distinction changes the controls. Drafting can be handled with retrieval authorization, output handling, logging, and user review. Closing tickets requires tool authorization, approval policy, rollback, and audit evidence.

## Step 2: Identify assets

Assets include incident ticket contents, customer identifiers, internal runbooks, credentials accidentally stored in documents, ticket status, audit logs, model prompts, retrieved context, and tool outputs.

The most sensitive asset is not the model. It is the combination of restricted operational data and state-changing tools.

## Step 3: Map trust boundaries

User prompts are untrusted input. Ticket comments are untrusted or semi-trusted data. Retrieved runbooks may be trusted for content but not for authority. Tool calls cross into operational state. Logs may contain sensitive fragments. The model provider boundary may matter if prompts or retrieved context leave the organization.

## Step 4: Write abuse cases

A malicious ticket comment instructs the assistant to ignore policy and close an unrelated ticket.

A user from tenant beta asks about alpha incidents and receives restricted context because retrieval authorization is missing.

A retrieved document contains HTML-like content that is rendered into a dashboard without encoding.

A model-generated summary includes sensitive data and is copied into a broad channel.

## Step 5: Select controls

Retrieval authorization must enforce tenant, role, classification, and allowed-user rules before context reaches the model.

Tool authorization must check user, tenant, role, target ticket, and action at execution time.

High-impact updates require approval.

Model output rendered in the UI must be encoded for the display context.

Audit logs must record retrieval source IDs, proposed action, authorization decision, approval result, and final tool result.

## Step 6: Validate

A beta viewer should not retrieve an alpha restricted document. A model-generated cross-tenant ticket update should be denied at the tool boundary. HTML-like output should be escaped in the render path. An approved ticket update should produce an audit record with user, target, decision, and result.

## Strong finding

The assistant can be induced to propose a cross-tenant ticket update, but the critical issue is missing authorization at the tool boundary. If the update endpoint accepts model-generated arguments without checking user tenant, role, and target ticket ownership, a malicious prompt or retrieved instruction can cause unauthorized state change. The fix is a tool broker authorization check that evaluates user, action, target object, tenant, approval requirement, and audit logging before execution. Validation is successful when the same model-generated request receives a deny response for cross-tenant targets and an allow response only for authorized same-tenant targets.

## Weak finding

The AI might close bad tickets. Add better guardrails.

## Residual risk

Even after tool authorization and retrieval controls are implemented, residual risk remains in summary quality, user over-trust, incomplete context, and operational rollback. Those risks should be handled with source display, human review for high-impact updates, monitoring, and clear rollback procedures.

## Why the strong finding is better

The strong finding names the root cause, the boundary, the impact, the control, and the validation method. The weak finding only describes a symptom.
