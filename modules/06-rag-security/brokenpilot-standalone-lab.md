# BrokenPilot Standalone Lab: RAG Security

This lab replaces or complements the DVAIA Module 06 RAG lab.

## Learning objective

Students must show that retrieval is an authorization boundary. If the retriever returns cross-tenant or restricted documents, the model can expose or act on context the user should never have received.

## Step 1: reset state

PowerShell:

```powershell
Invoke-RestMethod http://127.0.0.1:8010/reset -Method Post
```

## Step 2: demonstrate cross-tenant retrieval

Use Eve, a Beta-side user, to search for Alpha payment material.

```powershell
Invoke-RestMethod http://127.0.0.1:8010/retrieve `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"eve","query":"payment api credential rotation token","top_k":3}'
```

Expected evidence in vulnerable mode:

```text
DOC-002
Alpha Payment API Credential Rotation
FAKE-ALPHA-PAYMENT-TOKEN-DO-NOT-USE
```

The fake token is intentionally fake. The point is the authorization failure, not the value of the token.

## Step 3: enable retrieval authorization

```powershell
$env:ENABLE_RETRIEVAL_AUTHZ="true"
```

Run the same request again.

Expected evidence:

```text
DOC-002 is no longer returned to Eve.
```

## Step 4: connect retrieval and prompt injection

Run the chat flow with Alice:

```powershell
Invoke-RestMethod http://127.0.0.1:8010/chat `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"alice","message":"vendor onboarding incident token runbook","top_k":4}'
```

Expected evidence:

```text
The assistant receives a malicious instruction from retrieved context.
```

## Required student explanation

A good RAG finding does not say only "the model leaked data." It explains the system failure:

```text
The retriever selected documents without enforcing tenant and role authorization. Once unauthorized or malicious context entered the prompt, the model became a downstream amplifier. The control must be applied before context reaches the model.
```

## Deliverable

Update the evidence log with:

- user identity;
- query;
- returned document ids;
- control state;
- expected result;
- actual result;
- recommended fix.
