# BrokenPilot Architecture

## High-level architecture

```text
employee browser
  |
  v
BrokenPilot web UI
  |
  v
BrokenPilot API
  |
  +-- identity/session service
  +-- prompt/context builder
  +-- policy and authorization service
  +-- model gateway
  +-- retrieval service
  |     +-- document store
  |     +-- embedding service
  |     +-- vector database
  |
  +-- tool gateway
  |     +-- ticket tool
  |     +-- incident tool
  |     +-- config lookup tool
  |     +-- notification tool
  |     +-- memory tool
  |
  +-- audit/logging service
  +-- monitoring and alerting
```

## Components

| Component | Purpose | Security relevance |
|---|---|---|
| Web UI | User interaction layer | Output rendering, session handling, user intent capture. |
| BrokenPilot API | Main backend orchestration | Central authorization and policy enforcement point. |
| Identity/session service | Maps user to role and team | Authorization decisions depend on accurate identity. |
| Prompt/context builder | Builds model input | Can confuse instructions, data, memory, and retrieved content. |
| Model gateway | Calls the LLM provider or local model | Needs rate limits, logging, policy, and provider isolation. |
| Retrieval service | Searches docs and vector DB | Needs document-level authorization and provenance. |
| Document store | Stores internal docs | Contains trusted and untrusted content. |
| Embedding service | Creates vector representations | Can leak or preserve sensitive content. |
| Vector database | Stores chunks and metadata | Requires metadata-preserving authorization. |
| Tool gateway | Allows the assistant to act | Requires least privilege and per-action authorization. |
| Ticket tool | Reads/creates/updates tickets | High-risk because it changes business workflows. |
| Incident tool | Reads and summarizes incidents | Sensitive operational context. |
| Config lookup tool | Returns service ownership/config | Can expose internal structure or secrets if poorly filtered. |
| Notification tool | Sends messages | Can amplify misinformation or trigger social engineering. |
| Memory tool | Stores user/workspace memory | Risk of memory poisoning and persistence. |
| Audit/logging | Records security-relevant events | Needed for investigation and non-repudiation. |
| Monitoring | Detects abuse, drift, and failures | Needed for response and governance. |

## Data-flow overview

```text
1. User sends message to BrokenPilot UI.
2. Backend authenticates the user and retrieves role/team attributes.
3. Prompt/context builder prepares model input.
4. Retrieval service searches documents and vector DB.
5. Retrieved chunks are added to context.
6. Model generates a response and may request tool calls.
7. Tool gateway validates tool call schema.
8. Authorization service decides whether the user, not the model, can perform the action.
9. High-risk actions require human approval.
10. Approved tool actions run against fake ticket/config/memory systems.
11. Response is returned to the user.
12. Security-relevant events are logged and monitored.
```

## Trust boundaries

| Boundary | Description | Risk |
|---|---|---|
| User to UI | User input enters the system | Direct prompt injection and malicious payloads. |
| UI to API | Authenticated session crosses into backend | Broken auth/session handling. |
| API to model gateway | System prompts and retrieved context are sent to model | Sensitive context exposure and provider trust assumptions. |
| API to retrieval service | User query becomes document retrieval | Retrieval authorization and query manipulation. |
| Retrieval service to vector DB | Chunks retrieved by semantic similarity | Cross-tenant leakage, missing metadata filters. |
| API to tool gateway | Model-requested actions become system actions | Tool misuse and excessive agency. |
| Tool gateway to backend systems | Fake business systems are changed | Integrity and availability impact. |
| API to memory service | Persistent state is written | Memory poisoning and stale instructions. |
| Logging boundary | Prompts, responses, and tool calls are logged | Sensitive data retention and log access risk. |

## Architecture anti-patterns intentionally present in the vulnerable design

The paper design assumes the initial BrokenPilot implementation contains several anti-patterns:

1. Retrieved content is inserted into the prompt without clear data/instruction separation.
2. The vector database stores chunks without reliable document-level authorization metadata.
3. The model can request tools and the backend trusts the request too much.
4. Some tool permissions are checked at the assistant level rather than per user and per action.
5. High-risk ticket updates do not require human approval.
6. Memory entries are trusted as helpful preferences without provenance or expiry.
7. Logs capture sensitive prompts and retrieved content without clear retention rules.
8. Incident summaries are treated as authoritative even when based on incomplete context.

## Secure architecture direction

The target design should move security decisions out of the model and into deterministic services:

```text
user request
  |
  v
identity and policy enforcement
  |
  v
retrieval with authorization filters
  |
  v
context builder with source labeling
  |
  v
model gateway
  |
  v
structured response / proposed actions
  |
  v
policy engine and tool authorization
  |
  +-- low-risk action: execute and log
  +-- medium-risk action: require confirmation
  +-- high-risk action: require approval
  +-- disallowed action: block and log
```

## Architectural principle

The model may help propose actions, summarize context, or draft text. It should not be the sole authority for authorization, policy, data access, or high-impact business decisions.
