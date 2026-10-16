# Audit remediation, 16 October 2026

This note records the follow-up to the 15 October student-style course audit. The required 40-hour path remains BrokenPilot, the toy classifier, and the Module 08 evidence review. AIGoat remains optional.

## Changes made

- Enabled GitHub Dependabot vulnerability alerts and security update pull requests. API checks returned enabled for both. Enabled repository secret scanning and push protection; a fresh repository settings read returned enabled for both. GitHub left non-provider secret patterns disabled, so this note does not claim they are active.
- Raised the toy classifier's development `pytest` pin from 8.3.4 to 9.1.1. The newly enabled Dependabot alert identified the old pin and named 9.0.3 as the first patched version. All seven toy classifier tests passed with 9.1.1 in an isolated Python 3.12 container.
- Added a pinned AIGoat v2.0 Windows launcher, MCP-only Compose configuration, setup guide, and course links. The launcher uses a full WSL Git archive to preserve Windows-incompatible media filenames, verifies the upstream commit, generates a local secret, starts no Ollama service, and retains learner data on stop.
- Kept the backend off host ports and on an internal Docker network. The backend runs as UID 10001 with a read-only root filesystem, all capabilities dropped, `no-new-privileges`, and a limited process count. The frontend publishes only `127.0.0.1:3000`. A one-shot container with no network prepares the database volume's ownership.

## Validation

- The launcher's default WSL clone path, startup, stop, and restart passed on one Windows and Docker Desktop host. The first default-clone attempt exposed a shell-quoting bug; a direct WSL argument call fixed it and a new clone then started successfully.
- Frontend and API returned HTTP 200. The pinned source and image each contained 34 media files. All 32 image URLs returned image content, including the seven quoted filenames that were missing in the earlier pilot. The remaining files are a video and a license file.
- MCP03-2 and MCP07-1 each passed Level 0 and Level 1 comparisons before and after switching the backend to UID 10001. The behavior matched upstream integrity tests. The backend's attempted external TCP connection failed, and inspection showed no backend host port.
- Restart preserved the learner database user count, 9 before and 9 after. After validation, all lab containers stopped and no listener remained on 3000, 8000, or 11434.
- The complete release gate passed in an isolated Python 3.12 container: strict MkDocs build and edit-link check for 552 pages, 37 BrokenPilot tests, seven toy classifier tests, and five offline artifact-promotion tests.

## Remaining gates

- An independent first-time student and instructor pilot is still needed, with setup time and support interventions recorded. No volunteer is available yet.
- macOS and native Linux setups have not been validated. Keep the new live AIGoat path optional; the source-review exercise needs no installation.
- AIGoat's upstream Dockerfile installs broad dependency ranges and large packages. The tested backend image was about 3.8 GB, with additional space used by build cache. Rebuilding later can select different packages. The launcher pins upstream source, but does not create a locked upstream dependency set.
- AIGoat's training license permits the credited noncommercial self-study route described here. Paid use of their labs or prompts needs separate written permission from their maintainers.
