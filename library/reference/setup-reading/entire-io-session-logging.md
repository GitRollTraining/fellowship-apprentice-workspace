<!-- MIRROR: do not edit. Re-cut from the source instead. -->
---
style: descriptive
---

# Setting up entire.io session logging

> **This is a copy.** The original is the programme's own Notion page, "Set up AI Session Log
> collection", and it is authoritative; if the two disagree, the original wins. Fetched 2026-08-22.
> It is mirrored here so an agent working offline in this repository can answer the question from
> house material instead of searching the web. GitRoll's own material, no third-party licence.

---

We use the Entire command-line tool to capture the work history between you and the AI agent, so it
can be reviewed later. You set it up once per repository.

## 1. Install Entire

```bash
curl -fsSL https://entire.io/install.sh | bash
```

Other installation methods: <https://docs.entire.io/cli/installation>

## 2. Enable it in the repository

```bash
cd your-repo
entire enable
```

Follow the prompts and choose the agent you use — Codex, Claude Code, or OpenCode.

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
