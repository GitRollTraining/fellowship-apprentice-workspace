# Form fill — derived fields and per-page event dispatch

Loaded by workflow step 3.

## The rule

**Set the value, fire the handlers the element itself declares, then assert the field you did not
touch.**

Legacy forms compute totals, codes and validation flags in `onkeyup` / `onblur` / `onchange`
attributes on the visible inputs, and write the result into hidden fields. Assigning `.value`
programmatically does not run those handlers, so the hidden field stays empty and the server rejects
the record with an error that names nothing.

```js
const set = (name, val) => {
  const el = w.document.getElementsByName(name)[0];
  el.value = val;
  ['onkeyup','onblur','onchange'].forEach(h => {
    if (el.getAttribute(h)) w.$(el).trigger(h.slice(2));   // jQuery pages only — see below
  });
};
set('unitPrice', 1250); set('quantity', 4); set('deliveryFee', 300);

// ASSERT the derived field, not the ones you set
w.document.getElementsByName('orderTotal')[0].value   // must be non-empty before saving
```

**Read the handler names off the element** rather than guessing which event a framework wants. The
attributes are right there, and guessing produces the exact silent failure this ref exists to prevent.

**Verify the derived field, never the field you set.** The one you set always reads back correctly.
That is not evidence of anything.

## Dispatch is per-page, not per-site

Check the library first (`reconnaissance.md`), because the two rules are opposites and both hosts of
one application can differ:

| Page stack | Correct behaviour | What happens if you get it wrong |
|---|---|---|
| **mootools** | Set `.value` and `.checked` **directly, dispatch nothing.** Forms validate on submit, not on change. | `new Event('change')` **throws** — mootools overwrites the global `Event` constructor. Surfaces as `Cannot read properties of undefined (reading 'test')` from inside `mootools.js`, which reads like a page bug rather than your bug. |
| **jQuery** | You **must** `$(el).trigger('keyup'/'blur'/'change')`. | Derived fields silently stay empty. Save fails with a generic server error. |
| **Neither / plain JS** | Try direct assignment, then assert. If the derived field is empty, call the handler attribute's code directly: `new Function(el.getAttribute('onblur')).call(el)`. | — |

Measured instance: one application spanned two hosts, one serving mootools and the other jQuery. The
same fill code was correct on one and broken on the other.

## Radios, checkboxes and selects

- **Radios:** set `.checked = true` on the specific input, do not assign to the group name.
- **Selects:** set `.value` to the option's `value`, not its visible text. Read the options first —
  legacy portals use opaque codes (`selectedIndex` is a worse choice; option order changes).
- **mootools pages:** `.checked = true` alone is sufficient and correct.

## Order matters when fields gate each other

Some portals only populate a dependent dropdown after the parent field's handler fires. Fill
parent → fire → wait for the dependent's options to appear → fill dependent. Do not fill both in one
pass and assume the second took.

```js
// after firing the parent's handler
await new Promise(r => setTimeout(r, 400));
w.document.getElementsByName('childField')[0].options.length   // > 1 before proceeding
```

## Lookups must go through the portal's own search

Where a field has a Search or Lookup button beside it, **use it.** A hand-typed value that looks
identical may not be linked to the underlying record, and the portal will not say so.

Measured instance: a name typed into a personnel field rather than selected through its lookup left the
field looking correct while silently disabling the notification and document-upload channel that depend
on the account link. The portal's own separate instruction sheet states this; nothing on the form warns
you.

**Generalise:** in any portal, a field with a lookup button is a foreign key. Typing into it creates a
string that resembles a relationship.
