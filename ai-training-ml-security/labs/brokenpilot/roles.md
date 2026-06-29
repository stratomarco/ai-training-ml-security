# BrokenPilot Roles and Personas

## Legitimate user roles

| Role | Normal use | Expected access |
|---|---|---|
| Engineer | Search docs, read own team tickets, create tickets, ask service questions. | Team docs, public engineering docs, own team tickets. |
| SRE | Summarize incidents, update incident tickets, query service config. | Incident docs, operational tickets, service metadata. |
| Security engineer | Review incident/security tickets, search security docs. | Security docs, security tickets, redacted operational data. |
| Support engineer | Read customer escalation tickets and create internal follow-ups. | Support tickets and approved customer context. |
| Engineering manager | Read summaries, status, and team metrics. | Team-level summaries and non-sensitive ticket metadata. |
| Admin | Manage BrokenPilot configuration. | Administrative settings, but still subject to audit and change control. |

## Attacker personas

| Persona | Capability | Goal |
|---|---|---|
| Curious employee | Has a normal internal account. | Access data outside their team. |
| Malicious insider | Has legitimate internal access and intent to abuse it. | Exfiltrate data, tamper with tickets, poison memory/docs. |
| Compromised employee account | Attacker controls a normal employee session. | Use BrokenPilot as a confused deputy. |
| External attacker through ticket/email/doc | Cannot log in, but can influence content ingested by BrokenPilot. | Indirect prompt injection or poisoned retrieval. |
| Supply-chain attacker | Can influence a dependency, model artifact, adapter, or document source. | Modify behavior or extract secrets. |
| Over-trusting operator | Not malicious; relies too much on BrokenPilot output. | Accidentally causes operational impact. |

## Permission assumptions

BrokenPilot should not have a single broad service account that can read and write everything.

Instead, target permissions should be based on:

- User identity.
- User role.
- Team membership.
- Target object.
- Requested action.
- Risk tier.
- Approval state.
- Current incident/change context.

## Abuse assumptions

Students should assume attackers may try to:

- Ask the model to ignore policy.
- Hide instructions inside documents.
- Create tickets that contain malicious instructions.
- Poison memory with persistent instructions.
- Cause the agent to update ticket priority/status incorrectly.
- Retrieve documents from another team.
- Extract incident summaries that include sensitive details.
- Use the assistant to generate misleading operational messages.
- Abuse expensive model calls or tool loops.

## Important teaching point

A valid user session is not enough to authorize an AI action.

The backend must ask:

1. Who is the real user?
2. What action is being requested?
3. What object is being affected?
4. Is the user allowed to perform this action directly?
5. Is the model merely proposing the action or causing it?
6. Does this action require confirmation or approval?
7. Can the action be audited and rolled back?
