# Package: final content audit pass

This package adds an end-to-end content audit before release cleanup.

It does not touch MkDocs strict mode, CI, or cleanup scripts. Its purpose is to decide whether the course is content-complete enough to enter cleanup/release hardening.

Apply:

```powershell
python scripts/apply_final_content_audit_pass.py
python scripts/check_final_content_audit_pass.py
```
