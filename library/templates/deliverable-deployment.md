---
style: template
role: template
produces: engagements/<client-slug>/deliverable/deployment.md
---

# Deliverable Deployment Template

Copy the block below to `engagements/<client-slug>/deliverable/deployment.md` and adapt it to the
delivery shape selected in the signed specification. This is the canonical deployment authority that
travels with the client package; the owner account may point here but must not maintain a second set of
instructions.

Do not write credential values. Name the client-owned account, secret location, permission scope and
revocation route instead.

--- COPY FROM HERE ---

# Deploy <delivered system name>

## Ownership and target

| Item | Recorded value |
|---|---|
| Intended runtime/environment | |
| Client deployment operator | |
| Routine operator | |
| Credential/access owner | |
| Package version | |
| Trusted out-of-band source for the B-approved archive SHA-256 | delivery message / client portal / other authorised route |
| Supported agent/tool version, if applicable | |

## Before installation

- Required software, accounts, permissions and network access:
- Required data and credential boundary decisions:
- Existing installation or state to preserve:
- Pre-install backup or export:
- Expected ongoing dependency or cost:

## Verify the package

1. Obtain the B-approved archive SHA-256 through the trusted route named above, calculate the received
   archive's SHA-256 before extraction, and compare them. Never paste the expected archive hash into a
   file inside that archive: changing the file would change the hash it claims to contain.
2. Open `package-manifest.md` and confirm every expected top-level item is present.
3. Stop if the package differs, contains an unexpected path or asks for a secret in a document.

## Install and configure

<Give exact, ordered commands or interface actions from a clean client environment. State which role
performs each external action and where non-secret configuration lives.>

For a delivered agent skill, install the **whole skill bundle**, not just its main file. Copy
`deliverable/skill.md` plus its companion directories into the client runtime's skill directory as
`<skill-slug>/SKILL.md`, preserving relative paths such as `references/`, `scripts/`, `assets/` and
`eval/`. The lowercase file is the engagement authoring convention; `SKILL.md` is the runtime entry
point. Replace this paragraph when the selected agent uses a different documented convention.

## Start or enable

<State the exact command, toggle or scheduled trigger. State the expected immediate signal.>

## Verify after installation

| Check | Command or action | Expected result | Stop/escalate when |
|---|---|---|---|
| Package/runtime visibility | | | |
| Safe representative case or health check | | | |

## Upgrade or replace

<Pin the incoming version, preserve necessary state, install it, verify it and only then retire the old
version. State whether parallel versions are supported.>

## Roll back

<Give the trigger, exact rollback steps, preserved version/state and verification. Do not say merely
“restore the previous version.”>

## Uninstall and revoke

<Remove installed files, triggers and integration access; revoke or rotate credentials; name retained
data, logs or backups and their deletion owner.>

## Escalation

| Condition | Stop safely by | Contact/route | Evidence safe to share |
|---|---|---|---|
| | | | |

--- COPY ENDS HERE ---
