# Credential inventory, isolation and attribution

Help the Fellow see and improve the credential arrangement; do not interrogate them for compliance.
Never request or record a password, API key, token, recovery code, cookie or other secret value.

## Build the inventory

Ask:

> Which accounts, OAuth connections, API keys, service accounts or managed connectors can this
> automation use? For each, give only its name, type, owner, purpose and where it is managed — not the
> secret itself.

Record only decision-relevant fields:

| Field | Meaning |
|---|---|
| System | Gmail, Notion, Stripe or another target |
| Credential type | Account, OAuth, API key, service account, managed connector or other |
| Acts as | Person, team mailbox, organisation or workload represented |
| Owner | Person or role responsible for granting and revoking it |
| Purpose | Workflow or tasks currently using it |
| Dedicatedness | Dedicated, reused personal, shared team or unknown |
| Environment | Prototype, test, production or mixed |
| Permission shape | High-level scopes or roles; never token contents |
| Storage/management | Platform-managed connection, OS store, local configuration, secret manager or unknown |
| Attribution | Whether an action can be traced to a person, automation/run or at least its owner |

"Dedicated" means meaningfully bounded to this workload or actor. It does not always require a new user
account: per-user OAuth can be the correct identity when the automation genuinely acts for that user.

## Look for useful improvements

For a reused or shared credential, explore rather than accuse:

- Does the provider support a separate key, restricted key, per-user OAuth grant, automation account or
  service identity?
- Would separation improve revocation, permissions or attribution for a concrete failure mode?
- Can test and production use different credentials without creating disproportionate administration?
- Is the present arrangement temporary, and what event would justify changing it?
- Who can actually create or approve the better credential?

Suggest the smallest improvement with worthwhile benefit. If a dedicated credential is easy and makes
revocation or attribution materially clearer, recommend it. If the provider or organisation makes that
expensive, record the limitation and consider lighter compensation such as narrower scope, run IDs,
separate logs or a named owner.

## Do not default to a secret manager

Secret storage and credential isolation are related but different. A dedicated restricted key can
still be badly stored; a centrally stored shared key can still have poor attribution.

Usually keep the existing simple mechanism for a short, single-user, attended prototype when the
credential stays out of Git, documents, chat and logs and is easy to revoke. Prefer a platform-native
credential field or operating-system facility already in use.

Consider stronger managed storage when facts justify it, such as:

- unattended or long-lived execution;
- a shared host or several operators;
- production or high-impact access;
- the same secret copied across runtimes;
- a real need for controlled access, rotation, revocation or audit;
- an existing team secret manager whose use adds little operational burden.

Prefer the runtime's adequate native secret facility before adding a standalone system. Recommend a
new external secret-management service only when native facilities are insufficient or centralisation
across environments solves an actual problem.

## Produce a current decision, not an ideal-state backlog

| Credential | Current arrangement | Current recommendation | Why proportionate now | Fellow decision | Upgrade trigger |
|---|---|---|---|---|---|
| Example: shared mailbox OAuth | Individual user grant | Keep for pilot; name owner and scope | Revocable and low setup; pilot remains attended | Accept | Move to client-owned grant before handoff |

The example illustrates the shape, not a default answer. Omit controls that are not warranted now.
