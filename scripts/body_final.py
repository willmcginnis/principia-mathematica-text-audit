import json, re, collections
X = json.load(open("scan/full/body_conf2.cx.json"))
F = [r for r in X if r["fc_pick"] == "read"]
numdot = lambda r: r["pg"] == "" and r["read"] == "." and re.search(r"\*\d+\.\d+$", r["ctx_pg"][:r["ctx"].find("【")])
for r in F:
    r["cls"] = "number-dot" if numdot(r) else ("dot-only" if set(r["pg"] + r["read"]) <= set(".:,") else "substantive")
    if r["cls"] == "substantive":
        if (len(r["pg"]) > 20 and len(r["read"]) < 3) or (len(r["read"]) > 20 and len(r["pg"]) < 3): r["cls"] = "alignment"
        elif any(k in r["pg"] + r["read"] for k in ("begin", "split", "align", "array", "text", "quad")): r["cls"] = "tex-residue"
print(len(F), collections.Counter(r["cls"] for r in F))
# published errata (PM's own) by page
ERR = collections.defaultdict(list)
for fn in ("data/errata_v1page.txt", "data/errata_v2page.txt", "data/errata_010.txt"):
    for m in re.finditer(r"page\s+(\d+)[^\n]*", open(fn, encoding="utf-8").read()): ERR[int(m.group(1))].append(m.group(0))
import fullpage_compare as fc
known = open("data/our_errata_scan.tsv", encoding="utf-8").read() + open("scan/pass3/tier2_entries.txt", encoding="utf-8").read()
KP = set(re.sub("·", ".", x) for x in re.findall(r"\*\d+·\d+", known))
strip = lambda t: fc.nospace(t.replace("\x01", "").replace("\x02", ""))
for r in F:
    g = strip(fc.pages.get(r["page"], "")); i = g.find(r["ctx_pg"])
    pre = g[:i + len(r["ctx"].split("【")[0])] if i >= 0 else r["ctx_pg"]
    nums = re.findall(r"\*(\d+\.\d+)", pre); r["prop"] = ("*" + nums[-1]) if nums else None
    r["pub_errata_same_page"] = ERR.get(r["page"], [])
    r["already_listed"] = bool(r["prop"] and r["prop"] in KP)
json.dump(F, open("scan/full/body_final.json", "w"), ensure_ascii=False, indent=1)
S = [r for r in F if r["cls"] == "substantive"]
print("substantive", len(S), "| pages with a published PM erratum:", sum(bool(r["pub_errata_same_page"]) for r in S), "| prop already in our lists:", sum(r["already_listed"] for r in S), "| distinct props:", len({r["prop"] for r in S}))
