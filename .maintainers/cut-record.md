---
style: descriptive
---

# How the cut was made

Maintainer record. Not part of an apprentice's view; the shipped inventory is
`library/reference/tool-inventory.md`.

## The test

**Does this help a beginner do the engagement?** One test, applied to every candidate.

Three tests were used in the first cut and are RETIRED, because each one deleted useful material for
a reason that does not survive inspection:

| Retired test | What it cost |
|---|---|
| Is it ours or theirs? | Eliminates every artifact-producing tool at once, because we own all of them. The renderers went this way |
| Does it travel? | Treats patchable coupling as disqualifying. Four skills were patched for exactly that coupling in the same round |
| One source of truth | Governs the source knowledge base. An extraction to another organisation is where copying IS the mechanism |

## The pool

Enumerated deterministically across seven scopes rather than listed by hand, because the first cut's
inventory was a hand-written table that ruled 30 of 222 candidates, in two scopes, and named one
skill that does not exist.

| Scope | Candidates |
|---|---|
| `agent-user` | 7 |
| `agent-workspace` | 9 |
| `skill-plugin` | 84 |
| `skill-user` | 27 |
| `skill-workspace` | 17 |
| `sop` | 15 |
| `template` | 87 |
| **total** | **246** |

## The verdicts

| Reason | Count |
|---|---|
| `no-engagement-use` | 180 |
| `helps-beginner` | 38 |
| `superseded` | 24 |
| `needs-credentials` | 2 |
| `cannot-run-elsewhere` | 1 |
| `confidential` | 1 |

**IN 38 / OUT 208.** Full per-candidate table with a reason for each, in the round record.

## Where the reasoning lives

| Artifact | What it holds |
|---|---|
| `verdicts.tsv` | One row per candidate: verdict, reason class, where it ships, and why |
| `adjudication.md` | Every change made to the first-pass ruling after the adversarial reports, and every proposed change rejected |
| `gaps.md` | Needs reported during ruling, and whether shipped material already closes them |

## What is deliberately absent

| Not shipped | Why |
|---|---|
| Anything wired to our own Notion, roadmap or deployment registry | It cannot function without our accounts, and pointing an apprentice at it teaches a dependency they cannot satisfy |
| The meeting pipeline | It runs our transcript records; the interview-recording skill covers the capability without them |
| Repository and software-engineering tooling | The programme's stopping point is a specification and a `skill.md`, not a codebase |
| The slide-deck machinery | Eleven of its fourteen scripts measure a slide canvas; an engagement produces a document, and the two renderers that ship do that better |
| Vendored `eval/` fixtures | Measured leak path: the confidential content in an extraction lives in fixtures and worked examples, not in the prose. The cost is real and is stated below |

## Known cost of that last one

Every vendored skill ships without its evaluation baseline, so a maintainer cannot prove that a
future edit preserved behaviour. Rebuilding baselines from sanitised inputs is the fix and it was
not done here.

## Revalidation

The tool layer turns over roughly annually. **Owner and cadence: unassigned, twelve months.** Without
both, this list ships stale, which is the failure the programme record already named against itself.
