# Release Checklist

Use this checklist before tagging the first release.

## Repository health

- [ ] `README.md` accurately describes the project.
- [ ] `syllabus.md` matches the current twelve-module course.
- [ ] `course-map.md` links modules, labs, templates, and assessments correctly.
- [ ] `references.md` contains only useful, defensible references.
- [ ] `project-backlog.md` separates completed work from future work.
- [ ] `CHANGELOG.md` is up to date.
- [ ] `VERSION.md` shows the intended release version.
- [ ] `ROADMAP.md` describes post-v1.0 direction.

## Module completeness

For every module from `01` to `12`, confirm:

- [ ] `README.md`
- [ ] `slides.md`
- [ ] `instructor-notes.md`
- [ ] `student-handout.md`
- [ ] exercise file
- [ ] `checklist.md`
- [ ] `quiz.md`
- [ ] `references.md`

## Content quality

- [ ] The course avoids claiming that prompts are security boundaries.
- [ ] The course ties AI risks back to security engineering.
- [ ] Labs are framed as controlled, local, fake-data training exercises.
- [ ] No lab tells students to attack systems they do not own.
- [ ] Mitigations are practical and engineering-oriented.
- [ ] Every major module includes both attack and defense.
- [ ] Executive communication and residual risk are included.

## Licensing

- [ ] Confirm final license strategy.
- [ ] Confirm third-party content was not copied without permission.
- [ ] Confirm DVAIA and other third-party labs are linked rather than copied.
- [ ] Confirm whether `LICENSE.md` is enough or whether formal license files should be added.

## GitHub readiness

- [ ] Issue templates render correctly.
- [ ] Pull request template renders correctly.
- [ ] Security policy is acceptable.
- [ ] Code of conduct is acceptable.
- [ ] Repository description and topics are set.
- [ ] Repository visibility is correct: private or public.

Suggested GitHub topics:

```text
ml-security ai-security llm-security rag-security agent-security appsec threat-modeling adversarial-ml secure-mlops owasp biml mitre-atlas nist-ai-rmf
```

## Release commands

After review:

```powershell
git status
git add .
git commit -m "Prepare v1.0 release candidate"
git tag -a v1.0.0 -m "AI Training ML Security v1.0.0"
git push
git push origin v1.0.0
```

Create the GitHub release using:

```text
docs/releases/v1.0.0.md
```

## Post-release

- [ ] Create issues from `ROADMAP.md`.
- [ ] Validate DVAIA labs locally.
- [ ] Start BrokenPilot implementation planning.
- [ ] Add optional diagrams and examples.
