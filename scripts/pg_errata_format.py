#!/usr/bin/env python3
"""Convert draft items to Gutenberg's preferred 'context line + old ==> new' errata format.
A model proposes {context, old, new}; deterministic checks decide whether it is accepted."""
import json, os, re, subprocess, sys, html
from concurrent.futures import ThreadPoolExecutor
G = open(os.environ.get("GUTFILE", "work/gutenberg/vol1-pg78050.html"), encoding="utf8").read()
GU = html.unescape(G)
D = json.load(open("vol1_items.json"))
units = []
for it in D["items"]:
    for img in it["images"]:
        i = G.find(f'src="images/{img}"'); s = G.rfind("<", 0, i)
        before = re.sub(r"\s+", " ", G[max(0, s - 400):s])
        units.append({"n": it["n"], "img": img, "hdr": it["hdr"], "source": it["source"][img], "html_before": before,
                      "scan": it.get("scan", ""), "change": it.get("change", "") or it.get("note", ""), "current_in_draft": it.get("current", "")})
PROMPT = """You convert errata items for a Project Gutenberg ebook of Principia Mathematica into Gutenberg's preferred format:
a CONTEXT line copied verbatim from the ebook source, then "OLD ==> NEW".
For each unit you get: the exact ebook source string for the formula image ("source", LaTeX from the data-tex attribute),
the raw HTML just before the image ("html_before", for label/text items), what the 1910 print shows ("scan"), and the agreed change ("change").
Return one JSON object per unit, one per line, no other text:
{"key": <key>, "where": "formula" or "html", "context": <verbatim substring of source (or of html_before when the error is in the surrounding HTML text, e.g. a proposition label)>, "old": <verbatim substring of context, as short as possible but long enough to be unambiguous inside context>, "new": <the corrected replacement for old, in the same notation (LaTeX for formulas)>, "comment": <optional very short comment, or "">}
Rules: context must be copied character-for-character from source/html_before (25 to 100 characters, containing old). Make the change minimal and exactly what "change" describes; do not fix anything else. If no edit can express it, set old and new to "" and explain in comment.
UNITS:
"""
def run(batch):
    payload = "\n".join(json.dumps({"key": k, **{x: u[x] for x in ("source", "html_before", "scan", "change")}}, ensure_ascii=False) for k, u in batch)
    env = dict(os.environ)   # expects CLAUDE_CODE_OAUTH_TOKEN in the environment
    for attempt in range(2):
        r = subprocess.run(["claude", "-p", "--model", "claude-opus-5-5"], input=PROMPT + payload, capture_output=True, text=True, env=env, timeout=900)
        out = {}
        for line in r.stdout.splitlines():
            line = line.strip().strip("`")
            if line.startswith("{"):
                try: o = json.loads(line); out[o["key"]] = o
                except Exception: pass
        if len(out) >= len(batch) * 0.8: return out
    return out
keyed = list(enumerate(units))
batches = [keyed[i:i + 12] for i in range(0, len(keyed), 12)]
res = {}
with ThreadPoolExecutor(4) as ex:
    for o in ex.map(run, batches): res.update(o)
ok = 0
for k, u in keyed:
    o = res.get(k, {}); u.update({x: o.get(x) for x in ("where", "context", "old", "new", "comment")})
    src = u["source"] if u.get("where") != "html" else u["html_before"]
    c, a, b = u.get("context") or "", u.get("old") or "", u.get("new")
    checks = {"model_answered": k in res, "context_in_source": bool(c) and c in (src or ""),
              "old_in_context": bool(a) and a in c, "old_unique_in_context": bool(a) and c.count(a) == 1,
              "changes_something": bool(a) and a != b}
    hits = G.count(c) if "&" not in c else G.count(html.escape(c, quote=True))
    checks["context_hits_in_file"] = hits
    u["checks"] = checks; u["accepted"] = all(v for kk, v in checks.items() if kk != "context_hits_in_file") and hits >= 1
    ok += u["accepted"]
json.dump(units, open("vol1_arrow_units.json", "w"), ensure_ascii=False, indent=1)
print(f"{ok}/{len(units)} accepted")
for u in units:
    if not u["accepted"]: print(" REJECT", u["n"], u["img"], {k: v for k, v in u["checks"].items() if not v}, (u.get("comment") or "")[:120])
