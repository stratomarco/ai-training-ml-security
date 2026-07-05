from __future__ import annotations

from pathlib import Path

ROOT = Path.cwd()

MODULES = {
    "01-security-engineering-for-ai": {
        "title": "Module 01: Security Engineering for AI",
        "problem": "Students often enter AI security by looking for AI-specific tricks. This module resets the frame: AI systems still fail through assets, trust boundaries, incentives, confused authority, weak defaults, and missing assurance. The AI part changes the shape of uncertainty, but it does not remove the need for security engineering.",
        "question": "What security property is at risk, who can influence the system, and where should enforcement live?",
        "decisions": [
            "Separate model behavior from system authority.",
            "Choose security properties that can be validated, not slogans such as safe or aligned.",
            "Decide which risks belong in architecture, policy, monitoring, or user training.",
            "Explain why usability and developer velocity matter to whether a control survives production."
        ],
        "lab": "Use the module exercise to turn a vague AI concern into assets, trust boundaries, abuse cases, controls, validation evidence, and residual risk. This is a reasoning lab. The graded artifact is the security argument, not a running exploit.",
        "strong": "A strong submission names the security property, explains the root cause, chooses controls that enforce that property, and states what evidence would change the decision.",
        "misreadings": [
            "Treating AI security as prompt wording instead of system design.",
            "Listing frameworks without using them to make a decision.",
            "Assuming the model can enforce permissions that the application did not enforce."
        ],
        "exit": "Write one sentence that starts with: The model may suggest, but the system must..."
    },
    "02-ml-system-architecture": {
        "title": "Module 02: ML System Architecture",
        "problem": "Most AI security failures are easier to understand when the system is drawn correctly. The module teaches students to see data sources, training paths, retrieval stores, tools, approval gates, identities, logs, and model outputs as one security-relevant system.",
        "question": "Where does untrusted data enter, where does authority get exercised, and where can a decision be reversed or audited?",
        "decisions": [
            "Identify the minimum diagram needed to reason about risk.",
            "Distinguish data flow from authority flow.",
            "Choose where to place enforcement so the model cannot bypass it.",
            "Decide what must be logged to reconstruct an AI-assisted action."
        ],
        "lab": "Use the architecture exercise to produce a trust-boundary diagram and a short risk review. This is foundational for BrokenPilot and for the later supply-chain evidence review.",
        "strong": "A strong submission makes the risky path visible: untrusted input, model interpretation, downstream authority, and the control that prevents unsafe execution.",
        "misreadings": [
            "Drawing only the model and ignoring retrieval, tools, identities, and deployment pipelines.",
            "Using a data-flow diagram as if it were an authorization design.",
            "Treating logs as evidence without asking whether the right fields are captured."
        ],
        "exit": "Point to one edge in your diagram where data crosses a trust boundary and one edge where authority is exercised."
    },
    "03-owasp-ml-top-10": {
        "title": "Module 03: OWASP ML Security Top 10",
        "problem": "This module turns OWASP categories into engineering judgment. The point is not to memorize a list. The point is to recognize when a failure is about input manipulation, poisoned data, model theft, output integrity, supply-chain weakness, or excessive agency, and then select the right control family.",
        "question": "Which failure mode is present, and what evidence would prove that the proposed control changes the security property?",
        "decisions": [
            "Map an observed behavior to a risk category without forcing a poor fit.",
            "Distinguish model-level attacks from application-level authorization failures.",
            "Decide whether a classifier can safely be used as a hard gate.",
            "Choose validation evidence for evasion, poisoning, extraction, and output integrity."
        ],
        "lab": "Use the toy-classifier app for observable classical ML attacks. BrokenPilot is not the right target for these attacks. The graded artifact is a short attack-to-control mapping with test evidence and residual risk.",
        "strong": "A strong submission shows before and after behavior, explains why the naive fix is insufficient, and recommends whether the model should be advisory, gated, monitored, or backed by fallback review.",
        "misreadings": [
            "Using BrokenPilot for classical ML attacks just because it is the main app.",
            "Reporting an evasion example without explaining the deployment decision it affects.",
            "Assuming accuracy is the same thing as security assurance."
        ],
        "exit": "Pick one OWASP ML category and write the smallest test that would demonstrate a control improving it."
    },
    "04-biml-architectural-risk-analysis": {
        "title": "Module 04: BIML Architectural Risk Analysis",
        "problem": "BIML-style analysis asks students to reason before testing. The goal is to find structural security risk early, when it is cheaper to change the architecture than to patch symptoms after launch.",
        "question": "What can go wrong because of the architecture, even if the model appears to perform well in normal tests?",
        "decisions": [
            "Choose which components and trust boundaries deserve review depth.",
            "Turn abuse cases into architecture changes, not generic warnings.",
            "Prioritize risks by consequence, exposure, and control feasibility.",
            "Decide which assumptions must be validated before launch."
        ],
        "lab": "Use the DocOps architecture review lab as a reasoning lab. The deliverable is an architecture risk review with clear findings, recommended controls, and explicit residual risk.",
        "strong": "A strong submission connects a system path to a failure mode, names a concrete control, and explains how the team would know the control works.",
        "misreadings": [
            "Treating the exercise like a checklist completion task.",
            "Writing risk statements that do not point to a system path.",
            "Proposing policy-only fixes for architecture-level failures."
        ],
        "exit": "Write one architecture finding in this shape: path, failure, consequence, control, validation."
    },
    "05-llm-application-security": {
        "title": "Module 05: LLM Application Security",
        "problem": "This module teaches the difference between text generation and authority. Prompt injection matters because untrusted text can be mistaken for instruction. Insecure output handling matters because model text can be passed into a downstream context that has different safety rules.",
        "question": "Where is untrusted text being treated as instruction or as safe output for another interpreter?",
        "decisions": [
            "Separate direct prompt injection from indirect prompt injection by entry point, not by root cause.",
            "Decide what the model is allowed to influence and what must be enforced outside the model.",
            "Choose output encoding or validation based on the downstream context.",
            "Reject controls that only make the prompt sound stricter."
        ],
        "lab": "Use BrokenPilot for direct injection, indirect injection, and output handling. DVAIA can remain optional enrichment. The graded artifact should show vulnerable behavior, controlled behavior, the root cause, and a control that lives at the right boundary.",
        "strong": "A strong submission explains why marker detection is a teaching stand-in, then recommends instruction/data separation, privilege reduction, contextual output handling, and validation evidence.",
        "misreadings": [
            "Thinking the attack is the specific marker string rather than the trust-boundary failure.",
            "Calling escaped output safe in every context.",
            "Treating prompt hardening as an authorization control."
        ],
        "exit": "Name one input boundary and one output boundary in the lab, then state the correct control for each."
    },
    "06-rag-security": {
        "title": "Module 06: RAG Security and Indirect Prompt Injection",
        "problem": "RAG changes the attack surface by making retrieved content part of the model context. Retrieval is not just search quality. It is an authorization and trust decision. A bad RAG design can leak data, follow hostile document instructions, or give the model context it should never see.",
        "question": "Who is allowed to retrieve this content, why is it trusted, and what should the model be allowed to do with it?",
        "decisions": [
            "Apply authorization before retrieval results enter model context.",
            "Separate source trust from semantic relevance.",
            "Decide how to represent document classification, tenant, role, and user-specific access.",
            "Validate that restricted content is unavailable to unauthorized users, not merely hidden in the UI."
        ],
        "lab": "Use BrokenPilot retrieval authorization and indirect prompt-injection flows. The old paper RAG lab should point to the runnable path instead of duplicating it.",
        "strong": "A strong submission includes evidence that unauthorized retrieval is blocked before model context construction, explains the root cause as authorization after retrieval or missing retrieval authorization, and adds a note on residual risk such as logging, cache, or embedding metadata leakage.",
        "misreadings": [
            "Assuming vector similarity is a security decision.",
            "Filtering final answers while still placing restricted documents in context.",
            "Treating all internal documents as equally trusted."
        ],
        "exit": "Explain why the correct place to enforce retrieval authorization is before model invocation."
    },
    "07-agent-tool-security": {
        "title": "Module 07: Agent and Tool Security",
        "problem": "Agents become risky when model-generated intent can trigger tools with real authority. The memorable lesson is defense in depth: memory or retrieved content may steer the agent, but the tool broker must still authorize the action against the target object.",
        "question": "What action is being requested, who requested it, what target object is affected, and who authorizes execution?",
        "decisions": [
            "Distinguish model intent from tool execution authority.",
            "Define per-tool, per-user, and per-target authorization checks.",
            "Decide which actions need approval, rollback, and audit evidence.",
            "Handle memory as untrusted or reviewed context, not as authority."
        ],
        "lab": "Use BrokenPilot tool authorization, approval, memory poisoning, and audit flows. This remains the reference attack lab for the course.",
        "strong": "A strong submission shows the same malicious intent under different controls, explains the root cause as model intent being confused with execution authority, and explains why one layer can fail while another prevents execution.",
        "misreadings": [
            "Assuming a better system prompt can enforce tool policy.",
            "Checking only user role and not the target object tenant.",
            "Forgetting rollback and audit in the remediation plan."
        ],
        "exit": "Write the authorization rule for closing a ticket in one precise sentence."
    },
    "08-secure-mlops-supply-chain": {
        "title": "Module 08: Secure MLOps and AI Supply Chain",
        "problem": "MLOps supply-chain security risk is usually visible in evidence: missing provenance, mutable artifacts, unpinned dependencies, weak promotion gates, unsafe notebooks, and registry metadata that cannot prove what was trained, tested, approved, and deployed.",
        "question": "Can the team prove where this model came from, what data and code produced it, who approved it, and how to roll it back?",
        "decisions": [
            "Decide which artifacts require hashes, signatures, review, and promotion gates.",
            "Separate experiment convenience from production promotion requirements.",
            "Choose what evidence is required before a model moves between environments.",
            "Explain supply-chain risk to leadership without exaggerating it into a generic breach story."
        ],
        "lab": "Use the MLOps evidence-pack review. It is intentionally a reasoning lab because realistic supply-chain review is evidence review, not a fake pipeline demo.",
        "strong": "A strong submission cites specific evidence-pack files, identifies concrete integrity gaps, recommends promotion controls, and states what residual risk remains after the controls.",
        "misreadings": [
            "Treating accuracy metrics as deployment approval.",
            "Fixing only dependencies while ignoring artifact identity and promotion rules.",
            "Equating a registry entry with trustworthy provenance."
        ],
        "exit": "Name three pieces of evidence you would require before production promotion."
    },
    "09-privacy-attacks": {
        "title": "Module 09: Privacy Attacks and Data Protection",
        "problem": "Privacy and security failures in AI systems often come from data exposure paths: retrieval leakage, logs, overbroad access, training data memorization, or inference about membership and sensitive attributes. This module keeps privacy concrete by tying each failure to data handling and access decisions.",
        "question": "What personal or sensitive information can be inferred, retrieved, logged, or reconstructed, and who can access it?",
        "decisions": [
            "Distinguish cross-tenant retrieval leakage from model memorization and membership inference.",
            "Decide which privacy failures can be demonstrated runnably and which are better reviewed as tabletop risks.",
            "Choose minimization, authorization, logging, retention, and monitoring controls.",
            "State residual risk honestly when privacy cannot be reduced to zero."
        ],
        "lab": "Use BrokenPilot for cross-tenant privacy leakage. Use the membership-inference tabletop for reasoning about privacy attacks that should not be forced into the LLM app.",
        "strong": "A strong submission shows the leaked fake fragment, proves retrieval authorization changes the privacy property, then discusses secondary leakage through logs and operational access.",
        "misreadings": [
            "Calling fake training secrets harmless and missing the real privacy property.",
            "Fixing answer filtering while leaving restricted context retrievable.",
            "Ignoring logs as a second data exposure surface."
        ],
        "exit": "Explain how retrieval authorization and log minimization protect different privacy surfaces."
    },
    "10-adversarial-ml-robustness": {
        "title": "Module 10: Adversarial ML and Robustness",
        "problem": "This module teaches students not to confuse benchmark accuracy with security assurance. Robustness is about behavior under stress, manipulation, drift, and uncertainty. The engineering decision is often whether a model can safely act as a hard gate.",
        "question": "What happens when inputs, labels, thresholds, or operating conditions shift away from the clean validation set?",
        "decisions": [
            "Design tests for evasion, poisoning, threshold tampering, and drift.",
            "Decide when a classifier should be advisory rather than authoritative.",
            "Choose fallback behavior when confidence, input quality, or distribution is questionable.",
            "Explain why a single evasion example is evidence of a class of risk, not the whole risk story."
        ],
        "lab": "Use the toy-classifier app for observable evasion and poisoning. Keep poisoning/backdoor tabletop work as reasoning where the question is control design and residual risk.",
        "strong": "A strong submission reports before and after behavior, explains the deployment implication, and recommends monitoring, fallback, retraining controls, and validation tests.",
        "misreadings": [
            "Treating word swaps as a magic trick instead of a proxy for input manipulation risk.",
            "Reporting confidence scores without tying them to an operational decision.",
            "Assuming retraining alone fixes poisoning risk."
        ],
        "exit": "State whether the toy classifier should be a hard authorization gate, and justify the answer."
    },
    "11-ai-red-team-methodology": {
        "title": "Module 11: AI Red Team Methodology",
        "problem": "AI red teaming should produce decision-grade security evidence, not a pile of clever prompts. This module teaches scope, hypotheses, safety constraints, evidence capture, finding quality, and remediation validation.",
        "question": "What decision will this test inform, and what evidence would be enough to change that decision?",
        "decisions": [
            "Choose a scope that is useful, bounded, and safe.",
            "Separate attack demonstration from exploit celebration.",
            "Write findings with evidence, root cause, control, validation, and residual risk.",
            "Decide which issues belong in the capstone report and which are observations."
        ],
        "lab": "Use BrokenPilot for attack-chain practice and use the scoping tabletop for planning quality. The graded output is a report that helps a system owner decide what to fix first.",
        "strong": "A strong submission is boring in the best way: reproducible evidence, clear scope, root cause, control recommendations, and no inflated claims.",
        "misreadings": [
            "Confusing creativity with risk severity.",
            "Writing a finding that does not include validation steps.",
            "Ignoring safety limits and test authorization."
        ],
        "exit": "Rewrite one weak finding into evidence, root cause, control, validation, and residual risk."
    },
    "12-capstone-brokenpilot": {
        "title": "Module 12: BrokenPilot Capstone",
        "problem": "The capstone asks students to combine the course into a practical security review of an AI agent system. It should not assess every module through the same runnable target. BrokenPilot demonstrates LLM, RAG, agent, privacy, and red-team chains. MLOps, membership inference, and adversarial ML stay as supporting tabletop or separate-lab evidence.",
        "question": "What should the system owner fix before launch, what evidence supports that recommendation, and what residual risk remains?",
        "decisions": [
            "Choose a small number of high-value findings rather than a long list of observations.",
            "Connect each finding to a security property and system path.",
            "Recommend controls that can be implemented and validated.",
            "Make a launch, limited pilot, or delay recommendation that leadership can act on."
        ],
        "lab": "Use the BrokenPilot capstone checkpoints. The report should integrate runnable evidence, reasoning-lab lessons, remediation backlog, and executive communication.",
        "strong": "A strong final report tells a coherent story: what was tested, what failed, the root cause, why it matters, how to fix it, how to prove the fix, and what risk remains.",
        "misreadings": [
            "Trying to include every module as a runnable BrokenPilot issue.",
            "Reporting screenshots without root cause or remediation validation.",
            "Saving all writing for the final day instead of using checkpoints."
        ],
        "exit": "Write the executive recommendation first, then check whether the evidence in the report actually supports it."
    },
}

COURSE_READING_FLOW = """# Student Reading Flow

This course is reading-first and lab-supported. Students should not try to read every file as if the repository were a linear book. Each module now has a student reading guide that explains what the module is really about, what decisions students must learn to make, which lab path applies, and what a strong submission looks like.

## How to study a module

1. Read the module README for the topic and scope.
2. Read `student-reading-guide.md` before the deep dive or lab.
3. Use the guide to identify the core security decision in the module.
4. Run the lab or complete the reasoning exercise.
5. Complete the deliverable using evidence, root cause, control, validation, and residual risk.

## How not to study the course

Do not treat the modules as a framework memorization exercise. Do not chase every reference before doing the lab. Do not collect attack screenshots without explaining the engineering decision they support.

## Reading to lab transfer

Every module should answer four questions:

- What security property is at risk?
- Where is the trust boundary or authority boundary?
- What control changes the security property?
- What evidence would convince a system owner that the control works?

## Instructor use

Instructors can open each module with the "question to keep in mind" from the reading guide and close it with the exit ticket. This gives the 40-hour course a consistent rhythm without adding more lecture time.
"""

EDITORIAL_GUIDE = """# Content Quality Editing Guide

This guide is for the final cleanup phase and for future contributors. It is intentionally practical: the goal is to make the course read like a security engineer teaching a serious class, not like a generated reference dump.

## Voice

Prefer direct, concrete prose. Use examples from the labs. Name the decision the student must make. Avoid generic claims such as "this is important" unless the next sentence explains why.

## Good module prose

Good module prose has a point of view:

- It tells the student what problem they are learning to solve.
- It distinguishes concepts that are often confused.
- It names weak controls and explains why they are weak.
- It connects reading to a lab or deliverable.
- It ends with a decision, not just a list of terms.

## Phrases to reduce in the final cleanup

During release cleanup, search for repetitive generated-sounding patterns and rewrite them manually where they add no value:

- "comprehensive overview"
- "robust framework"
- "critical importance"
- repeated module sections that use the same sentence structure

Do not mechanically replace words. Rewrite only when the surrounding paragraph becomes clearer.

## What to keep

Keep the strong engineering spine: McGraw, Anderson, Shostack, BIML, OWASP, NIST, MITRE ATLAS, and the lab evidence model. The cleanup should improve readability without weakening the security argument.
"""

TRANSFER_CHECKLIST = """# Reading to Lab Transfer Checklist

Use this checklist when reviewing student work or editing a module.

## Before the lab

- The student can name the security property at risk.
- The student can point to the relevant trust boundary or authority boundary.
- The student understands whether the lab is runnable or reasoning-based.
- The student knows the graded artifact before starting.

## During the lab

- Observable labs show vulnerable behavior and controlled behavior.
- Reasoning labs use concrete evidence and end in a decision.
- The student records evidence, not just conclusions.
- The student identifies at least one naive fix and explains why it is weak.

## After the lab

- The student explains root cause.
- The student proposes an implementable control.
- The student states validation steps.
- The student states residual risk.
- The student can explain the finding to a system owner without jargon.
"""

INSTRUCTOR_GUIDE = """# Instructor Guide: Teaching From the Reading Guides

The student reading guides are not extra homework. They are the connective tissue between module content, labs, and assessment.

## Opening a module

Start with the module question. Ask students to answer it quickly before they read deeply. Return to the same question after the lab.

## During lecture

Avoid walking through every bullet in the module. Use the reading guide to decide what to emphasize:

- the central failure mode
- the boundary where enforcement belongs
- the naive fix that fails
- the graded deliverable

## During labs

For runnable labs, keep students focused on the security property changing between vulnerable and controlled modes. For reasoning labs, keep students focused on evidence quality and control feasibility.

## Closing a module

Use the exit ticket from the guide. It should take five minutes. If students cannot answer it, they are not ready for the next module even if they completed the steps.

## Grading calibration

When grading, prefer a short answer with clear evidence, root cause, control, validation, and residual risk over a long answer that repeats framework language without making a decision.
"""

TEMPLATE = """# Module Reading Notes Template

Module:

## The core problem

What problem is this module teaching me to solve?

## Security property

What security property is at risk?

## Boundary

Where is the relevant trust boundary, authority boundary, or data boundary?

## Naive fix

What weak or naive fix might someone propose?

Why is it insufficient?

## Strong control

What control changes the security property?

Where should it be enforced?

## Evidence

What lab evidence, design evidence, or review evidence supports the finding?

## Validation

How would I prove the control works?

## Residual risk

What risk remains after the control?

## One sentence for leadership

Write the finding in one sentence a system owner can act on.
"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"wrote: {path.relative_to(ROOT)}")


def append_once(path: Path, marker: str, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if marker in current:
        return
    sep = "\n\n" if current.strip() else ""
    path.write_text(current.rstrip() + sep + text.rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"updated: {path.relative_to(ROOT)}")


def module_guide(slug: str, data: dict) -> str:
    decisions = "\n".join(f"- {item}" for item in data["decisions"])
    misreadings = "\n".join(f"- {item}" for item in data["misreadings"])
    return f"""# Student Reading Guide: {data['title']}

## What this module is really about

{data['problem']}

## Question to keep in mind

{data['question']}

## Decisions students must learn to make

{decisions}

## Lab or exercise connection

{data['lab']}

## What a strong submission looks like

{data['strong']}

## Common misreadings to avoid

{misreadings}

## Exit ticket

{data['exit']}
"""


def main() -> None:
    for slug, data in MODULES.items():
        module_dir = ROOT / "modules" / slug
        write(module_dir / "student-reading-guide.md", module_guide(slug, data))
        readme = module_dir / "README.md"
        append_once(
            readme,
            "<!-- student-reading-guide-link -->",
            """<!-- student-reading-guide-link -->

## Student reading guide

Before starting the lab or exercise, read [student-reading-guide.md](student-reading-guide.md). It explains the module's core security decision, lab path, common mistakes, and exit ticket.""",
        )

    write(ROOT / "docs" / "start-here" / "student-reading-flow.md", COURSE_READING_FLOW)
    write(ROOT / "CONTENT_QUALITY_EDITING_GUIDE.md", EDITORIAL_GUIDE)
    write(ROOT / "labs" / "READING_TO_LAB_TRANSFER_CHECKLIST.md", TRANSFER_CHECKLIST)
    write(ROOT / "instructor" / "teaching-from-reading-guides.md", INSTRUCTOR_GUIDE)
    write(ROOT / "course-templates" / "module-reading-notes-template.md", TEMPLATE)

    append_once(
        ROOT / "CLEANUP_BEFORE_RELEASE.md",
        "<!-- content-quality-cleanup-reminder -->",
        """<!-- content-quality-cleanup-reminder -->

## Content voice cleanup reminder

Before release, do a manual editing pass for generated-looking repetition. Keep the technical material and lab evidence, but reduce generic phrasing, repeated section intros, and temporary apply/check scripts that were only used during development.""",
    )

    append_once(
        ROOT / "README.md",
        "<!-- content-quality-reading-flow-note -->",
        """<!-- content-quality-reading-flow-note -->

## Study flow note

Each module includes a `student-reading-guide.md` file. Use it before the deep dive or lab to understand the core security decision, the lab modality, the expected deliverable, and the exit ticket for the module.""",
    )

    write(
        ROOT / "release-notes" / "v1.1-dev-content-quality-reading-flow-pass.md",
        """# v1.1-dev Content Quality Reading Flow Pass

This development package adds student reading guides for all twelve modules and connects module reading to labs, deliverables, and exit tickets.

It does not change MkDocs strict navigation or CI. Those remain release-hardening tasks after content and labs stabilize.
""",
    )

    print("\nApplied content-quality reading-flow pass.")


if __name__ == "__main__":
    main()
