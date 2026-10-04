#!/usr/bin/env python3
"""Apply hand fixes, re-run the deterministic checks, render Gutenberg's preferred errata format.
Each entry: locator line, a context line copied verbatim from the .htm file, then "old ==> new".
Inputs: data/vol1/pg_report_units.json (the formatter's output) and data/vol1/report_provenance.json (how each entry
was found and checked, traced from the pipeline data). Outputs: data/vol1/gutenberg_report_draft.txt and
data/vol1/report_held_back.json. Entries in a reader-unreliable class (METHODOLOGY §3: dots, E!/∃!, breves and
arrows, inverted D) are kept only if a later independent check picked the print (both full-page judges, or a
crop check); the rest are held back, with the reason."""
import json, re, os, html
R = os.environ.get("PM_WORK", "work")
G = open(os.environ.get("GUTFILE", f"{R}/gutenberg/vol1-pg78050.html"), encoding="utf8").read()
U = json.load(open(os.environ.get("UNITS", f"{R}/data/vol1/pg_report_units.json")))
PROV = {e["n"]: e for e in json.load(open(f"{R}/data/vol1/report_provenance.json"))["entries"]}
FIX = {("32", "755.svg"): dict(where="html", context="<b>1·5.</b>", old="<b>1·5.</b>", new="<b>*1·5.</b>"),
       ("72", "4532.svg"): dict(where="formula", context=r"\vdash.\exists !\text{Rl}ʻ P", old=r"\exists !", new=r"\text{E}!"),
       ("73", "4533.svg"): dict(where="formula", context=r"\vdash.\exists !\text{Rl ex}ʻ P", old=r"\exists !", new=r"\text{E}!"),
       ("3", "932.svg"): dict(where="formula", context=r"p \,\supset:\, q \,\supset.\, p \,.\, r \,\supset\, q \,.\, r", old=r"p \,\supset:\, q \,\supset.\, p \,.\, r \,\supset\, q", new=r"p \,\supset\, q \,.\supset:\, p \,.\, r \,.\supset.\, q"),
       ("96", "6366.svg"): dict(where="formula", context=r"\supset.{\in}_{\Delta}ʻ\kappa\cup\lambda\,\text{", old=r"ʻ\kappa\cup\lambda\,", new=r"ʻ(\kappa\cup\lambda)\,"),
       # *40·42: the whole formula as one change. The print (p. 326) differs from the ebook only by the dots around ⊃
       ("49", "3521.svg"): dict(where="formula",
            context=r"\vdash : (x).Rʻx = Pʻx \cup Qʻx \supset sʻRʻʻ\alpha = sʻ(Pʻʻ\alpha \cup Qʻʻ\alpha) = sʻPʻʻ\alpha \cup sʻQʻʻ\alpha",
            old=r"\vdash : (x).Rʻx = Pʻx \cup Qʻx \supset sʻRʻʻ\alpha = sʻ(Pʻʻ\alpha \cup Qʻʻ\alpha) = sʻPʻʻ\alpha \cup sʻQʻʻ\alpha",
            new=r"\vdash : (x).Rʻx = Pʻx \cup Qʻx .\supset. sʻRʻʻ\alpha = sʻ(Pʻʻ\alpha \cup Qʻʻ\alpha) = sʻPʻʻ\alpha \cup sʻQʻʻ\alpha")}
# *52·24: widen old/new to start at a whole LaTeX token (the formatter's pair began inside \text{Cls}); still unique in the context
FIX[("62", "4006.svg")] = dict(old=r"\text{Cls}.\text{1}\neq\Lambda", new=r"\text{Cls}.\text{1}\neq\text{V}")
PAGEFIX = {"4126.svg": "374", "5591.svg": "487"}   # Gutenberg's page marker sits one page early here; the readings place the line on these printed pages
HOLD_EXTRA = {22: "the forced-choice judge (Sonnet) answered NEITHER, and no later check picked the print",
              33: "no dedicated scan check: the only support is one whole-page reading whose prompt asks for ✱ labels"}
def both_judges(e): return any(x.get("opus_high") == "read" and x.get("codex_high") == "read" for x in (e.get("later_fullpage_pass") or []))
def hold_reason(k):
    e = PROV[k]
    if k in HOLD_EXTRA: return HOLD_EXTRA[k]
    if e.get("setaside_class") and not (both_judges(e) or e.get("crop_check")):
        return f"{e['setaside_class']} change (a reader-unreliable class) with no crop check and no later two-judge pick of the print"
    return None
def filetext(u, c):   # the string exactly as it appears in the .htm file
    return c if u.get("where") == "html" else html.escape(c, quote=True).replace("&#x27;", "'")
TOK = r"\\[A-Za-z]+(?:\{[^{}]*\})?|\\.|\{[^{}]*\}|[^\s\\{}]"
def lengthen(u):
    """A context that occurs more than once in the file is extended verbatim inside its own data-tex, a whole LaTeX
    token at a time (right first), until it is unique; it never takes in a run of spaces (email collapses them)."""
    c, src = u["context"], u["source"] or ""
    if u["where"] != "formula" or G.count(filetext(u, c)) <= 1 or c not in src: return c
    a = src.find(c); b = a + len(c)
    while G.count(filetext(u, src[a:b])) > 1:
        m = re.match(r"( ?)(" + TOK + ")", src[b:])
        if m and "  " not in src[a:b + m.end()]: b += m.end(); continue
        m = re.search(r"(" + TOK + r")( ?)$", src[:a])
        if m and "  " not in src[m.start():b]: a = m.start(); continue
        break
    return src[a:b]
bad = []
for k, u in enumerate(U, 1):
    u["entry"] = k
    f = FIX.get((u["n"], u["img"]))
    if f: u.update(f)
    u["new"] = (u["new"] or "").replace(r"\text{Cls}\,\text{ex}", r"\text{Cls ex}")   # one form; ^2 vs ^{2} follows each entry's own context
    u["context"] = lengthen(u)
    c, a, b = u["context"] or "", u["old"] or "", u["new"]
    src = G if u["where"] == "html" else (u["source"] or "")
    hits = G.count(filetext(u, c))
    ok = "  " not in c and bool(c) and c in src   # email bodies collapse runs of spaces, so a context must not contain one
    ok = ok and bool(a) and c.count(a) == 1 and a != b and hits >= 1
    u["file_hits"] = hits; u["accepted"] = ok; u["held_back"] = hold_reason(k)
    if not ok: bad.append((k, u["img"]))
print("rejected:", bad)
print("contexts still occurring more than once:", [(u["entry"], u["img"], u["file_hits"]) for u in U if u["file_hits"] > 1])
PAGES = [(m.start(), m.group(1)) for m in re.finditer(r'id="Page_(\d+)"', G)]
def page_of(img):
    i = G.find(f'src="images/{img}"'); pg = None
    for pos, n in PAGES:
        if pos > i: break
        pg = n
    return pg
def loc(u):
    hdr = u["hdr"]; ids = re.findall(r"\*\d+·\d+", hdr); imgs = re.findall(r"(\d{3,5})\.svg", hdr)
    me = u["img"].split(".")[0]
    if len(ids) == len(imgs) and me in imgs: pid = ids[imgs.index(me)]
    else:
        pre = hdr[:hdr.find(me)] if me in hdr else hdr
        found = re.findall(r"\*\d+·\d+", pre)
        pid = found[-1] if found else (ids[0] if ids else hdr.split(" — ")[0])
    if u["where"] == "html":
        m = re.search(r"p\.\s?(\d+)", hdr); pg = m.group(1) if m else page_of(u["img"])
    else: pg = PAGEFIX.get(u["img"]) or page_of(u["img"])
    return f"{pid}, p. {pg}, images/{u['img']}"
NOTES = {"*1·4": "as transcribed it is not a valid law; the ebook's own summary and the following paragraph have q ∨ p",
         "*84·03": "the print reads \"Cls ex² excl\"; as transcribed, the definition defines \"Cls² excl\" in terms of itself. The same \"ex\" is missing in the *84, *88 and *97·16 entries below",
         "*88·37": "the print has the negation: Λ is not a member of κ",
         "*73·801": "printed p. 487; the ebook's page marker places this image on p. 486"}
def group(k): return "prop" if k <= 32 or k >= 38 else "replay"
KEEP = [u for u in U if not u["held_back"]]
num = {u["entry"]: i for i, u in enumerate(KEEP, 1)}
def ranges(ns):
    ns = sorted(ns); out = []
    for n in ns:
        if out and n == out[-1][1] + 1: out[-1][1] = n
        else: out.append([n, n])
    s = ", ".join(f"{a}" if a == b else (f"{a}, {b}" if b == a + 1 else f"{a}–{b}") for a, b in out)
    return " and ".join(s.rsplit(", ", 1)) if ", " in s else s
prop = [num[u["entry"]] for u in KEEP if group(u["entry"]) == "prop"]
replay = [num[u["entry"]] for u in KEEP if group(u["entry"]) == "replay"]
pass1 = [num[u["entry"]] for u in KEEP if u["entry"] <= 2]
fp = [num[u["entry"]] for u in KEEP if both_judges(PROV[u["entry"]])]
sa = [num[u["entry"]] for u in KEEP if PROV[u["entry"]].get("setaside_class")]
assert set(sa) <= set(fp)
out, done = [], set()
for u in KEEP:
    k = num[u["entry"]]
    if group(u["entry"]) == "replay" and "replay" not in done:
        out.append("The next entries were found by replaying the proofs by machine (a broken line stops the replay):"); done.add("replay")
    if group(u["entry"]) == "prop" and u["entry"] >= 38 and "ext" not in done:
        out.append("The rest come from the same check extended over *31–*97 (printed pp. 251–666):"); done.add("ext")
    L = loc(u); pid = L.split(",")[0]
    e = f"{k}. {L}\n{filetext(u, u['context'])}\n{filetext(u, u['old'])} ==> {filetext(u, u['new'])}"
    if pid in NOTES and pid not in done: e += f"\n({NOTES[pid]})"; done.add(pid)
    out.append(e)
n = len(KEEP)
head = f"""Hello,

In "Principia Mathematica, Vol. 1 (of 3)," by Alfred North Whitehead and Bertrand Russell, EBook #78050, I found the following {n} places where the ebook appears to differ from the 1910 first edition.

File: the HTML version under "more files" (78050-h.htm). The formulas are images whose LaTeX is in each image's data-tex attribute, so for a formula the context line and the correction are that LaTeX, copied verbatim from the file (so "&amp;" appears as it does there). Each entry gives the printed page and image file as locators, one context line, then "old ==> new".

How they were checked: against the 1910 first-edition scan on Wikimedia Commons ("Russell, Whitehead - Principia Mathematica, vol. I, 1910.djvu"; djvu page = printed page + 22), using its 1920-pixel page images. The checking was done by AI models under my direction:
- Entries {ranges(prop)}: two machine readings of the page image from different model families (Claude and OpenAI Codex), neither given the ebook text, agreed with each other and differed from the ebook. Claude Opus then re-read the disputed line from the image, again without the ebook text. For all of these except {ranges(pass1)}, a third model (Claude Sonnet) was also shown the page and the two versions of the line, unlabelled, and picked the printed one.
- Entries {ranges(replay)}: found by replaying the proofs by machine, then checked by one Claude Opus reading of that line from the page image.
- Entries {ranges(fp)} were also found independently by a later full-page check: two Codex readings of the page agreed against the ebook, and two judges (Claude Opus and Codex), each shown the page and both versions unlabelled, both picked the print.
- Entries {ranges(sa)} change only PM's dots or E! for ∃!, marks that machine readers often get wrong. Each of them is in the previous group, but none has had an enlarged close-up check.

Places where the ebook differs from the 1910 print because it applied the published Errata, as its Transcriber's Note says, are not included (e.g. *10·23 on p. 144, *23·81, *25·37 (zRw corrected to zSw), *25·412, *40·18).

"""
tail = """

Thank you to everyone at Distributed Proofreaders and Project Gutenberg for this transcription. It is an extraordinary piece of work, and it is making a machine check of Principia possible.

Best regards,
""" + os.environ.get("SIGNATURE", "") + "\n"
text = head + "\n\n".join(out) + tail
open(os.environ.get("OUT", f"{R}/data/vol1/gutenberg_report_draft.txt"), "w").write(text)
HB = [dict(draft_entry=u["entry"], locator=loc(u), context=filetext(u, u["context"]), old=filetext(u, u["old"]), new=filetext(u, u["new"]),
           reason=u["held_back"], found_by=PROV[u["entry"]].get("found_by"), checked_by=PROV[u["entry"]].get("checked_by")) for u in U if u["held_back"]]
json.dump(HB, open(f"{R}/data/vol1/report_held_back.json", "w"), ensure_ascii=False, indent=1)
print(n, "entries;", len(HB), "held back;", len(text), "chars")
