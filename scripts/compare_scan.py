#!/usr/bin/env python3
"""Compare blind model scan readings (scan/<pass>/<model><djvu>.json) with Gutenberg #78050, page by page.
Usage: compare_scan.py PASSDIR [MODEL]   (djvu page = printed page + 22)"""
import re, sys, json, glob, html, collections, os, unicodedata
import dots
GUT = os.path.expanduser(os.environ.get("GUTFILE", os.path.join(os.environ.get("PM_WORK", "work"), "gutenberg/vol1-pg78050.html")))
t = open(GUT, encoding="utf-8").read()
pgs = [(m.start(), int(m.group(1))) for m in re.finditer(r'\[Pg\s*(\d+)\]', t)]
def page_at(off):
    p = None
    for o, n in pgs:
        if o <= off: p = n
        else: break
    return p
def canon(s, force_flat=False):
    try:
        s = html.unescape(s).strip()
        s = re.sub(r'^\s*\\[\(\[]\s*|\s*\\[\)\]]\s*$', '', s)
        s = re.sub(r'\s*\[[^\[\]]*\]\s*\.?\s*$', '', s)          # trailing [hint]
        s = re.sub(r'\\qquad.*$|\\quad.*$', '', s)
        s = re.sub(r'\s+(Pp|Df|\\text\{Pp\}|\\text\{Df\})\.?\s*$', '', s)
        s = re.sub(r'\.\s*$', '', s) if not re.search(r'[:.]\s*\.\s*$', s) else s
        s = s.replace("∼", "~").replace("∴", ":.").replace("·", ".").replace("∶", ":")
        if "∨" not in s and "\\lor" not in s: s = re.sub(r'(?<=[\s~])v(?=\s)', '∨', f" {s} ").strip()
        try:
            if force_flat: raise ValueError
            return repr(dots.parse(dots.tokenize(s)))
        except Exception:   # Df/rules/quantified: dot-sensitive, whitespace-insensitive flat compare
            return flat(s)
    except Exception:
        return None
GREEK = {r"\\phi": "φ", r"\\psi": "ψ", r"\\chi": "χ", r"\\theta": "θ", r"\\exists": "∃",
         r"\\alpha": "α", r"\\beta": "β", r"\\gamma": "γ", r"\\kappa": "κ", r"\\lambda": "λ", r"\\mu": "μ"}
SUBS = {"ₓ": "_x", "ᵧ": "_y", "_{": "_", "ι": "℩", "\u2032": "'", "′": "'"}
LATEX_SYM = {r"\\in": "ε", r"\\epsilon": "ε", r"\\varepsilon": "ε", r"\\subset": "⊂", r"\\cup": "∪", r"\\cap": "∩",
    r"\\Lambda": "Λ", r"\\xi": "ξ", r"\\eta": "η", r"\\delta": "δ", r"\\rho": "ρ", r"\\sigma": "σ", r"\\tau": "τ",
    r"\\omega": "ω", r"\\nu": "ν", r"\\pi": "π", r"\\zeta": "ζ", r"\\iota": "℩", r"\\cdot": ".", r"\\times": "×",
    r"\\upharpoonright": "↾", r"\\upharpoonleft": "↿", r"\\Arrowvert": "‖", r"\\Vert": "‖", r"\\parallel": "‖", r"\\Delta": "Δ", r"\\ast": "*", r"\\star": "*", r"\\restriction": "↾", r"\\supseteq": "⊇", r"\\subseteq": "⊆",
    r"\\mid": "|", r"\\rightarrow": "→", r"\\leftarrow": "←", r"\\uparrow": "↑", r"\\downarrow": "↓", r"\\vert": "|"}
POST = {"ꓷ": "ᗡ", "Ꮯ": "ᗡ", "⇂": "↧", "Ꭰ": "ᗡ", "ϵ": "ε", "∥": "‖", "⌉": "↿", "◁": "↿", "⫡": "⥏", "ῐ": "℩\u0306", "∊": "ε", "“": "‘‘", "‼": "!!", "Ɑ": "ᗡ", "£": "⥏", "✱": "*", "∗": "*", "˘": "\u0306", "⁰": "^0", "¹": "^1", "²": "^2", "³": "^3", "⁴": "^4", "⁵": "^5", "⁶": "^6", "⁷": "^7", "⁸": "^8", "⁹": "^9", "₀": "_0", "₁": "_1", "₂": "_2", "₃": "_3", "₄": "_4", "₅": "_5", "₆": "_6", "₇": "_7", "₈": "_8", "₉": "_9", "∈": "ε", "⋐": "⊂\u0307", "⩀": "∩\u0307", "⩁": "∪\u0307", "⪽": "⊂\u0307", "⊍": "∪\u0307", "∸": "-\u0307", "−": "-", "ʻ": "‘", "'": "‘", "’": "‘", "‛": "‘", "ι": "℩"}
def flat(s):
    if "\\" in s: s = s.replace("~", " ")                                   # LaTeX literal ~ = non-breaking space
    for _ in range(3): s = re.sub(r'\\(?:text|mathrm|mathit|textit)\s*\{([^{}]*)\}', r' \1 ', s)   # unwrap text first (nested in accents); keep a separator
    for k, v in list(GREEK.items()) + list(LATEX_SYM.items()): s = re.sub(k + r'(?![a-zA-Z])', v, s)    # symbol macros before accents
    s = re.sub(r'\\breve\s*\{\s*([^{}]+?)\s*\}', lambda m: m.group(1) + "\u0306", s)
    s = re.sub(r'\\breve\s*([^\s{\\])', lambda m: m.group(1) + "\u0306", s)          # unbraced \breve R
    s = re.sub(r'˘\s*(\S)', lambda m: m.group(1) + "\u0306", s)                         # spacing breve before its base
    s = re.sub(r'\\overrightarrow\s*\{\s*([^{}]+?)\s*\}', lambda m: m.group(1) + "\u20d7", s)
    s = re.sub(r'\\overleftarrow\s*\{\s*([^{}]+?)\s*\}', lambda m: m.group(1) + "\u20d6", s)
    s = re.sub(r'\\overleftrightarrow\s*\{\s*([^{}]+?)\s*\}', lambda m: m.group(1) + "\u20e1", s)
    s = re.sub(r'\\overline\s*\{\s*([^{}]+?)\s*\}', lambda m: "".join(c + "\u0305" for c in m.group(1)), s)
    s = re.sub(r'\\unicode\{x([0-9a-fA-F]+)\}', lambda m: chr(int(m.group(1), 16)), s)
    s = s.replace("\\{", "").replace("\\}", "")                      # PM curly brackets: models often omit them
    s = re.sub(r'\\(?:text|mathrm)\{([^{}]*)\}', r'\1', s)
    for k, v in LATEX_SYM.items(): s = re.sub(k + r'(?![a-z])', v, s)
    s = re.sub(r'\\dot\{\s*([^{}]+?)\s*\}', lambda m: m.group(1) + "\u0307", s)
    s = re.sub(r'\\dot\s*(\S)', lambda m: m.group(1) + "\u0307", s)
    for k, v in GREEK.items(): s = re.sub(k + r'(?![a-z])', v, s)
    s = re.sub(r'\\(?:LATEXSYMDONE)', '', s)
    s = re.sub(r'\\hat\s*\{?\s*(\w)\s*\}?', lambda m: m.group(1) + "\u0302", s)
    s = s.replace("\\mathop", "")
    s = re.sub(r'\\quad\s*\[.*$|\\qquad.*$', '', s)                 # trailing hint
    s = re.sub(r'\\(?:text|mathrm)\{([^{}]*)\}', r'\1', s)           # keep E, and, prose
    s = s.replace(r"\neq", "≠").replace(r"\ne ", "≠").replace("&", "")
    s = dots.norm(s)
    for k, v in SUBS.items(): s = s.replace(k, v)
    s = s.replace("∼", "~").replace("·", ".").replace("∶", ":").replace("\\", "")
    for k, v in POST.items(): s = s.replace(k, v)
    s = re.sub(r'\s+', '', s)
    s = re.sub(r'(Df|Pp)\.?$', '', s)
    s = re.sub(r'^[✱*]?\d+\.\d+\.?', '', s)
    s = re.sub(r'(?<![\w\u0370-\u03ff℩∩∪⊂⊃∃Λ\-\u0300-\u036f\u20d0-\u20ff])([\u0306\u0307])(.)', lambda m: m.group(2) + m.group(1), s)   # mark written before its base
    s = re.sub(r'\[[^\[\]]*(?:\*|✱|Proof|Transp|Syll|Id|frac)[^\[\]]*\]$', '', s)   # trailing hint
    s = s.rstrip(".")
    s = unicodedata.normalize("NFD", s).replace("\u030c", "\u0306").replace("\u0304", "\u0305")   # caron->breve, macron->overline
    s = unicodedata.normalize("NFC", s)
    return "FLAT:" + s if s else None
def coarse(s):
    """Model-blind-spot projection: drop dots over relation signs and merge the restriction signs."""
    f = canon(s, True)
    if not f: return f
    f = unicodedata.normalize("NFD", f).replace("\u0307", "")
    for a in "↿⥏": f = f.replace(a, "↾")
    return unicodedata.normalize("NFC", f)
def pid_of(x):
    m = re.search(r'(\d+)\s*[·.]\s*(\d+)', x or "")
    return f"*{m.group(1)}.{m.group(2)}" if m else None
gut = collections.defaultdict(list)   # printed page -> [(pid, tex, offset)]
for m in re.finditer(r'\*(\d+)·(\d+)(?:</a>)?\s*\.?\s*</b>\s*(?:</td>\s*<td[^>]*>)?\s*(?:<span[^>]*>\s*)?<img[^>]*data-tex="([^"]*)"', t):
    gut[page_at(m.start())].append((f"*{m.group(1)}.{m.group(2)}", html.unescape(m.group(3)), m.start()))
def main():
    global passdir, model
    passdir, model = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "claude")
    rows, stats = [], collections.Counter()
    for f in sorted(glob.glob(f"{passdir}/{model}*.json"), key=lambda p: int(re.findall(r'(\d+)\.json$', p)[0])):
        djvu = int(re.findall(r'(\d+)\.json$', f)[0]); printed = djvu - 22
        raw = open(f, encoding="utf-8").read()
        try: d = json.loads(raw[raw.index("{"):raw.rindex("}") + 1])
        except Exception: stats["bad_json"] += 1; rows.append({"djvu": djvu, "status": "BAD_JSON"}); continue
        if d.get("printed_page") != printed: stats["page_mismatch"] += 1
        g = collections.defaultdict(list)
        for pid, tex, off in gut.get(printed, []): g[pid].append((tex, off))
        seen = set()
        for p in d.get("propositions", []):
            pid = pid_of(p.get("id")); seen.add(pid)
            cm = canon(p.get("formula", ""))
            if pid not in g:   # compare against every Gutenberg occurrence of this id, any page
                elsewhere = [(tex, off) for pg in gut.values() for q, tex, off in pg if q == pid]
                if not elsewhere: stats["model_only"] += 1; rows.append({"djvu": djvu, "printed": printed, "id": pid, "status": "MODEL_ONLY", "model": p.get("formula")}); continue
                g[pid] = elsewhere; stats["matched_off_page"] += 1
            for tex, off in g[pid]:
                cm1, cg = cm, canon(tex)                       # per-occurrence copies (no cross-occurrence leakage)
                if cm1 and cg and cm1.startswith("FLAT:") != cg.startswith("FLAT:"):
                    cm1, cg = canon(p.get("formula", ""), True), canon(tex, True)
                if cm1 != cg and canon(p.get("formula", ""), True) == canon(tex, True): cm1 = cg   # notation-only difference
                if cm1 is None or cg is None: st = "UNPARSED"
                elif cm1 == cg: st = "AGREE"
                else: st = "DISAGREE"
                stats[st] += 1
                if st != "AGREE": rows.append({"djvu": djvu, "printed": printed, "id": pid, "status": st, "model": p.get("formula"), "gutenberg": tex, "offset": off})
        for pid in g:
            if pid not in seen: stats["gutenberg_only"] += len(g[pid]); rows.append({"djvu": djvu, "printed": printed, "id": pid, "status": "GUTENBERG_ONLY", "gutenberg": g[pid][0][0]})
    print(dict(stats))
    for r in rows:
        if r["status"] in ("DISAGREE", "BAD_JSON"): print(json.dumps(r, ensure_ascii=False)[:600])
    json.dump(rows, open(f"{passdir}/compare_{model}.json", "w"), ensure_ascii=False, indent=1)

if __name__ == "__main__": main()
