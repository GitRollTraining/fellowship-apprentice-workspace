# Gotchas

Each item names the trigger, the tempting wrong default and the corrective behaviour.

## A single universal integration ranking

**Trigger:** connector, MCP, API, browser and undocumented API are all possible.

**Wrong default:** rank them once by theoretical technical quality.

**Correct:** start with the Fellow-facing order in `integration-selection.md`, then reorder for the
workflow's stage, existing access, volume, reliability need and maintenance capacity.

## MCP treated as managed infrastructure

**Trigger:** an option is labelled "MCP".

**Wrong default:** assume OAuth, hosting, multi-user access and maintenance are already handled.

**Correct:** ask only the operational questions that matter: who hosts it, who authorises it, whose
identity it uses, what it stores and who maintains it.

## Browser automation declared inherently brittle

**Trigger:** the automation uses a browser.

**Wrong default:** reject it because selectors, pop-ups and UI layout can change.

**Correct:** check the actual harness. A capable screenshot/DOM-aware agent can tolerate semantic UI
changes and may be fastest to build, while still being heavier, slower and dependent on browser state.

## Model price used as a prompt-injection score

**Trigger:** untrusted content is processed by a cheaper or smaller model.

**Wrong default:** claim every cheaper model is categorically unsafe, or that the strongest model is
safe.

**Correct:** name the exact model/version/harness uncertainty, constrain authority proportionately and
never use model capability as the only security boundary.

## Maximum credential isolation becomes the goal

**Trigger:** a personal or shared credential appears.

**Wrong default:** always prescribe a new account, service identity and separate infrastructure.

**Correct:** identify the concrete attribution, revocation or permission problem and recommend the
smallest worthwhile improvement now.

## Secret manager as a ritual recommendation

**Trigger:** any API key or token exists.

**Wrong default:** recommend a standalone secret manager because it is a security best practice.

**Correct:** prefer an adequate platform-native or operating-system facility already in use; add new
infrastructure only for an actual shared, persistent, high-impact, rotation or multi-runtime need.

## Shared credential confused with shared responsibility

**Trigger:** several people or agents use one credential.

**Wrong default:** record the credential name and assume actions are attributable.

**Correct:** record its owner, represented principal and available run/user attribution; suggest a
dedicated credential or compensating run identity only when the benefit warrants it.

## High stakes means approval on every run

**Trigger:** the Fellow calls an action high stakes.

**Wrong default:** require a conditional plan and human confirmation before every execution.

**Correct:** compare low-impact tests, limits, staged autonomy, deterministic checks, exception review
and recovery; preserve the automation's intended value.

## Future production scale drives today's prototype

**Trigger:** the workflow might later serve more users or run unattended.

**Wrong default:** build the production identity, hosting, observability and secret stack now.

**Correct:** choose for the current stage and record concrete upgrade triggers.

## Risk warning mistaken for a decision

**Trigger:** several concerns have been identified.

**Wrong default:** return a warning list without choosing an approach.

**Correct:** make one primary recommendation, state its trade-off, then clearly separate the Fellow's
decision and any accepted residual risk.
