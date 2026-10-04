import json, collections, os, re, sys
import normalize as s3
H = os.path.join(os.environ.get("PM_WORK", "work"), "scan2v/full")
ERRP = {int(x) for x in open(os.path.join(os.environ.get("PM_WORK", "work"), "data/errata_vol2_pages.txt")).read().split("\n")[1].split()}
opus = {}
for f in ["fcq2_agree.fc.json", "fcq2_agree_b.fc.json", "fcq2_agree_c.fc.json"]:
    if os.path.exists(f"{H}/{f}"):
        for r in json.load(open(f"{H}/{f}")): opus[(r["page"], r["ctx"])] = r.get("fc_answer", "")
F = []
for f in ["v2_scanpicks.cx.json", "v2b_scanpicks.cx.json", "v2c_scanpicks.cx.json"]:
    if not os.path.exists(f"{H}/{f}"): continue
    for r in json.load(open(f"{H}/{f}")):
        if r.get("fc_pick") == "read" and not (r["pg"] == "" and set(r["read"]) <= set(".…")) and s3.post(r["pg"]) != s3.post(r["read"]) and not s3.blind(r["pg"], r["read"]):
            F.append(dict(page=r["page"], pg=r["pg"], scan=r["read"], ctx_pg=r["ctx_pg"], ctx_scan=r["ctx_read"],
                          on_published_errata_page=r["page"] in ERRP,
                          opus_note=re.sub(r"\b(?:[Rr]eading )?[AB]\b", "one reading", opus.get((r["page"], r["ctx"]), "").split(":", 1)[-1].strip()),
                          codex_note=r.get("fc_answer", "").split(":", 1)[-1].strip()))
F.sort(key=lambda x: (x["page"], x["ctx_pg"]))
E = [x for x in F if x["on_published_errata_page"]]; F = [x for x in F if not x["on_published_errata_page"]]
json.dump(E, open(f"{H}/v2_errata_page_rows.json", "w"), ensure_ascii=False, indent=1)   # held back: Gutenberg says it applied all published errata
json.dump(F, open(f"{H}/v2_final.json", "w"), ensure_ascii=False, indent=1)
print(len(F), "rows on", len({x["page"] for x in F}), "pages;", len(E), "held back (published-errata pages)")
c = collections.Counter((x["pg"][:12], x["scan"][:12]) for x in F)
for k, v in c.most_common(15): print(v, repr(k[0]), "->", repr(k[1]))
