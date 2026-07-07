from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    "roadmaps/v2-architecture-implementation-plan.md": [
        "v1.1.0 remains the stable teaching release",
        "v2.0 focuses",
        "Every v2 lab must have",
    ],
    "labs/brokenpilot-v2/AGENTIC_ARCHITECTURE.md": [
        "Orchestrator agent",
        "Tool broker",
        "MCP-like server boundary",
        "Trust boundaries",
    ],
    "labs/brokenpilot-v2/MESSAGE_ENVELOPE.md": [
        "sender_agent",
        "receiver_agent",
        "delegated_authority",
        "replay prevention",
    ],
    "labs/brokenpilot-v2/MCP_TRUST_BOUNDARY.md": [
        "Descriptor model",
        "Spoofed capability advertisement",
        "Descriptor drift",
        "trusted issuer list",
    ],
    "labs/brokenpilot-v2/FAILURE_CHAINS.md": [
        "Descriptor poisoning to unsafe tool routing",
        "Inter-agent replay",
        "Rogue agent impersonates a peer",
        "Cascading failure across delegation",
    ],
    "labs/brokenpilot-v2/CONTROL_MATRIX.md": [
        "Spoofed MCP-like descriptor",
        "Inter-agent replay",
        "Control quality standard",
    ],
    "labs/brokenpilot-v2/TEST_STRATEGY.md": [
        "descriptor validation",
        "Scenario tests",
        "v1 release gate must stay stable",
    ],
    "modules/v2-agentic-mcp-security/README.md": [
        "development-track module draft",
        "Agentic and MCP Security",
        "Required lab bar",
    ],
}

ROOT_PROCESS_DOC_NAMES = {
    "CLEANUP_BEFORE_RELEASE.md",
    "FINAL_HUMAN_POLISH_REPORT.md",
    "FINAL_RELEASE_REVIEW.md",
    "GENERATED_SCAFFOLDING_CLEANUP_REPORT.md",
    "QUALITY_GATE_BASELINE.md",
    "VALIDATION_BASELINE.md",
    "VOICE_POLISH_PASS_REPORT.md",
    "STYLE_AND_VOICE_FINAL_PASS.md",
    "RELEASE_CANDIDATE_CHECKLIST.md",
    "RELEASE_CHECKLIST.md",
    "QUALITY_IMPROVEMENT_PLAN.md",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required_files(errors: list[str]) -> None:
    for rel, needles in REQUIRED_FILES.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing required v2 file: {rel}")
            continue
        text = read(path)
        for needle in needles:
            if needle not in text:
                errors.append(f"{rel} missing required text: {needle}")


def check_workflow_script_references(errors: list[str]) -> None:
    workflows = ROOT / ".github" / "workflows"
    if not workflows.exists():
        return

    pattern = re.compile(r"python(?:\s+-m)?\s+(scripts/[A-Za-z0-9_\-./]+\.py)")
    for yml in list(workflows.glob("*.yml")) + list(workflows.glob("*.yaml")):
        text = read(yml)
        for match in pattern.finditer(text):
            rel = match.group(1)
            if not (ROOT / rel).exists():
                errors.append(f"{yml.relative_to(ROOT)} references missing script: {rel}")


def check_root_process_docs(errors: list[str]) -> None:
    for name in sorted(ROOT_PROCESS_DOC_NAMES):
        if (ROOT / name).exists():
            errors.append(f"process/release doc should not be at repository root: {name}")


def check_no_package_helpers(errors: list[str]) -> None:
    scripts = ROOT / "scripts"
    if not scripts.exists():
        return
    bad_prefixes = ("apply_", "repair_", "add_", "fix_")
    allowed = {"check_v2_dev_scaffold.py", "check_v2_architecture_spec.py"}
    for path in scripts.glob("*.py"):
        if path.name in allowed:
            continue
        if path.name.startswith(bad_prefixes):
            errors.append(f"package-era helper still active in scripts/: {path.relative_to(ROOT)}")


def check_markdown_links_in_v2(errors: list[str]) -> None:
    candidates = []
    for folder in [
        ROOT / "labs" / "brokenpilot-v2",
        ROOT / "modules" / "v2-agentic-mcp-security",
        ROOT / "roadmaps",
    ]:
        if folder.exists():
            candidates.extend(folder.glob("*.md"))

    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in candidates:
        text = read(path)
        for target in link_pattern.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            if "#" in target:
                target = target.split("#", 1)[0]
            if not target:
                continue
            target_path = (path.parent / target).resolve()
            try:
                target_path.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)} has link escaping repo: {target}")
                continue
            if not target_path.exists():
                errors.append(f"{path.relative_to(ROOT)} has missing relative link: {target}")


def main() -> None:
    errors: list[str] = []

    check_required_files(errors)
    check_workflow_script_references(errors)
    check_root_process_docs(errors)
    check_no_package_helpers(errors)
    check_markdown_links_in_v2(errors)

    if errors:
        print("v2 architecture spec check failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("v2 architecture spec check passed.")


if __name__ == "__main__":
    main()
