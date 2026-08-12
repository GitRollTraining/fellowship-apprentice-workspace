# High-stakes action controls

Let the Fellow decide which actions are high stakes. Common signals include money, external messages,
permissions, deletion, legal commitments, safety, sensitive records or changes that are hard to reverse.
Do not assume every write is high stakes or that every high-stakes action needs the same control.

## Understand the action

Ask only what changes the design:

- What is a reasonable worst-case mistake?
- How many people, records or dollars can one run affect?
- How quickly would someone notice?
- Can the change be cancelled, reversed or repaired?
- Is the action attended, scheduled or event-driven?
- Would review on every run erase most of the automation's value?
- What risk is the Fellow willing to accept for speed or convenience?

## Control menu

Choose the lightest combination that materially improves the workflow:

- **Low-impact test:** dummy data, sandbox, test tenant, internal stakeholder, draft-only mode or a
  low-consequence first case.
- **Scope limit:** allowlisted recipients/records, maximum amount, batch size, frequency or date range.
- **Staged autonomy:** drafts first, first N runs reviewed, sampled review, then broader execution.
- **Deterministic validation:** check required fields, totals, identifiers, recipients or preconditions
  outside the language model.
- **Exception review:** ask a person only for unusual, ambiguous or threshold-crossing cases.
- **Reversibility:** keep an idempotency key, cancellation path, backup or record of the prior state when
  the system supports it.
- **Detection and stop:** make failures visible, identify an owner and provide a practical way to halt
  future runs.
- **Conditional execution plan:** state preconditions and refuse when they fail only when the action's
  context changes between planning and execution enough to justify this friction.

Recommend a low-impact test when its expected learning exceeds its setup cost. If the Fellow skips it,
record the reason and residual uncertainty rather than blocking the design.

## Preserve the point of automation

Do not default to human approval for every action. Consider approval only for the first runs,
exceptions, values over a threshold, irreversible transitions or a small class of materially different
cases. A control that recreates the entire manual process needs an explicit benefit strong enough to
justify it.

Do not require a formal conditional plan for every high-stakes action. It is useful when preconditions,
time-sensitive facts or execution scope must be rechecked; it is needless ceremony when deterministic
limits or a low-impact rollout already handle the important risk.

## Record the decision

State:

- control recommended now and the concrete risk it addresses;
- friction and maintenance introduced;
- Fellow's decision or override;
- residual risk accepted;
- trigger for adding, removing or tightening the control later.
