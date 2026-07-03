from __future__ import annotations
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "labs/LAB_QUALITY_STANDARD.md",
    "course-templates/reasoning-lab-deliverable-template.md",
    "assessments/reasoning-lab-quality-rubric.md",
    "labs/privacy-labs/worked-examples/strong-membership-inference-risk-review.md",
    "labs/privacy-labs/worked-examples/weak-membership-inference-risk-review.md",
    "labs/adversarial-ml-labs/worked-examples/strong-poisoning-backdoor-tabletop.md",
    "labs/adversarial-ml-labs/worked-examples/weak-poisoning-backdoor-tabletop.md",
    "labs/architecture-risk-review-labs/worked-examples/strong-docops-architecture-risk-review.md",
    "labs/architecture-risk-review-labs/worked-examples/weak-docops-architecture-risk-review.md",
    "labs/ai-red-team-labs/worked-examples/strong-ai-red-team-scope.md",
    "labs/ai-red-team-labs/worked-examples/weak-ai-red-team-scope.md",
    "modules/01-security-engineering-for-ai/exercise-deliverable-anchor.md",
    "modules/02-ml-system-architecture/exercise-deliverable-anchor.md",
]
SNIPPETS = {
    "labs/LAB_QUALITY_STANDARD.md": ["Observable failure and observable fix", "The fix is the graded artifact", "Reasoning labs are design"],
    "course-templates/reasoning-lab-deliverable-template.md": ["Residual risk", "Final decision", "Naive fix"],
    "assessments/reasoning-lab-quality-rubric.md": ["Minimum passing answer", "Excellent answer", "Validation"],
    "labs/agent-labs/README.md": ["The runnable agent-security path is BrokenPilot", "tool permission matrix"],
    "labs/rag-labs/README.md": ["The runnable RAG-security path is BrokenPilot", "retrieval authorization"],
}
STRONG = [
    "labs/privacy-labs/worked-examples/strong-membership-inference-risk-review.md",
    "labs/adversarial-ml-labs/worked-examples/strong-poisoning-backdoor-tabletop.md",
    "labs/architecture-risk-review-labs/worked-examples/strong-docops-architecture-risk-review.md",
]
WEAK = [
    "labs/privacy-labs/worked-examples/weak-membership-inference-risk-review.md",
    "labs/adversarial-ml-labs/worked-examples/weak-poisoning-backdoor-tabletop.md",
    "labs/architecture-risk-review-labs/worked-examples/weak-docops-architecture-risk-review.md",
    "labs/ai-red-team-labs/worked-examples/weak-ai-red-team-scope.md",
]
def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")
def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")
def main() -> None:
    for path in REQUIRED:
        require((ROOT / path).exists(), f"missing required file: {path}")
    for path, snippets in SNIPPETS.items():
        require((ROOT / path).exists(), f"missing file for snippet check: {path}")
        text = read(path)
        for snippet in snippets:
            require(snippet in text, f"missing snippet in {path}: {snippet}")
    for path in STRONG:
        text = read(path)
        for snippet in ["Evidence", "Risk statement", "Recommended controls", "Residual risk", "Decision"]:
            require(snippet in text, f"strong anchor missing {snippet}: {path}")
    scope = read("labs/ai-red-team-labs/worked-examples/strong-ai-red-team-scope.md")
    for snippet in ["In scope", "Out of scope", "Rules of engagement", "Success criteria"]:
        require(snippet in scope, f"strong red-team scope missing {snippet}")
    for path in WEAK:
        require("Why this is weak" in read(path), f"weak anchor lacks critique: {path}")
    print("Lab improvement Part 6 quality-standard checks passed.")
if __name__ == "__main__":
    main()
