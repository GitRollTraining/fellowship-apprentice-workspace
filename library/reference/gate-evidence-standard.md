---
style: procedural
role: reference
status: draft — derived from one completed round, not yet used on a client engagement
---

# When a passing check counts as evidence

A gate is any check whose result decides whether work advances: a validator step, a structural check, a
script that exits non-zero. Three rules. Each was written after a round where a gate passed and the work
was still wrong.

## 1. Choose gates by what fails invisibly

A defect that announces itself does not need a gate. A defect that reports success and produces nothing
does. Before writing a check, name the failure it catches and say how that failure would otherwise
surface.

One round ran six gates over a generated brief. The two that caught real defects were the two attacking
the requirement most likely to fail silently — that no cached input could reach an output. The other
four guarded failures a reader would have seen anyway.

## 2. A gate you have not watched fail is not a gate

Feed the check an input you know is bad and confirm it goes red before you trust a green. Do it when you
write the gate, and record the input you used. A check that has only ever passed has not been tested; it
has been run.

## 3. A fix verified only against the input that reported it is not verified

Re-running the failing case proves the symptom is gone on that case. It does not prove the fix is right.

In the same round, one repair was verified against the single input that reported the defect — a brief
for one date. The defect survived on six of the other nine dates, because the repair had been applied in
one of the two places that printed the sentence. Check at the level of the property, not the instance.

## What this does not cover

Which checks a *deliverable* needs is `library/reference/deliverable-review-checklist.md`. This file is
about the checks the fellow writes and runs.
