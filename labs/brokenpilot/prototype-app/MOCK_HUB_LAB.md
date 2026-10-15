# BrokenPilot Mock Hub: credential exposure and scope

## Purpose

This optional offline exercise separates two controls: keeping credentials out of diagnostics and giving an inference worker only the registry permissions it needs. The Hub, revisions, and tokens are in-memory fakes. The app does not contact Hugging Face, load weights, execute code, or store a model file.

The 2024 Hugging Face Spaces secrets incident is a useful discussion prompt about credential scope. The diagnostic endpoint in this lab is fictional; it is not presented as the cause of that incident.

## Run the vulnerable profile

First follow the [BrokenPilot first-run setup](README.md#first-run-and-guided-path) to create the virtual environment and install the app dependencies. From `labs/brokenpilot/prototype-app` with that environment active, start:

```text
python run_lab.py --profile vulnerable
```

Open `http://127.0.0.1:8010` and find **Mock model Hub**.

1. Check that the active fake revision is `approved-v1`.
2. Select **Inspect diagnostics**. The response contains a generated `LAB-WRITE-...` token and reports `runtime_credential_scope: write`.
3. Copy only that lab token into **Fake registry token**. Select **Promote unreviewed revision**.
4. Confirm that the API allows the request and the active fake revision becomes `unreviewed-v2`. Inspect the response and the audit log. The token is never written to the audit log.
5. Select **Reset fake lab state**. Reset restores `approved-v1` and rotates both lab tokens. A token from before reset no longer works.

No real model behavior changes. The observable effect is the mock registry state transition.
The UI shows the fake token in the live diagnostic response but redacts it from saved and exported notebook evidence.
The separate artifact-promotion gate uses the same fictional model name for comparison, but the two labs do not share state or enforce each other's decisions.

## Compare the controls

Stop the app with `Ctrl+C` before each profile change. A new process starts with fresh fake state and credentials.

| Profile | Diagnostic result | Promoting with the diagnostic token |
|---|---|---|
| `vulnerable` | Exposes a write-scoped token | Allowed |
| `hub-redaction` | Omits the token; worker still has write scope | No token is available through diagnostics |
| `hub-least-privilege` | Exposes a read-scoped token | Denied with `mock_hub_write_scope_required`; revision stays `approved-v1` |
| `all-controls` | Omits the token; worker has read scope | No diagnostic token; worker lacks registry write scope |

Redaction reduces one exposure path. Least privilege limits what a leaked worker token can do. They are separate controls, so compare each before enabling both.

## Explain the boundary

In a real design, an inference worker should receive only the short-lived, narrowly scoped access needed to read an approved artifact. Promotion should belong to a separate identity and workflow. Diagnostics, logs, and browser responses must not expose either credential. A real registry would also need identity verification, audit, and approval policy. This lab demonstrates only the credential-scope decision.

Do not use real registry credentials, real model repositories, or personal data. The local app has no user authentication; keep it bound to loopback.
