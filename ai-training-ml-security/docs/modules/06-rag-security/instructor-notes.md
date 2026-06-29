# Module 6 Instructor Notes — RAG Security and Indirect Prompt Injection

## Teaching goal

Students should leave this module understanding that RAG security is primarily an architecture, data governance, and access-control problem.

Do not let the session become only a prompt-injection trick workshop. The exploit is useful because it reveals a design flaw. The fix should usually be in the retrieval pipeline, policy layer, data model, or workflow design.

## Instructor framing

Open with this contrast:

```text
Without RAG:
User asks a question. The model answers from its built-in behavior and prompt context.

With RAG:
User asks a question. The system retrieves private or external content, injects it into the model context, and the model answers using that content.
```

Then ask:

> Who decided the model was allowed to see those documents?

This question usually exposes whether the architecture has real authorization or only semantic retrieval.

## Concepts to emphasize

### 1. Similarity is not authorization

Vector search returns semantically similar content. It does not know whether the user has permission to see that content unless the system explicitly includes policy filters.

### 2. Retrieved content is untrusted input

Even internal documents can be malicious, stale, wrong, or attacker-influenced.

Examples:

- shared wiki pages
- tickets created by users
- support emails
- vendor documentation
- public webpages
- code comments
- markdown files
- PDFs

### 3. Prompt separation helps but does not enforce policy

It is useful to label retrieved content as data. But if a sensitive document reaches the model, the system has already exposed it to a component that may summarize or transform it.

### 4. Chunking is a security operation

Chunking can accidentally remove classification, tenant, owner, or policy context. Make students think of chunking as a transformation that must preserve security metadata.

### 5. RAG failures are often invisible

The user may see a normal answer. They may not see that the answer used a sensitive document, a poisoned document, or a low-trust source.

## Suggested timing

| Activity | Time |
|---|---:|
| Architecture walkthrough | 20 min |
| Direct vs indirect prompt injection | 20 min |
| RAG trust boundary discussion | 20 min |
| Lab setup and exploitation | 45–60 min |
| Mitigation design workshop | 30 min |
| Quiz and review | 15 min |

## Walkthrough prompts

Use these questions during the session:

1. What documents are in the index?
2. Who is allowed to read each document?
3. Does the vector database know that?
4. Does every chunk preserve that metadata?
5. Can query rewriting expand the search beyond the user's authorization?
6. Is retrieval filtered before the model sees the context?
7. Can the model cite a source the user cannot open?
8. Are retrieved chunks logged? Who can read the logs?
9. What happens if a document contains instructions to the assistant?
10. What happens if retrieved sources conflict?

## Common student mistakes

### Mistake: Treating RAG as only a prompt problem

Corrective framing:

> The prompt is the last mile. The security problem started when the system selected and inserted context.

### Mistake: Filtering after generation

Corrective framing:

> Output filters help, but they are not a substitute for pre-retrieval authorization. The model may already have processed unauthorized content.

### Mistake: Assuming internal documents are trusted

Corrective framing:

> Internal does not mean trusted. Many internal systems accept user-generated or vendor-generated content.

### Mistake: Ignoring metadata

Corrective framing:

> Metadata is security state. If the chunk loses metadata, the system loses the ability to enforce policy.

### Mistake: Believing citations solve the problem

Corrective framing:

> Citations improve traceability. They do not guarantee authorization, correctness, or safe disclosure.

## Demonstration idea

Use a small set of documents:

1. `public-policy.md` — accessible to everyone
2. `finance-plan.md` — finance team only
3. `malicious-runbook.md` — contains hidden instructions
4. `deprecated-security-guide.md` — stale guidance
5. `tenant-a-incident.md` — tenant A only
6. `tenant-b-incident.md` — tenant B only

Then ask the assistant questions as different user roles.

Expected failures:

- normal user receives finance content
- tenant A user receives tenant B content
- malicious runbook changes model behavior
- deprecated guide is treated as current
- answer cites a source the user should not access

## Discussion: what is a good fix?

A strong answer includes:

- document classification at ingestion
- access labels copied to chunks
- tenant filters in vector search
- pre-retrieval policy decision
- source trust ranking
- exclusion of secrets and sensitive data
- output policy check
- human review for high-impact answers
- logging of retrieved document IDs
- adversarial regression tests

A weak answer says only:

- make the prompt stronger
- block the words `ignore previous instructions`
- ask the LLM to follow policy
- rely on citation display

## Instructor note on safety

Keep all payloads local and educational. The lab should not instruct students to attack real RAG systems or extract real secrets. Use fake documents, fake tenants, and fake sensitive data.

