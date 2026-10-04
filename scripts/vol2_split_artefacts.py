#!/usr/bin/env python3
"""Vol II: split the judged candidate list into kept rows (data/vol2/v2_final.json) and comparator artefacts
(data/vol2/v2_set_aside.json, one reason per row). Idempotent: it re-merges both files before splitting, so no row is lost.
Inputs not in this repo: the Gutenberg #78255 HTML (GUTFILE) and the two blind readings per page (SCANBASE/{codex,codexhi}/<djvu>.txt).

Rules, applied in this order:
 1 renderer_tex_residue: the hunk no longer exists when the page is re-compared with the fixed Gutenberg renderer
   (fullpage_compare.pg_render used to unescape TeX before stripping tags, so a "<" in a formula ate text up to the
   next ">", leaving raw LaTeX such as "[beginalign", "[l", "upharpoonright" and stray brackets in the stream).
 2 small_capital_typography: normalize.blind() now sets the pair aside (case-only roman numerals, e.g. Vol. IV / iv).
 2b notation_representation: normalize.notation(): the same printed glyph written two ways (⇷/↦ vs ←+, ʻʻ vs ",
   ↓_{.,} vs a combining diaeresis below, a lone combining mark on a dotted operator). Added 2026-10-04 after review.
 3 page_marker_placement: whole text present on one side only, touching the page edge, and found on the adjacent page:
   - Gutenberg-only text starting at offset 0 of page p, matching (similarity >= 0.85) a window in the last len+80
     characters of blind reading 1 of page p-1 (the print has it at the foot of p-1; Gutenberg's [Pg p] marker sits early);
   - print-only text ending at the last character of page p, matching (>= 0.85) a window in the first len+80
     characters of Gutenberg's page p+1 (Gutenberg's marker sits late).
   The text itself is the same on both sides; only the page marker's position differs.
 4 IMAGE: page-edge rows the rule cannot decide were decided by looking at the page images (listed below).
"""
import os, sys, re, json, html, difflib
W = os.environ.get("PM_WORK", "work")
os.environ.setdefault("GUTFILE", os.path.join(W, "gutenberg/vol2-pg78255.html"))
os.environ.setdefault("OFF", "40"); os.environ.setdefault("POSTNORM", "1")
SCANBASE = os.path.expanduser(os.environ.get("SCANBASE", os.path.join(W, "scan2v/full")))
os.environ["SCANBASE"] = SCANBASE
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fullpage_compare as fc, normalize as s3
D = os.environ.get("V2DATA", os.path.join(W, "data/vol2"))
FIN, SET = f"{D}/v2_final.json", f"{D}/v2_set_aside.json"
EXTRA = ("set_aside_class", "reason", "decided_by")
IMAGE = {   # (page, start of Gutenberg span): reason, from looking at the 1912 page images
    (3, "PARTIII.CARDINALARIT"): "page_marker_placement: the heading 'PART III. CARDINAL ARITHMETIC.' is printed on the part-title page p. 1 "
                                 "(image checked; both blind readings of p. 1 have it); Gutenberg places it at the head of p. 3",
    (308, "sinceitisverifiedwhe"): "page_marker_placement: the clause ends the paragraph at the foot of p. 307 (image checked); Gutenberg's "
                                   "[Pg 308] marker sits inside that sentence, and the p. 307 footnote is re-attached between the two parts",
    (497, "25.⊢.ΣNr'P↓.,'Q=Nr'("): "page_marker_placement: *183·25 is printed at the foot of p. 496 (image checked); Gutenberg's [Pg 497] "
                                   "marker sits one proposition early. The span also contains Gutenberg's '*183-26' (hyphen; the print has "
                                   "*183·26 with a centred dot), a separate possible slip that was not judged on its own: held for follow-up",
}

def old_render(fragment):   # the renderer that produced the judged rows (TeX unescaped before tag stripping)
    fragment = re.sub(r'<a class="fnanchor[^>]*>\[(\d+)\]</a>', lambda m: f"\x03{m.group(1)}\x04", fragment)
    fragment = re.sub(r'<img[^>]*data-tex="([^"]*)"[^>]*>', lambda m: "\x05" + html.unescape(m.group(1)) + "\x06", fragment)
    fragment = re.sub(r"<br\s*/?>", " ", fragment); fragment = re.sub(r"<[^>]+>", " ", fragment)
    return html.unescape(fragment)
def build_pages(render):    # same loop as fullpage_compare's Gutenberg side
    pages, marks = {}, [(m.start(), m.group(1)) for m in re.finditer(r'\[Pg\s*(\w+)\]', fc.body)]
    for i, (o, n) in enumerate(marks):
        if not n.isdigit(): continue
        end = marks[i + 1][0] if i + 1 < len(marks) else len(fc.body)
        t = render(fc.body[o:end]); t = re.sub(r"\[Pg\s*\w+\]", " ", t)
        fns = re.findall(r"\x03(\d+)\x04", t); t = re.sub(r"\x03\d+\x04", "*", t)
        t += " " + " ".join("* " + render(fc.foot.get(f, "")) for f in fns)
        pages[int(n)] = s3.post(fc.nospace(fc.norm_mixed(t)))
    return pages
def best(t, s):
    L = len(t); return max((difflib.SequenceMatcher(None, t, s[i:i + L], autojunk=False).ratio() for i in range(max(1, len(s) - L + 1))), default=0.0)

rows = json.load(open(FIN)) + (json.load(open(SET)) if os.path.exists(SET) else [])
rows = [{k: v for k, v in r.items() if k not in EXTRA} for r in rows]
rows.sort(key=lambda x: (x["page"], x["ctx_pg"]))
OLD, NEW = build_pages(old_render), build_pages(fc.pg_render)
RD = {}
def reader(m, p):
    if (m, p) not in RD:
        t = fc.model_text(f"{SCANBASE}/{m}/{p + int(os.environ['OFF'])}.txt")
        RD[(m, p)] = s3.post(fc.nospace(t)) if t is not None else ""
    return RD[(m, p)]
keep, aside = [], []
for r in rows:
    p, a, b = r["page"], r["pg"], r["scan"]
    g = OLD[p]
    hit = [h for h in fc.hunks(g, reader("codex", p)) if g[h[1]:h[2]] == a and h[3] == b and g[max(0, h[1] - 35):h[1]] + a + g[h[2]:h[2] + 35] == r["ctx_pg"]]
    assert len(hit) == 1, (p, a, b, len(hit))
    _, i1, i2, _ = hit[0]
    why = None
    if NEW[p] != g:
        h1, h2 = fc.hunks(NEW[p], reader("codex", p)), fc.hunks(NEW[p], reader("codexhi", p))
        if not any(NEW[p][h[1]:h[2]] == a and h[3] == b and any(o[1:] == h[1:] for o in h2) for h in h1):
            why = ("renderer_tex_residue", "the hunk disappears when the page is re-compared with the fixed Gutenberg renderer "
                   "(LaTeX or brackets left in the stream by the old tag-stripping bug)", "rule")
    if not why and s3.blind(a, b):
        why = ("small_capital_typography", "case-only roman numeral: the print sets it in small capitals", "rule")
    if not why and s3.notation(a, b):
        why = ("notation_representation", "the same printed glyph written two ways (Gutenberg's notation vs the readers' "
               "Unicode), not a text difference", "rule")
    if not why and (a == "") != (b == ""):
        T = a or b
        if a and i1 == 0:
            s = best(T, reader("codex", p - 1)[-(len(T) + 80):])
            if s >= 0.85:
                why = ("page_marker_placement", f"Gutenberg-only text at the top of p. {p}; the print has it at the foot of p. {p - 1} "
                       f"(blind reading of p. {p - 1}, similarity {s:.2f}). Gutenberg's [Pg {p}] marker sits early", "rule")
        elif b and i2 == len(g):
            s = best(T, OLD.get(p + 1, "")[:len(T) + 80])
            if s >= 0.85:
                why = ("page_marker_placement", f"print-only text at the foot of p. {p}; Gutenberg has it at the top of p. {p + 1} "
                       f"(similarity {s:.2f}). Gutenberg's [Pg {p + 1}] marker sits late", "rule")
    if not why:
        k = next((v for (pp, pre), v in IMAGE.items() if pp == p and a.startswith(pre)), None)
        if k: why = (k.split(":", 1)[0], k.split(":", 1)[1].strip(), "page image")
    if why: aside.append({**r, **dict(zip(EXTRA, why))})
    else: keep.append(r)
used = {(x["page"], x["pg"][:20]) for x in aside if x["decided_by"] == "page image"}
assert len(used) == len(IMAGE), "an IMAGE decision no longer matches a row"
json.dump(keep, open(FIN, "w"), ensure_ascii=False, indent=1)
json.dump(aside, open(SET, "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(len(rows), "judged rows ->", len(keep), "kept on", len({x["page"] for x in keep}), "pages;", len(aside), "set aside",
      dict(Counter(x["set_aside_class"] for x in aside)), "by", dict(Counter(x["decided_by"] for x in aside)))
