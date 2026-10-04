import json, os, re, glob, statistics
import fullpage_compare as fc
C = json.load(open("scan/full/intro_confirmed.json"))
HELD = {10, 28, 34, 38, 44, 49, 54, 56, 61, 70, 73, 78}
strip = lambda t: fc.nospace(t.replace("\x01", "").replace("\x02", ""))
def core(r, k=10):
    L = r["ctx_read"]; i = r["ctx_pg"].find(r["pg"]) if r["pg"] else None
    # ctx_read = L + read + R with L = 35 chars before; take k chars each side around the read span
    pre = r["ctx_pg"][:r["ctx_pg"].find(r["pg"])] if r["pg"] else None
    return L
res = {}
for d in ["codex", "codex-low", "codex-medium", "codex-high", "codexhi"]:
    found = held = 0; hunks = 0; pages = 0; miss = []
    for r in C:
        t = fc.model_text(f"scan/full/{d}/{r['page'] + 22}.txt")
        if t is None: continue
        if "ctx_read" not in r or "【" not in r.get("ctx", ""): continue
        s = strip(t)
        # robust core: 12 chars left of span + read + 12 chars right, taken from ctx_read
        cr = r["ctx_read"]; pos = len(r["ctx"].split("【")[0])
        c = cr[max(0, pos - 12): pos + len(r["read"]) + 12]
        ok = c in s; found += ok; held += (r["page"] in HELD and ok)
        if not ok: miss.append(r["page"])
    for p in range(1, 89):
        g = fc.pages.get(p); t = fc.model_text(f"scan/full/{d}/{p + 22}.txt")
        if g is None or t is None: continue
        pages += 1; hunks += len(fc.hunks(strip(g), strip(t)))
    toks = []
    res[d] = dict(confirmed_found=found, of=len(C), heldout_found=held, pages=pages, hunks=hunks, hunks_per_page=round(hunks / max(pages, 1), 1), miss=sorted(set(miss))[:20])
    print(d, res[d])
json.dump(res, open("scan/full/sweep_eval.json", "w"), indent=1)
