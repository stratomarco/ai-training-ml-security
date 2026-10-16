# Optional AIGoat MCP labs on Windows

This setup runs two AIGoat v2.0 exercises, `mcp03-2` and `mcp07-1`, as an optional extension to Module 07. [AIGoat](https://github.com/AISecurityConsortium/AIGoat/releases/tag/v2.0) is maintained by AISecurityConsortium. This course is independent and is not endorsed by them. Its training content is [CC BY-NC-SA 4.0](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/TRAINING_LICENSE.md), so this route is for noncommercial self-study. Read the license before using it in another setting.

The course launcher fetches upstream source into Ubuntu on WSL, verifies commit `e1c538badb93c6c1c2307096ab5d709a9ee0fe55`, and builds its images through Docker Desktop. Keeping the checkout in WSL preserves seven media filenames that Windows cannot store. Docker Desktop's WSL integration does not need to be enabled because the launcher calls its Windows `docker.exe` from WSL. The two selected MCP exercises do not use an Ollama model, so this Compose setup starts no Ollama service and downloads no model. Other AIGoat labs are outside this supported setup.

## Before starting

- Windows with WSL and an Ubuntu distribution named `Ubuntu-22.04`, or pass your distribution name with `-Distro`.
- Docker Desktop running Linux containers. Allow substantial free disk space and time for the first build: the tested backend image was about 3.8 GB, and build cache needs additional space. Upstream installs large AI dependencies even though these two exercises do not use a model.
- Git and tar in the Ubuntu distribution. GitHub access is needed for the initial clone and dependency downloads for the initial Docker builds.
- A private, trusted machine. Use only fake lab data and demo credentials. The app contains intentional vulnerabilities.

Open PowerShell in the course repository and run:

```powershell
.\scripts\aigoat-mcp-windows.ps1 -Action start
```

If script execution is blocked by your PowerShell policy, run the same script in a PowerShell session you have configured to permit local scripts. Do not copy a bypass command from an untrusted source.

The first run creates an ignored `.local/aigoat-mcp/config.yml` with a random local session secret. It retains the same secret and lab database on later starts. The source and media remain in WSL, outside this course repository. Once the containers report healthy, open <http://127.0.0.1:3000> and use the upstream demo account described in [AIGoat's README](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/README.md). Only port 3000 is published, and it is bound to loopback. The backend runs without root privileges on an internal Docker network, with a read-only filesystem and no Linux capabilities. The initial build still downloads upstream code and packages.

Check that the browser can load the storefront and product images. The selected exercises are in AIGoat's MCP lab section. For each one, reset the lab before comparing Level 0 with its defended level. Record the advertised tool, actual tool call, returned data, control decision, and residual risk in the [MCP trust-boundary review](mcp-trust-boundary-review.md). Do not use real credentials or connect the app to another network.

To inspect the containers or stop the lab:

```powershell
.\scripts\aigoat-mcp-windows.ps1 -Action status
.\scripts\aigoat-mcp-windows.ps1 -Action stop
```

Stopping retains the local lab database and Docker images so the next start is faster. If a build or launch fails, stop the stack, copy the error message and the output of `docker compose -f labs/aigoat-guides/docker-compose.mcp.yml ps`, and report your Docker Desktop, Windows, and WSL versions. Keep local secrets out of the report.

This is an optional Windows route. The [source-review exercise](mcp-trust-boundary-review.md) remains usable without Docker. A separate first-time learner pilot is still needed before this becomes a required course path.
