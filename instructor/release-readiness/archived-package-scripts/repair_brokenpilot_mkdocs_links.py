from pathlib import Path

brokenpilot_readme = Path("labs/brokenpilot/README.md")
prototype_readme = Path("labs/brokenpilot/prototype/README.md")

brokenpilot_readme.write_text("""# BrokenPilot Labs

BrokenPilot is the main runnable capstone environment for the course.

Use the current application in [`prototype-app/`](prototype-app/README.md). It is the supported lab target for:

- LLM application security
- RAG authorization and cross-tenant leakage
- direct prompt injection
- insecure output handling
- agent tool authorization
- approval gates
- memory poisoning
- audit evidence
- final capstone reporting

## Current lab path

Start with:

1. [`prototype-app/README.md`](prototype-app/README.md)
2. [`prototype-app/LAB_GUIDE.md`](prototype-app/LAB_GUIDE.md)
3. [`prototype-app/DIRECT_PROMPT_INJECTION_LAB.md`](prototype-app/DIRECT_PROMPT_INJECTION_LAB.md)
4. [`prototype-app/OUTPUT_HANDLING_LAB.md`](prototype-app/OUTPUT_HANDLING_LAB.md)
5. [`prototype-app/TOOL_CALLING_LAB.md`](prototype-app/TOOL_CALLING_LAB.md)
6. [`prototype-app/MEMORY_POISONING_LAB.md`](prototype-app/MEMORY_POISONING_LAB.md)
7. [`CAPSTONE_CHECKPOINTS.md`](CAPSTONE_CHECKPOINTS.md)
8. [`CAPSTONE_FINAL_REPORT_CURRENT_PATH.md`](CAPSTONE_FINAL_REPORT_CURRENT_PATH.md)

## Status of older prototype notes

Earlier planning notes were used to design the lab environment. They are not part of the student-facing course path and are not required to run the labs.

The supported target is `prototype-app/`.
""", encoding="utf-8", newline="\n")

prototype_readme.write_text("""# BrokenPilot Prototype Planning Notes

This folder is retained only as a historical marker for the early BrokenPilot design work.

The active and supported lab environment is:

[`../prototype-app/`](../prototype-app/README.md)

Do not use this folder as the student lab entry point. The runnable app, tests, lab guides, and capstone evidence path live in `prototype-app/`.

Earlier planning documents were archived out of the published course path during release cleanup.
""", encoding="utf-8", newline="\n")

print("patched BrokenPilot README files to remove stale prototype-planning links")
