# Uploads and frames — getting a file into an unreachable input

Loaded by workflow step 4. Two separate obstacles that often appear together.

## Obstacle 1: the upload control is a popup, not a file input

An upload button whose handler calls `openFileDialog(...)` → `window.open(...)` cannot be driven. The
Chrome extension addresses **only tabs inside its own tab group**, so the popup is unreachable — and
forcing it into a tab does not help, because a page-opened tab also lands outside the group.

**Do not open the popup. Do its job from the parent page.**

```js
// 1 — capture the popup URL instead of opening it
const orig = window.open; let cap = null;
window.open = u => { cap = u; return { closed:false, focus(){}, close(){} } };
document.querySelector('a[onclick*="openFileDialog"]').click();
window.open = orig;
if (!cap) throw new Error('no popup URL captured — the handler is not window.open');

// 2 — fetch the popup and read ITS OWN form; never hardcode the endpoint
const doc = new DOMParser().parseFromString(
  await (await fetch(cap, { credentials:'include' })).text(), 'text/html');
const form = doc.querySelector('form');

// 3 — rebuild its multipart body: every hidden field, plus the file
const fd = new FormData();
[...form.elements].filter(e => e.type === 'hidden').forEach(e => fd.append(e.name, e.value));
fd.append('<the file field name from the form>', document.getElementById('agentUpload').files[0]);

// 4 — POST same-origin
const rt = await (await fetch(new URL(form.getAttribute('action'), location.origin).href,
  { method:'POST', body:fd, credentials:'include' })).text();
if (!rt.includes('<the portal\'s success string>')) throw new Error('upload rejected');

// 5 — run the response's OWN callback, with opener bound to this window
const s = rt.indexOf('function fillForm'), e = rt.indexOf('</script>', s);
new Function('opener', rt.slice(s, e) + '\nfillForm();')(window);
```

**Step 5 is what makes this durable.** The response defines a function that writes the new file id into
`opener`'s fields. Parsing the id out and writing the fields yourself bakes in a format assumption that
will drift the next time the portal is touched. Running the site's own function cannot drift.

**Read hidden tokens from a fresh GET every time.** They frequently carry a per-load timestamp or nonce
— the portals this was derived against carry one in a field named `actionId`. Reusing one from an
earlier fetch fails silently.

**Success is the portal's own string, not the HTTP status.** A 200 carrying a re-rendered form with an
error banner is a failure. Assert on the success text.

## Obstacle 2: the input is inside a frameset

The accessibility tree does not traverse nested framesets, so `find` cannot see the input and
`file_upload` has nothing to target.

**Inject the input at the top level, attach there, then move the File across.**

```js
// A — inject into the TOP-LEVEL document, visibly, so file_upload can target it
const i = document.createElement('input');
i.type = 'file'; i.id = 'agentUpload';
i.style.cssText = 'position:fixed;top:8px;left:8px;z-index:99999;background:#ff0;padding:6px';
document.body.appendChild(i);
```

Then use the extension's `file_upload` tool against `#agentUpload`. Then:

```js
// B — transfer the File into the frame's real input (same origin only)
const dt = new DataTransfer();
dt.items.add(document.getElementById('agentUpload').files[0]);
const target = w.document.getElementsByName('<real input name>')[0];
target.files = dt.files;
w.$(target).trigger('change');          // jQuery pages; omit entirely on mootools
```

`DataTransfer` is same-origin only. Across origins there is no path — fall back to asking the user to
attach the file themselves, and say plainly which input.

## When the upload plugin is bound to a grid row

jQuery-fileupload widgets attached to a data grid need a **row selected** before their `add` handler
will run, and the binding is **destroyed by any grid re-render**:

- `Cannot read properties of undefined (reading 'ID')` → no row selected. Select one first
  (`getselectedrowindex`), and note the grid may use a radio rather than a selection API — see
  `gotchas.md`.
- `cannot call methods on fileupload prior to initialization` → the grid re-rendered and orphaned the
  binding. Do not re-initialise it. Bypass the widget entirely: POST the multipart body to the upload
  endpoint, then commit it with the portal's own state parameter on the record page.

Once you are two failures deep into a JS widget, stop debugging it and go around it. The HTTP endpoint
underneath is simpler and more stable than the widget on top.
