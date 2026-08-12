# Automation approach decision brief

Keep the brief concise enough that the Fellow can review it in one sitting. Omit empty sections rather
than filling them with generic advice. Never include secret values.

```markdown
# Automation approach — <workflow>

## Decision

- **Fellow's decision:** <chosen approach or provisional choice>
- **Skill's recommendation:** <one primary configuration>
- **Why this is proportionate now:** <risk addressed, benefit, setup/maintenance cost, lighter option>
- **Lifecycle stage:** <prototype / pilot / long-lived operation>
- **Decision status:** <agreed / overridden / provisional>

## Context and priorities

- **Workflow:** <read, decide, change, send or delete>
- **Users and operator:** <who uses and who keeps it running>
- **Priorities and accepted trade-offs:** <what matters and what can be sacrificed>
- **Important assumptions:** <facts not yet verified>

## Deployment and trust boundaries

- **Runtime:** <where it runs and who administers it>
- **Data movement:** <important environment/vendor crossings>
- **Untrusted input:** <sources and path to action>
- **Current safeguards:** <only measures warranted now>

## Access method

| Choice | Capability and setup | Runtime/maintenance | Why selected or rejected |
|---|---|---|---|
| <connector/MCP/API/browser/internal API> | <fit and authentication> | <weight, reliability, owner> | <decision reason> |

## Credential inventory and design

| Credential (no secret) | Owner / acts as | Current use and permissions | Current recommendation | Fellow decision |
|---|---|---|---|---|
| <name and type> | <owner/principal> | <dedicated/shared, environment, scope> | <proportionate change or keep> | <choice> |

## High-stakes actions

| Action | Impact / detectability / reversibility | Control now | Friction and reason |
|---|---|---|---|
| <action> | <brief assessment> | <test, limit, staged autonomy, review, recovery or none> | <trade-off> |

## Overrides and residual risk

- **Recommendation overridden:** <what, or none>
- **Reason / benefit sought:** <Fellow's explanation or unknown>
- **Residual risk accepted:** <specific consequence or uncertainty>

## Upgrade triggers

- <concrete change that should cause reassessment> → <control or option to reconsider>

## Open questions

- <no more than three questions that could still change a material decision>
```
