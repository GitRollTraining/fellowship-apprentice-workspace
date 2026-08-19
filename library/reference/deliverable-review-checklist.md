---
style: procedural
role: reference
status: draft — not yet used on a client deliverable
---

# Deliverable Review Checklist

Use this checklist to attack the design, instructions and claimed evidence of any engagement deliverable
before Validator A issues a verdict. It is deliberately independent of delivery shape: apply it to one
skill, several skills, scripts, integrations, services or a larger system.

This is a review surface, not a validator and not yet a reusable skill. It helps a reviewer find concrete
failure modes. Validator A separately runs cases, records observed results and decides the release gate.
Promote this checklist into a more automated system only after real reviews show which judgements recur.

## Finding standard

Record a finding only when all of these are present:

| Field | Required content |
|---|---|
| Location | Exact file, component, instruction, interface or omitted responsibility |
| Trigger | The input, state or action that exposes the problem |
| Violated contract | The `R-*`, `AC-*`, specification clause, boundary or operating claim at risk |
| Evidence | Concrete contradiction, reproduction, unresolved absence or trace pointer |
| Severity | `BLOCKING` or `NON-BLOCKING` |
| Remediation | The smallest change that would resolve or explicitly accept it |

“Could be clearer” is not a finding. State who will misunderstand what, under which condition, and what
observable harm or contract failure follows.

Use `BLOCKING` when the issue can cause a signed acceptance criterion to fail, cross a safety/data/
credential/authorisation boundary, produce a false success, prevent deployment or recovery, or leave a
required component unverified. Use `NON-BLOCKING` only when signed scope and boundaries still hold. Every
accepted non-blocking finding must appear in `deliverable/known-defects.md`.

## 1. Scope and traceability

- [ ] Every delivered component is named in `deliverable/INDEX.md` and has an owner or operator.
- [ ] Each component responsibility points to the technical specification or a named technical necessity.
- [ ] Every signed `R-*` and `AC-*` has one explicit implementation and verification disposition.
- [ ] No component introduces stakeholder-visible behaviour absent from the signed PRD.
- [ ] Deferred and not-applicable items have recorded owner acceptance and do not masquerade as complete.
- [ ] Claims, defaults, thresholds and guarantees resolve through the source chain without a broken hop.

## 2. Trigger, inputs and outputs

- [ ] The initiating event, schedule or human action is explicit.
- [ ] Required and optional inputs, accepted formats, size/rate limits and invalid-input behaviour are explicit.
- [ ] Output destination, schema, naming, ordering, idempotency and partial-output behaviour are explicit.
- [ ] Repeated, concurrent, delayed and out-of-order invocations have a defined result where applicable.
- [ ] Time zones, locale, encoding, units and rounding are explicit where they can change behaviour.
- [ ] Human approval points cannot be silently bypassed by a retry, fallback or alternate entry point.

## 3. Interfaces and dependencies

- [ ] Each external service, model, datastore, file format and human handoff has a contract and owner.
- [ ] Version assumptions and compatibility bounds are explicit.
- [ ] Timeout, rate-limit, quota, authentication expiry and unavailable-dependency behaviour are defined.
- [ ] Retries are bounded and safe; duplicate side effects cannot be hidden behind a success response.
- [ ] A degraded path does not claim the same result as the normal path unless it satisfies the same contract.
- [ ] Dependency cost, licensing and client-account ownership match the current Decision Register.

## 4. Failure, recovery and observability

- [ ] Every named discovery failure mode has prevention, detection, response and recovery behaviour.
- [ ] Errors expose enough context to act without leaking prohibited data or credentials.
- [ ] Success is based on the intended downstream effect, not only on a request being sent.
- [ ] Partial state, restart, replay, compensation and manual recovery are addressed where applicable.
- [ ] Logs, health signals and alerts identify failures before the owner must infer them from business harm.
- [ ] Escalation says who acts, with what evidence, and what must not be attempted.

## 5. Data, credentials and high-stakes actions

- [ ] Every read, write, copy, transform, retention and deletion stays inside the engagement boundary.
- [ ] The client delivery boundary is checked separately from the in-engagement working boundary.
- [ ] Secret values are absent from source, logs, examples, fixtures, reports and the handoff package.
- [ ] Credential owner, minimum permissions, storage, access, rotation and revocation are defined.
- [ ] High-stakes actions require the agreed human confirmation at the moment it remains meaningful.
- [ ] The deliverable does not widen access or send data to a provider absent from the approved design.

## 6. Deployment, operations and retirement

- [ ] `deployment.md` defines prerequisites, installation, configuration, start, upgrade, rollback and uninstall.
- [ ] `operations.md` defines normal use, monitoring, failure response, recovery, credential rotation and escalation.
- [ ] Instructions distinguish Fellow-owned, client-owned and provider-owned actions.
- [ ] A new operator can follow the instructions without private knowledge or unexplained local state.
- [ ] State-changing steps have a dry run, backup, rollback or explicitly accepted recovery alternative.
- [ ] Ongoing cost, maintenance cadence, version ownership and end-of-life behaviour are explicit.

## 7. Verification quality

- [ ] Tests exercise observable business outcomes rather than implementation-shaped proxies alone.
- [ ] Happy path, invalid input, named exception, approval, dependency failure and boundary cases are covered.
- [ ] Fixtures are representative, permitted, versioned and separated from secret or live client data.
- [ ] Expected results come from the signed PRD/specification, not from copying current implementation output.
- [ ] Commands, environment, exit codes and evidence paths are sufficient for an authorised reviewer to repeat.
- [ ] A failed, skipped or unsafe-to-run case cannot be reported as passed.
- [ ] Changes that invalidate prior evidence are named and detectable.

## Completion

The review is complete only when every applicable box has evidence or a recorded finding, every finding
has a disposition, and Validator A can independently reproduce the checks on which a pass would depend.
Do not erase a finding after fixing it; retain its disposition in the validation report.
