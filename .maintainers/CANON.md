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

Every one was patched for the same class of reason — the upstream file instructed the agent to read
something that lives in a private GitRoll repository and does not ship here, so the instruction resolved
to nothing for the person the copy was given to.

| Component | Why it diverges from its source |
|---|---|
| `library/reference/explanation-style.md` | a confirmation line named an individual and an internal event |
| `library/skills/kb-restructure/SKILL.md` | same repoint; its eval fixtures were built against GitRoll's knowledge base and were not shipped |
| `library/skills/create-skill/SKILL.md` | routed to two doctrine files that did not ship; and its scope, workspace-probe and promotion machinery addressed GitRoll's own repositories and a script in the author's home directory |
| `library/skills/create-skill/references/checklist.md` | same repoint; two checks looked in a home directory |
| `library/skills/create-skill/references/questions.md` | the scope question offered a choice that does not exist here |
| `library/skills/create-skill/references/skeleton.md` | same repoint; the skill-location row named a home directory |
| `library/skills/digest-doc/SKILL.md` | same repoint; its step-0 probe recognised exactly two GitRoll repositories and halted here; the govdoc family and both eval baselines were built from federal contract documents and were not shipped |
| `library/skills/digest-doc/references/routing.md` | the destination table named GitRoll's two repositories; rewritten for this workspace |
| `library/skills/explain/SKILL.md` | routed to a doctrine file that did not ship; repointed to `library/reference/` |
| `library/skills/flowchart/SKILL.md` | same repoint; its first workflow step copied its own scripts out of the author's home directory; its eval fixture was a named client's delivery architecture and was not shipped |

Nothing here was patched to change what a skill teaches.

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
| Rows | 113 |
| Vendored from a source repository | 75 |
| Written for this workspace (`authored`) | 38 |
| Vendored files carrying a local patch | 52 |
| Original cut date | 2026-08-11 |
| Last manifest update | 2026-08-14 |

## What this file does NOT do

It does not pull updates, it does not notify anyone, and it does not know whether an upstream change
matters. A `MOVED` row is a question, not an instruction. The mechanism that answers such questions
automatically is being designed separately; this manifest is deliberately usable without it.

## The manifest

```tsv
library/INDEX.md	authored	-	-	6bc0b9508dcb23cd73f195f8bedf640ef5594f18f8335e2208c8c61e26650bba	library	-
library/personas/INDEX.md	authored	-	-	8b5455a188a9d5842f08e32a1955ec1fc45db39e4fa54c9379cbc93e86989686	personas	-
library/personas/adversarial-reviewer.md	authored	-	-	2f032ac6d2b37faa0fac06128458e7db1681a7ee2e904f0933af9cd04f299e2c	personas	-
library/playbooks/INDEX.md	authored	-	-	e7eb02f7708f868c20fb3c9e6f68342280991bc466f78b181828e5cd9ea2cb35	playbooks	-
library/playbooks/playbook-elicitation-to-sop.md	authored	-	-	a19a2c3e12e8388a45ef13a9655651df3548037fd0a68068d26752277e776cc2	playbooks	-
library/playbooks/playbook-environment-setup.md	authored	-	-	c7b9d854e58bf21628ede8ef57ee2a63e19969cdec85e5fcaca731de3243c452	playbooks	-
library/playbooks/playbook-interview.md	gitroll-dev/curriculum	~/Documents/jobs/gitroll/tasks/gitroll-curriculum.nosync/programs/ai-fellowship/playbooks/playbook-interview.md	2c97511	f4bce3af1552284d2c212fae554f5b1220e101018a7d23b0ee06776556ba5815	playbooks	f4bce3af1552284d2c212fae554f5b1220e101018a7d23b0ee06776556ba5815
library/playbooks/playbook-interview.runbook.md	authored	-	-	aae146951fa79bcc20cf218a44377a627e48d1517545a0cd7b8a935c83b6a061	playbooks	-
library/playbooks/playbook-output-phraser.md	authored	-	-	6e06e6fc3114c6d1229af7d5da1e527b9b66bae1daa75e7b059a204104c862de	playbooks	-
library/playbooks/playbook-validator.md	authored	-	-	a2b940b36fe4330cc01b6f9025358fb08d0d91f6d001aada7a7d33e977e32b81	playbooks	-
library/reference/INDEX.md	authored	-	-	d59c2cd35cb333bb1aa8a16c851f0cf3896e43db970c42badc9f89c398ee1e0a	reference	-
library/reference/agent-quality-guidelines.md	WeiKuoWei/dotclaude	~/.claude/references/agent-quality-guidelines.md	41bf600	1d456ebac204b7d969b5066a9e2c1035b6cbaaaa9f10ed0d7be944d4b666c812	reference	2858e976ea40f034e99c6553ef4a20e7260d87bc5a74aaa713fc0cea9742e9ce
library/reference/explanation-style.md	WeiKuoWei/dotclaude	~/.claude/references/explanation-style.md	41bf600	5235a4d6fd52a2de4c5632b5f2ac33ed9f13421099ce822986203fd97bbaf9f9	reference	707357542cbd78e128d171bd3455f3f03b183bdd7b7aa46bbb9d94e14545e885
library/reference/skill-architecture.md	WeiKuoWei/dotclaude	~/.claude/references/skill-architecture.md	41bf600	7bbe590050fdd4e833c3e6c9b56938e49ad7a50f0157162f227cd1cb7d852d4b	reference	87fab4d6d0aba33b1f0ca99f3f0fe0fdb1cfaaa5608da47470cbfdd4d994a566
library/reference/terminology.md	authored	-	-	312132e73cb628057857267d243b71ad16be3a44756568221be19063ff8d75c8	reference	-
library/reference/tool-inventory.md	authored	-	-	5b4e4cd9cee04667876b4d4237f6b6a25ca55316a02045a9b0e019bb16d76ed9	reference	-
library/renderers/INDEX.md	authored	-	-	11f394e257f2db313ef09822413905eee3043c8ecbaac0672463a3087d3932ed	renderers	-
library/renderers/build-document-pdf.py	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/_styles/build_formal_pdf.py	-	ce7f30691d38a484e784f2c5f2f4ea710a24eb07db7246ac90c5cbb03d0a30bf	renderers	155d4a173a4246494f74b2c1c339e8ab48396db045ba5433e9789bc90d38eb3d
library/renderers/check-document-pdf.py	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/_styles/check_formal_pdf.py	-	995a7810a55f4d65384c50bc123a300ef412789b75cc713064baf3b222c4c8c0	renderers	68ac7d1335f877afbca723fd6cbdbdc906bceda02ae8609f512c5623846f2448
library/renderers/make-the-handover-file.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/admin/admin-md-to-docx-conversion.md	-	f753750e67fbbc5a08291e752eeabfa0553b1823c0b4611a4ddbb4cad7a0c177	renderers	8ea65890d45262db6935b0e9c76691280dd5ef53be3a663c7199b72a2d757fd7
library/skills/INDEX.md	authored	-	-	8667145bbec29e834ebf36de2596edcde5e2fed255966f26a5f5217add3cf4e2	skills	-
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
library/skills/create-skill/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/SKILL.md	41bf600	cc17a30e180a54393e078183f9be612fa9e762105278135e2de0cd51aa611448	skills	63d75b392243b5a58103eecb14baa6c12038c9d7f180770b163c27524b9a6ea0
library/skills/create-skill/references/checklist.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/references/checklist.md	41bf600	8ae68ae8b7a7fe85cccbdcaa43d6734f02805f88aa8d3ea92ec68e10b9841446	skills	c5e4c08834fa5cfc3a3e35b290b9e1476cb9a51ee311dea7c85d6ff85d52a7b5
library/skills/create-skill/references/questions.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/references/questions.md	41bf600	a61e97e4b61d25a33533a1ebeeac6176e4a77ceb05f0aafe248231cc8381d470	skills	69db3e6543310ec1d2a8499c9f9f09ec519ea87e84059841afe8df37bc9ad2cc
library/skills/create-skill/references/skeleton.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-create-skill/references/skeleton.md	41bf600	0376dfc8a5235c473963267f7070a402d3ec7ada861c496653923a60e26ec612	skills	146ee961c50c929380737ee909df1ddfd3423dea79fc5ace39583ffab9053221
library/skills/digest-doc/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-digest-doc/SKILL.md	41bf600	c94e865160cbc3905c8dae58ddf093ed5124b41516746da9dec70e3481ec2511	skills	b8e4182c92a7908021364fa92249175925e58685cf6eef4d104c2b2fdf033bc6
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
library/skills/flowchart/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/SKILL.md	41bf600	9185d66e38a1bddcf504f81f8796cea5fcb3942d2fb98756f794b289ec94c903	skills	5f373e652193a5a67b1a61971e691562957faa2f660dd7e02a6a4bed0f799894
library/skills/flowchart/references/gotchas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/references/gotchas.md	41bf600	375ed2910c37b012d7c7a067bcbc576afaa8fd9e0e735601d34fa977fdd75265	skills	375ed2910c37b012d7c7a067bcbc576afaa8fd9e0e735601d34fa977fdd75265
library/skills/flowchart/references/layout.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/references/layout.md	41bf600	5278c7a798b883e579cd434fa544eb9368123d231a9a325b2906b619a5b89e48	skills	5278c7a798b883e579cd434fa544eb9368123d231a9a325b2906b619a5b89e48
library/skills/flowchart/references/symbols.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/references/symbols.md	41bf600	d326852be81c84f5491f9a868b3aac96a4b7eeadfecae13f5a363edf9a56c6c3	skills	d326852be81c84f5491f9a868b3aac96a4b7eeadfecae13f5a363edf9a56c6c3
library/skills/flowchart/scripts/check_map.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/check_map.py	41bf600	7fd6e6a539a90281cb563897fb351a9095fb06e8111916b0372e87b921be6ff2	skills	7fd6e6a539a90281cb563897fb351a9095fb06e8111916b0372e87b921be6ff2
library/skills/flowchart/scripts/layout.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/layout.py	41bf600	dcd2c054268a4ae9c4bdffd1a18807faed70b99c0501237218dae60a00472604	skills	dcd2c054268a4ae9c4bdffd1a18807faed70b99c0501237218dae60a00472604
library/skills/flowchart/scripts/render.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/render.py	41bf600	a3cd8cc799b83d243db9c982a3ae085e9056af31e0e0aa1ab4dbdca9812eb322	skills	a3cd8cc799b83d243db9c982a3ae085e9056af31e0e0aa1ab4dbdca9812eb322
library/skills/flowchart/scripts/render_to.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/render_to.py	41bf600	82c7f4fd89c83a37edc223369d3e52c4f499bd12b9f38053c66da39132638429	skills	82c7f4fd89c83a37edc223369d3e52c4f499bd12b9f38053c66da39132638429
library/skills/flowchart/scripts/shapes.py	WeiKuoWei/dotclaude	~/.claude/skills/wei-flowchart/scripts/shapes.py	41bf600	c93dd10fa42512ce294d8f77727f74e12a4f816dc01d92c739029f901bfcaa7c	skills	c93dd10fa42512ce294d8f77727f74e12a4f816dc01d92c739029f901bfcaa7c
library/skills/interview-recording/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-meeting-plaud/SKILL.md	-	6d0f9e69194405cbfd33a14b3cf22c8fa75a7d75d98561494bbaaa266139fd2c	skills	304b61f4cc5f4dec22965b6dce6e736a43ea3b7472194bd6c568dfa03ae8ac4f
library/skills/interview-recording/references/gotchas.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-meeting-plaud/references/gotchas.md	-	fe7e7b9b068ae28524c6d1b4ac96f96c7bef051786c50c5834bcd5ceb0d417c9	skills	5de84867e8715dfcbe7fac306918016b3dd11a30359ed39fb2515e6107ec08ca
library/skills/interview-recording/references/refine-and-breakdown.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-meeting-plaud/references/refine-and-breakdown.md	-	b6f409611668559d17056a5856472a97ecde4f40ab7a4331c347708bfef5ab9f	skills	c3e2b0b3768e3a7bba9cc0d4002f7619d66af91cdd760e3dddb86d8040c2323b
library/skills/kb-restructure/SKILL.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/SKILL.md	9e51feb6	f967a2183f789ce49f694843d524497b2ac6347b710a5c37806a2599d3ef3d7d	skills	9860d9bba894f0c6b94d7ebfc8975b5f27efe5808751283b0d9c890ed9a8a750
library/skills/kb-restructure/references/classification.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/references/classification.md	9e51feb6	32d7e10ce0439a59824e7560d90f565531f49829cdb35cbc1c023f473e48b311	skills	32d7e10ce0439a59824e7560d90f565531f49829cdb35cbc1c023f473e48b311
library/skills/kb-restructure/references/playbook-archive.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/references/playbook-archive.md	9e51feb6	95faf9d6fbe63da86e6a8978a665727a7b8d12bfec1c3268114d1cd20d502d5f	skills	95faf9d6fbe63da86e6a8978a665727a7b8d12bfec1c3268114d1cd20d502d5f
library/skills/kb-restructure/references/playbook-rename.md	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/references/playbook-rename.md	9e51feb6	f9e8f20039ce85b6161a25e5192230634f2dde968c6ccf892aefbe05e4e58e7a	skills	f9e8f20039ce85b6161a25e5192230634f2dde968c6ccf892aefbe05e4e58e7a
library/skills/kb-restructure/scripts/linkcheck.sh	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/scripts/linkcheck.sh	9e51feb6	37b4564ba3b3813eb74df41196b2280ea22b5fc05d697475c9a0b21b23e8270f	skills	37b4564ba3b3813eb74df41196b2280ea22b5fc05d697475c9a0b21b23e8270f
library/skills/kb-restructure/scripts/refscan.sh	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/scripts/refscan.sh	9e51feb6	5eb49ae2fdd727090bd675a6fb392b08171fcb9f8e119fdbf9ed1256005c4c18	skills	5eb49ae2fdd727090bd675a6fb392b08171fcb9f8e119fdbf9ed1256005c4c18
library/skills/kb-restructure/scripts/symcheck.sh	WeiKuoWei/gitroll-operations	~/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/kb-restructure/scripts/symcheck.sh	9e51feb6	350f65ab1679fdfa49c6b30f768810da079768934996c313445b77bab19924d8	skills	350f65ab1679fdfa49c6b30f768810da079768934996c313445b77bab19924d8
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
library/skills/youtube-transcript/SKILL.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-youtube/SKILL.md	-	9485207343cd2e0af1208ca14828edd1058fd9c585aed45d3c33fcd5bf86477a	skills	38a0212abae861066238938ec0f16c8013fc76ba5840cb161ffbc50c2b92a879
library/skills/youtube-transcript/references/setup.md	WeiKuoWei/dotclaude	~/.claude/skills/wei-youtube/references/setup.md	-	bd6ab06fdbddabd6961b4d47f0218464c87460e15d8437d326c252070300f010	skills	b2f56954807229da0e5783e929b71b24c9bf832cedb42f03c8ec794b07873ba7
library/skills/youtube-transcript/scripts/clean_vtt.py	authored	-	-	534fbfda46a4085dcc4903788139fe5db37797ac064e0a5ce26d862c12e7aaf1	skills	-
library/sops/INDEX.md	authored	-	-	639706f4ff9a8d02c21e88de68ed402875e1eac9edc1bf137ada0780999065f3	sops	-
library/sops/agent-settings.md	authored	-	-	890ed829d286e93fdf18e44dba7801ec9121f39f8cbe8bc333dc678c7ad1a997	sops	-
library/sops/working-standards.md	authored	-	-	654626a30723e6c01d582ae074f252b63be54221abe941d4123cabfa094d30b4	sops	-
library/templates/INDEX.md	authored	-	-	91922653d4b642a599e974078b516be699bd463e920f79277ba01b93d6432985	templates	-
library/templates/brief-design/SKILL.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/ray-notion-brief/SKILL.md	-	e2a0abf1a6e881d293c348e08bf8ee95357575671b54a18139611f3a7fbec9d4	templates	392615b778d97fe937d8cc7721308b9121dcac4252d5252cd23805aafd7670ad
library/templates/brief-design/reference/anti-patterns.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/ray-notion-brief/reference/anti-patterns.md	-	6ad4aaea116cdce6f05fa78987236a0ad7a9c1e02e3a72b095c052c2a53ce1ba	templates	f07bc3d7606fedb198e725c17adc0506bb6c10242adbe335ee103cbcc76bbcb4
library/templates/brief-design/reference/base.html	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/ray-notion-brief/reference/base.html	-	52010bf038b5aced0bfd8f4f1b84f00e8c4fd9f02fd1b83f7505f9630259e2a4	templates	09f76303513684fdf480d758e5df6ae8f04a2e3eafd6bdbe8af276bfccf5a002
library/templates/brief-design/reference/components.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/ray-notion-brief/reference/components.md	-	dbd6b05780916f7df6daddcb4c5d50e07005047da8b7794ad590ab2f860a5b05	templates	c860e9de2f367c6b24a4fc8898e2296b5df8f0745dc20cc025ebb24330e2a464
library/templates/brief-design/reference/composition.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/ray-notion-brief/reference/composition.md	-	ec9f888bbf047b8e18533876be4999fe64bb2d7f3a9b741b44583e8e808fbee5	templates	31ce2ddfbf64462aab4f67719ca233af71cc5311c671b0d9d008c2a5b53c5938
library/templates/brief-design/reference/philosophy.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/ray-notion-brief/reference/philosophy.md	-	5e4fcea597693e075dd251948e8b2daa64b0138f30c8b18bf1aad9a3f7385d2d	templates	b6eea5cf29ad0eb3ade6e1c90f11e9428f624b9241ddc2272660dfc30d8ce7e0
library/templates/brief-design/reference/tokens.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/.claude/skills/ray-notion-brief/reference/tokens.md	-	bc8e2cbfcfa0155e8a5495ff3e4906312910d3edef597159b5a1f084c3045ec2	templates	f70d480156dccb312431b036bb8301c9342f11f8870b4397fedd461d34b00325
library/templates/engagement-notes.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/admin/admin-planning-notes.md	-	00ff1dfa2c3530769f5d67f48195b9388c9433488be90d618aff10841dda6da4	templates	b1aa6999f1657a4fc2ca719e321432bc69168ccd3924b0d2cdc0483d4fd4cea3
library/templates/engagement-progress-log.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/admin/admin-planning-progress.md	-	bcb73f3c5da26e4e984a8e98941bdb0e13e68b927fa5b9e2a6fc6f5fab043ddd	templates	31f3e752e3ab9f02eb9d92202e2f5257dbc4c83b318d4825e423bcf8a885c044
library/templates/handover.md	authored	-	-	bf5cd117b720975ecaa8820d34b1387a7e393dcf55ff0e8dd7661c24ea2a2a38	templates	-
library/templates/index-manifest.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/admin/admin-index-manifest.md	-	2a606eb4c7b1dba287bc2876bed9db688033651fcd44ea0268857f8544b9911d	templates	65c45b79453eb8912d174b33bbac4814c6e429090ed3d2ae235628a57fa8368a
library/templates/interview-record.md	authored	-	-	63134e3f01cf7e77d3ab6faa5bd31e32d2ebcb0e20bff03c52cc0fd78bee8370	templates	-
library/templates/process-confirmation.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/comm/comm-client-workflow-confirmation.md	-	03a065e770fe163fc3b3bd0c193f01e0804796c8dddac50076a2efa96e486ccf	templates	9083831b9957ebc0c091dc488c05e9c70b0a49464ab830f0ea34c843cef5183b
library/templates/process-inventory.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/research/research-workflow-inventory.md	-	70f2b8ab854c34dd303dcd4e257b3c5face8d38e59a25b9c676ddc833c177e38	templates	b5ada5e67b77a359a1f8876a8cce869c6267a5c22b7576eda69ed12ce6886be5
library/templates/process-reconstruction.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/research/research-workflow-step-worksheet.md	-	ace0957e922b2ef0a2fb2f76e30c3d235358cdfdd2c2b7bd85796e00119baca1	templates	3d4c117da58f122ecd4b287fef0b1d02183c4a483b0ee32ca55e2d23fe71bd1b
library/templates/requirements-gathering.md	WeiKuoWei/gitroll-operations	/Users/weikuo/Documents/jobs/gitroll/tasks/operations.nosync/templates/comm/comm-client-requirements-gathering.md	-	2b55d6a9d26db3f11f10efb5295b2f6f62f5fe2c67b5e312fc0c482f8907f11a	templates	3ea47825b28b62190fdd489bbb3670e873ce8d5720008cdd60679efb78bbc042
library/templates/specification.md	authored	-	-	39f23bf7de1a6ad17493fe90688adaba76f867d861b74f6d766ea3e8d1c5f919	templates	-
```
