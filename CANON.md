---
style: descriptive
---

# CANON — provenance for everything in `library/`

Every file under `library/` came from somewhere. This file records where, and the hash it was at when
it was copied. It exists so the next person can answer **"what has moved upstream since this was cut?"**
with one command instead of an archaeology pass.

Four earlier attempts to share this material — a knowledge-base extraction that halted in March 2026,
and three extractions after it — all failed the same way, and none of them failed for lack of a sync
mechanism. **They failed because nothing recorded what had been cut from what.** That is the only
failure this file is built to prevent. It does not sync anything and does not claim to.

## Columns

| Column | Meaning |
|---|---|
| 1 `component` | Path inside this repository |
| 2 `source_repo` | The repository it came from, or `authored` if it was written for this workspace |
| 3 `source_path` | Where it lives upstream, written relative to your home directory. `-` when authored |
| 4 `cut_commit` | The upstream commit it was taken at. `-` when authored |
| 5 `sha256_at_cut` | Hash of the file **as shipped here**. The gate checks this against the file itself |
| 6 `layer` | Which library layer it belongs to |
| 7 `sha256_at_source` | Hash of the upstream file at the moment of the cut. `-` when authored |

**Columns 5 and 7 differ exactly where this copy carries a deliberate local patch.** That is what the
seventh column is for: a divergence from the source is recorded rather than silent, and anyone can list
the patched files with one comparison. Where they are equal, the file is byte-identical to its source.

## Files this repository patched, and why

Every one was patched for the same class of reason — the upstream file instructed the agent to read
something that lives in a private GitRoll repository and does not ship here, so the instruction resolved
to nothing for the person the copy was given to.

| Component | Why it diverges from its source |
|---|---|
| `library/reference/explanation-style.md` | a confirmation line named an individual and an internal event |
| `library/skills/kb-restructure/SKILL.md` | same repoint; its eval fixtures were built against GitRoll's knowledge base and were not shipped |
| `library/skills/wei-create-skill/SKILL.md` | routed to two doctrine files that did not ship; and its scope, workspace-probe and promotion machinery addressed GitRoll's own repositories and a script in the author's home directory |
| `library/skills/wei-create-skill/references/checklist.md` | same repoint; two checks looked in a home directory |
| `library/skills/wei-create-skill/references/questions.md` | the scope question offered a choice that does not exist here |
| `library/skills/wei-create-skill/references/skeleton.md` | same repoint; the skill-location row named a home directory |
| `library/skills/wei-digest-doc/SKILL.md` | same repoint; its step-0 probe recognised exactly two GitRoll repositories and halted here; the govdoc family and both eval baselines were built from federal contract documents and were not shipped |
| `library/skills/wei-digest-doc/references/routing.md` | the destination table named GitRoll's two repositories; rewritten for this workspace |
| `library/skills/wei-explain/SKILL.md` | routed to a doctrine file that did not ship; repointed to `library/reference/` |
| `library/skills/wei-flowchart/SKILL.md` | same repoint; its first workflow step copied its own scripts out of the author's home directory; its eval fixture was a named client's delivery architecture and was not shipped |

Nothing here was patched to change what a skill teaches.

## Checking what has moved

Run from the repository root, on a machine that has the source repositories checked out:

```bash
bash scripts/canon-check.sh
```

`GONE` means the upstream file was renamed, moved or deleted. `MOVED` means it was edited upstream and
this copy is behind. `LOCAL` means the shipped file no longer matches its own recorded hash, which
should never happen and means somebody edited `library/` in place.

**This script is for whoever maintains the library, not for the fellow.** Run on a machine without
GitRoll's repositories it prints `GONE` for every vendored file, which means "the source is not here",
not "the source was deleted".

## Counts at this cut

| | |
|---|---|
| Rows | 46 |
| Vendored from a source repository | 30 |
| Written for this workspace (`authored`) | 16 |
| Vendored files carrying a local patch | 10 |
| Cut date | 2026-08-11 |

## What this file does NOT do

It does not pull updates, it does not notify anyone, and it does not know whether an upstream change
matters. A `MOVED` row is a question, not an instruction. The mechanism that answers such questions
automatically is being designed separately; this manifest is deliberately usable without it.

## The manifest

```tsv
library/INDEX.md	authored	-	-	4c66e902ed9f8fe961c321d5ba1ba31ebebc72d00044d9bcb919f2254c5eec57	library	-
library/personas/INDEX.md	authored	-	-	8b5455a188a9d5842f08e32a1955ec1fc45db39e4fa54c9379cbc93e86989686	personas	-
library/personas/adversarial-reviewer.md	authored	-	-	adbb0b02e5d845d3f0a53702d0af44bf5e3a9a94c73c41dfa0bad58774515664	personas	-
library/playbooks/INDEX.md	authored	-	-	fe38bbe26ee4178d82f7c8e761ea64f4ba2c04fb6e528a450201e91b702bad58	playbooks	-
library/playbooks/playbook-elicitation-to-sop.md	authored	-	-	a19a2c3e12e8388a45ef13a9655651df3548037fd0a68068d26752277e776cc2	playbooks	-
library/playbooks/playbook-environment-setup.md	authored	-	-	c7b9d854e58bf21628ede8ef57ee2a63e19969cdec85e5fcaca731de3243c452	playbooks	-
library/playbooks/playbook-interview.md	gitroll-dev/curriculum	~/Documents/jobs/gitroll/tasks/gitroll-curriculum.nosync/programs/ai-fellowship/playbooks/playbook-interview.md	2c97511	f4bce3af1552284d2c212fae554f5b1220e101018a7d23b0ee06776556ba5815	playbooks	f4bce3af1552284d2c212fae554f5b1220e101018a7d23b0ee06776556ba5815
library/playbooks/playbook-interview.runbook.md	authored	-	-	52c7eb82b6ea3fa3458a8b4319faaacfcd6fcb8af286d2376775a5f75938d04a	playbooks	-
library/playbooks/playbook-output-phraser.md	authored	-	-	6e06e6fc3114c6d1229af7d5da1e527b9b66bae1daa75e7b059a204104c862de	playbooks	-
library/playbooks/playbook-validator.md	authored	-	-	a2b940b36fe4330cc01b6f9025358fb08d0d91f6d001aada7a7d33e977e32b81	playbooks	-
library/reference/INDEX.md	authored	-	-	ef74418f00e67247bbb8a063be2d81cb5f16bd36a0233787fe99c9c82ff72e4e	reference	-
library/reference/agent-quality-guidelines.md	WeiKuoWei/dotclaude	~/.claude/references/agent-quality-guidelines.md	41bf600	2858e976ea40f034e99c6553ef4a20e7260d87bc5a74aaa713fc0cea9742e9ce	reference	2858e976ea40f034e99c6553ef4a20e7260d87bc5a74aaa713fc0cea9742e9ce
library/reference/explanation-style.md	WeiKuoWei/dotclaude	~/.claude/references/explanation-style.md	41bf600	1715b1be739d8fc79b98c67e888c4480a7b369f72ac33d44e01d58f66713cf39	reference	707357542cbd78e128d171bd3455f3f03b183bdd7b7aa46bbb9d94e14545e885
library/reference/skill-architecture.md	WeiKuoWei/dotclaude	~/.claude/references/skill-architecture.md	41bf600	87fab4d6d0aba33b1f0ca99f3f0fe0fdb1cfaaa5608da47470cbfdd4d994a566	reference	87fab4d6d0aba33b1f0ca99f3f0fe0fdb1cfaaa5608da47470cbfdd4d994a566
library/reference/terminology.md	authored	-	-	81494f982286b827a8349370b0319e444b148f04e6bec7df41d10428ca3201af	reference	-
library/reference/tool-inventory.md	authored	-	-	7630a8556fcd5691859f1d5849c29d35574b5dd8d58286b3e2c6a410825cfde0	reference	-
library/skills/INDEX.md	authored	-	-	f8a7d2b617fa79600642c4df9825e73b7172ce08420392137f435d9cb1892df9	skills	-
library/skills/kb-restructure/SKILL.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/SKILL.md	9e51feb6	f2a15305e2a77c55fb8d7a4eda469de4c4f95d02c6e182796eb05fdd3dffc3e7	skills	9860d9bba894f0c6b94d7ebfc8975b5f27efe5808751283b0d9c890ed9a8a750
library/skills/kb-restructure/references/classification.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/references/classification.md	9e51feb6	32d7e10ce0439a59824e7560d90f565531f49829cdb35cbc1c023f473e48b311	skills	32d7e10ce0439a59824e7560d90f565531f49829cdb35cbc1c023f473e48b311
library/skills/kb-restructure/references/playbook-archive.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/references/playbook-archive.md	9e51feb6	95faf9d6fbe63da86e6a8978a665727a7b8d12bfec1c3268114d1cd20d502d5f	skills	95faf9d6fbe63da86e6a8978a665727a7b8d12bfec1c3268114d1cd20d502d5f
library/skills/kb-restructure/references/playbook-rename.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/references/playbook-rename.md	9e51feb6	f9e8f20039ce85b6161a25e5192230634f2dde968c6ccf892aefbe05e4e58e7a	skills	f9e8f20039ce85b6161a25e5192230634f2dde968c6ccf892aefbe05e4e58e7a
library/skills/kb-restructure/scripts/linkcheck.sh	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/scripts/linkcheck.sh	9e51feb6	37b4564ba3b3813eb74df41196b2280ea22b5fc05d697475c9a0b21b23e8270f	skills	37b4564ba3b3813eb74df41196b2280ea22b5fc05d697475c9a0b21b23e8270f
library/skills/kb-restructure/scripts/refscan.sh	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/scripts/refscan.sh	9e51feb6	5eb49ae2fdd727090bd675a6fb392b08171fcb9f8e119fdbf9ed1256005c4c18	skills	5eb49ae2fdd727090bd675a6fb392b08171fcb9f8e119fdbf9ed1256005c4c18
library/skills/kb-restructure/scripts/symcheck.sh	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/scripts/symcheck.sh	9e51feb6	350f65ab1679fdfa49c6b30f768810da079768934996c313445b77bab19924d8	skills	350f65ab1679fdfa49c6b30f768810da079768934996c313445b77bab19924d8
library/skills/wei-create-skill/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/SKILL.md	41bf600	d0fc4d3c4b0c0084b619ac4a05c830340778b07e4b60be67fbea0374fba8c832	skills	63d75b392243b5a58103eecb14baa6c12038c9d7f180770b163c27524b9a6ea0
library/skills/wei-create-skill/references/checklist.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/references/checklist.md	41bf600	df44dbe5faba336b86b5a51843172e901ab27a679eadc727c521bdc54439d69f	skills	c5e4c08834fa5cfc3a3e35b290b9e1476cb9a51ee311dea7c85d6ff85d52a7b5
library/skills/wei-create-skill/references/questions.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/references/questions.md	41bf600	014451b7d5f7c0aabfac2f347806aa8cf9d3f5b1e169cd256edc5800403c07b8	skills	69db3e6543310ec1d2a8499c9f9f09ec519ea87e84059841afe8df37bc9ad2cc
library/skills/wei-create-skill/references/skeleton.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/references/skeleton.md	41bf600	0376dfc8a5235c473963267f7070a402d3ec7ada861c496653923a60e26ec612	skills	146ee961c50c929380737ee909df1ddfd3423dea79fc5ace39583ffab9053221
library/skills/wei-digest-doc/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/SKILL.md	41bf600	d326a160cc9d41093e31813db3e092f6a4b1ad7b79ac3bceb8dfb44995b22fb1	skills	b8e4182c92a7908021364fa92249175925e58685cf6eef4d104c2b2fdf033bc6
library/skills/wei-digest-doc/references/article-gotchas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/references/article-gotchas.md	41bf600	b243c178d8977f3ca050270a8071a335ca251f01ef559f8504107e8d72bb62fa	skills	b243c178d8977f3ca050270a8071a335ca251f01ef559f8504107e8d72bb62fa
library/skills/wei-digest-doc/references/article-importance-rules.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/references/article-importance-rules.md	41bf600	bb8fc7a34b631e5d4ba40260b2dd6a38ffd3743974217bfaea6d421b40df8cf6	skills	bb8fc7a34b631e5d4ba40260b2dd6a38ffd3743974217bfaea6d421b40df8cf6
library/skills/wei-digest-doc/references/article-schemas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/references/article-schemas.md	41bf600	149ced42e4f73ae93a20e5b2a998bcf6cba317598a05640e4a5acd5c3f9bf7e5	skills	149ced42e4f73ae93a20e5b2a998bcf6cba317598a05640e4a5acd5c3f9bf7e5
library/skills/wei-digest-doc/references/routing.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/references/routing.md	41bf600	735a0a2292921547b5841bfd20853a4f55751376c5954fe8dbd69b4088a010f6	skills	57f1b164f83ca7bd15b9b95c5c2f96053417f0f35baf0b097a9bf9eafda18ee4
library/skills/wei-explain/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-explain/SKILL.md	41bf600	632208245330c7b073b90def488e69fc5c28ac175810643d19ca2caf3965b85c	skills	fd9137c2f1e4460a2040ac51453babf0f901a8c225f2117c3d4bec9f48751ce4
library/skills/wei-flowchart/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/SKILL.md	41bf600	63fcb5771e515e130b2e730961f37fdd2d5bbff3839430818442819360c6fbdd	skills	5f373e652193a5a67b1a61971e691562957faa2f660dd7e02a6a4bed0f799894
library/skills/wei-flowchart/references/gotchas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/references/gotchas.md	41bf600	375ed2910c37b012d7c7a067bcbc576afaa8fd9e0e735601d34fa977fdd75265	skills	375ed2910c37b012d7c7a067bcbc576afaa8fd9e0e735601d34fa977fdd75265
library/skills/wei-flowchart/references/layout.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/references/layout.md	41bf600	5278c7a798b883e579cd434fa544eb9368123d231a9a325b2906b619a5b89e48	skills	5278c7a798b883e579cd434fa544eb9368123d231a9a325b2906b619a5b89e48
library/skills/wei-flowchart/references/symbols.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/references/symbols.md	41bf600	d326852be81c84f5491f9a868b3aac96a4b7eeadfecae13f5a363edf9a56c6c3	skills	d326852be81c84f5491f9a868b3aac96a4b7eeadfecae13f5a363edf9a56c6c3
library/skills/wei-flowchart/scripts/check_map.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/check_map.py	41bf600	7fd6e6a539a90281cb563897fb351a9095fb06e8111916b0372e87b921be6ff2	skills	7fd6e6a539a90281cb563897fb351a9095fb06e8111916b0372e87b921be6ff2
library/skills/wei-flowchart/scripts/layout.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/layout.py	41bf600	dcd2c054268a4ae9c4bdffd1a18807faed70b99c0501237218dae60a00472604	skills	dcd2c054268a4ae9c4bdffd1a18807faed70b99c0501237218dae60a00472604
library/skills/wei-flowchart/scripts/render.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/render.py	41bf600	a3cd8cc799b83d243db9c982a3ae085e9056af31e0e0aa1ab4dbdca9812eb322	skills	a3cd8cc799b83d243db9c982a3ae085e9056af31e0e0aa1ab4dbdca9812eb322
library/skills/wei-flowchart/scripts/render_to.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/render_to.py	41bf600	82c7f4fd89c83a37edc223369d3e52c4f499bd12b9f38053c66da39132638429	skills	82c7f4fd89c83a37edc223369d3e52c4f499bd12b9f38053c66da39132638429
library/skills/wei-flowchart/scripts/shapes.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/shapes.py	41bf600	c93dd10fa42512ce294d8f77727f74e12a4f816dc01d92c739029f901bfcaa7c	skills	c93dd10fa42512ce294d8f77727f74e12a4f816dc01d92c739029f901bfcaa7c
library/sops/INDEX.md	authored	-	-	639706f4ff9a8d02c21e88de68ed402875e1eac9edc1bf137ada0780999065f3	sops	-
library/sops/agent-settings.md	authored	-	-	45bf6e5c2b3df050c73eff9e9c99648f2744c873f127a4a8ad24653267f69ba9	sops	-
library/sops/working-standards.md	authored	-	-	b2a3a8400a795c3aae4ce63d9b66a755940605eb2477665341738340af1143b7	sops	-
```
