# Cross-Platform Setup

The course should be usable on Windows, macOS, and Linux. Use the command set that matches your environment.

For the full course, use Python 3.12. The toy classifier pins scikit-learn 1.5.2; a fresh Windows install with Python 3.14 attempted a source build and failed. Check `python --version` or `python3 --version` before creating a virtual environment.

## MkDocs local website preview

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts\sync_mkdocs_content.py
mkdocs serve
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 scripts/sync_mkdocs_content.py
mkdocs serve
```

Open:

```text
http://127.0.0.1:8000
```

## BrokenPilot runnable prototype

Windows PowerShell:

```powershell
cd labs\brokenpilot\prototype-app
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest
python run_lab.py --profile vulnerable
```

macOS or Linux:

```bash
cd labs/brokenpilot/prototype-app
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
pytest
python run_lab.py --profile vulnerable
```

Open:

```text
http://127.0.0.1:8010
```

The launcher binds to `127.0.0.1` and sets an explicit teaching profile. If another local service already uses port 8010, start with `python run_lab.py --profile vulnerable --port 8011` and open `http://127.0.0.1:8011`. Use the same port when following API examples. Stop the process before starting a different profile.

## Optional DVAIA comparison lab

BrokenPilot is the core runnable course lab. Use these commands only if you choose the external DVAIA comparison exercise.

Windows PowerShell:

```powershell
$labRoot = Join-Path $env:USERPROFILE 'ai-labs'
New-Item -ItemType Directory -Force $labRoot | Out-Null
Set-Location $labRoot
git clone https://github.com/airtasystems/DVAIA-Damn-Vulnerable-AI-Application.git
cd .\DVAIA-Damn-Vulnerable-AI-Application
git checkout 23c115252554caa445c0e6ba28641c1110c118e1
Copy-Item .env.example .env
.\run_docker.ps1 -Local
```

macOS or Linux:

```bash
mkdir -p ~/ai-labs
cd ~/ai-labs
git clone https://github.com/airtasystems/DVAIA-Damn-Vulnerable-AI-Application.git
cd DVAIA-Damn-Vulnerable-AI-Application
git checkout 23c115252554caa445c0e6ba28641c1110c118e1
cp .env.example .env
docker compose up --build
```

## Notes

- Keep DVAIA and BrokenPilot on localhost.
- Do not connect lab applications to real data, production credentials, production systems, or customer environments.
- If a command differs on your platform, update the setup docs so future students do not need to rediscover it.
