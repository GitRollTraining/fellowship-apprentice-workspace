---
style: descriptive
---

# Setting up entire.io session logging

> **This file is the source.** It began as a copy of the Notion page "Set up AI Session Log
> collection", which was archived on 2026-08-23 when this became authoritative. Edit here.
> GitRoll's own material, no third-party licence.

---

We use the Entire command-line tool to capture the work history between you and the AI agent, so it
can be reviewed later. You set it up once per repository.

## 1. Install Entire

Pick the line for your machine.

**macOS**

```bash
brew tap entireio/tap && brew trust entireio/tap && brew install --cask entire
```

**Windows**

```bash
scoop bucket add entire https://github.com/entireio/scoop-bucket.git && scoop install entire/cli
```

**Linux**

```bash
curl -LO https://github.com/entireio/cli/releases/latest/download/entire-linux-amd64.tar.gz
tar -xzf entire-linux-amd64.tar.gz
sudo mv entire /usr/local/bin/
```

There is also a one-line installer, `curl -fsSL https://entire.io/install.sh | bash`. It works, and
it is the Linux build. It also fetches a script off the network and runs it in the same breath, so
**an agent will usually decline to run it for you**. That refusal is the agent behaving correctly,
not you doing something wrong. Use the line for your platform above and the agent can install it,
or run the one-liner yourself.

Other installation methods: <https://docs.entire.io/cli/installation>

## 2. Enable it in the repository

```bash
cd your-repo
entire enable
```

Follow the prompts and choose **the agent you actually work in** — Codex, Claude Code, or
OpenCode. Codex is this programme's default and most apprentices choose it; the other two are
allowed and work the same way.

**Choose the one you really use, and do not skip the prompt.** Naming an agent you do not use is a
silent failure: the command succeeds, `entire status` reports the repository enabled, and nothing
is ever captured. Session logs are one of the three kinds of evidence this programme assesses, and
they cannot be reconstructed afterwards. If you are unsure which agent you are in, ask your trainer
before running this rather than guessing.

## 3. Work as usual

From then on each AI session is captured automatically. Secrets and personal data are redacted
automatically, and the session logs are stored on a separate branch, `entire/checkpoints/v1`,
without touching your main branch or your working branch.

## 4. Push

When you push, Entire also pushes the session logs to the remote `entire/checkpoints/v1` branch.
Nothing else to do.

Check the state at any time:

```bash
entire status
```

## Known open question — the ChatGPT desktop application

The published Entire documentation for Codex describes the Codex **command-line tool**. Whether the
same setup covers the **ChatGPT desktop application in Codex mode** is not stated there, and has not
been confirmed for this programme.

This was hit for real on 2026-08-22: an apprentice onboarding in the desktop application found
Entire already installed but the repository not enabled, and the agent correctly refused to enable
it rather than guess at an integration the documentation does not describe. If you are in the
desktop application, ask your trainer before enabling, and record the answer here.

Reference: <https://docs.entire.io/agents/codex>
