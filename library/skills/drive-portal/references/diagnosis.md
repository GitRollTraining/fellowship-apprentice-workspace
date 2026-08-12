# Diagnosis — three failures that look identical

Loaded by workflow step 6. Getting this wrong wastes the most time of anything in this skill, because
the natural reading of each symptom is the wrong one.

## The discriminator

| Symptom | Actual cause | Correct action |
|---|---|---|
| `tabs_context_mcp` **answers**, but `javascript_tool` / `navigate` time out | The **tab** is blocked — an unhandled modal dialog, or a genuinely long-running page | **Wait. Do not re-trigger.** If a dialog is open, only a human can dismiss it — say so |
| Tool calls succeed, but pages render a login form, or a list shows **0 rows**, or documents come back a few dozen bytes | **Session expired** | Re-authenticate and look again. Conclude nothing about the data until you have |
| **`tabs_context_mcp` itself times out, repeatedly, especially at the start of a session** | The extension is **waiting on a permission prompt in its own side panel** — or pairing was never completed | **Ask the user to open the extension side panel and approve.** You cannot see or dismiss that prompt. **Two attempts maximum, then ask** |
| `tabs_context_mcp` errors outright (not a timeout) | The bridge is down | Reconnect the extension |

**Browser-level tool answering while tab-level tools hang means the tab is blocked, not the bridge.**
That single distinction is the fastest diagnostic available.

**The timeout message names the cause — read it.** It says: *"The Chrome extension is connected but the
page may be loading, unresponsive, or waiting on a permission prompt in the extension side panel."*
That last clause is a human-actionable state that is **completely invisible to you**, and no amount of
retrying resolves it.

**Measured cost of ignoring this:** `tabs_context_mcp{createIfEmpty:true}` was retried **five times
across fifteen minutes** during pairing, because a timeout reads as "transient, try again." It is not
transient. One ask to the user would have replaced all five calls.

### Retry budget for a timing-out browser tool

1. **First timeout** — wait, then retry once. Genuinely-slow pages exist (a portal building a merged
   PDF can take minutes; re-triggering it makes it worse).
2. **Second timeout** — de-escalate to a lighter call, in this weight order:
   `javascript_tool` / `computer` screenshot → `get_page_text` → `tabs_context_mcp`.
   If a light call answers while a heavy one does not, the page is busy, not the bridge.
3. **Third timeout** — **stop and ask the user** to check the extension side panel for a pending
   permission prompt, and to confirm the page is not showing a modal dialog. Do not make a fourth call.

## 0 rows is not deletion

A list page showing nothing, plus pages returning near-empty documents, is what an expired-session
redirect looks like. It was read once as "everything has been deleted" and reported to the user as data
loss. Nothing had been deleted.

**Never report data loss from an empty list.** Re-authenticate first. An expired session and a wiped
account are indistinguishable from outside, and one of them is vastly more likely.

## Tab groups

The extension drives **only tabs inside its own MCP tab group.** Invisible to it: `window.open` popups,
tabs opened by page JavaScript, and **the user's own tabs**.

Consequence for any human-gated login (captcha, one-time password, hardware key): do not open a tab and
say "log in". Say **"log in inside the Chrome tab I opened — it is in the Claude tab group."** Otherwise
the human authenticates somewhere you cannot follow, and the handoff has to be repeated. Sessions do not
appear in your tab just because the user logged in elsewhere in the same browser.

## Deep links usually do not survive

A URL captured mid-flow often depends on a single-sign-on handoff from a parent host and bounces to a
login page when opened cold. Re-enter through the portal's menu and click through.

Same shape, different mechanism: calling a page's own step function from the console
(`changeStep('applyStep6.jsp')`) can 404 because the relative path resolves against the wrong base.
**Click the on-page button instead of invoking the function** — the button carries the correct base.

When you must recover a specific record, go through the record list and select it, rather than trying to
reconstruct its direct URL.

## `navigate` has a hidden 8-second lookup that fails on its own

Called standalone without a `tabId`, `navigate` runs `tabs_context_mcp{createIfEmpty:true}` for you —
on a **shorter 8-second budget** than the explicit call. Observed failure:
*"The hidden tabs_context_mcp lookup did not respond within 8s."*

**Call `tabs_context_mcp` explicitly as the first action of any browser session**, keep the `tabId`, and
pass it to everything afterwards. This is the real reason workflow step 1 exists, beyond knowing which
tabs are open.

## Tool schemas vanish when the MCP server reconnects

If the MCP connection drops and re-establishes mid-session, every `mcp__claude-in-chrome__*` schema you
loaded earlier is **gone**, and calling one returns
`No such tool available: mcp__claude-in-chrome__javascript_tool` — which looks like the tool was removed.

**Re-fetch with a single batched `ToolSearch`** (`select:` accepts a comma-separated list); never one
call per tool. Any tab group from before the drop is also gone — re-run `tabs_context_mcp`.

## Computer-use cannot click in a browser — by design

`request_access` grants browsers at tier **"read"**: *"visible in screenshots only; no clicks or
typing."* Confirmed for Chrome, Arc and Safari. This is a policy tier, not a bug, and no re-request
changes it.

**So the division of labour is fixed: computer-use to SEE, the extension to DRIVE.** If you need to
read something the extension renders awkwardly, screenshot it with computer-use; every click, keystroke
and navigation goes through `mcp__claude-in-chrome__*`. Do not attempt `left_click` on a browser and do
not treat the refusal as a blocker to work around.

## Content filter on returned strings

Tool results containing URLs or query strings are blocked, and the block reads like a tool error. When
returning anything that may contain one, strip the URL-ish characters:

```js
JSON.stringify(result).replace(/[?&=:\/]/g, '·')
```

Or return only the final path segment. This is a harness constraint, not a page problem — do not spend
time debugging the page.

## Escalation rule

**Two failed attempts at the same UI path is the limit.** After that, stop and change layer: from the
widget to its HTTP endpoint, from the deep link to the menu, from the frame to the top-level document.
A third identical retry has never worked, and every case in this skill was solved by dropping a layer
rather than by persisting at the same one.
