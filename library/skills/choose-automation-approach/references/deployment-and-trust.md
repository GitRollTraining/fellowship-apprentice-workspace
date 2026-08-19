# Deployment and trust boundaries

Choose a deployment model by who owns, administers, can inspect and must keep the runtime working — not
by treating cloud or local as inherently safer.

## Common deployment models

| Model | Convenient when | Boundary and trade-off to surface |
|---|---|---|
| Fellow's personal computer | One person, attended work, fast prototype | Tied to that device, login state and person's availability; local files and other sessions share the host |
| Fellow's personal vendor cloud environment | Fast setup and remote execution under an existing Claude/Codex-style account | Workflow ownership, billing, stored data and access may leave with the Fellow |
| Company-managed device assigned to one person | Organisation manages patching and recovery while one operator retains context | Admins can access the host; user login and device lifecycle still affect the workflow |
| Shared workstation or dedicated Mac mini | Several colleagues need the same physical runtime or browser session | Shared login state can blur attribution; physical access, patching and concurrent use need an owner |
| Company-managed VM, container, serverless job or internal server | Persistent or unattended operation with an existing operations owner | Setup and observability cost rise; network, identity, patching and recovery become explicit duties |
| Client-owned runtime | The client must retain control after handoff | Usually clearer ownership, but setup depends on the client's technical capacity |
| Managed automation SaaS | Connectors and scheduling matter more than infrastructure control | Provider receives data and often tokens; capability, export, audit and vendor dependency vary |
| Third-party hosted agent or MCP service | Provider removes hosting and OAuth setup work | Provider trust, data handling, scopes, tenancy and revocation become part of the boundary |
| Hybrid: local or company agent calling hosted services | Existing harness plus managed integrations gives the fastest useful combination | Data and authority cross several boundaries; do not evaluate only the agent host |

Add another model when the actual workflow does not fit these. The list is a prompt, not a taxonomy the
Fellow must obey.

## Map the boundary

For the leading option, identify:

- runtime owner and day-to-day operator;
- people or vendors with administrative access;
- trigger: manual, scheduled, event-driven or public-facing;
- data entering and leaving each environment;
- where credentials, logs, files and model context persist;
- who handles renewal, failure, patching, handoff and shutdown;
- whether the workflow depends on one person's device, account or browser session.

Do not demand complete infrastructure documentation. Ask only where an answer could change the choice.

## Untrusted input to privileged action

Treat messages, email, documents, webpages, attachments, comments and tool results from colleagues or
external people as potentially instruction-bearing input. Direct conversation with an agent that also
has powerful tools creates a shorter path from untrusted text to action.

Possible controls, from lighter to heavier, include:

- avoid direct conversational access when a form or structured intake is sufficient;
- keep the first pass read-only and extract only the fields needed downstream;
- validate recipients, amounts, identifiers, domains or action parameters deterministically;
- restrict the available tool and permission scope for the step reading untrusted content;
- separate an untrusted-content reader from a privileged actor and pass only allowlisted structured
  fields between them rather than open-ended instructions;
- screen proposed actions against the Fellow's original intent;
- review selected, exceptional or high-impact actions rather than every action;
- seek a targeted security review for a named unresolved question when its plausible impact justifies
  the extra work;
- log enough context to diagnose a bad action without logging secret values.

Recommend only controls proportionate to the path and consequence.

## Model and harness capability

Prompt-injection robustness varies by exact model, version, training, harness, tool policy and input
representation. Do not claim that every cheaper or smaller model is less robust in the same way. When a
less capable, low-cost or untested model reads untrusted input, be more cautious about giving that same
component broad action authority. A frontier model may reduce errors but is not a security boundary.

For browser work, account for what the harness can actually perceive. A capable multimodal agent that
uses screenshots, or a model that reliably interprets the relevant DOM/HTML, can tolerate some UI
changes better than selector-only automation. It still carries execution latency, context and resource
cost, login-state dependencies and ambiguity that a stable machine interface may avoid.
