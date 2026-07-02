"""Repository structure checks for the course.

This check prevents the two most common drift problems:
1. A nested full copy of the repository accidentally committed.
2. Hand-maintained duplicate MkDocs copies of canonical content.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
failures = []

nested = ROOT / "ai-training-ml-security"
if nested.exists():
    failures.append("Nested ai-training-ml-security/ subtree exists. Delete it before committing.")

for rel in ["docs/modules", "docs/labs", "docs/templates", "docs/instructor", "docs/assessments"]:
    if (ROOT / rel).exists():
        failures.append(f"Duplicate generated content exists at {rel}. Run cleanup and generate .mkdocs-src instead.")

if failures:
    print("Repository structure check failed:\n")
    for item in failures:
        print(f"- {item}")
    sys.exit(1)

print("Repository structure checks passed.")
