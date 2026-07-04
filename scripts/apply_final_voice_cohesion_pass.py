from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MODULES = [
    ("01-security-engineering-for-ai", "Security Engineering for AI", "plain security engineering language", "what the model can influence", "where the system must enforce boundaries"),
    ("02-ml-system-architecture", "ML System Architecture", "system mapping language", "where data, authority, artifacts, logs, and outputs move", "which trust boundaries matter"),
    ("03-owasp-ml-top-10", "OWASP ML Top 10", "finding classification language", "which ML risk category explains the observed failure", "how evidence becomes a concrete finding"),
    ("04-biml-architectural-risk-analysis", "BIML Architectural Risk Analysis", "architecture risk language", "which design assumptions must be tested", "what must be controlled before implementation"),
    ("05-llm-application-security", "LLM Application Security", "instruction boundary language", "when untrusted text is treated as authority", "how the application constrains model behavior"),
    ("06-rag-security", "RAG Security", "retrieval boundary language", "who can retrieve which context and why", "how retrieval and generation inherit data-access risk"),
    ("07-agent-tool-security", "Agent and Tool Security", "action authorization language", "which actions the model may propose", "which actions the system may execute"),
    ("08-secure-mlops-supply-chain", "Secure MLOps and AI Supply Chain", "artifact trust language", "whether a model artifact can be promoted", "what provenance, integrity, approval, and rollback evidence exists"),
    ("09-privacy-attacks", "Privacy Attacks and Data Protection", "information exposure language", "what information can be disclosed, inferred, reconstructed, or logged", "which privacy control changes that exposure"),
    ("10-adversarial-ml-robustness", "Adversarial ML and Robustness", "decision reliability language", "whether the model is reliable enough for its decision role", "when fallback, monitoring, or human review is required"),
    ("11-ai-red-team-methodology", "AI Red Team Methodology", "decision-grade evidence language", "what evidence would change a launch or control decision", "how to report findings without theatrics"),
    ("12-capstone-brokenpilot", "BrokenPilot Capstone", "integrated risk language", "how multiple AI security failures combine", "which controls, validations, and residual risks matter most"),
]


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.strip() + "\n", encoding="utf-8", newline="\n")
    print(f"wrote: {path}")


def append_once(path: str, marker: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    existing = p.read_text(encoding="utf-8") if p.exists() else ""
    if marker in existing:
        return
    p.write_text(existing.rstrip() + "\n\n" + content.strip() + "\n", encoding="utf-8", newline="\n")
    print(f"updated: {path}")


def module_note(slug: str, title: str, language: str, decision: str, evidence: str, index: int) -> str:
    prev_title = MODULES[index - 1][1] if index > 0 else "the course introduction"
    next_title = MODULES[index + 1][1] if index < len(MODULES) - 1 else "the final course debrief"
    return f"""
# Cohesion note: {title}

## Why this module exists

This module gives students a shared way to talk about {decision}. It should not be taught as a list of isolated risks. It should be taught as one step in the course story: AI systems are software systems with unusual trust boundaries, feedback loops, and evidence problems.

## Language to keep consistent

Use {language}. Avoid treating the model as the only security boundary. The central question is: {evidence}?

## Handoff from the previous module

The previous module, {prev_title}, gives students the vocabulary needed for this module. Start by reconnecting the class to that vocabulary before introducing new terms.

## Handoff to the next module

The next module, {next_title}, should feel like a consequence of this module, not a restart. End this module by naming what is still unresolved and what the next module will make concrete.

## Instructor emphasis

Keep the discussion grounded in engineering decisions. A good answer names the boundary, the evidence, the control, the validation method, and the residual risk. A weak answer only names the attack or says to add guardrails.

## Student exit line

By the end of this module, a student should be able to say: I can explain {decision}, show what evidence supports the risk, recommend a control, and describe how I would validate that the control worked.
"""


def main() -> None:
    write("COURSE_STORYLINE.md", """
# Course storyline

This course has one through-line: AI security is security engineering for systems that contain models. The model matters, but the model is not the whole system and should not be treated as the only boundary.

The course starts with foundations, then moves through architecture, taxonomy, and design risk. It then turns those foundations into hands-on work across LLM applications, RAG, agents, supply chain, privacy, adversarial robustness, and red team reporting. The capstone asks students to combine these threads into a decision-grade review of BrokenPilot with validation evidence and residual risk.

## The course arc

1. Establish the security engineering lens.
2. Map the AI system as a set of data, authority, artifact, and output flows.
3. Classify risks with OWASP ML and related frameworks without becoming checklist-driven.
4. Use BIML-style architectural risk analysis to find assumptions before implementation.
5. Observe LLM application failures and learn why prompts are not security boundaries.
6. Observe RAG failures and learn why retrieval authorization is part of access control.
7. Observe agent failures and learn why action authorization must live outside the model.
8. Review MLOps evidence and learn why model promotion is a supply-chain decision.
9. Observe privacy leakage and learn to reason about disclosure, inference, reconstruction, and logging.
10. Observe classical ML robustness failures and learn why accuracy is not enough.
11. Convert tests into decision-grade red team evidence.
12. Integrate the course in the BrokenPilot capstone.

## Repeated message

Every module should return to the same question: What can the model influence, and where must the system enforce the boundary?

## What students should stop saying

- The model was tricked, so we need a stronger prompt.
- The answer was wrong, so the model is insecure.
- We found an attack, so the system cannot launch.
- The tool called the API, so the model was authorized.

## What students should start saying

- This text crossed a trust boundary and was treated as instruction.
- This retrieval result bypassed an authorization decision.
- This action needs target-object authorization outside the model.
- This artifact lacks enough provenance and integrity evidence for promotion.
- This finding changes the launch decision because the control is missing or unvalidated.
""")

    write("COURSE_VOICE_AND_COHESION_REVIEW.md", """
# Course voice and cohesion review

This file defines the voice target for the course before final cleanup.

## Voice target

The course should sound like an experienced security engineer teaching a practical internal training. It should be direct, evidence-driven, and careful about claims. It should avoid sounding like marketing copy, a compliance checklist, or a collection of generated summaries.

## Preferred style

- Start with the engineering decision.
- Explain the failure mode in ordinary security language.
- Show the trust boundary.
- Name the weak mitigation and why it fails.
- Name the enforceable control.
- Describe how the control is validated.
- End with residual risk and ownership.

## Phrases to reduce during final cleanup

These phrases are not banned, but they should not appear repeatedly:

- robust framework
- comprehensive approach
- holistic security
- best practice
- leverage guardrails
- seamless integration
- end-to-end solution
- it is important to note
- in today's rapidly evolving landscape

## Course-specific language to keep

- model proposes, system enforces
- retrieval is an access-control boundary
- prompts are behavior hints, not security controls
- evidence changes decisions
- accuracy is evidence, not assurance
- residual risk is a product decision, not a footnote

## Final voice review questions

1. Does this page teach a decision, or only list facts?
2. Does it distinguish model behavior from system enforcement?
3. Does it explain why the naive fix fails?
4. Does it connect to a lab, tabletop, or capstone artifact?
5. Does it ask students to validate a control?
6. Could a student repeat the page as an engineering recommendation?
""")

    write("modules/MODULE_HANDOFF_MAP.md", """
# Module handoff map

This map helps instructors teach the course as one continuous story rather than twelve independent topics.

| From | To | Handoff question |
|---|---|---|
| 01 | 02 | If AI security is system security, what system are we securing? |
| 02 | 03 | Once the architecture is mapped, how do we classify the failure modes? |
| 03 | 04 | Once risks are classified, which assumptions must be reviewed before implementation? |
| 04 | 05 | What changes when the application contains an LLM that receives untrusted text? |
| 05 | 06 | What changes when untrusted text comes from retrieved documents instead of the user? |
| 06 | 07 | What changes when the model can trigger tools or actions? |
| 07 | 08 | What changes when the model and its dependencies become promoted artifacts? |
| 08 | 09 | What information can the pipeline, model, retrieval layer, logs, and outputs expose? |
| 09 | 10 | How reliable is the model under manipulation, drift, or adversarial pressure? |
| 10 | 11 | How do we turn tests and observations into decision-grade evidence? |
| 11 | 12 | How do we combine evidence, controls, validation, and residual risk in a capstone report? |

## Instructor rule

Start every module by naming what the previous module made visible and what this module makes actionable.
""")

    write("instructor/teaching-the-course-narrative.md", """
# Teaching the course narrative

The instructor should repeat the same core story throughout the week: the model is one component in a larger security system. Students should leave with a way to reason about authority, data, artifacts, actions, outputs, validation, and residual risk.

## Daily narrative

### Day 1: Find the system

Students learn that AI security work starts by mapping the system, not by prompting the model. The expected artifacts are system context, trust boundaries, and initial abuse cases.

### Day 2: Watch text cross boundaries

Students observe direct injection, indirect injection, RAG leakage, and output handling. The key message is that untrusted text must not become authority.

### Day 3: Control actions and artifacts

Students move from model output to system action. They learn why tool authorization and model artifact promotion need independent controls.

### Day 4: Test reliability and privacy

Students study privacy leakage, adversarial robustness, and red team scoping. The key message is that test results must become evidence for a decision.

### Day 5: Integrate and recommend

Students write and present a capstone review. They are graded on evidence, root cause, controls, validation, residual risk, and leadership clarity.

## Instructor habits

- Ask where enforcement happens.
- Ask what evidence would change the decision.
- Ask what a naive fix would miss.
- Ask what remains risky after the control is applied.
- Avoid letting students stop at exploit demonstration.
""")

    write("instructor/final-voice-cohesion-review-guide.md", """
# Final voice and cohesion review guide

Use this guide during the final cleanup phase. Do not run this review while major content is still moving.

## Review order

1. Read the module README.
2. Read the student reading guide.
3. Read the lab path.
4. Read the deep-dive family of files.
5. Read the assessment or deliverable.
6. Remove repeated phrasing and tighten transitions.

## What to preserve

- The security engineering stance.
- The lab-quality standard.
- The BrokenPilot defense-in-depth lesson.
- The distinction between runnable attack labs and reasoning labs.
- The 40-hour delivery model.

## What to cut

- Repeated setup text.
- Generic statements about AI risk.
- Pages that restate the same framework without a decision.
- Temporary package notes after they have served their purpose.
- Apply scripts that are no longer needed after content is merged.
""")

    write("labs/LAB_DEBRIEF_LANGUAGE_GUIDE.md", """
# Lab debrief language guide

A lab debrief should not celebrate the exploit. It should convert the observation into an engineering decision.

## Use this sequence

1. What failed?
2. Which boundary was crossed?
3. Why did the naive fix fail?
4. Which control changed the security property?
5. How did the student validate the control?
6. What residual risk remains?
7. What would you tell an engineering lead?

## For attack labs

Attack labs need observable failure and observable fix. Students should show vulnerable behavior, enable or propose the control, and show the security property changes.

## For reasoning labs

Reasoning labs need a graded artifact. Students should produce a review, memo, scope, rubric, or remediation plan that can be assessed against anchors.

## Common debrief correction

If a student says, "the model was tricked," ask: which component accepted untrusted output as authority?
""")

    write("assessments/voice-and-cohesion-review-checklist.md", """
# Voice and cohesion review checklist

Use this checklist before the release-hardening phase.

## Module-level checks

- The module has a clear decision students must learn to make.
- The module connects to the previous and next module.
- The module names the relevant trust boundary.
- The module explains weak and strong controls.
- The module has a lab, tabletop, or graded deliverable.
- The module asks students to validate a control or recommendation.

## Lab-level checks

- Runnable labs show failure and fix.
- Reasoning labs produce a graded artifact.
- Each lab has a debrief path.
- Each lab has strong or weak anchors, or a rubric.
- Each lab connects to the capstone or course storyline.

## Voice checks

- The writing is direct and practical.
- The page avoids generic AI risk language.
- The page avoids repeated stock phrasing.
- The page sounds like course material, not product marketing.
- The page ends with a decision, deliverable, or validation question.
""")

    write("course-templates/final-voice-cohesion-review-template.md", """
# Final voice and cohesion review template

## Page reviewed

Path:

## Decision taught by this page

What engineering decision should the student be able to make after reading it?

## Boundary or control emphasized

Which trust boundary, authority boundary, artifact boundary, or output boundary matters here?

## Lab or deliverable connection

Which lab, tabletop, checkpoint, or capstone artifact does this page support?

## Repeated or generic phrasing to cut

List sentences or phrases to rewrite.

## Missing transition

What should this page connect to before or after?

## Final rewrite note

What one change would make the page sound more like a senior security engineer teaching the course?
""")

    write("release-notes/v1.1-dev-final-voice-cohesion-pass.md", """
# v1.1-dev final voice and cohesion pass

This development package adds course-wide voice and cohesion guidance before the final cleanup phase.

It does not clean generated artifacts, rewrite MkDocs navigation, or change CI. It creates the material needed to do those steps deliberately after content has stopped moving.

## Added

- Course storyline.
- Course voice and cohesion review.
- Module handoff map.
- Per-module cohesion notes.
- Instructor narrative guide.
- Lab debrief language guide.
- Voice and cohesion review checklist.
- Final voice review template.
""")

    for idx, (slug, title, language, decision, evidence) in enumerate(MODULES):
        write(f"modules/{slug}/cohesion-note.md", module_note(slug, title, language, decision, evidence, idx))
        append_once(
            f"modules/{slug}/README.md",
            "<!-- cohesion-note-link -->",
            f"""
<!-- cohesion-note-link -->

## Course cohesion note

For instructor handoff language and the module's place in the full course story, see [cohesion-note.md](cohesion-note.md).
""",
        )

    append_once(
        "README.md",
        "<!-- course-storyline-link -->",
        """
<!-- course-storyline-link -->

## Course storyline

The course is organized as one security engineering journey: map the AI system, identify trust boundaries, observe failure modes, design enforceable controls, validate those controls, document validation evidence, and communicate residual risk. See [COURSE_STORYLINE.md](COURSE_STORYLINE.md) and [COURSE_VOICE_AND_COHESION_REVIEW.md](COURSE_VOICE_AND_COHESION_REVIEW.md).
""",
    )

    append_once(
        "CLEANUP_BEFORE_RELEASE.md",
        "<!-- final-voice-cohesion-cleanup-reminder -->",
        """
<!-- final-voice-cohesion-cleanup-reminder -->

## Final voice and cohesion cleanup reminder

Before release, use COURSE_VOICE_AND_COHESION_REVIEW.md and instructor/final-voice-cohesion-review-guide.md to remove temporary scaffolding, reduce repeated generated-looking phrasing, and make the course read like a hand-curated professional training.
""",
    )

    print("\nApplied final voice and cohesion pass.")


if __name__ == "__main__":
    main()
