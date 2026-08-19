# `choose-automation-approach` design record

## Status

- **Component:** `library/skills/choose-automation-approach/`
- **Type:** locally authored, reusable decision-support skill
- **Initial design:** 2026-08-13

## Problem

A Fellow who can reproduce a business process still has to choose how the automation reaches external
systems, where it runs, whose authority it uses and how much friction to add around consequential
actions. These decisions interact: a hosted MCP may remove OAuth setup but add a vendor boundary; a
browser agent may be fast to build but heavy to run; a dedicated credential may improve revocation but
cost more to obtain than a short prototype justifies.

The curriculum trains an automation specialist rather than a software or security engineer. Some
failure modes become legible only through project experience, yet omitting them leaves a Fellow to make
high-impact choices with no prompt to examine them. The skill therefore supplies decision support and
gotchas without claiming that the curriculum taught security engineering.

This creates a deliberate tension with the library's curriculum-scope rule: curated components are
normally limited to domains the curriculum teaches. Treat this skill as an explicit exception, not as
evidence that secure deployment or security engineering has become a taught competency.

## Design goal

Help the Fellow choose the least operationally burdensome arrangement that keeps risk within their
stated tolerance, then preserve their decision, overrides, residual risk, assumptions and upgrade
triggers.

The skill optimises decision quality, not maximum isolation or minimum risk.

## Non-goals

- Certify that an automation is secure or compliant.
- Replace a specialist security, legal or organisational review.
- Turn recommendations into non-overrideable gates.
- Teach MCP transport implementation or general cloud engineering.
- Optimise model/runtime cost; that belongs in later cost-management work.
- Build, deploy or connect the chosen automation itself.

## The four themes

| Theme | Question answered | Runtime reference |
|---|---|---|
| Automation security and trust boundaries | Where does it run, who administers it, what crosses boundaries and can untrusted input influence action? | `references/deployment-and-trust.md` |
| Credential inventory, isolation and attribution design | What authority exists, who owns it and what improvement is proportionate now? | `references/credential-design.md` |
| Automation access and integration strategy | Should the Fellow use a connector, MCP, official API, browser or undocumented API? | `references/integration-selection.md` |
| High-stakes action controls | Which tests, limits, reviews or recovery measures preserve enough automation value? | `references/high-stakes-actions.md` |

The themes are reasoning lenses, not four mandatory questionnaires. The agent loads and asks about a
theme only when it could change the recommendation.

## Runtime contract

1. Reuse the workflow context already present.
2. Obtain the minimum useful facts: action, users/runtime, inputs/access, available methods, failure
   impact and Fellow priorities.
3. Ask no more than three questions at a time and stop when another answer is unlikely to change a
   material decision.
4. Make one primary recommendation. Add a fallback only for a named uncertainty.
5. For every proposed control, state the risk addressed, benefit, setup/maintenance cost, why now and
   lighter alternative.
6. Put stronger controls under upgrade triggers unless facts warrant them today.
7. Separate feasibility facts and external constraints from skill recommendations.
8. Let the Fellow accept, modify or override every recommendation; missing rationale is recorded, not
   converted into a block.

## Proportionality guard

The recurring failure to prevent is advice that always climbs toward a production security ideal:
service identity, separate environment, secret manager, full observability and human approval. Each may
be correct in context; recommending the whole stack by default defeats short pilots and teaches ritual
rather than judgement.

The skill therefore uses a `current recommendation / upgrade trigger` split. A new system is current
only when its marginal risk reduction is worth its operational cost and an owner exists for that cost.
The eval must fail a result that recommends a standalone secret manager for connector-managed OAuth in
a short single-user pilot without another concrete need.

## Access-method abstraction

Connector, MCP, official API, browser/computer use and undocumented UI API appear side by side because
that is the Fellow's choice boundary: "what can I use to call Gmail?" MCP internals matter only where
hosting, authentication, permissions, data handling, maintenance or multi-user use changes.

The simple first-look order is connector, hosted/managed MCP, official API, browser, undocumented API.
It is deliberately reorderable: browser moves earlier for fast low-frequency UI-native pilots;
official API moves earlier for persistent high-volume or precision-sensitive work; MCP moves later when
self-hosting or authentication erases its convenience advantage.

## Prompt injection and model capability

The skill does not encode a monotonic "cheaper model equals less secure" rule. Robustness varies by
exact model, version, harness, safeguards and input representation. A less capable or untested model
reading untrusted content is a reason to constrain its authority more carefully, while a frontier model
is never treated as a security boundary.

## Credential interaction style

The agent builds an inventory with the Fellow rather than asking whether they comply with an ideal.
It never requests secret values. When a non-dedicated credential appears, it explains the concrete
attribution, revocation or permission trade-off and helps find the smallest worthwhile improvement.
Dedicated credentials and secret storage remain separate decisions.

## High-stakes interaction style

The Fellow defines what is high stakes and may trade safety for automation value. Low-impact testing is
a strong contextual recommendation, not an absolute condition. Conditional plans and human approval
are options for changing preconditions, exceptions or materially consequential cases; they are not
attached to every action by default.

## Artifact map

| Artifact | Audience and role |
|---|---|
| `SKILL.md` | Runtime dispatcher and behavioural contract |
| `references/principles.md` | Stable Fellow-readable decision principles |
| `references/interview.md` | Adaptive minimum-input and stopping protocol |
| Four theme references | Detailed questions and heuristics loaded only when relevant |
| `references/gotchas.md` | Compact decision traps in trigger/wrong-default/correct-behaviour form |
| `references/output-template.md` | Decision brief separating recommendation from Fellow decision |
| `eval/` | Paired baseline and anti-over-engineering/generalisation checks |
| This design record | Maintainer rationale, scope and revalidation surface |

## Gotcha policy

`gotchas.md` is intentionally human-readable but primarily loaded by the agent before recommendation.
Add a gotcha when a non-obvious wrong default is supported by observed use, an eval failure or stable
primary guidance. Keep hypothetical concerns in principles or the relevant theme reference until they
earn that stronger treatment.

## Evaluation

The canonical case is a short Gmail drafting pilot with external untrusted input, a low-cost model,
personal cloud runtime, personal OAuth and an adequate built-in connector. It catches the two opposed
failures: ignoring risk and over-engineering the pilot.

Additional probes cover a trivial local prototype, a shared unattended payment workflow, a
browser-first pilot and a third-party hosted MCP. Re-run them when model behaviour or this skill changes;
the expected result is decision behaviour, not verbatim prose.

## Revalidation triggers

- A Fellow reports that the interview feels like an audit or regularly stops before a recommendation.
- Runs repeatedly prescribe maximum isolation, a secret manager or approval on every action.
- Runs fail to surface untrusted-input-to-action paths or credential ownership on consequential cases.
- Connector/MCP hosting or authorisation conventions change materially.
- A new model or harness changes browser perception or prompt-injection behaviour enough to alter a
  selection heuristic.
- The curriculum formally adds secure deployment or security engineering; revisit this exception.

Until the library assigns an owner and cadence for the whole tool layer, this component inherits that
open maintenance risk. Revalidate at least when one of the triggers above occurs; do not pretend an
unowned calendar reminder solves the ownership gap.
