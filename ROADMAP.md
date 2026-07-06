# Roadmap

This roadmap describes work after the first complete curriculum release.

## v1.0  -  Complete Markdown curriculum

Goal: first complete teachable release.

Included:

- Twelve complete modules.
- BrokenPilot capstone.
- Lab wrappers.
- Templates.
- Instructor support material.
- Assessment material.
- Release readiness files.

Not included:

- Custom runnable BrokenPilot application.
- Validated DVAIA installation instructions.
- Rendered slide decks.

## v1.1  -  Lab validation release

Goal: make the lab experience more concrete.

Planned work:

- Install and test DVAIA locally.
- Add confirmed setup instructions.
- Add expected outputs for selected labs.
- Add troubleshooting notes.
- Add lab difficulty ratings.
- Add instructor reset notes.

## v1.2  -  BrokenPilot runnable prototype

Goal: create the first local vulnerable capstone application.

Planned work:

- Minimal web app.
- Fake docs, tickets, users, and configuration records.
- RAG retrieval with intentional authorization gaps.
- Agent tools with intentional over-permissioning.
- Memory poisoning scenario.
- Basic logging.
- Docker Compose.
- Instructor reset script.

## v1.3  -  Secure reference implementation

Goal: show vulnerable and hardened variants side by side.

Planned work:

- Policy checks outside the model.
- Tool permission matrix enforcement.
- Retrieval authorization.
- Human approval gates.
- Audit logs.
- Rate limits and budget controls.
- Secure memory handling.
- Evidence of mitigations.

## v1.4  -  Instructor delivery pack

Goal: improve teachability.

Planned work:

- Timing plans for 2-hour, half-day, one-day, two-day, and twelve-week delivery.
- More facilitator notes.
- More discussion prompts.
- Sample student answers.
- Sample final reports.
- Executive briefing variant.

## v2.0  -  Full hands-on training environment

Goal: combine curriculum, labs, and capstone into a mature training platform.

Planned work:

- Runnable BrokenPilot lab.
- DVAIA integration notes.
- Optional local LLM mode.
- Optional API-provider mode.
- Test data generator.
- Instructor dashboard or grading support.
- Full release documentation.


## v1.1  -  Website Edition

Goal: turn the Markdown repository into a browsable course website.

Planned/completed scope:

- Add MkDocs Material.
- Add local preview instructions.
- Add GitHub Pages deployment workflow.
- Add Start Here section.
- Add lab setup and DVAIA prerequisite pages.
- Expose modules, labs, templates, instructor notes, and assessments through site navigation.

Future improvement:

- Decide whether `docs/` becomes the single source of truth, or whether a small sync script should preserve root-level compatibility.


## v1.1-dev  -  Quality and testability focus

Do not tag a new release until the course is more testable and instructor-ready.

Priority order:

1. Validate DVAIA locally and document exact setup notes for Modules 05–07 and 11.
2. Design and then build a minimal runnable BrokenPilot prototype.
3. Add worked student examples for BrokenPilot deliverables.
4. Add delivery format guidance for 2-hour, half-day, 1-day, 2-day, and 12-week formats.
5. Add concrete control deliverables so students must produce implementable fixes.
6. Deepen Module 10 with worked adversarial ML examples.
7. Continue website improvements only after lab testability improves.

The next release should be based on a measurable improvement in student experience, not only documentation structure.

## Future roadmap

- [v2 roadmap: agentic systems, MCP, and automated security evaluation](roadmaps/v2-roadmap.md)
