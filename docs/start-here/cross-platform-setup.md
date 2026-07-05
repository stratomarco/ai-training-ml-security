# Cross-Platform Setup

The course should be usable on Windows, macOS, and Linux. Use the command set that matches your environment.

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
uvicorn app.main:app --reload --host 127.0.0.1 --port 8010
```

macOS or Linux:

```bash
cd labs/brokenpilot/prototype-app
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
pytest
uvicorn app.main:app --reload --host 127.0.0.1 --port 8010
```

Open:

```text
http://127.0.0.1:8010
```

## DVAIA external lab dependency

Windows PowerShell:

```powershell
mkdir F:\ai-labs -ErrorAction SilentlyContinue
cd F:\ai-labs
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
