---
name: drive-portal
description: Use when driving a legacy or government web form through the Chrome extension — popup uploads, nested framesets, derived hidden fields, or a save that fails with an error naming nothing.
---

# Drive a Legacy Portal

> Operating procedure for filling and submitting forms on legacy or government web portals with the
> Chrome extension. These portals predate the assumptions the browser tools are built on: uploads open
> popups the extension cannot see, inputs hide inside nested framesets the accessibility tree cannot
> traverse, and totals live in hidden fields the page computes in its own event handlers. Every
> technique here was derived against a live portal, not from documentation.

## When this fires in an engagement

Twice, for different reasons. While **reconstructing** a process that runs through a portal, you drive
the portal to see what the owner sees — which fields are mandatory, which are computed, and where the
process actually stops. While **automating** it, the same procedure is what the delivered skill does.

**A mutation on a client's system is the owner's decision, not yours.** Drive read-only until they say
otherwise, and do the first saving run with them watching.

## Inputs

None. This skill is context-triggered — it fires when you are about to drive a form and carries the
procedure, not a task. The portal, the credentials, and the target form come from the conversation.

## Workflow

1. **Establish the tab before anything else.** Call `tabs_context_mcp` **explicitly** and keep the
   `tabId` — `navigate`'s implicit lookup runs on a shorter budget and fails on its own. If it times
   out twice, stop and ask the user to check the extension side panel; do not retry a third time. If
   login is human-only (captcha, one-time password, hardware key), tell the user to log in **inside the
   tab you opened** — their own tab's session is invisible to you. `references/diagnosis.md`.
2. **Map the page before touching it.** Enumerate frames, detect the JS library, and list the form
   field names. One read now prevents every guess later — `references/reconnaissance.md`.
3. **Fill fields, then fire the handlers the element declares, then assert the DERIVED field.**
   Setting `.value` alone leaves computed totals empty and the save fails with an unnamed error.
   Dispatch rules are per-page, not per-site — `references/form-fill.md`.
4. **Check what an upload control actually is before using it.** A `+Browse` that calls `window.open` is not a
   file input and cannot be driven directly. Route it through the parent page —
   `references/upload-and-frames.md`.
5. **Save behind an alert trap, then verify against the authoritative page.** Trap
   `window.alert`/`confirm` to capture the result, and confirm the change on the list or index page,
   not on the form you just submitted — `references/verify-save.md`.
6. **Diagnose before retrying when something breaks.** The three failure modes look identical from
   outside and have different fixes — `references/diagnosis.md`.

## Gotchas

Sixteen verified failure modes with their triggers and correct behaviour:
**`references/gotchas.md`**. Read it before the first mutating action, not after the first failure.

The four that cost the most time, in short:

- **A list page showing 0 rows is an expired session, not deleted data.** Do not conclude anything was
  destroyed until you have re-authenticated and looked again.
- **`new Event('change')` throws on mootools pages** — mootools overrides the global `Event`
  constructor. Set `.value` / `.checked` directly and dispatch nothing.
- **A stale alert-capture variable reports a failure that already succeeded.** Initialise the capture
  to a sentinel before every run.
- **Assigning `.value` skips the page's own `onkeyup`/`onblur`**, so hidden derived fields stay empty.
  The field you set always reads back fine; that proves nothing.

## Constants

| Key | Value |
|---|---|
| Skill location | `library/skills/drive-portal/`, reached through the `.claude/skills` symlink |
| Companion refs | `references/{reconnaissance,form-fill,upload-and-frames,verify-save,diagnosis,gotchas}.md` |
| Browser tools | `mcp__claude-in-chrome__*` — the Chrome extension, part of this workspace's base set of connected servers |
| Provenance | Derived 2026-07-29/30 against two live public-sector grant portals serving one application, one built on mootools and one on jQuery |

## Output

No artifact. Report, in this order:

1. **What state the portal is now in** — named by the portal's own status string, quoted rather than
   paraphrased (for example "Submitted - pending review", spelled exactly as the page spells it), plus
   the case or record id.
2. **What was verified and how** — which authoritative page was re-read to confirm it.
3. **What is still pending, and on whom** — the human's remaining steps, each with its deadline.
4. **Any new failure mode encountered**, as a candidate line for `references/gotchas.md`.

Never report a mutation as done on the strength of a save handler returning without error.

## Eval

**No eval harness ships with this copy, and this skill could not be automated anyway.** Every portal it
was derived against sits behind a captcha plus a one-time password that only a human can clear, so there
is no canned input a test could replay.

What stands in for it: the build-verify discipline lives inside workflow steps 3 and 5, where it runs on
every real session — assert the derived field before saving, re-read the authoritative page after. Those
two checks are the acceptance criteria for any run. A save handler returning without error is not one.

## Quality Guidelines

Adhere to the quality guidelines in `library/reference/agent-quality-guidelines.md` (runtime behaviour)
and the structural principles in `library/reference/skill-architecture.md`.
