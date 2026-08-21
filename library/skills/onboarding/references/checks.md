---
style: descriptive
---

# The nineteen checks

One row per checklist item: what verifies it, what a pass looks like, and what the apprentice sees
when it fails. Some have a real command, some are answerable only by the apprentice, and several are
partial — a command narrows the question without settling it.

**Do not count them into a summary and do not repeat a total.** Which items are checkable depends on
the apprentice's machine and on which agent they are using, so any fixed tally is wrong for
somebody.

**Say which kind you are doing.** A reminder confirmed by the apprentice and a check run by a
command are different evidence, and the record keeps them apart.

## Before day one

| Item | Check | Pass looks like |
|---|---|---|
| Read: version control systems | none — reading is not observable | the apprentice says so; record the date |
| Read: Git and GitHub | none | the apprentice says so; record the date |
| Create a GitHub account | partial, and only after the GitHub tool is signed in: `gh api users/<name> --jq .login` | the username echoes back. This proves the account exists, not that it is theirs |
| Send your GitHub username to Ray | none — it is a message on a channel this repository never names | the apprentice says so |

The username gates repository *access*, not the clone: an anonymous `git ls-remote` against a public
repository succeeds. Do not hold up the rest of the session for it.

## Your machine

### The three that fail silently — use these forms, not the obvious ones

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

**The skills symlink — use `test -L`, not `ls`.** This one belongs to the workspace step, not the
machine step: there is nothing to test until the repository has been cloned. It sits here because it
fails in the same silent way as the two above, and it is the third of the three. Run it after the
clone, not before. The link is tracked in git as mode `120000`. On a
Windows checkout without symlink support git writes a **17-byte ordinary text file** containing the
text `../library/skills`. Nothing errors, and the agent then loads **zero skills** — an empty skills
directory is not an error condition. The apprentice can work for a week without the skills this
workspace is built around.

```bash
test -L .claude/skills && echo "symlink OK" || { echo "NOT a symlink; contents:"; cat .claude/skills; }
```

If it is not a symlink, `library/sops/agent-settings.md` gives the fallback: copy the directory
instead — and re-copy after every `git pull`, or what the agent loads and what the library holds
drift apart silently.

**If you take the copy fallback, `test -L` will fail forever after**, correctly and permanently. Do
not keep re-running it and do not record the item as failed. Record it as verified with the note
`copied, not linked — re-copy after every git pull`, so the next session knows the check no longer
applies and knows what the apprentice now owes on every pull.

### The rest

| Item | Check | Notes |
|---|---|---|
| Codex | `ls -d /Applications/ChatGPT.app` on macOS | Partial. There is no `codex` command. The real failure is quieter: the app is installed, the apprentice never finds the mode selector, and uses plain chat for a week. Ask them to confirm they are in Codex mode, not chat |
| Package manager | `brew --version` on macOS | This repository names no package manager for Windows anywhere. On Windows say so and fall back to general practice |
| Code editor | `code --version` | A missing `code` command does not mean a missing editor — in Visual Studio Code the shell command is a separate opt-in step |
| Git | `git --version` | see above |
| GitHub command-line tool | `gh --version` | inside this repository the whole `gh` namespace raises an approval prompt |
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
| Set up session logging on entire.io | none this repository describes — it is named nowhere in the tracked tree | Ask the apprentice to follow the page their trainer gave them and confirm it is running. Do this **first**: it records the whole programme |
| Join Google Classroom | none — joining changes state on Google's servers, not the laptop | Ask for the link the trainer sent. Never store it |
| Join Discord | none — same shape | Ask for the invite the trainer sent. Never store it |
| Set up your workspace | see below | |
| Open Classroom, open one subject, read the first page | none | Record **which subject** — the name is the evidence they got in |
| Put office hours in your calendar | none | Ask; record the date |

### Setting up the workspace

Clone, then check the symlink with `test -L` as above. Then the plugins.

**The plugin block does not behave the way its own introduction describes.** The introduction in
`library/sops/agent-settings.md` says three of the four plugins live in third-party marketplaces
that must be added first. The command block below it contains **five** install commands and only
**two** marketplace-add commands, so three installs run with no marketplace added ahead of them.

**Do not predict which one will fail.** Some of those three resolve from a marketplace that is
already present; which ones do is a property of the apprentice's machine, not of this page. Run the
block in order, one at a time as the page instructs, and record what actually failed.

Treat a failure as expected rather than as the apprentice's mistake. Record what failed and tell
them to report it — this repository asks for library problems to be reported, not repaired in
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
alongside `id` and `enabled`, and the same plugin can appear more than once at different scopes with
*different* `enabled` values. A grep for the plugin name will match a row belonging to some other
project and report a pass. Filter, and say which row you used.

**Read `enabled`, not presence.** Installed-but-disabled is a real state, and a check that only
looks for the name passes it.

**In Codex none of this applies.** These are Claude Code plugins and there is no equivalent. Record
the step as not applicable and move on; nothing else in this skill depends on it.
