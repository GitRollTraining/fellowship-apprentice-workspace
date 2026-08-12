# Integration selection

Compare choices at the Fellow-facing boundary: "I need to use ___ to work with Gmail." The Fellow cares
about capability, setup, authentication, hosting, speed, reliability, permissions, data handling and
maintenance. They usually do not care whether an MCP uses SSE, WebSocket or another transport unless
that detail changes one of those concerns.

## Default first-look order

Use this as a simple starting point, not a universal ranking:

| Order | Method | Start here when | Move away when |
|---|---|---|---|
| 1 | Built-in connector | It already covers the required action and the platform manages authentication acceptably | Capability, scopes, multi-user behaviour, data handling or export is inadequate |
| 2 | Hosted or managed MCP | It removes meaningful OAuth/hosting work and its operator and permissions are acceptable | The Fellow must still host/authenticate it, provider trust is unclear or capability is incomplete |
| 3 | Official API/SDK | Exact behaviour, throughput, structured data, observability or long-term control justifies integration work | Setup and maintenance cost exceed the current workflow's value |
| 4 | Browser/computer use | The task is UI-native, no adequate interface exists, or a fast low-frequency pilot matters most | High volume, low latency, deterministic execution or resource efficiency dominates |
| 5 | Undocumented/internal UI API | No official interface suffices, browser execution is too heavy, and the endpoint and authorisation assumptions have been deliberately evaluated | Stability, authentication, provider terms or maintenance ownership is unclear |

Reorder deliberately:

- Move browser work earlier for a fast, attended or low-frequency pilot when the agent can understand
  the UI reliably.
- Move the official API earlier for persistent, high-volume or precision-sensitive execution.
- Keep an existing adequate connector ahead of a custom integration; "more engineered" is not itself a
  benefit.
- Move an MCP down when self-hosting, manual authentication or multi-user setup removes its convenience
  advantage.

## What each label hides

### Connector

Confirm the exact operations, who authorises it, whether users grant access separately, what the host
stores, permission granularity, audit/export and what happens when a user leaves. A familiar label is
not proof of adequate scopes or ownership.

### MCP

Treat MCP as an access option but distinguish operationally relevant forms:

- first-party hosted;
- third-party hosted/managed;
- self-hosted remote;
- local process packaged with the client or skill.

Ask who hosts it, who configures upstream authentication, whether each colleague authorises separately,
what data/token material the operator sees, how permissions are scoped, and who maintains it. Do not
turn transport implementation into a Fellow-facing decision unless it affects deployment.

### Official API/SDK

Check whether the required operation exists, authentication complexity, approval requirements,
rate/usage limits, permission scopes, event/webhook support and maintenance ownership. Official does not
always mean simpler; it often means more control and a clearer contract.

### Browser/computer use

Distinguish selector-only scripts from semantic agents using screenshots, accessibility data or
DOM/HTML. A capable model can survive some UI changes and is often quick to prototype because a human
demonstration already defines the path. Browser execution is still usually heavier and slower, and can
depend on login state, pop-ups, permissions and ambiguous visual state.

### Undocumented/internal UI API

Calling the network interface used by the real UI can be faster and lighter than driving the browser,
but the contract, authentication flow and provider tolerance may change without notice. Use it only
after naming who will detect and repair that change and any terms or authorisation uncertainty.

## Make the recommendation

Select one primary method. Include a fallback only if a named uncertainty could realistically change
the choice. For each, state capability fit, setup/authentication, runtime weight, reliability,
permissions/data boundary and maintenance owner in plain language.
