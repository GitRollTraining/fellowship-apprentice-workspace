---
name: scan-agent-skill
description: Scan a local agent skill package for prompt injection, data exfiltration, malicious code, obfuscation, and risky tool use with a pinned security scanner. Use before installing or executing a third-party skill, after modifying a skill, or before handing a skill over. Do not use a clean scan as proof that a skill is safe.
---

# Scan an agent skill

Run a repeatable security check without copying the scanner or its dependencies into the workspace.
The wrapper uses [Cisco AI Skill Scanner `2.0.13`](https://github.com/cisco-ai-defense/skill-scanner/releases/tag/2.0.13),
released under Apache-2.0 at commit `ec7c7f09c38c30af00e145e113b69fae96cbeb1a`.

## Input

Require one local path: a skill directory, `SKILL.md`, or the lowercase `skill.md` used for a Fellow's
deliverable. Download a remote skill for inspection before scanning it; do not scan and execute a
remote repository in one step.

## Workflow

1. Run `scripts/scan.sh <path>` from this skill directory.
2. If the script reports that `skill-scanner` is missing, explain that installation downloads a large
   third-party Python dependency set and writes to the user's pipx tool environment. Ask before running:

   ```bash
   pipx install cisco-ai-skill-scanner==2.0.13
   ```

   If `pipx` itself is unavailable, stop and ask the user how they want Python tools installed. Do not
   choose a system-wide `pip` installation for them.
3. Re-run the wrapper after installation. Keep the default local-only scan. Do not enable LLM,
   VirusTotal, Cisco AI Defense, file uploads, or API keys unless the user explicitly requests and
   approves that separate data flow.
4. Read the detailed Markdown report. Report the command's exit status, each finding's severity and
   evidence path, and a disposition:
   fix, accept with a stated reason, or investigate manually.
5. Inspect the skill manually even when the scanner reports no findings. Check its instructions,
   scripts, hidden files, network destinations, credential access, and destructive operations.

## Interpretation

- A non-zero result means the scan failed or found an issue at the configured threshold; read the
  output before deciding which.
- A finding is evidence to review, not proof of malicious intent.
- No findings means only that this scanner version and policy detected none. It is not certification,
  and it never replaces human review.

## Gotchas

- **Auto-installing the scanner.** The dependency is much larger than this wrapper. Ask before changing
  the user's tool environment.
- **Uploading a client's skill for a stronger scan.** Local scanning is the default. Never send client
  material or hashes to a cloud analyzer without explicit approval.
- **Scanning only `SKILL.md`.** Scripts and bundled resources carry most executable risk. Pass the
  entire skill directory.
- **Treating severity as disposition.** A high-severity false positive still needs a recorded reason;
  a low-severity real exfiltration path still needs repair.

## Quality guidelines

Adhere to:

- `library/reference/agent-quality-guidelines.md` for runtime behavior.
- `library/reference/skill-architecture.md` for structural principles.
