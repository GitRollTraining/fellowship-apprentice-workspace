---
style: template
role: template
produces: engagements/<client-slug>/handover/package-manifest.md
---

# Handoff Package Manifest Template

Copy the block below to `engagements/<client-slug>/handover/package-manifest.md`, then include it at the
root of the client package. This is a navigation document, not the internal hash or validation report.
Replace each `HC-<next>` comment with a unique claim ID continued from the owner account; comments remain
invisible to the client but are mapped internally.

--- COPY FROM HERE ---

# What is in this handoff

<!-- handoff-source-map: ../verification/handoff-source-map.md -->

**Business:** <business name>

**Package version:** <v1>

**Prepared:** <YYYY-MM-DD>

<!-- claim: HC-<next> -->
## Start here

Open `<owner-account.pdf or owner-account.html>` first. It explains what was delivered, what it will not
do, what to check and where to go when something fails.

<!-- claim: HC-<next> -->
## Package contents

| Path | What it is | When to use it |
|---|---|---|
| `<owner-account.*>` | The plain-language account | Read first and keep for checking or recovery |
| `deliverable/` | The files that perform the work | Install and operate as described below |
| `deliverable/deployment.md` | Canonical installation, configuration, upgrade, rollback and removal instructions | Before installation or change |
| `deliverable/operations.md` | Canonical normal-use, monitoring, recovery, credential and escalation instructions | During routine operation and incidents |
| `deliverable/known-defects.md` | Known limitations that remain after validation | Before relying on an affected case; omit this row only when the file does not exist |
| `deliverable/<verify command>` | A smoke or health check the client can run | After installation and when health is uncertain; omit this row only when no proportionate check exists and the owner account says why |

<!-- claim: HC-<next> -->
## Ownership and support

| Responsibility | Owner | Contact or route |
|---|---|---|
| Installation and configuration | | |
| Routine operation | | |
| Credentials and access | | |
| Maintenance and upgrades | | |
| Escalation when recovery fails | | |

<!-- claim: HC-<next> -->
## Known limits

<State each delivered limitation in plain words and point to the applicable `known-defects.md` section.
If there is no known-defects file, state only what the owner-facing account can support; do not claim
that no defect exists.>

--- COPY ENDS HERE ---
