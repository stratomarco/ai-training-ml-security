from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_PARTS = {
    ".git",
    ".venv",
    "site",
    ".mkdocs-src",
    "__pycache__",
}

REPLACEMENTS = {
    "(dvaia-guides/)": "(dvaia-guides/README.md)",
    "(rag-labs/)": "(rag-labs/README.md)",
    "(agent-labs/)": "(agent-labs/README.md)",
    "(toy-ml-attacks/)": "(toy-ml-attacks/README.md)",
    "(mlops-supply-chain-labs/)": "(mlops-supply-chain-labs/README.md)",
    "(privacy-labs/)": "(privacy-labs/README.md)",
    "(adversarial-ml-labs/)": "(adversarial-ml-labs/README.md)",
    "(ai-red-team-labs/)": "(ai-red-team-labs/README.md)",
    "(architecture-risk-review-labs/)": "(architecture-risk-review-labs/docops-assistant-architecture-review.md)",
    "(brokenpilot/)": "(brokenpilot/README.md)",

    "(../../labs/adversarial-ml-labs/)": "(../../labs/adversarial-ml-labs/README.md)",
    "(../../labs/ai-red-team-labs/)": "(../../labs/ai-red-team-labs/README.md)",
    "(../../labs/brokenpilot/)": "(../../labs/brokenpilot/README.md)",

    "(../01-security-engineering-for-ai/)": "(../01-security-engineering-for-ai/README.md)",
    "(../02-ml-system-architecture/)": "(../02-ml-system-architecture/README.md)",
    "(../05-llm-application-security/)": "(../05-llm-application-security/README.md)",
    "(../06-rag-security/)": "(../06-rag-security/README.md)",
    "(../07-agent-tool-security/)": "(../07-agent-tool-security/README.md)",
    "(../08-secure-mlops-supply-chain/)": "(../08-secure-mlops-supply-chain/README.md)",
    "(../09-privacy-attacks/)": "(../09-privacy-attacks/README.md)",
    "(../10-adversarial-ml-robustness/)": "(../10-adversarial-ml-robustness/README.md)",
    "(../11-ai-red-team-methodology/)": "(../11-ai-red-team-methodology/README.md)",
}


def should_skip(path: Path) -> bool:
    return any(part in SKIP_PARTS for part in path.parts)


def main() -> None:
    changed = 0

    for path in ROOT.rglob("*.md"):
        if should_skip(path):
            continue

        text = path.read_text(encoding="utf-8")
        updated = text

        for old, new in REPLACEMENTS.items():
            updated = updated.replace(old, new)

        if updated != text:
            path.write_text(updated, encoding="utf-8", newline="\n")
            changed += 1
            print(f"updated: {path.relative_to(ROOT)}")

    print(f"\nFiles changed: {changed}")


if __name__ == "__main__":
    main()
