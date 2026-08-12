# Verifying a save

Loaded by workflow step 5. The signature failure of portal automation is a mutation reported as done
that did not persist. Two independent checks, both cheap.

## Check 1: trap the dialog before clicking

Legacy portals report outcomes through `alert()`, and an unhandled dialog **blocks every subsequent
browser command** until a human dismisses it. Trapping it is both the way to read the result and the
way to avoid deadlocking the session.

```js
w.__lastAlert = '(none)';        // <- INITIALISE FIRST. Non-negotiable.
w.alert   = m => { w.__lastAlert = String(m) };
w.confirm = m => { w.__lastAlert = String(m); return true };
w.document.getElementsByName('<save button>')[0].click();
```

Then, after a pause, read `w.__lastAlert`.

**Initialising the sentinel is the whole trick.** A value left over from a previous attempt caused a save
that had actually succeeded to be reported to the user as still broken. Any capture variable read across
two runs must be reset at the top of every run.

**`confirm` must return a value.** A trap that returns `undefined` silently answers "cancel", so the
save never happens and the alert never fires — which looks exactly like a hung page.

## Check 2: re-read the authoritative page

The form you just submitted is not evidence. Navigate to the **list or index page** the portal itself
uses as the record of truth, and confirm:

- the record appears, with the values you set;
- the row count is what you expect — a **duplicate** is as much a failure as a missing row;
- the status string reads what you intended, quoted from the page rather than paraphrased.

A blocked submit that the user retried can land twice. That happened: one record was created under two
different primary keys, and the list page was the only place it was visible.

## Deleting a duplicate

Find the portal's own batch-delete endpoint and post the key. Then **re-read the list again** — a
delete that returns 200 with no success string usually means the session expired mid-operation, not
that the delete worked. See `diagnosis.md`.

## What "done" means before you report it

Report a mutation as complete only when **all** hold:

1. The alert trap captured the portal's success string, not just an absence of errors.
2. The authoritative list page shows the record, once, with the intended status.
3. Any derived field the record depends on is non-empty (`form-fill.md`).
4. If a human step follows (a counter-signature, a forward-to-agency), you have said so and named who
   owns it.

A save handler returning without throwing satisfies none of these.
