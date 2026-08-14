---
style: descriptive
role: playbook
status: draft — disposable smoke test only; never run on a client engagement
serves: D-01, D-03, D-09, D-12
---

# Set up an engagement environment

Run this at the start of every engagement, before the first owner interview and before client material
enters the fork. The outcome is an engagement ready for safe discovery: its files have a home, its
current decisions have one record, and the limits that matter now are explicit.

This is not Fellow onboarding and it is not production setup. It assumes the repository itself is
already usable. It does not select the final runtime, integration, credential design or high-stakes
controls; it creates those decision areas for later work.

## Inputs

Obtain only what the current stage needs:

- client display name and a kebab-case client slug;
- the process or opportunity in one provisional sentence;
- the business owner and the person authorised to approve access and data handling;
- whether the engagement is `not-started` or `running`;
- the client material and systems that discovery is expected to need;
- the initial time, spend and iteration ceilings, and who may raise them.

Do not request a password, token, API key, recovery code, cookie or other secret value. Record an
identity's name, type, owner, purpose, permission scope and storage mechanism only.

## Preconditions

Do not begin until all of these hold:

1. You are at the root of the Fellow's fork and can read `CLAUDE.md`, `engagements/` and `library/`.
   Missing base plugins, skills or account-level setup is an onboarding problem: report it and stop
   rather than installing a substitute inside a client engagement.
2. One client and one engagement have been named. Do not create a shared directory for several
   clients or put reusable material under a client slug.
3. Someone authorised by the client can rule on workspace data and system access. A Fellow can propose
   a limit; they cannot grant the client permission on the client's behalf.
4. No client material has been copied into a new tracked path. The workspace data boundary is decided
   before ingestion, not inferred from what has already been committed.

## Workflow

### 1. Resolve the target without overwriting it

Normalise the slug to kebab-case and inspect `engagements/<client-slug>/`.

- If it does not exist, this is a new setup.
- If it exists and its `INDEX.md` identifies the same engagement, resume it. Inventory what is already
  present before adding anything.
- If it exists without a readable `INDEX.md`, identifies another engagement or contains unrelated
  material, stop. Never merge or overwrite it based on the slug alone.

### 2. Create the engagement structure

For a new setup, copy the directory shape in `engagements/example-client/` to the resolved slug. Confirm
that `interview/`, `process/`, `spec/`, `deliverable/` and `handover/` each exist with an `INDEX.md`.

Edit the copied root `INDEX.md` so its title, purpose and freshness describe the real engagement. Add
the client directory to `engagements/INDEX.md` in the same operation. Do not leave `example-client` as
the title of a live engagement.

### 3. Initialise the control files

Create these from the marked blocks in their templates:

| File in the engagement root | Template | When |
|---|---|---|
| `notes.md` | `library/templates/engagement-notes.md` | always |
| `decision-register.md` | `library/templates/engagement-decision-register.md` | always |
| `progress-log.md` | `library/templates/engagement-progress-log.md` | only when status is `running` |

Add every created file to the copied engagement `INDEX.md`. For `not-started`, fill only the minimal
notes fields and do not invent a session log. For `running`, fill the firm success criteria and first
runnable slice and create the log.

Keep the Decision Register's field definitions and starter rows. They are the common vocabulary and
initial decision surface, not answers to copy from one client to another.

### 4. Set the engagement workspace boundary before data ingestion

Resolve `EW-001`, `EW-002` and `EW-003` in `decision-register.md` before importing client material or
connecting client systems. Record:

- which data categories may enter the fork;
- which may be Git-tracked, which must use an ignored `*.local.*` path, and which must remain in a
  client-owned system;
- which client-owned identities may be used, their permission scope and storage mechanism;
- who owns retention, deletion and access revocation.

Do not put restricted content in the register. Record that a restriction exists, where it applies and
who can clarify it. Never move one client's data into another client's directory.

The deliverable boundaries are separate. Leave `DP-001` and `DR-001` as `candidate` until discovery and
specification establish what the package and installed runtime require; never assume they inherit the
workspace rule.

### 5. Set the operating baseline for discovery

Resolve the decisions required before the first interview:

- `EW-004`: an action-class autonomy matrix. Reading and writing engagement files, contacting a client,
  changing an external system and deploying are separate action classes, not one autonomy level.
- `EW-005`: time, spend and iteration ceilings plus the person who may raise them.
- `EW-006`: whether discovery needs client systems or connectors. If not, mark it `not-applicable`. If
  it does, name only the minimum current access.

Do not use this step to choose the final automation. Keep `AA-001` through `AA-005` as candidates for
the later `choose-automation-approach` workflow. In particular, lifecycle is a path: record the current
stage, intended trajectory and promotion evidence later instead of treating prototype, pilot and
long-lived operation as permanent alternatives.

### 6. Verify required access without changing client state

For each discovery connector or client system required now:

1. confirm the active identity belongs to or is controlled by the client;
2. confirm the client can revoke it;
3. perform the smallest read-only probe that proves the required source is visible;
4. record what was verified, not the returned client data.

`library/sops/agent-settings.md` explains the connector boundary and how to inspect configured MCP
connections. Do not send a message, edit a record, create production credentials or enable
computer-use merely to prove setup.

### 7. Evaluate the current stage gate

Read every row whose `Required before` value is the current stage or an earlier one.

- A `candidate` does not pass its gate. Confirm whether it is relevant, then mark it `not-applicable`
  or use one of the states for a real decision.
- An `open` row blocks the stage.
- `provisional`, `agreed` and `not-applicable` pass.
- `superseded` passes only when `Current position` names a live replacement ID.

Future-stage candidates do not block current work. A deliverable deployment question is not a reason
to postpone an interview.

### 8. Record the setup result and hand off to discovery

Update the Decision Register's review date and every affected `INDEX.md` freshness row. If the
engagement is `running`, append the first progress entry with what was created, what was verified, the
decision IDs changed, any blocker and the next action.

Report one of these outcomes:

- **ready for interview** — all gates through `interview` pass;
- **structure ready, interview not scheduled** — the engagement remains `not-started` and later gates
  are intentionally unresolved;
- **blocked** — name each blocking decision ID, its owner and the evidence or access still required.

The next procedure is `library/playbooks/playbook-interview.md`, using
`library/playbooks/playbook-interview.runbook.md` for workspace destinations.

## Stop conditions and recovery

| Condition | Stop before | Recovery |
|---|---|---|
| Target slug collides with an unknown or different directory | any write | Choose a different slug or have the owner identify the existing directory; never merge automatically |
| No authorised owner for workspace data or system access | data ingestion | Record the open decision and obtain a client ruling |
| A credential value appears in a tracked file | commit or push | Remove it from the tracked working tree and notify its owner; if it was exposed outside the machine, stop and let the owner decide rotation and history repair |
| Connector is authenticated as the Fellow, the training provider or another client | client access | Disconnect it and obtain a client-controlled identity; do not use a working but wrongly owned connection |
| Required connector is unavailable | the operation that needs it | Keep the decision open. Continue only if the current stage does not require that system |
| Budget, iteration ceiling or current autonomy gate has no owner | first interview | Name the blocker; do not invent approval authority |
| Setup stops after creating only some files | destructive cleanup | Leave the partial directory intact, inventory it, and resume from step 1; never recopy over it |
| Base workspace tooling is missing | client-specific installation | Route to the separate onboarding owner; this playbook does not mutate global setup |

## Completion check

- The target and all five subdirectories have accurate `INDEX.md` files.
- `notes.md` and `decision-register.md` exist, are listed in the root inventory and agree on the
  engagement status.
- `progress-log.md` exists if and only if the engagement is `running`.
- Every decision at or before the current gate passes the register rules.
- Every connector needed now was verified read-only under a client-controlled identity.
- No secret value or disallowed client data was written to a tracked path.
- The output names the exact next action or blocking decision ID.

Passing this check proves only that the engagement is filed and bounded well enough to begin discovery.
It does not approve the eventual automation, package or deployment.
