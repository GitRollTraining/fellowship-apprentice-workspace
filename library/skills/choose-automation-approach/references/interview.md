# Adaptive interview

Use this as a routing guide, not a form to administer in full. Reuse context already present, ask at
most three questions per turn and stop when further answers are unlikely to change the recommendation.

## Minimum useful context

Obtain or infer, with assumptions stated:

1. **Desired action:** what the automation reads, produces, changes, sends, approves or deletes.
2. **Users and runtime:** who starts or relies on it, where it runs and whether it is attended.
3. **Inputs and access:** which systems, data, credentials and untrusted sources it touches.
4. **Available methods:** connectors, MCP servers, APIs, browser access or existing tools already within
   reach.
5. **Failure impact:** a reasonable worst case, how quickly it is noticed and whether it is reversible.
6. **Trade-off priorities:** speed to build, ease of use, execution speed, reliability, auditability,
   maintenance, cost and safety — especially what the Fellow is willing to trade.

"I don't know" is a valid answer. Produce a conditional recommendation when unknowns remain.

## Opening questions

Prefer one compact opening:

> What should the automation do, who will use it, and what would a useful first version look like?

Then ask only the missing questions most likely to change the design. Useful probes include:

- Will it only prepare a draft, or also take the external action?
- Is this a short prototype, a pilot or something expected to run after the Fellow leaves?
- What existing connector, MCP, API, account or browser access is already available?
- Which inputs come from colleagues, customers or the public rather than a trusted internal source?
- What is the worst plausible mistake, and could someone detect and reverse it?
- Which matters more here: shipping quickly, reducing manual work, reliability, or lowering exposure?

## Conditional branches

### Deployment and untrusted input

Load `deployment-and-trust.md` when the workflow is shared, persistent, externally triggered, handles
sensitive data or lets untrusted content influence a tool-enabled agent.

### Credentials

Load `credential-design.md` whenever the workflow uses an account, OAuth connection, API key, token,
service account or managed connector. Ask for metadata only, never the secret value.

### Integration choice

Load `integration-selection.md` when more than one access path exists, or when the obvious path has
meaningful authentication, hosting, reliability or maintenance trade-offs.

### High-stakes actions

Load `high-stakes-actions.md` when the Fellow says an error could materially affect money, external
communications, permissions, records, legal commitments, safety or an irreversible state.

## Stop rules

Stop questioning and issue a provisional brief when any of these is true:

- The Fellow asks for the recommendation now.
- One option clearly dominates under the Fellow's priorities and remaining unknowns would only tune
  implementation details.
- The next question would document completeness but would not change a decision.
- The Fellow cannot obtain the missing information during this session.

List no more than three decision-relevant unknowns. Do not punish the Fellow with a long questionnaire
because the skill knows more questions it could ask.
