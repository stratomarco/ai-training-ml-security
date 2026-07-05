# DVAIA Setup

DVAIA is treated as an external lab dependency. This course does not copy, vendor, or maintain DVAIA.

Use the upstream DVAIA project instructions to install and run it locally. Then return to the course lab guides.

## Responsibility split

| This course provides | DVAIA provides |
|---|---|
| Learning objectives | Vulnerable runtime |
| Attack explanation | Target application |
| Lab walkthroughs | Hands-on behavior |
| Mitigation discussion | Scenario implementation |
| Reporting templates | Local practice environment |


## Known-good revision

The course was validated against this DVAIA commit:

```text
23c115252554caa445c0e6ba28641c1110c118e1
```

Recommended setup on Windows PowerShell:

```powershell
mkdir F:\ai-labs -ErrorAction SilentlyContinue
cd F:\ai-labs
git clone https://github.com/airtasystems/DVAIA-Damn-Vulnerable-AI-Application.git
cd .\DVAIA-Damn-Vulnerable-AI-Application
git checkout 23c115252554caa445c0e6ba28641c1110c118e1
Copy-Item .env.example .env
.\run_docker.ps1 -Local
```

Recommended setup on macOS or Linux:

```bash
mkdir -p ~/ai-labs
cd ~/ai-labs
git clone https://github.com/airtasystems/DVAIA-Damn-Vulnerable-AI-Application.git
cd DVAIA-Damn-Vulnerable-AI-Application
git checkout 23c115252554caa445c0e6ba28641c1110c118e1
cp .env.example .env
docker compose up --build
```

If the pinned revision fails because of upstream dependency changes, document the failure, test the current upstream revision, and update `docs/lab-setup/dvaia-validation.md` with the new commit and observed behavior.

## Before starting a DVAIA-based lab

1. Install DVAIA from the upstream project.
2. Start it locally.
3. Confirm the application is reachable in your browser.
4. Read the corresponding course lab guide.
5. Keep all testing inside your local lab environment.

## Course mapping

See [DVAIA Course Mapping](../labs/dvaia-guides/dvaia-course-mapping.md).
