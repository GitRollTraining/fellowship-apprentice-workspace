---
style: descriptive
---

# The nineteen checks

One row per checklist item: what verifies it, what a pass looks like, and what the apprentice sees
when it fails. Some have a real command, some are answerable only by the apprentice, and several are
partial — a command narrows the question without settling it.

**The nineteen is fixed; every other number here is not.** The checklist is a frozen roster, so
saying "nineteen items" is safe. How many of them a command can check is not — it depends on the
apprentice's machine and on which agent they are using, so any fixed tally of *checkable* items is
wrong for somebody. Count what is in front of you and do not carry a number between apprentices.

**Say which kind you are doing.** A reminder confirmed by the apprentice and a check run by a
command are different evidence, and the record keeps them apart.

## Before day one

| Item | Check | Pass looks like |
|---|---|---|
| Read: version control systems | none — reading is not observable | the apprentice says so; record the date |
| Read: Git and GitHub | none | the apprentice says so; record the date |
| Create a GitHub account | partial, and only after the GitHub tool is signed in: `gh api users/<name> --jq .login` | the username echoes back. This proves the account exists, not that it is theirs |
| Send your GitHub username to Ray | none — it is a message on a channel this workspace never names | the apprentice says so |

The username gates repository *access*, not this setup. Do not hold up the rest of the session for
it.

## Your machine

### Two checks whose obvious form is wrong — both fail silently

Both pass on a broken machine without printing anything wrong. Read both before running either.

**Git — use `git --version`, never `command -v git`.** On a Mac with no Xcode command line tools
`/usr/bin/git` exists as a shim, so `command -v git` succeeds and prints a path for a machine that
has no git. `git --version` on that machine opens a **graphical dialog** asking to install the
tools, and the terminal blocks until a human clicks it. To the agent this looks like a hang. If a
version check appears to stall, tell the apprentice to look at their screen.

**Git identity — a non-empty answer is not a passing answer.** Two different failures hide here and
the second is the dangerous one.

*Empty.* With nothing set, `git config --global --get user.email` prints nothing and exits 1, with
no message. "No error text" reads as success to a beginner and to a careless agent. It surfaces much
later, at their first commit, as `Author identity unknown`.

*Somebody else's.* On a shared or borrowed machine — or any machine another person set up — these
commands return a real name and a real address belonging to **the wrong person**. That passes an
empty-string test perfectly, and the apprentice's commits then carry someone else's identity.

```bash
git config --global --get user.name
git config --global --get user.email
gh auth status
```

**Show the apprentice the values and ask whether they are theirs. Do not decide it yourself.**

- Empty output — fail.
- A name or address the apprentice does not recognise as their own — fail, and say which value you
  saw. Do not record it as verified because a command exited zero.
- `gh auth status` naming a GitHub account that is not the username they gave you earlier — fail,
  and the same rule applies.

This is the one place in the whole checklist where a green command is weaker evidence than the
apprentice's own eyes.

**The skills symlink check is gone.** The workspace's skills used to reach the agent through a
symlink that a Windows checkout could silently turn into a text file. They now come from the plugin,
so there is nothing to test here; the workspace step checks the plugin and the folder instead
(§ Setting up the workspace, below).

### The rest

| Item | Check | Notes |
|---|---|---|
| Codex | `ls -d /Applications/ChatGPT.app` on macOS | Partial. There is no `codex` command. The real failure is quieter: the app is installed, the apprentice never finds the mode selector, and uses plain chat for a week. Ask them to confirm they are in Codex mode, not chat |
| Package manager | `brew --version` on macOS | This workspace names no package manager for Windows anywhere. On Windows say so and fall back to general practice |
| Code editor | `code --version` | A missing `code` command does not mean a missing editor — in Visual Studio Code the shell command is a separate opt-in step |
| Git | `git --version` | see above |
| GitHub command-line tool | `gh --version` | the agent asks before running `gh` commands |
| Node.js and Python | `node --version` then `python3 --version` | on macOS `python --version` may be absent while `python3` works |
| Git name and email | see above | |
| Sign in to GitHub from the terminal | `gh auth status` | names the account and the scopes. `gh auth login` is interactive and cannot be driven for them |

### One pass over the whole machine

Run the roster in a loop, not as an `&&` chain. A chain stops at the first missing tool and sends a
beginner round three separate install-and-rerun cycles; the loop reports everything in one pass.

```bash
for c in "git --version" "gh --version" "node --version" "python3 --version" "brew --version" "code --version"; do
  out=$(sh -c "$c" 2>&1); rc=$?
  printf '%-14s %-4s %s\n' "${c%% *}" "$([ $rc -eq 0 ] && echo PASS || echo FAIL)" "$(printf '%s' "$out" | head -1)"
done
```

Capture the status from `sh -c` directly. Piping into `head` and then reading `$?` returns the
status of `head`, which turns a missing tool into a pass.

**This pass does not cover everything the machine section lists.** Codex has no version command,
and neither an identity nor a sign-in has a version number. Do not present a clean run of this loop
as proof that the whole machine section is done.

## Day one

| Item | Check | Notes |
|---|---|---|
| Set up session logging on entire.io | `entire status`, run inside the project repository | Do this **first**: it records the whole programme. `entire status` is the only check that runs on the apprentice's machine, and it answers one question, whether logging is wired up. It does not answer whether anything is being recorded. See the note below the table |
| Join Google Classroom | none — joining changes state on Google's servers, not the laptop | Ask for the link the trainer sent. Never store it |
| Join Discord | none — same shape | Ask for the invite the trainer sent. Never store it |
| Set up your workspace | see below | |
| Open Classroom, open one subject, read the first page | none | Record **which subject** — the name is the evidence they got in |
| Put office hours in your calendar | none | Ask; record the date |

**Session logging needs a second check, later, and not on this machine.**

`entire enable` wires logging up and pushes nothing. The branch it writes to,
`entire/checkpoints/v1`, only appears once the apprentice has actually worked with the
agent and pushed. So on day one, a missing branch proves nothing.

That makes "I set it up" unverifiable at onboarding time, and it is one of the three
kinds of evidence the programme assesses. The trainer closes it after the apprentice's
first real working session:

```bash
gh api repos/<their-github-username>/financial-health-brief/branches --jq '[.[].name]'
```

`entire/checkpoints/v1` present means it is recording. Only `main` means the sessions so
far were not captured, and **session logs cannot be reconstructed after the fact**. The
GitHub username is on their row in the Apprentices roster.

### Setting up the workspace

Three checks, in this order.

**The plugin.** This skill ships in the `apprentice-workspace` plugin, so if it is running, the
plugin is installed in the agent in front of you. Record which agent: the ChatGPT app (Codex) or
Claude Code.

**The workspace folder.** At the repository root, both must hold:

```bash
test -f apprentice-workspace/AGENTS.md && grep -q 'apprentice-workspace: start' AGENTS.md && echo "workspace OK"
```

In Windows PowerShell: `(Test-Path apprentice-workspace/AGENTS.md) -and (Select-String -Quiet 'apprentice-workspace: start' AGENTS.md)`.
Anything missing: run the `setup` skill, which adds only what is missing, and check again.

**The plugins in `library/sops/agent-settings.md`.** They come third.

`library/sops/agent-settings.md` lists **two** plugins: `planning-with-files`, which needs its
marketplace added first, and `plugin-dev@claude-plugins-official`, which does not. Its introduction
and its command block agree on that count.

**Do not predict which one will fail.** Whether a marketplace is already present is a property of
the apprentice's machine, not of this page. Run the block in order, one at a time as the page
instructs, and record what actually failed.

Treat a failure as expected rather than as the apprentice's mistake. Record what failed and tell
them to report it — this workspace asks for library problems to be reported, not repaired in
place.

**Checking what actually installed.** The page says the install "cannot be scripted", and the
interactive part is genuinely interactive. The *verification* is not: at Claude Code 2.1.238 a
`claude plugin list --json` command exists and returns one entry per plugin with `id`, `enabled`
and `scope`.

```bash
claude plugin list --json
```

Two traps in reading that output.

**It lists plugins from every project on the machine, not this one.** Each row carries a `scope`
alongside `id` and `enabled`, and the same plugin id can appear more than once — at different
scopes, and also **twice at the same scope with different `enabled` values**. A grep for the plugin
name will match a row belonging to some other project, or the wrong one of a duplicated pair, and
report a pass either way. Filter on the rows, look at every match rather than the first, and say
which one you used and why.

**Read `enabled`, not presence.** Installed-but-disabled is a real state, and a check that only
looks for the name passes it.

**In Codex the command above does not exist.** Ask the apprentice to open the ChatGPT app's plugin
screen and read you what is installed, or run `codex plugin list` if the Codex command-line tool is
installed. A plugin on that page that is not offered for Codex is recorded as not applicable, with
its name in the note. Nothing else in this skill depends on it — but
`library/playbooks/playbook-environment-setup.md` will later refuse to start on missing base
plugins, so flag it to the trainer rather than leaving it as a silent gap.
