---
style: descriptive
role: playbook stub
status: STUB — not written. Contents specified, author unassigned.
serves: D-04, D-05, D-09
---

# Validator — STUB

**When the fellow runs it:** before every ship, on every artifact.

**What it must contain, at minimum:**

1. A deterministic check that runs without the fellow's judgement — a command with an exit code, not a
   reading.
2. The principle it is built on, stated by a practitioner and worth carrying: the model reasons, the
   code computes, the system verifies. Atomic provenance, scoped determinism, derivation chains.
3. Multi-layer completion verification that never trusts a self-report. An agent claiming "done" is an
   input to the check, never the check.
4. What to do when the validator and the fellow disagree.

**Two open questions the author inherits:**

- **Does this duplicate the assessment engine?** The engine grades at the gate; this checks before every
  ship. One instrument at two moments, or two instruments. Unruled.
- **Does the business receive the validator at handover?** If it does not, quality decays the moment the
  fellow leaves. Also unruled, and it changes what the playbook may depend on — a validator the owner
  runs cannot depend on our library.
