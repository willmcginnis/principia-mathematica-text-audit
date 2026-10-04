#!/usr/bin/env python3
"""Shared normalizer and set-aside filters for the full-page comparison (used here for Vol II).
post() maps both text streams to one normalized form after space stripping; blind() is the set-aside test.
The same code also serves the Vol III comparison, whose input (DP's unposted text) is not published."""
import re, unicodedata
SUB = str.maketrans({**{c: d for c, d in zip("₀₁₂₃₄₅₆₇₈₉", "0123456789")}, **{c: d for c, d in zip("ₐₑₒₓₕₖₗₘₙₚₛₜᵣᵤᵥ", "aeoxhklmnpstruv")},
                      **{c: d for c, d in zip("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")}, "⊦": "⊢", "⥏": "↾", "⋖": "<", "⋗": ">", "″": '"', "ʹ": "'", "′": "'",
                      "∔": "+", "ϖ": "ϖ", "\\": None, "{": None, "}": None, "_": None, "^": None,
                      "\u0307": None, "\u0306": None, "\u20d7": None, "\u20d6": None, "\u0302": None, "\u0305": None})
MAC = [("infty", "∞"), ("int", "∫"), ("in", "ε"), ("geq", "≥"), ("leq", "≤"), ("breve", ""), ("ldots", "…"), ("...", "…"), ("&", ""), ("varsigma", "ς"), ("varpi", "ϖ"), ("varphi", "φ"), ("vartheta", "θ"), ("nabla", "∇"), ("prime", "'"), ("dashv", "⊣"),
       ("overleftrightarrow", ""), ("overleftarrow", ""), ("overrightarrow", ""), ("supset", "⊃"), ("subset", "⊂"), ("smallfrown", ""),
       ("overset", ""), ("downarrow", "↓"), ("uparrow", "↑"), ("parallel", "∥"), ("upharpoonright", "↾"), ("upharpoonleft", "↿"), (";", "'"),
       ("vdash", "⊢"), ("operatorname", ""), ("mathrm", ""), ("mathit", ""), ("mathbf", ""), ("text", ""), ("ldotp", "."), ("colon", ":"),
       ("cdot", "."), ("lor", "∨"), ("equiv", "≡"), ("sim", "∼"), ("cap", "∩"), ("cup", "∪"), ("exists", "∃"), ("epsilon", "ε"), ("hat", "")]
SETASIDE = [("ς", "s"), ("⊢⊣", "↦"), ("⇸", "↦"), ("↤", "↦"), ("⩿", "≤"), ("≦", "≤"), ("⪀", "≥"), ("≧", "≥"), ("ᴿ", "R"), ("ᵝ", "β"), ("ᵦ", "β"), ("ᵧ", "γ"), ("ᵞ", "γ"), ("ᵨ", "ρ"), ("ᵩ", "φ"), ("ᵠ", "φ"), ("ᵪ", "χ"), ("ᵅ", "α"), ("ᵟ", "δ"), ("ᶿ", "θ"), ("ⁱ", "i"), ("ᵢ", "i"), ("ʲ", "j"), ("ⱼ", "j"),  ("qquad", ""), ("quad", ""), ("beginarray", ""), ("endarray", ""), ("neq", "≠"), ("rightarrow", "→"), ("⟝", "⊢"), ("ⁿ", "n"), ("ᵐ", "m"), ("ᶜ", "c"),  ("[pd]", "∂"), ("´", "'"), ("∷", "::"),  ("dagger", "*"), ("bar", ""), ("⇷", "↦"), ("₍", "("), ("₎", ")"), ("⁽", "("), ("⁾", ")"), ("„", ",,"),  ("hfill", ""), ("ϖ", "π"),  ("＊", "*"), ("℩", "1"), ("⤉", "⨣"), ("<tb>", "")]
GREEK = {n: unicodedata.lookup("GREEK SMALL LETTER " + ("LAMDA" if n == "lambda" else n.upper())) for n in "alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu nu xi omicron pi rho sigma tau upsilon phi chi psi omega".split()}
GREEK.update({"Lambda": "Λ", "Omega": "Ω", "Sigma": "Σ", "Pi": "Π", "Phi": "Φ", "Psi": "Ψ", "Delta": "Δ", "Gamma": "Γ", "Theta": "Θ", "aleph": "ℵ", "partial": "∂", "dfrac": "frac"})
def _mac(t):
    # LaTeX macro names are replaced only when written as macros (backslash-prefixed), so prose is untouched
    for a, b in sorted(MAC, key=lambda x: -len(x[0])):
        if a[0].isalpha():
            t = re.sub(r"\\" + re.escape(a) + r"(?![A-Za-z])", lambda m, b=b: b, t)
        else:
            t = t.replace(a, b)
    return re.sub(r"\\(" + "|".join(sorted(GREEK, key=len, reverse=True)) + r")(?![A-Za-z])", lambda m: GREEK[m.group(1)], t)
def _mac_math(t):
    # inside math segments the upstream LaTeX flattener can leave bare macro names (backslash already gone)
    for a, b in sorted(MAC, key=lambda x: -len(x[0])):
        if len(a) >= 5 or not a[0].isalpha(): t = t.replace(a, b)     # short names (in, cap, int, sim) collide with words inside \text{}
    return re.sub(r"(?<![a-z])\\?(" + "|".join(sorted((g for g in GREEK if len(g) >= 4), key=len, reverse=True)) + r")(?![a-z])", lambda m: GREEK[m.group(1)], t)
def post(t):   # applied to both streams after space stripping; \x01..\x02 marks math segments
    t = re.sub(r"[—–‒−]", "-", t)
    t = re.sub(r"\\?infty", "∞", t)   # bare 'infty' survives on the Vol II Gutenberg side (backslash lost upstream); never an English word
    t = "".join(_mac_math(_mac(p[1:-1])) if p.startswith("\x01") else _mac(p) for p in re.split(r"(\x01.*?\x02)", t, flags=re.S))
    t = t.replace("\x01", "").replace("\x02", "")
    t = unicodedata.normalize("NFD", t).translate(SUB)
    for a, b in SETASIDE: t = t.replace(a, b)
    t = re.sub(r"ᗡ|Cℓ|ℭ", "ᗡ", t)          # converse-domain glyph family: set aside, as in Vol I
    t = re.sub(r"\.{4,}", "", t)
    return re.sub(r"\*(?!\d)", "", t)
DOTS = set(".:'ʻ,")
PAIRS = {frozenset(x) for x in [("×", "x"), ("S", "s"), ("C", "c"), ("P", "p"), ("⊂", "ε"), ("E", "∃"), ("1", "i"), ("1", "ι"), ("1", "↧"), ("1", "t"), ("⨣", "↑"), ("⨣", "↟"), ("⨣", "↥"), ("⨣", "+"), ("↦", "+→"), ("↦", "↣"), ("c", "꜀"), ("'", '"')]}
def blind(a, b):
    if frozenset((a, b)) in PAIRS: return True   # set-aside classes carried over from Vol I (dots, ᗡ glyph, E/∃), plus apostrophe-only hunks
    if set(a + b) <= DOTS: return True
    if set(a + b) <= set("[]<>=") : return True                       # DP bracket-notation residue
    if a == "ᗡ" and b in {"C", "Cl", "D", "1", "ℂ", "G", "Cℓ", "ℭ"}: return True
    if len(a) > 1 and a != b and a.lower() == b.lower() and set(a.lower()) <= set("ivxlc"): return True   # small-capital roman numerals (Vol. IV / iv)
    return {a, b} == {"E", "∃"}
# Notation representation (2026-10-04 review): the same printed glyph written two ways, not a text difference.
# ⇷ (Gutenberg's leftward arrow with a stroke) is mapped to ↦ in SETASIDE, and readers write it ←+; Gutenberg's ʻʻ
# double inverted comma arrives as '' and readers write "; Gutenberg's ↓_{.,} subscript dots vs a combining diaeresis
# below; a lone combining mark (dotted operators: SUB strips U+0307 but not U+0308). Used by vol2_split_artefacts.py;
# not yet part of blind(), so earlier Vol I and Vol III counts are unchanged until those comparisons are re-run.
NOTATION = {frozenset(x) for x in [("↦", "←+"), ("''", '"'), (".,", "̤")]}
def notation(a, b):
    if frozenset((a, b)) in NOTATION: return True
    return bool(a + b) and all(unicodedata.combining(c) for c in a + b)
