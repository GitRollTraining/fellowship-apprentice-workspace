#!/usr/bin/env python3
"""Apply agent-proposed sanitization to transcript.json -> digest-transcript.json.

Agents PROPOSE, this script DISPOSES. Whitelist (frozen; see references/methodology.md):
  W1 speaker-label formatting (preserve prefixes verbatim; no inference)
  W2 punctuation/whitespace normalization (token-neutral)
  W3 canonical name/term substitution authorized by the engagement's name list — the
     proper nouns collected from the owner; an EXACT string match is the only authorization
  W4 artifact removal (hallucinated transcriber/subtitle strings; patterns below)
  W5 pure-filler segment drops (every content token in the filler lexicon, <=8 tokens)
FORBIDDEN: summarization, paraphrase, reordering, merging/splitting, translation,
fact edits, speaker inference, t0/t1/src mutation.

Guards enforced here (violating proposals REJECTED, not fixed):
  - per-segment content-token preservation >= 0.85 (same tokenizer as the digest verify step)
  - drops: class 'filler' -> token-subset-of-lexicon + <=8 tokens (or zero-token segment);
           class 'artifact' -> text matches a known artifact pattern
  - t0/t1/src copied byte-identical from source; order preserved; no segment invented

Input edits file: {"edits":[{"t0":f,"new_text":s,"op":"W2|W3|W4","reason":s}],
                   "drops":[{"t0":f,"reason":s,"class":"artifact|filler"}]}
Prints a JSON report (applied/rejected with reasons) to stdout.
"""
import argparse, json, re, sys

def toks(t):  # same tokenizer as the digest verify step
    t = re.sub(r'^[A-Za-z .]+:', '', t)
    return set(re.findall(r"[A-Za-z0-9']+|[一-鿿]", t.lower()))

def toks_cased(t):  # case-sensitive variant, for the case-only-change guard below
    t = re.sub(r'^[A-Za-z .]+:', '', t)
    return re.findall(r"[A-Za-z0-9']+|[一-鿿]", t)

FILLER_LATIN = {
    "um", "uh", "uhh", "er", "ah", "ok", "okay", "cool", "yeah", "yep", "yes", "no",
    "mm", "hmm", "mhm", "hm", "you", "i", "right", "alright", "all", "oh", "wow", "huh",
    "well", "so", "thanks", "thank", "bye", "hello", "hey", "gotcha", "sure",
}
FILLER_ZH = set("嗯啊喔哦噢欸誒诶呃唔呀吧呢嘛啦咯囉了好對对是的這这樣样就行哈呵謝谢拜掰再見见沒没問问題题可以喂")

ARTIFACT_PATTERNS = [  # hallucinated transcriber/subtitle strings seen in real recordings
    r"字幕由\s*Amara\.org\s*社區提供", r"以上言論不代表本台立場",
    r"請不吝點贊|訂閱.*轉發.*打賞", r"本期視頻就先說到這裡", r"此字幕由AI產生",
    r"整理&字幕志願者", r"多謝您收睇時局新聞", r"已進行編輯以加入正確的標點符號",
    r"這條語音備忘錄", r"edited to include proper punctuation", r"This is a voice memo",
    r"現在正在進行編輯", r"若您有任何疑慮.*請與我聯繫", r"請看下方資訊欄", r"點個贊吧",
]

def is_filler(text):
    ts = toks(text)
    if not ts:
        return True
    if len(ts) > 8:
        return False
    return all(w in FILLER_LATIN or (len(w) == 1 and w in FILLER_ZH) for w in ts)

def is_artifact(text):
    return any(re.search(p, text) for p in ARTIFACT_PATTERNS)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript")
    ap.add_argument("edits")
    ap.add_argument("out")
    ap.add_argument("--verdicts", default=None,
                    help="verdicts.json to inject applied segment_drops + sanitization_edits log into")
    a = ap.parse_args()
    src = json.load(open(a.transcript))
    prop = json.load(open(a.edits))
    by_t0 = {}
    for i, s in enumerate(src):
        by_t0.setdefault(round(s["t0"], 3), i)

    report = {"applied_edits": [], "rejected_edits": [], "applied_drops": [], "rejected_drops": []}
    new_text = {}
    for e in prop.get("edits", []):
        key = round(float(e["t0"]), 3)
        rec = {"t0": e["t0"], "op": e.get("op", "?"), "reason": e.get("reason", "")}
        if key not in by_t0:
            report["rejected_edits"].append({**rec, "why": "no segment at t0"}); continue
        seg = src[by_t0[key]]
        rec["t0"] = seg["t0"]  # exact source float, not the agent echo
        ts, td = toks(seg["text"]), toks(e["new_text"])
        keep_ratio = (len(ts & td) / len(ts)) if ts else 1.0
        rec.update(before=seg["text"][:80], after=e["new_text"][:80])
        if ts and keep_ratio < 0.85:
            report["rejected_edits"].append({**rec, "why": f"token preservation {keep_ratio:.2f} < 0.85"}); continue
        # case-only-change guard: toks() lowercases, so "save"->"SAFE" passes the ratio check
        # above at 1.0 while smuggling an uncanonicalized fact-edit past it (found in the build
        # run's audit rounds). A pure case flip on an otherwise-identical token is exactly the
        # ambiguous case the W3 name-list authorization exists for -- reject, don't apply.
        cs, cd = toks_cased(seg["text"]), toks_cased(e["new_text"])
        if len(cs) == len(cd) and cs != cd and [w.lower() for w in cs] == [w.lower() for w in cd]:
            report["rejected_edits"].append({**rec, "why": "case-only token change (unauthorized substitution, not W2/W3)"}); continue
        if by_t0[key] in new_text:
            report["rejected_edits"].append({**rec, "why": "duplicate edit for segment"}); continue
        new_text[by_t0[key]] = e["new_text"]
        report["applied_edits"].append(rec)

    drops = set()
    for d in prop.get("drops", []):
        key = round(float(d["t0"]), 3)
        rec = {"t0": d["t0"], "class": d.get("class", "?"), "reason": d.get("reason", "")}
        if key not in by_t0:
            report["rejected_drops"].append({**rec, "why": "no segment at t0"}); continue
        seg = src[by_t0[key]]
        rec["t0"] = seg["t0"]
        rec["text"] = seg["text"][:80]
        cls = d.get("class")
        if cls == "filler" and not is_filler(seg["text"]):
            report["rejected_drops"].append({**rec, "why": "not pure filler per lexicon guard"}); continue
        if cls == "artifact" and not is_artifact(seg["text"]):
            report["rejected_drops"].append({**rec, "why": "no artifact-pattern match"}); continue
        if cls not in ("filler", "artifact"):
            report["rejected_drops"].append({**rec, "why": "unknown drop class"}); continue
        drops.add(by_t0[key])
        report["applied_drops"].append(rec)

    out = []
    for i, s in enumerate(src):
        if i in drops:
            continue
        t = new_text.get(i, s["text"])
        t = re.sub(r"[ \t]{2,}", " ", t).strip()  # W2 floor: whitespace normalization
        out.append({"t0": s["t0"], "t1": s["t1"], "text": t, "src": s["src"]})
    json.dump(out, open(a.out, "w"), ensure_ascii=False, indent=1)
    if a.verdicts:
        vd = json.load(open(a.verdicts))
        vd["segment_drops"] = [{"t0": r["t0"], "reason": r["reason"], "class": r["class"]}
                               for r in report["applied_drops"]]
        vd["sanitization_edits"] = (
            [{**r, "status": "applied"} for r in report["applied_edits"]]
            + [{**r, "status": "rejected"} for r in report["rejected_edits"]])
        json.dump(vd, open(a.verdicts, "w"), ensure_ascii=False, indent=1)
    print(json.dumps({
        "segments_in": len(src), "segments_out": len(out),
        "edits_applied": len(report["applied_edits"]), "edits_rejected": len(report["rejected_edits"]),
        "drops_applied": len(report["applied_drops"]), "drops_rejected": len(report["rejected_drops"]),
        "detail": report}, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
