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

> Illustrative, not exhaustive. The authoritative divergence list is the block below:
> every row whose column 5 differs from column 7 carries a deliberate local patch.

The original patches replaced instructions that resolve only inside private GitRoll repositories. A
literal pre-pilot walkthrough also found a few invocation and filename mismatches that stop a new Fellow
even when the underlying tools work; those local repairs are called out below.

| Component | Why it diverges from its source |
|---|---|
| `library/reference/explanation-style.md` | a confirmation line named an individual and an internal event |
| `library/renderers/make-the-handover-file.md` | retains the inherited renderer but extends its invalidation rule so a rebuilt owner account also invalidates operational evidence tied to the old package |
| `library/skills/kb-restructure/SKILL.md` | same repoint; its eval fixtures were built against GitRoll's knowledge base and were not shipped |
| `library/skills/create-skill/SKILL.md` | routed to two doctrine files that did not ship; its scope, workspace probe and promotion machinery addressed GitRoll's repositories; the engagement route now tolerates its scaffold, distinguishes authoring from runtime filenames and verifies the installed whole bundle |
| `library/skills/create-skill/references/checklist.md` | repoints unavailable home-directory checks, accepts an explicit library or engagement authoring file and tests a client skill from the documented installed bundle |
| `library/skills/create-skill/references/questions.md` | the scope question offered a choice that does not exist here |
| `library/skills/create-skill/references/skeleton.md` | repoints the home-directory location, distinguishes library and engagement filenames, prevents a client skill from citing workspace-only guidance that does not ship, and documents the verified portability boundary of `argument-hint` |
| `library/skills/digest-doc/SKILL.md` | same repoint; its step-0 probe recognised exactly two GitRoll repositories and halted here; the govdoc family and both eval baselines were built from federal contract documents and were not shipped; its colon-bearing YAML description is quoted so the skill loader can parse it |
| `library/skills/digest-doc/references/routing.md` | the destination table named GitRoll's two repositories; rewritten for this workspace |
| `library/skills/explain/SKILL.md` | routed to a doctrine file that did not ship; repointed to `library/reference/` |
| `library/skills/flowchart/SKILL.md` | same repoint; its first workflow step copied its own scripts out of the author's home directory; its eval fixture was a named client's delivery architecture and was not shipped; the documented render and check commands now pass the paths their shipped scripts require, and the sample defines every referenced node |
| `library/skills/interview-recording/SKILL.md` | quotes a colon-bearing YAML description and requires authorised provider, identity, retention and deletion positions before client audio leaves the workspace; raw provider data stays ignored and derived artifacts follow the engagement boundary |
| `library/skills/interview-recording/references/gotchas.md` | replaces the inherited commit/no-commit shortcut with per-artifact boundary classification and the ignored raw filenames |
| `library/skills/interview-recording/references/refine-and-breakdown.md` | reads the ignored raw transcript and permits tracked, ignored or client-system outputs only as the engagement boundary allows |
| `library/templates/brief-design/SKILL.md` | writes the HTML owner account to the canonical Output Phraser filename instead of an unreferenced alternate name |
| `library/templates/brief-design/reference/anti-patterns.md` | replaces the inherited hosted-font preference with the reviewed portable one-file/offline rule |
| `library/templates/brief-design/reference/base.html` | removes the Google Fonts request and replaces the premature `Handed over` example with a neutral package version |
| `library/templates/brief-design/reference/components.md` | makes the copied header example a candidate prepared for review rather than a false final-state claim |
| `library/templates/brief-design/reference/philosophy.md` | records the local system-font rationale instead of the inherited hosted Geist rationale |
| `library/templates/brief-design/reference/tokens.md` | keeps font tokens consistent with the offline system stack and removes Geist-only settings |
| `library/templates/engagement-notes.md` | keeps the inherited planning shape while making its objective delivery-shape-neutral, placing implementation after the accepted requirements/specification gates and tying `handed-over` to current operational evidence |
| `library/templates/engagement-progress-log.md` | preserves the inherited append-only log while removing a second mutable engagement-status field that could drift from Notes and the Decision Register |
| `library/templates/index-manifest.md` | aligns the inherited recursive “every directory” rule with the shipped repository by defining governed work areas and a parent-inventoried companion/generated/evidence-directory exception |
| `library/templates/process-reconstruction.md` | makes the current-state diagram default and the delivery-shape-neutral specification language agree with the engagement playbooks |

These corrections make existing instructions executable; they do not replace the renderer or redesign
the inherited skills.

## Checking what has moved

Run from the repository root, on a machine that has the source repositories checked out:

```bash
bash .maintainers/canon-check.sh
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
| Rows | 134 |
| Vendored from a source repository | 75 |
| Written for this workspace (`authored`) | 59 |
| Vendored files carrying a local patch | 52 |
| Original cut date | 2026-08-11 |
| Last manifest update | 2026-08-22 |

## What this file does NOT do

It does not pull updates, it does not notify anyone, and it does not know whether an upstream change
matters. A `MOVED` row is a question, not an instruction. The mechanism that answers such questions
automatically is being designed separately; this manifest is deliberately usable without it.

## The manifest

```tsv
library/INDEX.md	authored	-	-	389f9bc31c767557a58423bb11d5ecc5b6705415010d3eac88171419b073172e	library	-
library/personas/INDEX.md	authored	-	-	6e7e6c3fa33d56d760fbac679546fb4aeb9191406b6c63f140fcad4182aa23ff	personas	-
library/personas/adversarial-reviewer.md	authored	-	-	d21a47a2d37774928e7de26798698d0121aa8401ecf4af56199a358ff5f181b3	personas	-
library/personas/non-technical-owner.md	authored	-	-	c7800098fb0dffc484b5b8c681aa09e8f977dcf191e581da8f0bf48e5e6f4152	personas	-
library/playbooks/INDEX.md	authored	-	-	dfa844ecc106fb335912c85c79860c25c2478ec67fcee246281a5001b70d1db8	playbooks	-
library/playbooks/playbook-discovery-to-deliverable.md	authored	-	-	f3a9a7065d873159f84c471997c3b03135a28c3b188a5d9621ce942ed73b82f4	playbooks	-
library/playbooks/playbook-environment-setup.md	authored	-	-	a3d4105e7f3791f9b4db4b74c56882418f3330d398f59c0b9e97656f888902d4	playbooks	-
library/playbooks/playbook-interview.md	gitroll-dev/curriculum	~/Documents/jobs/gitroll/tasks/gitroll-curriculum.nosync/programs/ai-fellowship/playbooks/playbook-interview.md	2c97511	f4bce3af1552284d2c212fae554f5b1220e101018a7d23b0ee06776556ba5815	playbooks	f4bce3af1552284d2c212fae554f5b1220e101018a7d23b0ee06776556ba5815
library/playbooks/playbook-interview.runbook.md	authored	-	-	7d5cefeb8e451df1340e588de9e7a7293290d55070513677b63587455a2c92ca	playbooks	-
library/playbooks/playbook-output-phraser.md	authored	-	-	bc6f3f814e77729901adb63fb5e23561128b630d9fd0ebfa9defaafb87596cbd	playbooks	-
library/playbooks/playbook-validate-deliverable.md	authored	-	-	af0d61d56b5a952a02c54354b48d899154c2071e51ef4e5f33e0e99960eb64a3	playbooks	-
library/playbooks/playbook-validate-handoff.md	authored	-	-	71f41e02241ddde4d5a3e838b8c70dd718217f0c69675423c28b818bd7e30931	playbooks	-
library/reference/INDEX.md	authored	-	-	805245f551328307178e8170ece1184751ab6833d5e9d0cc73e4f2468ea84b90	reference	-
library/reference/agent-quality-guidelines.md	WeiKuoWei/dotclaude	~/.claude/references/agent-quality-guidelines.md	41bf600	1d456ebac204b7d969b5066a9e2c1035b6cbaaaa9f10ed0d7be944d4b666c812	reference	2858e976ea40f034e99c6553ef4a20e7260d87bc5a74aaa713fc0cea9742e9ce
library/reference/deliverable-review-checklist.md	authored	-	-	8c5af4709f25fed8f8b6f42956d75edb1952908871b6fa8a0f2402f64da18cab	reference	-
library/reference/explanation-style.md	WeiKuoWei/dotclaude	~/.claude/references/explanation-style.md	41bf600	5235a4d6fd52a2de4c5632b5f2ac33ed9f13421099ce822986203fd97bbaf9f9	reference	707357542cbd78e128d171bd3455f3f03b183bdd7b7aa46bbb9d94e14545e885
library/reference/skill-architecture.md	WeiKuoWei/dotclaude	~/.claude/references/skill-architecture.md	41bf600	7bbe590050fdd4e833c3e6c9b56938e49ad7a50f0157162f227cd1cb7d852d4b	reference	87fab4d6d0aba33b1f0ca99f3f0fe0fdb1cfaaa5608da47470cbfdd4d994a566
library/reference/terminology.md	authored	-	-	b3972b4bd96a8a2248e92f7825a2bbc549db122e8818233f7d517805f145549f	reference	-
library/reference/tool-inventory.md	authored	-	-	e998c7849f50f17137fc21a2fe0f808763fb095882e8fe6ba4114f93b9382508	reference	-
library/renderers/INDEX.md	authored	-	-	214260a5cc6a828a27e84b2aee188347818b9e2bd32580519aaef7b83ba6b76e	renderers	-
library/renderers/build-document-pdf.py	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/_styles/build_formal_pdf.py	-	6e4adebfd987fe8c092c49cdaa0afecaa381936d158bd2a7689d8b82d7aa8b4e	renderers	155d4a173a4246494f74b2c1c339e8ab48396db045ba5433e9789bc90d38eb3d
library/renderers/check-document-pdf.py	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/_styles/check_formal_pdf.py	-	995a7810a55f4d65384c50bc123a300ef412789b75cc713064baf3b222c4c8c0	renderers	68ac7d1335f877afbca723fd6cbdbdc906bceda02ae8609f512c5623846f2448
library/renderers/make-the-handover-file.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/admin/admin-md-to-docx-conversion.md	-	3d7027bd970033ddd2dbf4bcdb3cf89ab32fc3ff2515a559bda33a56fc19b49e	renderers	8ea65890d45262db6935b0e9c76691280dd5ef53be3a663c7199b72a2d757fd7
library/skills/INDEX.md	authored	-	-	959091744f6d1fa6ecffe9fe27941b3e83fe662fdaabd84793decf57869e69ce	skills	-
library/skills/choose-automation-approach/SKILL.md	authored	-	-	572fafef397512f6be7aa44a0d995e55b0da2c7abfb62cf8ae5e37255f4944e1	skills	-
library/skills/choose-automation-approach/agents/openai.yaml	authored	-	-	108a51c4d4a184bd0478b05ca8aa9d1685dd3111109c468396daa4ac1f22ffcb	skills	-
library/skills/choose-automation-approach/eval/acceptance-criteria.md	authored	-	-	582f5a639b51e5fa6ed10b7833b341702ef27312b6bee10d76921b801d00001d	skills	-
library/skills/choose-automation-approach/eval/baseline-input.md	authored	-	-	dda0f4b0316448c94e5b11b9dc9f027642d872370555395b6d9327711c968cf1	skills	-
library/skills/choose-automation-approach/eval/baseline-output.md	authored	-	-	d5077589394db32279a47b6dc0a067380e5d84e533b20e9d2b72277e8bd8b894	skills	-
library/skills/choose-automation-approach/references/credential-design.md	authored	-	-	bb442c35ca246842995140b3544803a486858540d5f334d9ad68f2e5ffc08cd5	skills	-
library/skills/choose-automation-approach/references/deployment-and-trust.md	authored	-	-	3de556784a2af717c8f227c2a1f51d93dce57c4d14e66431e29c862aba3f0ebf	skills	-
library/skills/choose-automation-approach/references/gotchas.md	authored	-	-	31b44e4cc72f325628744640aa974c77a726f69eb646c915bee8fa9917e98044	skills	-
library/skills/choose-automation-approach/references/high-stakes-actions.md	authored	-	-	06c2d73e7e7296282e730f4f1ea920702ca91fd740866f434eb3ed1e6275a6d2	skills	-
library/skills/choose-automation-approach/references/integration-selection.md	authored	-	-	76cca89ee6909291fdb75f5c79a1bd89fca8b61a5568b2799fae799f2ccfa6e4	skills	-
library/skills/choose-automation-approach/references/interview.md	authored	-	-	4a30278a5a7c1f6b8e60e3962bcecf293fa1cf9ab6d0881b03827946fa5fe99b	skills	-
library/skills/choose-automation-approach/references/output-template.md	authored	-	-	8cd067289851f679a1813da842e614226243b7ff6add1600123295cd9e5352e5	skills	-
library/skills/choose-automation-approach/references/principles.md	authored	-	-	6bcd2c045ccd7884bba1929418355ce93383f00c2bad9c172059d0fc11742651	skills	-
library/skills/create-skill/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/SKILL.md	41bf600	4cd79972d80aaeefc9f99435f17f07100d10defd47b744745923c6b3e88f3cb9	skills	63d75b392243b5a58103eecb14baa6c12038c9d7f180770b163c27524b9a6ea0
library/skills/create-skill/references/checklist.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/references/checklist.md	41bf600	6b15ba1a875f07abebab71ad94548480f1035cb4b60ce8a89bab0d8704f9017a	skills	c5e4c08834fa5cfc3a3e35b290b9e1476cb9a51ee311dea7c85d6ff85d52a7b5
library/skills/create-skill/references/questions.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/references/questions.md	41bf600	a61e97e4b61d25a33533a1ebeeac6176e4a77ceb05f0aafe248231cc8381d470	skills	69db3e6543310ec1d2a8499c9f9f09ec519ea87e84059841afe8df37bc9ad2cc
library/skills/create-skill/references/skeleton.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/references/skeleton.md	41bf600	4acac9a2ee8b5656d89fe63ce763d615fa71cfb02b9d09a34eb6cf232e6994e9	skills	146ee961c50c929380737ee909df1ddfd3423dea79fc5ace39583ffab9053221
library/skills/digest-doc/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/SKILL.md	41bf600	2be2038e881ac675b76da0b465c693c1fbf9eaa1057231b5f1b1e49ce1675da9	skills	b8e4182c92a7908021364fa92249175925e58685cf6eef4d104c2b2fdf033bc6
library/skills/digest-doc/references/article-gotchas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/references/article-gotchas.md	41bf600	46075a9478c892e6bbba32fd8c2235181eb21a46e3642e71e1aeef3b2a1c9515	skills	b243c178d8977f3ca050270a8071a335ca251f01ef559f8504107e8d72bb62fa
library/skills/digest-doc/references/article-importance-rules.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/references/article-importance-rules.md	41bf600	17b853b9d6da4ffe56e4ce1522b66f6c1838c48da81d61495007bd2509c40025	skills	bb8fc7a34b631e5d4ba40260b2dd6a38ffd3743974217bfaea6d421b40df8cf6
library/skills/digest-doc/references/article-schemas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/references/article-schemas.md	41bf600	60e4e3ba77a3ad1d7dc630b94336a87cf7fb79cc913a67195c83b5826f5eccde	skills	149ced42e4f73ae93a20e5b2a998bcf6cba317598a05640e4a5acd5c3f9bf7e5
library/skills/digest-doc/references/routing.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/references/routing.md	41bf600	735a0a2292921547b5841bfd20853a4f55751376c5954fe8dbd69b4088a010f6	skills	57f1b164f83ca7bd15b9b95c5c2f96053417f0f35baf0b097a9bf9eafda18ee4
library/skills/drive-portal/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-drive-portal/SKILL.md	-	18fafdc50188d66f6c7f407c3562146d6de440c196857b485f0a579e7f386171	skills	f5c3565ff73ef79f7016ff37713a903ae26a7dc705ce69e86ca7df8c7f09d21b
library/skills/drive-portal/references/diagnosis.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-drive-portal/references/diagnosis.md	-	dea9ff86ff59eb5c8de94f62b64a4e0b7a36c8997fe3d5db4d7f8091333183a2	skills	cd00bc90ebe5c386da292f229fa247c659acdc5c377b2630e4d9f06e072ca7ac
library/skills/drive-portal/references/form-fill.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-drive-portal/references/form-fill.md	-	b43e2d99ee6471eb5d02fbdcc062b7b04eeebd382a030142232a123c9c8096b1	skills	9da1d43c8fc1cd42647b53297dba951a21f1b88ca95cb7b328ff6ea87194d122
library/skills/drive-portal/references/gotchas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-drive-portal/references/gotchas.md	-	53ebbc2c3c747543f34fa8e47d17b23ab7fc3b08769d5851a17c2dbe6d629544	skills	d1067df85b6477949d356b59e2263597bd3ce3d26077959d05b5e06cd1984203
library/skills/drive-portal/references/reconnaissance.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-drive-portal/references/reconnaissance.md	-	e316d282306c66169707216f11b5afbaf41f26380e6080339a9538a8eec35233	skills	e316d282306c66169707216f11b5afbaf41f26380e6080339a9538a8eec35233
library/skills/drive-portal/references/upload-and-frames.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-drive-portal/references/upload-and-frames.md	-	9ba0503297910bb223e8f93c5724b2149d8594c8921847be358592b1520c4c2f	skills	b737f888bd456963ebe9c6c3fbdc7f04f525a60c0121ec0f3c3bd4d93043df11
library/skills/drive-portal/references/verify-save.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-drive-portal/references/verify-save.md	-	f6bf156e3419968098007aed841eca8a0fb665ecd9285512f0aed51c11162023	skills	e0637a925f1ca8a627327e7b619c32d1ebdd4cdf0f861e54b699c0005db760f9
library/skills/explain/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-explain/SKILL.md	41bf600	bd3ab2293e88cfcb0a3e01fc9ee38e461d84df532a54ab2b7f8a39d8c92b85ce	skills	fd9137c2f1e4460a2040ac51453babf0f901a8c225f2117c3d4bec9f48751ce4
library/skills/flowchart/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/SKILL.md	41bf600	284b2a27825847065417646aa92dd0a4baaec7acdac0555ffa7f1888191ea83b	skills	5f373e652193a5a67b1a61971e691562957faa2f660dd7e02a6a4bed0f799894
library/skills/flowchart/references/gotchas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/references/gotchas.md	41bf600	375ed2910c37b012d7c7a067bcbc576afaa8fd9e0e735601d34fa977fdd75265	skills	375ed2910c37b012d7c7a067bcbc576afaa8fd9e0e735601d34fa977fdd75265
library/skills/flowchart/references/layout.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/references/layout.md	41bf600	5278c7a798b883e579cd434fa544eb9368123d231a9a325b2906b619a5b89e48	skills	5278c7a798b883e579cd434fa544eb9368123d231a9a325b2906b619a5b89e48
library/skills/flowchart/references/symbols.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/references/symbols.md	41bf600	d326852be81c84f5491f9a868b3aac96a4b7eeadfecae13f5a363edf9a56c6c3	skills	d326852be81c84f5491f9a868b3aac96a4b7eeadfecae13f5a363edf9a56c6c3
library/skills/flowchart/scripts/check_map.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/check_map.py	41bf600	7fd6e6a539a90281cb563897fb351a9095fb06e8111916b0372e87b921be6ff2	skills	7fd6e6a539a90281cb563897fb351a9095fb06e8111916b0372e87b921be6ff2
library/skills/flowchart/scripts/layout.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/layout.py	41bf600	dcd2c054268a4ae9c4bdffd1a18807faed70b99c0501237218dae60a00472604	skills	dcd2c054268a4ae9c4bdffd1a18807faed70b99c0501237218dae60a00472604
library/skills/flowchart/scripts/render.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/render.py	41bf600	a3cd8cc799b83d243db9c982a3ae085e9056af31e0e0aa1ab4dbdca9812eb322	skills	a3cd8cc799b83d243db9c982a3ae085e9056af31e0e0aa1ab4dbdca9812eb322
library/skills/flowchart/scripts/render_to.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/render_to.py	41bf600	82c7f4fd89c83a37edc223369d3e52c4f499bd12b9f38053c66da39132638429	skills	82c7f4fd89c83a37edc223369d3e52c4f499bd12b9f38053c66da39132638429
library/skills/flowchart/scripts/shapes.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/shapes.py	41bf600	c93dd10fa42512ce294d8f77727f74e12a4f816dc01d92c739029f901bfcaa7c	skills	c93dd10fa42512ce294d8f77727f74e12a4f816dc01d92c739029f901bfcaa7c
library/skills/interview-recording/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-meeting-plaud/SKILL.md	-	ae936db52390e6ca4d1893a611eb03453976e3b18331a2cd174c1f1c98359957	skills	304b61f4cc5f4dec22965b6dce6e736a43ea3b7472194bd6c568dfa03ae8ac4f
library/skills/interview-recording/references/gotchas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-meeting-plaud/references/gotchas.md	-	e1aca92eb41addc87fe18511d5e1b13ac2423d87c7e4c68d56bc76b26103caf5	skills	5de84867e8715dfcbe7fac306918016b3dd11a30359ed39fb2515e6107ec08ca
library/skills/interview-recording/references/refine-and-breakdown.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-meeting-plaud/references/refine-and-breakdown.md	-	fd848f2c1261c7af356c1495fff14874fcc02cad65de7fd36274a49e70f066f0	skills	c3e2b0b3768e3a7bba9cc0d4002f7619d66af91cdd760e3dddb86d8040c2323b
library/skills/kb-restructure/SKILL.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/SKILL.md	9e51feb6	f967a2183f789ce49f694843d524497b2ac6347b710a5c37806a2599d3ef3d7d	skills	9860d9bba894f0c6b94d7ebfc8975b5f27efe5808751283b0d9c890ed9a8a750
library/skills/kb-restructure/references/classification.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/references/classification.md	9e51feb6	32d7e10ce0439a59824e7560d90f565531f49829cdb35cbc1c023f473e48b311	skills	32d7e10ce0439a59824e7560d90f565531f49829cdb35cbc1c023f473e48b311
library/skills/kb-restructure/references/playbook-archive.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/references/playbook-archive.md	9e51feb6	95faf9d6fbe63da86e6a8978a665727a7b8d12bfec1c3268114d1cd20d502d5f	skills	95faf9d6fbe63da86e6a8978a665727a7b8d12bfec1c3268114d1cd20d502d5f
library/skills/kb-restructure/references/playbook-rename.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/references/playbook-rename.md	9e51feb6	f9e8f20039ce85b6161a25e5192230634f2dde968c6ccf892aefbe05e4e58e7a	skills	f9e8f20039ce85b6161a25e5192230634f2dde968c6ccf892aefbe05e4e58e7a
library/skills/kb-restructure/scripts/linkcheck.sh	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/scripts/linkcheck.sh	9e51feb6	37b4564ba3b3813eb74df41196b2280ea22b5fc05d697475c9a0b21b23e8270f	skills	37b4564ba3b3813eb74df41196b2280ea22b5fc05d697475c9a0b21b23e8270f
library/skills/kb-restructure/scripts/refscan.sh	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/scripts/refscan.sh	9e51feb6	5eb49ae2fdd727090bd675a6fb392b08171fcb9f8e119fdbf9ed1256005c4c18	skills	5eb49ae2fdd727090bd675a6fb392b08171fcb9f8e119fdbf9ed1256005c4c18
library/skills/kb-restructure/scripts/symcheck.sh	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/scripts/symcheck.sh	9e51feb6	350f65ab1679fdfa49c6b30f768810da079768934996c313445b77bab19924d8	skills	350f65ab1679fdfa49c6b30f768810da079768934996c313445b77bab19924d8
library/skills/onboarding/SKILL.md	authored	-	-	ab79a211654da507b32dfdedb0ded6e94be5d4fea17ec58d2f1bee5b60f62962	skills	-
library/skills/onboarding/agents/openai.yaml	authored	-	-	e93135e9cbda606502c6295e0d44978a91c2bf3bbe0a96e6d6b0328f0b889278	skills	-
library/skills/onboarding/references/checks.md	authored	-	-	1d32040befaf2f3f67c56ade3e8cdb68580217058c41f9c63ec32151445de575	skills	-
library/skills/onboarding/references/record-format.md	authored	-	-	fd98fcc58de2661ac8cc7582fdd654af3056b1fbc0d68c2b1d9b1ca6d80e4e72	skills	-
library/skills/scan-agent-skill/SKILL.md	authored	-	-	86dda943037583a8fa8f66432d7fe0c4fc10802ca8762034fa77f13f8fdbcf79	skills	-
library/skills/scan-agent-skill/agents/openai.yaml	authored	-	-	fb413c417dbc9906f22973354aa159136d9aae2cb184dba7854205ae6e6fa672	skills	-
library/skills/scan-agent-skill/scripts/scan.sh	authored	-	-	7eb56cc04b4eddcf0e7d4016c4216c63ccff97ad1fc0249f624569a37e0938ef	skills	-
library/skills/video-to-markdown/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/SKILL.md	-	a124c6ff83c406152fb867b914c14d7e6c2f87e28c9234e9556970b770def918	skills	d31ae309c860953ba8247307507e856669ba3bad8a7193ff921aa14045d0235e
library/skills/video-to-markdown/references/gotchas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/references/gotchas.md	-	307a14571903202f41c7087d6c1eb315750734d8734450519964eeac171bbf4d	skills	873e981206644202220734a31925137c8267a0c2e4fc372c061fb2090a118260
library/skills/video-to-markdown/references/methodology.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/references/methodology.md	-	6fc6fff17278f0a8ba6f670ee023069b4ab8d70d7ad432961d056d7e9ce2abd1	skills	93590fcf40c73b1d17b8baf88ce1c082e25c072b6be48612dcf1a4cc9f20efd9
library/skills/video-to-markdown/references/pipeline.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/references/pipeline.md	-	cdfb0124f6e1a11f90d890855bed8f6f5ce7d11796f30447ceb94d1b9fea0212	skills	d3ce569678e675774aac20a35a5d9b60e39e79a92cd3859d60ff4426f664f033
library/skills/video-to-markdown/scripts/assemble.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/scripts/assemble.py	-	8c9d12bf7a0a29b1d2777a1a6c0370fd8f4a4bb198f0c55d6b54ffdce044e0e7	skills	8c9d12bf7a0a29b1d2777a1a6c0370fd8f4a4bb198f0c55d6b54ffdce044e0e7
library/skills/video-to-markdown/scripts/dedupe_stills.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/scripts/dedupe_stills.py	-	d34842b2cf5adc4a356b45182b095b5bb5c6f77d7fde3a53825db00f104b29e8	skills	d34842b2cf5adc4a356b45182b095b5bb5c6f77d7fde3a53825db00f104b29e8
library/skills/video-to-markdown/scripts/digest_batches.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/scripts/digest_batches.py	-	4039a33064b894604f2802ba1e68ffa35980d08a5c3f279b2da6c6ad045958ca	skills	4039a33064b894604f2802ba1e68ffa35980d08a5c3f279b2da6c6ad045958ca
library/skills/video-to-markdown/scripts/digest_merge.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/scripts/digest_merge.py	-	9ed669cf3960a4c7fe8a6afee9bf1f03af46872fcbd9c8a1f13c511e32800e5d	skills	9ed669cf3960a4c7fe8a6afee9bf1f03af46872fcbd9c8a1f13c511e32800e5d
library/skills/video-to-markdown/scripts/extract_stills.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/scripts/extract_stills.py	-	95a8c165ecc1af64686cb08185cb75829722e52244250a0f09f55664d60b303d	skills	ebb5458bf460e9f60ea0619271cd5a5ca264b8c3c6227cb5a169efd54417b1a7
library/skills/video-to-markdown/scripts/make_sheet.sh	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/scripts/make_sheet.sh	-	e1e6f9750d47f9b7706b682fb4d07fe9ddf19190e10ea9c26f265ad1eee538f2	skills	e1e6f9750d47f9b7706b682fb4d07fe9ddf19190e10ea9c26f265ad1eee538f2
library/skills/video-to-markdown/scripts/render_digest.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/scripts/render_digest.py	-	9876f549a6e30379d4d532aaa54a8e9d26c0ca9610fc0602a08d01905abec85d	skills	9876f549a6e30379d4d532aaa54a8e9d26c0ca9610fc0602a08d01905abec85d
library/skills/video-to-markdown/scripts/render_transcript.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/scripts/render_transcript.py	-	0b4b5a4ae42375569c82cabba26bb39fd7b7d65c4c61867e392f2eabb201a845	skills	0b4b5a4ae42375569c82cabba26bb39fd7b7d65c4c61867e392f2eabb201a845
library/skills/video-to-markdown/scripts/run_session.sh	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/scripts/run_session.sh	-	9faae44c7d6b79f7189946089527ee546d375d18e7a331d0021db9f5b895a7d1	skills	59c70f5a34733beca619bd57d90078b2ec0af2711c8d174b610ab81d3512c2e4
library/skills/video-to-markdown/scripts/sanitize_transcript.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/scripts/sanitize_transcript.py	-	69907129bea8f725ee9c635928f73d7c07ed8ef3a25df5f343614237018a4c54	skills	4598df7b4f0500f76bc4341fc75eb35ffb326c2d72aa837bb0a2c4b40769b036
library/skills/video-to-markdown/scripts/srt_to_transcript.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/scripts/srt_to_transcript.py	-	0483c6670282984b6ef73aa3acd35826d4d4a727b154f95186af11fbaf99640c	skills	049c81526de1add046c6fab43cc81c2366351101fcb3bec782292424574de3f7
library/skills/video-to-markdown/scripts/transcribe_timed.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-video-to-markdown/scripts/transcribe_timed.py	-	0aaa08a501abe26d0a34736e7b92469ecb88794372b7589b8301296b4cbd1c7b	skills	eda2f978e342e1200c0049941279f6981cf55a98b062f679d206e1924b968ab1
library/skills/workspace-help/SKILL.md	authored	-	-	be47bb5951933932362e532b0210e9d7dd5be69d4b25244ed7dfd4b74ccf101a	skills	-
library/skills/workspace-help/agents/openai.yaml	authored	-	-	1ce00af0130218e327348e3c0f6e8308e71c9c126ae805b0d1d08a3d96d72dea	skills	-
library/skills/workspace-help/references/enumeration.md	authored	-	-	9f813806256925ca44b28ec9d7f00930e74271c9c56197abb513dc61769202f8	skills	-
library/skills/youtube-transcript/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-youtube/SKILL.md	-	9485207343cd2e0af1208ca14828edd1058fd9c585aed45d3c33fcd5bf86477a	skills	38a0212abae861066238938ec0f16c8013fc76ba5840cb161ffbc50c2b92a879
library/skills/youtube-transcript/references/setup.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-youtube/references/setup.md	-	bd6ab06fdbddabd6961b4d47f0218464c87460e15d8437d326c252070300f010	skills	b2f56954807229da0e5783e929b71b24c9bf832cedb42f03c8ec794b07873ba7
library/skills/youtube-transcript/scripts/clean_vtt.py	authored	-	-	534fbfda46a4085dcc4903788139fe5db37797ac064e0a5ce26d862c12e7aaf1	skills	-
library/sops/INDEX.md	authored	-	-	639706f4ff9a8d02c21e88de68ed402875e1eac9edc1bf137ada0780999065f3	sops	-
library/sops/agent-settings.md	authored	-	-	1089dac694ca2b6cba0c2d5567aa278b1c62e4d7663b8bde9d334cd6f2e8d0a0	sops	-
library/sops/working-standards.md	authored	-	-	654626a30723e6c01d582ae074f252b63be54221abe941d4123cabfa094d30b4	sops	-
library/templates/INDEX.md	authored	-	-	beec750355669ab13ac482384401259e732b0c16716145c11cbf02a93fb69553	templates	-
library/templates/brief-design/SKILL.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/ray-notion-brief/SKILL.md	-	672a4c831ab64da77845cd0916008ec1b49bcb3e1d8d4e58ec000180211671fc	templates	392615b778d97fe937d8cc7721308b9121dcac4252d5252cd23805aafd7670ad
library/templates/brief-design/reference/anti-patterns.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/ray-notion-brief/reference/anti-patterns.md	-	b6d9020749299b0c3edbc3e7a5dba70deb1ad6ab722313662fec5d74619e4424	templates	f07bc3d7606fedb198e725c17adc0506bb6c10242adbe335ee103cbcc76bbcb4
library/templates/brief-design/reference/base.html	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/ray-notion-brief/reference/base.html	-	af6c7db1c95e48fb09426d1c74c6cd060734c774cdcc42a6367f5714e650207b	templates	09f76303513684fdf480d758e5df6ae8f04a2e3eafd6bdbe8af276bfccf5a002
library/templates/brief-design/reference/components.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/ray-notion-brief/reference/components.md	-	e65a6b24344093d5020f9c32ce2fd07bbffd7991c50a748e303368c5203990e4	templates	c860e9de2f367c6b24a4fc8898e2296b5df8f0745dc20cc025ebb24330e2a464
library/templates/brief-design/reference/composition.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/ray-notion-brief/reference/composition.md	-	ec9f888bbf047b8e18533876be4999fe64bb2d7f3a9b741b44583e8e808fbee5	templates	31ce2ddfbf64462aab4f67719ca233af71cc5311c671b0d9d008c2a5b53c5938
library/templates/brief-design/reference/philosophy.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/ray-notion-brief/reference/philosophy.md	-	5cb943677462ac90c082918867c3efe8cf918d9de4c247a512648895dca19146	templates	b6eea5cf29ad0eb3ade6e1c90f11e9428f624b9241ddc2272660dfc30d8ce7e0
library/templates/brief-design/reference/tokens.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/ray-notion-brief/reference/tokens.md	-	6e014f0b5a92058238f96c16e10c44ce20ab5ce889edd0c7f8297324383154d2	templates	f70d480156dccb312431b036bb8301c9342f11f8870b4397fedd461d34b00325
library/templates/deliverable-deployment.md	authored	-	-	f9e8a454daf10a36c685f0e3c60bbad5c7b0356929bd744912179de862d9738d	templates	-
library/templates/deliverable-operations.md	authored	-	-	9700d49ef3554390547e5a03174e6a86fbe923521eacebe0028408f848adfd2b	templates	-
library/templates/deliverable-validation-report.md	authored	-	-	52ada60eb0b8ae7682477e9791c6938cd4548a7b7307232535b7b00c574ef71d	templates	-
library/templates/engagement-decision-register.md	authored	-	-	85a6d222e1baddd3fc87a338a60fb12d9ad5a1e0fad2fb761c314d1863981d94	templates	-
library/templates/engagement-notes.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/admin/admin-planning-notes.md	-	199fb4e09a84a5bcdc3659cba2427d4932ace9d96def509bdf4f1618109c61af	templates	b1aa6999f1657a4fc2ca719e321432bc69168ccd3924b0d2cdc0483d4fd4cea3
library/templates/engagement-progress-log.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/admin/admin-planning-progress.md	-	49a609265d6c413480e207282da468ba570829ae1ae17cb39f7f13c64929b732	templates	31f3e752e3ab9f02eb9d92202e2f5257dbc4c83b318d4825e423bcf8a885c044
library/templates/handoff-package-manifest.md	authored	-	-	7b803decfffd9bc915eb2740f9267c1f5f0fc3c701d3693e1a3d4e171904c7cd	templates	-
library/templates/handoff-source-map.md	authored	-	-	049f647ee79e10e6b83aff09d9d8d2ef804b010d099bcb79f289fed49e5b6e3e	templates	-
library/templates/handoff-validation-report.md	authored	-	-	17b7127e6e13082e5b9e020b4f5701353f19d61dfb4ba9eea0d61c88f7a8df7e	templates	-
library/templates/handover.md	authored	-	-	cdfb76f0329c995e9c82db951fc3bd34c76ffd07bef49a223267329925927e70	templates	-
library/templates/index-manifest.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/admin/admin-index-manifest.md	-	95cdf121dcfc7e98a4a4ed736f0fdda22a3042d049512270052409f0180203c3	templates	65c45b79453eb8912d174b33bbac4814c6e429090ed3d2ae235628a57fa8368a
library/templates/interview-record.md	authored	-	-	63134e3f01cf7e77d3ab6faa5bd31e32d2ebcb0e20bff03c52cc0fd78bee8370	templates	-
library/templates/operational-acceptance.md	authored	-	-	24ffcd668f3d4b424221bc677356956fec67fce4f6758d13717e7aa2944fb0dc	templates	-
library/templates/owner-acceptance.md	authored	-	-	88afb87aa9b02abc8803f0c22c892c19f79cd59605b1209cc12c25f95c58e5f8	templates	-
library/templates/persona-preflight.md	authored	-	-	7150c18aab84066c6b95d25602dfb1b7559aee69bf60bead3e00cf52024fec05	templates	-
library/templates/process-confirmation.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/comm/comm-client-workflow-confirmation.md	-	cc68c45009a1b871580945d320d57e77ed37e1e85559be86033603ca162d3749	templates	9083831b9957ebc0c091dc488c05e9c70b0a49464ab830f0ea34c843cef5183b
library/templates/process-inventory.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/research/research-workflow-inventory.md	-	70f2b8ab854c34dd303dcd4e257b3c5face8d38e59a25b9c676ddc833c177e38	templates	b5ada5e67b77a359a1f8876a8cce869c6267a5c22b7576eda69ed12ce6886be5
library/templates/process-reconstruction.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/research/research-workflow-step-worksheet.md	-	68a74ea5544f3f299884c410935ee5671b0c675ea74090d1b0988b9db762c5a0	templates	3d4c117da58f122ecd4b287fef0b1d02183c4a483b0ee32ca55e2d23fe71bd1b
library/templates/requirements-gathering.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/comm/comm-client-requirements-gathering.md	-	5792420e6f0091169851dc1f1bda55cf5ac82c45299be931eca976c4ed80efdd	templates	3ea47825b28b62190fdd489bbb3670e873ce8d5720008cdd60679efb78bbc042
library/templates/source-data-survey.md	authored	-	-	45873613ac71daa6b0408c4a39c670037aa2d020c9402f97bc20061bde5bbf4b	templates	-
library/templates/specification.md	authored	-	-	c22e6b833f0b30d715100b155144782c2a689a849ab7a9b917250c8be178a478	templates	-
```
