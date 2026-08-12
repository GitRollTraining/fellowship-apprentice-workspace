---
name: choose-automation-approach
description: Guide an adaptive interview to choose proportionate deployment, integration, credential, and high-stakes controls when designing or revisiting an automated workflow.
---

# Choose an Automation Approach

> Help a Fellow make a practical, explicit design decision. This is decision support, not a security
> gate: recommend the least operationally burdensome arrangement that keeps risk within the Fellow's
> stated tolerance, then let the Fellow accept, change, or override it.

## Inputs

No fixed argument. Start from the workflow description, process record or specification already in the
conversation or workspace. Do not make the Fellow repeat known context.

Never ask for API keys, passwords, tokens, recovery codes or other secret values. Ask only for the
credential's name, type, owner, purpose and storage mechanism.

## Workflow

1. **Establish the decision.** Identify what the automation reads, decides, changes or sends; who uses
   it; its lifecycle stage; and which trade-offs matter. Use `references/interview.md`. Ask at most
   three questions at a time and stop when another answer is unlikely to change the recommendation.
2. **Map deployment and trust boundaries.** Identify where the harness runs, who administers it, where
   data crosses boundaries, and whether untrusted content can influence actions. Use
   `references/deployment-and-trust.md` when deployment or untrusted input matters.
3. **Choose the access method from the Fellow's point of view.** Compare connector, MCP, official API,
   browser/computer use and undocumented API as things the Fellow can choose. Use
   `references/integration-selection.md`; ignore transport details unless they change setup, hosting,
   authentication, permissions, data handling or multi-user operation.
4. **Build a credential inventory and improve it proportionately.** Record identities without secret
   values. Suggest a dedicated or more restricted credential only when the concrete reduction in risk
   is worth the setup and maintenance cost. Use `references/credential-design.md`.
5. **Select high-stakes controls.** Let the Fellow define what is high stakes. Recommend low-impact
   testing, limits, review or conditional planning only where each measure materially improves the
   workflow. Use `references/high-stakes-actions.md`.
6. **Make one primary recommendation.** State the evidence, expected benefit, setup and maintenance
   cost, why it is warranted now, and the lightest viable alternative. Put stronger future controls
   under upgrade triggers rather than current requirements.
7. **Record the Fellow's decision.** Separate the skill's recommendation from the Fellow's choice,
   overrides, accepted residual risk, assumptions and unknowns. Do not block completion because the
   Fellow rejects a recommendation or declines to provide more context. External law, organisational
   policy, provider limits and tool authorisation remain factual constraints, not recommendations to
   override.

## Recommendation discipline

Read `references/principles.md` before producing the recommendation. Do not optimise for theoretical
maximum isolation or safety. Do not recommend new infrastructure solely because it is a best practice.
Prefer an adequate capability the team already operates over a new system with its own failure modes.

Exact model, version, harness and safeguards affect prompt-injection robustness. Be more conservative
when a less capable or untested model processes untrusted input, but never treat a stronger model as a
security boundary.

## Gotchas

Read `references/gotchas.md` before finalising the recommendation. It covers misleading method labels,
browser-automation assumptions, model capability, shared credentials, secret-manager over-engineering
and high-stakes controls that accidentally recreate the manual process.

## Output

Use `references/output-template.md`. If this is an active engagement and the client slug is known, offer
to save the agreed brief at `engagements/<client-slug>/spec/automation-approach.md`; otherwise return it
in the conversation. Do not invent a client or destination.

## Eval

Paired-run baseline and anti-over-engineering checks live in `eval/`. A passing run must be decisive
without becoming a compliance checklist, must not request secrets, and must preserve the Fellow's
ability to trade safety for convenience deliberately.

## Quality Guidelines

Adhere to `library/reference/agent-quality-guidelines.md` and
`library/reference/skill-architecture.md`.
