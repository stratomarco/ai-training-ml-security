# Model Registry Access Control Template

## Registry scope

| Field | Value |
|---|---|
| Registry name |  |
| Environment |  |
| Owner |  |
| Criticality |  |

## Roles

| Role | Description |
|---|---|
| Viewer | Can view metadata and approved artifacts. |
| Contributor | Can register candidate artifacts. |
| Reviewer | Can review metadata and evaluation evidence. |
| Approver | Can approve stage promotion. |
| Deployer | Can deploy approved production artifacts. |
| Registry admin | Can manage registry configuration; should not bypass approval casually. |

## Permission matrix

| Action | Viewer | Contributor | Reviewer | Approver | Deployer | Admin | Notes |
|---|---|---|---|---|---|---|---|
| View model metadata |  |  |  |  |  |  |  |
| Download artifact |  |  |  |  |  |  |  |
| Register candidate model |  |  |  |  |  |  |  |
| Modify metadata |  |  |  |  |  |  |  |
| Promote to staging |  |  |  |  |  |  |  |
| Promote to production |  |  |  |  |  |  |  |
| Deploy production model |  |  |  |  |  |  |  |
| Roll back production model |  |  |  |  |  |  |  |
| Quarantine artifact |  |  |  |  |  |  |  |
| Delete artifact |  |  |  |  |  |  |  |

## Required approvals by stage

| Transition | Required evidence | Required approver |
|---|---|---|
| Experiment -> Candidate |  |  |
| Candidate -> Staging |  |  |
| Staging -> Production |  |  |
| Production -> Deprecated |  |  |
| Any -> Quarantined |  |  |

## Audit requirements

- [ ] Stage changes are logged.
- [ ] Artifact downloads are logged for sensitive models.
- [ ] Production promotions are logged.
- [ ] Deployment identity is logged.
- [ ] Rollbacks are logged.
- [ ] Quarantine actions are logged.

## Break-glass process

Describe emergency promotion, rollback, or quarantine process.

