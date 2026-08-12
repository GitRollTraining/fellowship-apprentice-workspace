# Baseline output

This is the expected decision, not wording that must be copied verbatim.

## Decision

- **Primary method:** use the built-in Gmail connector for the four-week pilot because it already
  supports the required read-and-draft scope, minimises setup and avoids unnecessary sending authority.
- **Deployment:** the Fellow's personal agent cloud environment is acceptable as a stated pilot
  trade-off, with ownership/handoff risk recorded. Reassess before the workflow becomes long-lived or
  must survive the Fellow's departure.
- **No current infrastructure project:** do not recommend a standalone secret manager, custom Gmail
  API integration, self-hosted MCP or company runtime for this pilot without another concrete need.

## Trust boundary

External email is untrusted and reaches the classification/drafting model. Keep the pilot's connection
draft-only, validate any extracted recipient/thread identifier outside free-form model output where the
connector permits it, and preserve staff review before sending. Do not claim the low-cost model will
necessarily fail or that a stronger model would make autonomous sending safe.

## Credentials

Record the personal OAuth grant as acting for the Fellow with access to the shared mailbox; do not
record token values. For the pilot, keeping it is a proportionate choice if the firm agrees. Recommend a
client-owned per-user grant or dedicated automation identity before handoff only if the workflow will
continue after the Fellow leaves or begins sending unattended. Do not recommend a separate secret
manager when the connector already manages OAuth.

## High-stakes action

Draft creation is low impact and already reviewed. Automatic sending is a later upgrade trigger, not a
pilot requirement. If adopted, reassess using a low-impact rollout, recipient/scope limits and staged or
exception review rather than automatically requiring approval on every eventual message.

## Fellow decision and unknowns

Clearly separate the skill recommendation from the Fellow's final choice and allow override. List no
more than three unknowns, and only if they could change a material choice — for example whether the
connector stores data outside an acceptable boundary or whether the client can own the OAuth grant.
