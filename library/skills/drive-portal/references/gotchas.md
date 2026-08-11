# Gotchas — drive-portal

Sixteen verified failure modes. Each: trigger / wrong default / correct behaviour. All were observed on
a live portal during 2026-07-29/30, not inferred.

## 1. Assigning `.value` leaves derived fields empty

**Trigger:** any form where a hidden field is computed from visible inputs.
**Wrong default:** set `.value` on each input, click save.
**Correct:** fire the handlers the element declares (`onkeyup`/`onblur`/`onchange`), then assert the
hidden field is non-empty before saving.
**Why:** five consecutive saves returned `Data archived failed. insertError` — an error naming nothing —
because a hidden total was never computed.

## 2. `new Event('change')` throws on mootools pages

**Trigger:** page loads `mootools.js`.
**Wrong default:** construct and dispatch a synthetic event.
**Correct:** set `.value` / `.checked` directly and dispatch nothing.
**Why:** mootools overwrites the global `Event` constructor. The error surfaces as
`Cannot read properties of undefined (reading 'test')` from inside `mootools.js`, which reads like a
page bug rather than yours.

## 3. jQuery pages require the opposite

**Trigger:** page loads jQuery, no mootools.
**Wrong default:** set `.value` and trust it.
**Correct:** `$(el).trigger('keyup')` / `('blur')` / `('change')`.
**Why:** the two rules are opposites and both hosts of one application can differ. One application
spanned a mootools host and a jQuery host; identical fill code was right on one, broken on the other.

## 4. A stale capture variable reports a failure that succeeded

**Trigger:** reading `window.__lastAlert` (or any capture var) across two runs.
**Wrong default:** read it after clicking save.
**Correct:** initialise to a sentinel at the top of every run, then read.
**Why:** a leftover value was read after a save that had in fact succeeded, and the user was told the
save was still failing.

## 5. `confirm` trap that returns nothing cancels the action

**Trigger:** replacing `window.confirm` to capture its message.
**Wrong default:** `w.confirm = m => { cap = m }`.
**Correct:** `w.confirm = m => { cap = m; return true }`.
**Why:** returning `undefined` answers "cancel", so nothing happens and no alert fires — which looks
exactly like a hung page.

## 6. An upload button is often not a file input

**Trigger:** upload control's handler calls `window.open`.
**Wrong default:** `file_upload` against it, or open the popup and drive it.
**Correct:** capture the URL by overriding `window.open`, then POST multipart from the parent page.
See `upload-and-frames.md`.
**Why:** the extension addresses only tabs in its own group. Popups *and* page-opened tabs fall outside.

## 7. The accessibility tree does not traverse framesets

**Trigger:** target input lives inside a nested frameset.
**Wrong default:** `find` for it, conclude it does not exist.
**Correct:** inject a file input at top level, `file_upload` there, move the File in with `DataTransfer`
(same origin only).

## 8. A frameset path is invalidated by any navigation

**Trigger:** an action that reloads the shell.
**Wrong default:** reuse `window.frames[1].frames[3]` from earlier in the session.
**Correct:** re-walk the frame tree after every navigation, and assert an expected field exists as the
first line of every fill.
**Why:** a submit's own redirect overtook a later `navigate`, so a fill ran against the wrong document
and reported success.

## 9. A list showing 0 rows is an expired session

**Trigger:** list page empty, documents come back a few dozen bytes.
**Wrong default:** conclude the data was deleted.
**Correct:** re-authenticate, then look again.
**Why:** an empty list was reported to the user as "everything is deleted". Nothing was.

## 10. jqxGrid row selection is not a selection API

**Trigger:** a `Modify` / `Edit` action on a jqxGrid rejects with "you have not checked the item".
**Wrong default:** call `selectrow`.
**Correct:** tick the grid's own radio input (commonly named `chooseData`), then click the button.

## 11. A fileupload binding is orphaned by a grid re-render

**Trigger:** `cannot call methods on fileupload prior to initialization`.
**Wrong default:** re-initialise the widget.
**Correct:** bypass it — POST the multipart body to the upload endpoint, then commit with the portal's
own state parameter on the record page.
**Why:** two failures deep into a JS widget, the HTTP endpoint underneath is simpler and more stable.

## 12. A field with a lookup button is a foreign key

**Trigger:** a field has a Search or Lookup button beside it.
**Wrong default:** type the value; it looks identical.
**Correct:** always use the lookup and select the record.
**Why:** typing a name into a personnel field rather than selecting it left the field looking correct
while silently disabling the notification and document-upload channel that depend on the account link.
Nothing on the form warns you; only the portal's separate instruction sheet says so.

## 13. A timing-out `tabs_context_mcp` is a human-action state, not a transient one

**Trigger:** `tabs_context_mcp` times out, especially at the start of a session.
**Wrong default:** treat a timeout as transient and retry.
**Correct:** two attempts maximum, then ask the user to check the **extension side panel** for a pending
permission prompt.
**Why:** it was retried five times across fifteen minutes during pairing. The error text said
"waiting on a permission prompt in the extension side panel" every time — a state invisible to the agent
and unresolvable by retrying. See `diagnosis.md` § Retry budget.

## 14. `navigate` without a tabId uses a shorter hidden lookup

**Trigger:** calling `navigate` standalone as the first browser action.
**Wrong default:** rely on its implicit tab lookup.
**Correct:** call `tabs_context_mcp` explicitly first, keep the `tabId`, pass it everywhere.
**Why:** the implicit lookup runs on an 8-second budget and fails independently —
"The hidden tabs_context_mcp lookup did not respond within 8s".

## 15. An MCP reconnect silently unloads every tool schema

**Trigger:** `No such tool available: mcp__claude-in-chrome__javascript_tool` on a tool used
successfully earlier in the same session.
**Wrong default:** conclude the tool was removed or the bridge is broken.
**Correct:** re-fetch with **one batched** `ToolSearch` (`select:a,b,c`), and re-run `tabs_context_mcp`
— any prior tab group is gone too.

## 16. computer-use cannot click in a browser, at any tier

**Trigger:** wanting to click something the extension renders awkwardly.
**Wrong default:** `request_access` for the browser and `left_click`.
**Correct:** browsers are granted at tier **"read"** — screenshots only, no clicks or typing. Confirmed
for Chrome, Arc, Safari. computer-use to SEE, the extension to DRIVE. A re-request does not change the
tier, and the refusal is not a blocker to route around.

## Candidate slot

When a new failure mode is found, add it here in the same shape — trigger, wrong default, correct
behaviour, and the observed incident. A gotcha without an observed incident behind it is speculation:
do not add one from imagination, and do not add a guard for a failure nobody has seen.
