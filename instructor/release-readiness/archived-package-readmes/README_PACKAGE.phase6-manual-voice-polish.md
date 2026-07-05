# v1.1-dev Release Cleanup Phase 6: Manual Voice Polish

This package applies a conservative final voice cleanup before MkDocs/navigation work.

It does not broadly rewrite course content. It removes package-era lines from student-facing Markdown, refreshes the final voice guidance, and records what remains before the release candidate.

## Apply

```powershell
cd C:\Dev\ai-training-ml-security
python scripts\apply_release_cleanup_phase6_manual_voice_polish.py
python scripts\check_release_cleanup_phase6_manual_voice_polish.py
```

Then run the normal validation baseline and lab tests.
