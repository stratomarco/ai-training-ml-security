# Package: Current BrokenPilot Final Report

Apply from the repository root:

```powershell
python scripts\apply_current_brokenpilot_final_report.py
python scripts\check_current_brokenpilot_final_report.py
```

This package adds a current complete BrokenPilot capstone final report aligned to the latest labs:

- direct prompt injection;
- insecure output handling;
- cross-tenant privacy leakage;
- tool authorization;
- memory poisoning and defense in depth.

It does not touch MkDocs strict mode, CI, or cleanup scripts.
