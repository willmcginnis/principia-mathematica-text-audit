#!/usr/bin/env python3
"""Triage single-reader (Codex-only) full-page hunks: drop formatting noise, set aside known blind-spot classes,
queue the rest for forced choice. Usage: body_triage.py CANDIDATES_JSON OUT_QUEUE_JSON"""
import json, re, sys, collections
SUB = str.maketrans({"ₐ": "a", "ₑ": "e", "ₒ": "o", "ₓ": "x", "ₚ": "p", "ₛ": "s", "ₜ": "t", "ᵣ": "r", "ᵤ": "u", "ᵥ": "v", "ₙ": "n", "ₘ": "m", "ₖ": "k", "ₗ": "l", "ₕ": "h"})
def fmt(s):
    s = s.translate(SUB).replace("″", '"').replace("∣", "|").replace("′", "'").replace("_", "").replace("{", "").replace("}", "")
    s = re.sub(r"operatorname|mathrm|mathrel|mathop|overrightarrow|overleftarrow|overline|textrm|\\?rm|text|frac|beginarray[lcr]*|endarray|mathfrak|mathcal|mathbf|displaystyle|\\^", "", s)
    s = s.replace("—", "-").replace("–", "-")
    s = s.translate(str.maketrans({"α": "a", "β": "b", "ε": "e", "ρ": "r", "σ": "s"})) if len(s) <= 3 else s   # Greek subscripts written as Latin ₐ/ₑ
    return s
MARKS = "̇̆̅̂⃗⃖⃡"            # dot, breve, overline, hat, arrows
BLIND = [lambda a, b: a.replace("ᗡ", "") == b.replace("ᗡ", "") or ("ᗡ" in a and re.fullmatch(r"(C|Cl|𝔇|D|ℭ|℩|Ɑ|Ꮯ)?", b)),
         lambda a, b: a.translate({ord(c): None for c in MARKS}) == b.translate({ord(c): None for c in MARKS}),
         lambda a, b: set(a) | set(b) <= set("↾↿⥏|'!↧↓℩"),
         lambda a, b: re.sub(r"[ṡ]", "s", a) == b]
def main():
    C = [r for r in json.load(open(sys.argv[1])) if r.get("status") in ("no_opus", "agree", "opus_other")]
    out, cnt = [], collections.Counter()
    for r in C:
        a, b = r["pg"], r["read"]
        if fmt(a) == fmt(b): cnt["formatting"] += 1; continue
        if any(f(fmt(a), fmt(b)) for f in BLIND): cnt["blindspot (set aside)"] += 1; r["triage"] = "blindspot"; continue
        if len(a) + len(b) > 80: cnt["block (alignment)"] += 1; continue
        cnt["queue"] += 1; out.append(r)
    json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
    print(cnt); c2 = collections.Counter((r["pg"], r["read"]) for r in out)
    for (a, b), n in c2.most_common(30): print(n, repr(a), "->", repr(b))
if __name__ == "__main__": main()
