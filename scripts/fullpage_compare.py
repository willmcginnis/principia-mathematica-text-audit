#!/usr/bin/env python3
"""Full-page comparison: blind model transcriptions (scan/full/<model>/<djvu>.txt) vs Gutenberg #78050 page text.
Prose + inline math + footnotes. Strong candidate = both model families disagree with PG the same way.
Usage: fullpage_compare.py FIRST_PRINTED LAST_PRINTED   -> scan/full/candidates_<a>_<b>.json"""
import re, sys, json, html, difflib, inspect, unicodedata
import compare_scan as cs
OFF = int(cs.os.environ.get("OFF", "22"))
# --- inline-math normalizer: cs.flat minus its proposition-level stripping (trailing dot, Df/Pp, leading number, hints)
src = inspect.getsource(cs.flat)
for drop in ["s = re.sub(r'(Df|Pp)\\.?$', '', s)", "s = re.sub(r'^[✱*]?\\d+\\.\\d+\\.?', '', s)", 's = s.rstrip(".")',
             "s = re.sub(r'\\\\quad\\s*\\[.*$|\\\\qquad.*$', '', s)"]:
    src = src.replace(drop, "pass")
src = "\n".join(("    pass" if ("qquad" in ln or "Proof|Transp" in ln) and "re.sub" in ln else ln) for ln in src.splitlines())
ns = {}; exec(src.replace("def flat(", "def mflat("), cs.__dict__, ns); mflat = ns["mflat"]
CH = {"ⁿ": "^n", "…": "...", "’": "'", "‘": "'", "‛": "'", "ʼ": "'", "“": '"', "”": '"', "—": "-", "–": "-", "­": "", "ﬁ": "fi", "ﬂ": "fl", "∗": "*", "✱": "*"}
def prose(s):
    s = unicodedata.normalize("NFC", html.unescape(s))
    for k, v in CH.items(): s = s.replace(k, v)
    return s
def math(s):
    s = re.sub(r"^\s*\\[\(\[]\s*|\s*\\[\)\]]\s*$", "", s.strip())       # TeX \( \) \[ \] delimiters
    s = re.sub(r"\\(?:begin|end)\{(?:array|aligned|align\*?|gathered|matrix|cases)\}(?:\{[^{}]*\})?", " ", s)
    s = s.replace("\\\\", " ")                                                 # TeX line breaks
    s = re.sub(r"\\(?:text|mathrm|textit|textrm|mbox)\s*\{([^{}]*)\}", r" \1 ", s)    # keep Pp, Df, and, E (dots.norm would delete them)
    s = re.sub(r"\\q?quad", " ", s)
    for k, v in (("\\Omega", "Ω"), ("\\aleph", "ℵ"), ("\\ldots", "…"), ("\\dots", "…"), ("\\cdots", "…"), ("\\gt", ">"), ("\\lt", "<"),
                 ("\\geq", "≥"), ("\\leq", "≤"), ("\\Gamma", "Γ"), ("\\Sigma", "Σ"), ("\\Pi", "Π"), ("\\Phi", "Φ"), ("\\Psi", "Ψ")):
        s = s.replace(k.replace("\\\\", "\\"), v)
    try: return "\x01" + re.sub(r"^FLAT:", "", mflat(s) or "") + "\x02"
    except Exception: return "\x01" + re.sub(r"\s+", "", s) + "\x02"
def finish(s):
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"(?<![A-Za-z0-9]) | (?![A-Za-z0-9])", "", s)     # keep spaces only between two word chars
    for k, v in cs.POST.items(): s = s.replace(k, v)              # same symbol map on prose and math
    s = s.replace("‘‘", '"').replace("“", '"').replace("”", '"').replace("‘", "'").replace("·", ".")
    return s.replace("~", "∼")

# ---------- Gutenberg side ----------
raw = open(cs.GUT, encoding="utf-8").read()
foot = {}
for m in re.finditer(r'id="Footnote_(\d+)"[^>]*>\[\d+\]</a>(.*?)</div>', raw, re.S): foot[m.group(1)] = m.group(2)
body = re.sub(r'<div class="footnotes">.*?</div>\s*</div>', "", raw, flags=re.S)
def pg_render(fragment):
    fragment = re.sub(r'<a class="fnanchor[^>]*>\[(\d+)\]</a>', lambda m: f"\x03{m.group(1)}\x04", fragment)
    # TeX stays HTML-escaped until the tags are gone: an unescaped "<" in a formula (Nc‘α < Nc‘β) was taken for a tag
    # by the next line and deleted everything up to the next ">", leaving raw LaTeX ("[beginalign", "[l") in the stream
    fragment = re.sub(r'<img[^>]*data-tex="([^"]*)"[^>]*>', lambda m: "\x05" + m.group(1) + "\x06", fragment)
    fragment = re.sub(r"<br\s*/?>", " ", fragment); fragment = re.sub(r"<[^>]+>", " ", fragment)
    return html.unescape(fragment)
def norm_mixed(t):  # \x05tex\x06 segments -> math, rest prose
    out = []
    for i, part in enumerate(re.split(r"\x05|\x06", t)):
        out.append(math(part) if i % 2 else prose(part))
    return finish(" ".join(out))
pages = {}
marks = [(m.start(), m.group(1)) for m in re.finditer(r'\[Pg\s*(\w+)\]', body)]
for i, (o, n) in enumerate(marks):
    if not n.isdigit(): continue
    end = marks[i + 1][0] if i + 1 < len(marks) else len(body)
    t = pg_render(body[o:end]); t = re.sub(r"\[Pg\s*\w+\]", " ", t)
    fns = re.findall(r"\x03(\d+)\x04", t); t = re.sub(r"\x03\d+\x04", "*", t)   # model writes * / † markers
    t += " " + " ".join("* " + pg_render(foot.get(f, "")) for f in fns)
    pages[int(n)] = norm_mixed(t)

# ---------- model side ----------
def model_text(path):
    try: s = open(path, encoding="utf-8", errors="replace").read()
    except OSError: return None
    s = re.sub(r"\ntokens used\s*\n[\d,]+\s*$", "", s)
    s = s.replace("†", "*").replace("‡", "*").replace("§", "*")
    s = re.sub(r"\$\$(.+?)\$\$|\$(.+?)\$", lambda m: "\x05" + (m.group(1) or m.group(2)) + "\x06", s, flags=re.S)
    return norm_mixed(s)

def words(t):
    return re.findall(r"[a-z]{2,}", re.sub(r"\x01.*?\x02", " ", t.lower()))
def nospace(t): return t.replace(" ", "")
def splitjoin(gw, rw):
    out = []
    sm = difflib.SequenceMatcher(None, gw, rw, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "replace" and "".join(gw[i1:i2]) == "".join(rw[j1:j2]):
            out.append((" ".join(gw[i1:i2]), " ".join(rw[j1:j2]), " ".join(gw[max(0, i1 - 5):i2 + 5])))
    return out
ERR = []   # (page, erratum text) from PM's own published errata to Vol I
for fn in [x for x in cs.os.environ.get("ERRFILES", "data/errata_v1page.txt,data/errata_v2page.txt,data/errata_010.txt").split(",") if x]:
    try:
        for m in re.finditer(r"page\s+(\d+)[^\n]*", open(cs.os.path.join(cs.os.environ.get("PM_WORK", "work"), fn), encoding="utf-8").read()):
            ERR.append((int(m.group(1)), m.group(0)))
    except OSError:
        pass
def _parts(line):
    q = r'["“”]([^"“”]*)["“”]'
    m = re.search(r"for\s+(?:(?:first|second)\s+)?" + q + r"\s+read\s+" + q, line)
    if m: return m.group(1), m.group(2)                      # print had X, corrected to Y
    m = re.search(r"after\s+" + q + r"\s+insert\s+" + q, line)
    if m: return "", m.group(2)
    m = re.search(r"delete\s+" + q, line)
    if m: return m.group(1), ""
    m = re.search(r"in place of\s+(?:reference to\s+)?" + q + r"\s+read\s+(?:reference to\s+)?" + q, line)
    if m: return m.group(1), m.group(2)
    return None
def erratum_for(page, pgspan, rdspan):
    k = lambda t: re.sub(r"[\s\"'“”‘’]|\.$", "", t).replace("·", ".")
    P, Rd = k(pgspan), k(rdspan)
    if len(P) + len(Rd) < 2: return None                      # one-character spans are too ambiguous to attribute
    for p, line in ERR:
        if p != page: continue
        pr = _parts(line)
        if not pr: continue
        X, Y = k(pr[0]).rstrip("."), k(pr[1]).rstrip(".")
        if (not Rd or Rd in X) and (not P or P in Y) and (P or Rd): return line.strip()
    return None
def hunks(a, b):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    return [(tag, i1, i2, b[j1:j2]) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != "equal"]

def main():
    A, B = int(sys.argv[1]), int(sys.argv[2])
    out = []
    base = cs.os.path.expanduser(cs.os.environ.get("SCANBASE", cs.os.path.join(cs.os.environ.get("PM_WORK", "work"), "scan/full")))
    for p in range(A, B + 1):
        g = pages.get(p)
        rc, ro = (model_text(f"{base}/{m}/{p + OFF}.txt") for m in ("codex", cs.os.environ.get("SECOND", "opus")))
        if g is None or rc is None:
            out.append({"page": p, "status": "missing", "pg": g is not None, "codex": rc is not None}); continue
        if cs.os.environ.get("POSTNORM"):
            import normalize as _s3
            strip = lambda t: _s3.post(nospace(t))
        else:
            strip = lambda t: nospace(t.replace("\x01", "").replace("\x02", ""))
        gw, cw, ow = words(g), words(rc), (words(ro) if ro is not None else None)
        osj = {(a, b) for a, b, _ in splitjoin(gw, ow)} if ow is not None else None
        for a, b, cx in splitjoin(gw, cw):
            st = "no_opus" if osj is None else ("agree" if (a, b) in osj else "opus_matches_pg")
            raw = re.sub(r"\x01.*?\x02", " ", g); mm = re.search(r"(?i)" + r"\W+".join(map(re.escape, a.split())), raw)
            win = raw[max(0, mm.start() - 40):mm.end() + 40] if mm else cx
            er = erratum_for(p, a, b); st = "applied_erratum" if er else st
            out.append({"page": p, "status": st, "erratum": er, "tag": "spacing", "pg": a, "read": b, "ctx_pg": win, "ctx_read": win.replace(a, b) if mm else cx.replace(a, b), "ctx": f"{win} [{a} -> {b}]"})
        g, rc, ro = strip(g), strip(rc), (strip(ro) if ro is not None else None)
        hc = hunks(g, rc); ho = hunks(g, ro) if ro is not None else None
        for tag, i1, i2, rep in hc:
            if ho is None: st = "no_opus"
            else:
                same = any(o[1] == i1 and o[2] == i2 and o[3] == rep for o in ho)
                touch = any((o[1] < i2 and i1 < o[2]) or (o[1] == o[2] == i1) or (i1 == i2 and o[1] <= i1 <= o[2]) for o in ho)
                st = "agree" if same else ("opus_other" if touch else "opus_matches_pg")
            L, R = g[max(0, i1 - 35):i1], g[i2:i2 + 35]
            er = erratum_for(p, g[i1:i2], rep)
            if er: st = "applied_erratum"
            out.append({"page": p, "status": st, "erratum": er, "tag": tag, "pg": g[i1:i2], "read": rep,
                        "ctx_pg": L + g[i1:i2] + R, "ctx_read": L + rep + R, "ctx": L + "【" + g[i1:i2] + "→" + rep + "】" + R})
    fn = f"{base}/candidates_{A}_{B}.json"
    json.dump(out, open(fn, "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    print(fn, Counter(r.get("status") for r in out))
    for r in out:
        if r.get("status") == "agree": print(r["page"], r["ctx"])
if __name__ == "__main__": main()
