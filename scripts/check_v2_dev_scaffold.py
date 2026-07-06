from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "roadmaps/v2-roadmap.md",
    "labs/brokenpilot-v2/README.md",
    "labs/brokenpilot-v2/ARCHITECTURE.md",
    "labs/brokenpilot-v2/THREAT_MODEL.md",
    "labs/brokenpilot-v2/LAB_QUALITY_BAR.md",
    "modules/v2-agentic-mcp-security/module-outline.md",
]

REQUIRED_TEXT = {
    "roadmaps/v2-roadmap.md": [
        "v1.1.0 remains the stable teaching release",
        "v2.0",
        "Multi-agent and MCP security",
        "living-content model",
    ],
    "labs/brokenpilot-v2/ARCHITECTURE.md": [
        "Tool broker",
        "MCP-like server boundary",
        "signed descriptor verification",
    ],
    "labs/brokenpilot-v2/THREAT_MODEL.md": [
        "Spoofed tool descriptor",
        "Cascading failure",
        "Descriptor drift",
    ],
    "labs/brokenpilot-v2/LAB_QUALITY_BAR.md": [
        "unsafe baseline",
        "naive-fix failure mode",
        "graded deliverable",
    ],
}


def main() -> None:
    errors: list[str] = []

    for rel in REQUIRED:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing: {rel}")
            continue

        text = path.read_text(encoding="utf-8")
        for needle in REQUIRED_TEXT.get(rel, []):
            if needle not in text:
                errors.append(f"{rel} missing required text: {needle}")

    # v2 planning should not alter v1 module sequence by accident.
    mkdocs = ROOT / "mkdocs.yml"
    if mkdocs.exists() and "v2-agentic-mcp-security" in mkdocs.read_text(encoding="utf-8"):
        errors.append("mkdocs.yml should not wire v2 planning into the v1 published nav yet")

    if errors:
        print("v2 dev scaffold check failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("v2 dev scaffold check passed.")


if __name__ == "__main__":
    main()
