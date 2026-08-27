<!-- upstream: library/INDEX.md -->
---
style: descriptive
---

# personas

An agent persona is a role an agent takes for one job, defined precisely enough that two people invoking
it get the same behaviour.

## Inventory

| Persona | Serves | State |
|---|---|---|
| `adversarial-reviewer.md` | verifying output and knowing how it fails [D-05], specification writing [D-06] | shipped, persona #1 |
| `non-technical-owner.md` | constrained cold-reader handoff preflight [D-05, D-29] | authored, persona #2; not yet compared with a real owner |
| `socratic-tutor.md` | tutoring the fellow through their own Stage 1 training work; demonstrates non-directive questioning [D-22] and answer-directed follow-up [D-25] | vendored from NotebookLM's Study Partner and patched in four lines, persona #3; not yet run against a module |
| business-owner simulator | interview domains [D-21 to D-27] | **named, not built** — it needs a case bank, and no case bank exists |

The non-technical-owner persona tests a finished handoff under a strict knowledge boundary; it is not
the still-unbuilt interview-practice simulator. A persona pass never replaces the real owner's check.

The socratic-tutor persona is not that simulator either, and it is the only one here that serves
`training/` rather than an engagement: it plays a teacher so the fellow learns a domain, where the
simulator would play a client so the fellow can practise interviewing one.
