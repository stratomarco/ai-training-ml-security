# Release Tagging Guide

Use this guide for the `v1.3.0` release. Run it from a clean `main` checkout after the release pull request and its checks have passed. Never move an existing release tag.

## Final validation

```powershell
python scripts\run_final_release_gate.py
```

Optional explicit commands:

```powershell
python scripts\check_repo_structure.py
python scripts\check_content_readiness.py
python scripts\check_lab_targets.py
python scripts\check_workflow_validation_baseline.py
python scripts\check_release_candidate_phase8.py
python scripts\check_instructor_track.py
python scripts\check_final_release_artifacts.py
mkdocs build --strict
```

```powershell
cd labs\brokenpilot\prototype-app
pytest
```

```powershell
cd ..\..\toy-ml-attacks\toy-classifier-app
pytest
```

## Verify the release commit

```powershell
git switch main
git pull --ff-only
git status --short
git rev-parse HEAD
git ls-remote --tags origin v1.3.0
```

The tag lookup must return no existing `v1.3.0` tag. Confirm `VERSION`, the manifest, the changelog, and the release notes all say `v1.3.0`.

## Tag the verified commit

```powershell
git tag -a v1.3.0 -m "AI Training ML Security v1.3.0"
git push origin v1.3.0
```

## Publish and verify

```powershell
gh release create v1.3.0 --verify-tag --title "AI Training: ML Security v1.3.0" --notes-file release-notes/v1.3.0.md
gh release view v1.3.0
```

Confirm the GitHub release is neither a draft nor a prerelease and that its tag resolves to the tested `main` commit. Check that the separate Pages workflow succeeds and the published student route is reachable before describing the website as current.
