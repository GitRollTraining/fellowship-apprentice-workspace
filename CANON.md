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

**Columns 5 and 7 are equal for every vendored file in this cut, and that is the point.** They are kept
separate so a later local edit becomes visible rather than silent: if they ever differ, this repository
has diverged from its source and somebody changed a file they were asked not to change.

## Checking what has moved

Run from the repository root, on a machine that has the source repositories checked out:

```bash
bash scripts/canon-check.sh
```

`GONE` means the upstream file was renamed, moved or deleted. `MOVED` means it was edited upstream and
this copy is behind. Neither is automatically wrong — both are decisions somebody has to make, which is
exactly what the four earlier attempts could not do.

## Counts at this cut

| | |
|---|---|
| Rows | 53 |
| Vendored from a source repository | 40 |
| Written for this workspace (`authored`) | 13 |
| Rows where the shipped hash differs from the source hash | 0 |
| Cut date | 2026-08-11 |

## What this file does NOT do

It does not pull updates, it does not notify anyone, and it does not know whether an upstream change
matters. A `MOVED` row is a question, not an instruction. The mechanism that answers such questions
automatically is being designed separately; this manifest is deliberately usable without it.

## The manifest

```tsv
library/INDEX.md	authored	-	-	b567df72096c440c1a9aa9cdaf9c5ed6e4a593f2c65bb3341dcb2992687ff96c	library	-
library/personas/INDEX.md	authored	-	-	8b5455a188a9d5842f08e32a1955ec1fc45db39e4fa54c9379cbc93e86989686	personas	-
library/personas/adversarial-reviewer.md	authored	-	-	adbb0b02e5d845d3f0a53702d0af44bf5e3a9a94c73c41dfa0bad58774515664	personas	-
library/playbooks/INDEX.md	authored	-	-	fe38bbe26ee4178d82f7c8e761ea64f4ba2c04fb6e528a450201e91b702bad58	playbooks	-
library/playbooks/playbook-elicitation-to-sop.md	authored	-	-	8145f3acdb9e8865b0e980c5020b630ac1f82c48f0301ec103e80bf53f610867	playbooks	-
library/playbooks/playbook-environment-setup.md	authored	-	-	c7b9d854e58bf21628ede8ef57ee2a63e19969cdec85e5fcaca731de3243c452	playbooks	-
library/playbooks/playbook-interview.md	gitroll-dev/curriculum	~/Documents/jobs/gitroll/tasks/gitroll-curriculum.nosync/programs/ai-fellowship/playbooks/playbook-interview.md	2c97511	f4bce3af1552284d2c212fae554f5b1220e101018a7d23b0ee06776556ba5815	playbooks	f4bce3af1552284d2c212fae554f5b1220e101018a7d23b0ee06776556ba5815
library/playbooks/playbook-interview.runbook.md	authored	-	-	41558734560280d33b6d277d2125c4d904ab96ff57ee396eec40e6fb1d14db3f	playbooks	-
library/playbooks/playbook-output-phraser.md	authored	-	-	6e06e6fc3114c6d1229af7d5da1e527b9b66bae1daa75e7b059a204104c862de	playbooks	-
library/playbooks/playbook-validator.md	authored	-	-	a2b940b36fe4330cc01b6f9025358fb08d0d91f6d001aada7a7d33e977e32b81	playbooks	-
library/skills/INDEX.md	authored	-	-	6813c145b1a9d907415b80a29d07b1e0c1284f78a5f875f9b00c0cb5cbe1c50a	skills	-
library/skills/kb-restructure/SKILL.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/SKILL.md	9e51feb6	9860d9bba894f0c6b94d7ebfc8975b5f27efe5808751283b0d9c890ed9a8a750	skills	9860d9bba894f0c6b94d7ebfc8975b5f27efe5808751283b0d9c890ed9a8a750
library/skills/kb-restructure/eval/baseline-input.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/eval/baseline-input.md	9e51feb6	0c2f8be31cbb5006382f34ef40a2538a831bbbba1adeaa94703d48118ab2e387	skills	0c2f8be31cbb5006382f34ef40a2538a831bbbba1adeaa94703d48118ab2e387
library/skills/kb-restructure/eval/baseline-output.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/eval/baseline-output.md	9e51feb6	c93cb542fbc4453fe7139657f625211871ac22b55d2ec93a9c13de8184e5fe94	skills	c93cb542fbc4453fe7139657f625211871ac22b55d2ec93a9c13de8184e5fe94
library/skills/kb-restructure/eval/judgment-cases.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/eval/judgment-cases.md	9e51feb6	941f9fe3b664dec842806d2eb06a487619942198c40cac20c016977042fb65c4	skills	941f9fe3b664dec842806d2eb06a487619942198c40cac20c016977042fb65c4
library/skills/kb-restructure/eval/run-eval.sh	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/eval/run-eval.sh	9e51feb6	6fcb63cdf4ff2277e5017f68597bbbcaff78dd24f582b4cf6a647b0310b1bb18	skills	6fcb63cdf4ff2277e5017f68597bbbcaff78dd24f582b4cf6a647b0310b1bb18
library/skills/kb-restructure/references/classification.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/references/classification.md	9e51feb6	32d7e10ce0439a59824e7560d90f565531f49829cdb35cbc1c023f473e48b311	skills	32d7e10ce0439a59824e7560d90f565531f49829cdb35cbc1c023f473e48b311
library/skills/kb-restructure/references/playbook-archive.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/references/playbook-archive.md	9e51feb6	95faf9d6fbe63da86e6a8978a665727a7b8d12bfec1c3268114d1cd20d502d5f	skills	95faf9d6fbe63da86e6a8978a665727a7b8d12bfec1c3268114d1cd20d502d5f
library/skills/kb-restructure/references/playbook-rename.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/references/playbook-rename.md	9e51feb6	f9e8f20039ce85b6161a25e5192230634f2dde968c6ccf892aefbe05e4e58e7a	skills	f9e8f20039ce85b6161a25e5192230634f2dde968c6ccf892aefbe05e4e58e7a
library/skills/kb-restructure/scripts/linkcheck.sh	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/scripts/linkcheck.sh	9e51feb6	37b4564ba3b3813eb74df41196b2280ea22b5fc05d697475c9a0b21b23e8270f	skills	37b4564ba3b3813eb74df41196b2280ea22b5fc05d697475c9a0b21b23e8270f
library/skills/kb-restructure/scripts/refscan.sh	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/scripts/refscan.sh	9e51feb6	5eb49ae2fdd727090bd675a6fb392b08171fcb9f8e119fdbf9ed1256005c4c18	skills	5eb49ae2fdd727090bd675a6fb392b08171fcb9f8e119fdbf9ed1256005c4c18
library/skills/kb-restructure/scripts/symcheck.sh	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/scripts/symcheck.sh	9e51feb6	350f65ab1679fdfa49c6b30f768810da079768934996c313445b77bab19924d8	skills	350f65ab1679fdfa49c6b30f768810da079768934996c313445b77bab19924d8
library/skills/wei-create-skill/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/SKILL.md	41bf600	63d75b392243b5a58103eecb14baa6c12038c9d7f180770b163c27524b9a6ea0	skills	63d75b392243b5a58103eecb14baa6c12038c9d7f180770b163c27524b9a6ea0
library/skills/wei-create-skill/references/checklist.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/references/checklist.md	41bf600	c5e4c08834fa5cfc3a3e35b290b9e1476cb9a51ee311dea7c85d6ff85d52a7b5	skills	c5e4c08834fa5cfc3a3e35b290b9e1476cb9a51ee311dea7c85d6ff85d52a7b5
library/skills/wei-create-skill/references/questions.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/references/questions.md	41bf600	69db3e6543310ec1d2a8499c9f9f09ec519ea87e84059841afe8df37bc9ad2cc	skills	69db3e6543310ec1d2a8499c9f9f09ec519ea87e84059841afe8df37bc9ad2cc
library/skills/wei-create-skill/references/skeleton.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/references/skeleton.md	41bf600	146ee961c50c929380737ee909df1ddfd3423dea79fc5ace39583ffab9053221	skills	146ee961c50c929380737ee909df1ddfd3423dea79fc5ace39583ffab9053221
library/skills/wei-digest-doc/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/SKILL.md	41bf600	b8e4182c92a7908021364fa92249175925e58685cf6eef4d104c2b2fdf033bc6	skills	b8e4182c92a7908021364fa92249175925e58685cf6eef4d104c2b2fdf033bc6
library/skills/wei-digest-doc/eval/article-baseline-input.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/eval/article-baseline-input.md	41bf600	d94dc67825fd3006a184e2239721406ef65c52aff9c815fc8998f45cbb6ad249	skills	d94dc67825fd3006a184e2239721406ef65c52aff9c815fc8998f45cbb6ad249
library/skills/wei-digest-doc/eval/article-baseline-output.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/eval/article-baseline-output.md	41bf600	039a6650dc2fcf98e6318610f2e11eca9f8fc69ff186b98bb2e2256988ab3427	skills	039a6650dc2fcf98e6318610f2e11eca9f8fc69ff186b98bb2e2256988ab3427
library/skills/wei-digest-doc/eval/baseline-input.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/eval/baseline-input.md	41bf600	65552fd4d3f8c21c1ac3c6dce86782369339c6f728770ab1a394b259c95c1511	skills	65552fd4d3f8c21c1ac3c6dce86782369339c6f728770ab1a394b259c95c1511
library/skills/wei-digest-doc/eval/baseline-output.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/eval/baseline-output.md	41bf600	c8f1d2aabeafbf2d3a0449d1ac8d4758b8d1cbdd2160621744a8f77d588e1da2	skills	c8f1d2aabeafbf2d3a0449d1ac8d4758b8d1cbdd2160621744a8f77d588e1da2
library/skills/wei-digest-doc/references/article-gotchas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/references/article-gotchas.md	41bf600	b243c178d8977f3ca050270a8071a335ca251f01ef559f8504107e8d72bb62fa	skills	b243c178d8977f3ca050270a8071a335ca251f01ef559f8504107e8d72bb62fa
library/skills/wei-digest-doc/references/article-importance-rules.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/references/article-importance-rules.md	41bf600	bb8fc7a34b631e5d4ba40260b2dd6a38ffd3743974217bfaea6d421b40df8cf6	skills	bb8fc7a34b631e5d4ba40260b2dd6a38ffd3743974217bfaea6d421b40df8cf6
library/skills/wei-digest-doc/references/article-schemas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/references/article-schemas.md	41bf600	149ced42e4f73ae93a20e5b2a998bcf6cba317598a05640e4a5acd5c3f9bf7e5	skills	149ced42e4f73ae93a20e5b2a998bcf6cba317598a05640e4a5acd5c3f9bf7e5
library/skills/wei-digest-doc/references/govdoc-gotchas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/references/govdoc-gotchas.md	41bf600	2287b85709dd7d83565dfe775e3be632bbc1d19dd4c87420216dd14d4e48f0c9	skills	2287b85709dd7d83565dfe775e3be632bbc1d19dd4c87420216dd14d4e48f0c9
library/skills/wei-digest-doc/references/govdoc-importance-rules.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/references/govdoc-importance-rules.md	41bf600	d6c4ba2d52c0b762371bd34e0ef962f5a994027b824679af0ecaccb8636b93d0	skills	d6c4ba2d52c0b762371bd34e0ef962f5a994027b824679af0ecaccb8636b93d0
library/skills/wei-digest-doc/references/govdoc-schemas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/references/govdoc-schemas.md	41bf600	8d5155c373255dea6bd6571aca8d6e933218b9e633aa18e2d8fba23d11d26b11	skills	8d5155c373255dea6bd6571aca8d6e933218b9e633aa18e2d8fba23d11d26b11
library/skills/wei-digest-doc/references/routing.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/references/routing.md	41bf600	57f1b164f83ca7bd15b9b95c5c2f96053417f0f35baf0b097a9bf9eafda18ee4	skills	57f1b164f83ca7bd15b9b95c5c2f96053417f0f35baf0b097a9bf9eafda18ee4
library/skills/wei-explain/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-explain/SKILL.md	41bf600	fd9137c2f1e4460a2040ac51453babf0f901a8c225f2117c3d4bec9f48751ce4	skills	fd9137c2f1e4460a2040ac51453babf0f901a8c225f2117c3d4bec9f48751ce4
library/skills/wei-flowchart/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/SKILL.md	41bf600	5f373e652193a5a67b1a61971e691562957faa2f660dd7e02a6a4bed0f799894	skills	5f373e652193a5a67b1a61971e691562957faa2f660dd7e02a6a4bed0f799894
library/skills/wei-flowchart/eval/baseline.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/eval/baseline.md	41bf600	d39181d6eb0f16fdbce92899b8d34e99f6c7ae10a3da97d29a29ad64db69093b	skills	d39181d6eb0f16fdbce92899b8d34e99f6c7ae10a3da97d29a29ad64db69093b
library/skills/wei-flowchart/eval/canonical_spec.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/eval/canonical_spec.py	41bf600	39709a56f037dc3f834310c85e6860132a9ff650514dfed0c65a87aaa77d132b	skills	39709a56f037dc3f834310c85e6860132a9ff650514dfed0c65a87aaa77d132b
library/skills/wei-flowchart/references/gotchas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/references/gotchas.md	41bf600	375ed2910c37b012d7c7a067bcbc576afaa8fd9e0e735601d34fa977fdd75265	skills	375ed2910c37b012d7c7a067bcbc576afaa8fd9e0e735601d34fa977fdd75265
library/skills/wei-flowchart/references/layout.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/references/layout.md	41bf600	5278c7a798b883e579cd434fa544eb9368123d231a9a325b2906b619a5b89e48	skills	5278c7a798b883e579cd434fa544eb9368123d231a9a325b2906b619a5b89e48
library/skills/wei-flowchart/references/symbols.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/references/symbols.md	41bf600	d326852be81c84f5491f9a868b3aac96a4b7eeadfecae13f5a363edf9a56c6c3	skills	d326852be81c84f5491f9a868b3aac96a4b7eeadfecae13f5a363edf9a56c6c3
library/skills/wei-flowchart/scripts/check_map.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/check_map.py	41bf600	7fd6e6a539a90281cb563897fb351a9095fb06e8111916b0372e87b921be6ff2	skills	7fd6e6a539a90281cb563897fb351a9095fb06e8111916b0372e87b921be6ff2
library/skills/wei-flowchart/scripts/layout.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/layout.py	41bf600	dcd2c054268a4ae9c4bdffd1a18807faed70b99c0501237218dae60a00472604	skills	dcd2c054268a4ae9c4bdffd1a18807faed70b99c0501237218dae60a00472604
library/skills/wei-flowchart/scripts/render.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/render.py	41bf600	a3cd8cc799b83d243db9c982a3ae085e9056af31e0e0aa1ab4dbdca9812eb322	skills	a3cd8cc799b83d243db9c982a3ae085e9056af31e0e0aa1ab4dbdca9812eb322
library/skills/wei-flowchart/scripts/render_to.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/render_to.py	41bf600	82c7f4fd89c83a37edc223369d3e52c4f499bd12b9f38053c66da39132638429	skills	82c7f4fd89c83a37edc223369d3e52c4f499bd12b9f38053c66da39132638429
library/skills/wei-flowchart/scripts/shapes.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/shapes.py	41bf600	c93dd10fa42512ce294d8f77727f74e12a4f816dc01d92c739029f901bfcaa7c	skills	c93dd10fa42512ce294d8f77727f74e12a4f816dc01d92c739029f901bfcaa7c
library/sops/INDEX.md	authored	-	-	639706f4ff9a8d02c21e88de68ed402875e1eac9edc1bf137ada0780999065f3	sops	-
library/sops/agent-settings.md	authored	-	-	c945ae7095a7c3ca82b9716167761f31ebb8d459f624e24042de2431eea98f95	sops	-
library/sops/working-standards.md	authored	-	-	b2a3a8400a795c3aae4ce63d9b66a755940605eb2477665341738340af1143b7	sops	-
```
