#!/usr/bin/env python3
"""Blindspot rows: locate the proposition on the page, crop the native-resolution DjVu band (2x upscale),
ask Opus mark-by-mark which reading matches the print. Usage: bs_check.py [PAR]"""
import json, os, re, sys, random, subprocess, tempfile, shutil, concurrent.futures as cf
from PIL import Image
H = os.environ.get("PM_WORK", "work"); DJVU = os.environ.get("DJVU", os.path.join(H, "djvu/vol1.djvu"))
TOK = os.environ.get("CLAUDE_CODE_OAUTH_TOKEN", "")  # optional; a normal claude login also works
def claude(prompt, img):
    w = tempfile.mkdtemp(); shutil.copy(img, f"{w}/img.png")
    try:
        p = subprocess.run(["claude", "-p", "--model", "claude-opus-5-5", "--effort", os.environ.get("EFFORT", "high"), "--allowedTools=Read"], input=prompt.replace("IMG", f"{w}/img.png"),
                           capture_output=True, text=True, cwd=w, timeout=900, env=dict(os.environ, **({"CLAUDE_CODE_OAUTH_TOKEN": TOK} if TOK else {})))
        return p.stdout.strip() or ("ERR " + p.stderr[-200:])
    except Exception as e:
        return f"ERR {e}"
    finally:
        shutil.rmtree(w, ignore_errors=True)
import threading, collections as _c
_LOCKS = _c.defaultdict(threading.Lock); _GL = threading.Lock()
def page_png(d):
    out = f"{H}/scan/hires/p{d}.png"
    with _GL: lk = _LOCKS[d]
    with lk:
        if not os.path.exists(out):
            os.makedirs(os.path.dirname(out), exist_ok=True)
            tmp = f"{out}.{threading.get_ident()}.pnm"
            subprocess.run(["ddjvu", "-format=pnm", f"-page={d}", DJVU, tmp], check=True)
            Image.open(tmp).save(out + ".part.png"); os.replace(out + ".part.png", out); os.remove(tmp)
    return out
def one(i_row):
    try:
        return _one(i_row)
    except Exception as e:
        return dict(i_row[1], bs_pick="error", bs_answer=f"{type(e).__name__}: {e}")
def _one(i_row):
    i, r = i_row
    pid = r["id"].replace("*", "✱").replace(".", "·")
    full = page_png(r["djvu"]); W, Hh = Image.open(full).size
    loc = claude(f"Read only the file IMG and nothing else. It is a page of Principia Mathematica. Find the proposition labelled {pid} "
                 "(its whole display, including continuation lines). Reply with one line only: TOP=<fraction> BOTTOM=<fraction>, "
                 "the vertical extent as fractions of the page height from the top (e.g. TOP=0.41 BOTTOM=0.47).", full)
    m = re.search(r"TOP=\s*([0-9.]+).*?BOTTOM=\s*([0-9.]+)", loc)
    if not m: return dict(r, bs_loc=loc, bs_pick="noloc")
    t, b = max(0, float(m.group(1)) - 0.02), min(1, float(m.group(2)) + 0.02)
    crop = full.replace(".png", f"_{i}.png")
    band = Image.open(full).crop((0, int(t * Hh), W, int(b * Hh)))
    hw = int(W * 0.58); L, R = band.crop((0, 0, hw, band.height)), band.crop((W - hw, 0, W, band.height))
    st = Image.new("RGB", (hw, band.height * 2 + 20), "white"); st.paste(L, (0, 0)); st.paste(R, (0, band.height + 20))
    if st.width > 1900: st = st.resize((1900, int(st.height * 1900 / st.width)), Image.LANCZOS)
    st.save(crop)
    rnd = random.Random(i); swap = rnd.random() < 0.5
    A, B = (r["gutenberg"], r["model"]) if swap else (r["model"], r["gutenberg"])
    ans = claude(f"Read only the file IMG and nothing else. It shows one Principia Mathematica line containing {pid} at full scan resolution, cut into an overlapping LEFT half (top) and RIGHT half (bottom) of the same line. "
                 "Look very closely at small marks: a dot above V, Λ, ⊂, ∪, ∩, −, ∃ or a relation letter; breves; arrows; the restriction signs ↾ ↿ and similar. "
                 "Ignore any handwriting. First list, in order, every sign in the printed formula that carries (or could carry) such a mark and what the print shows. "
                 f"Then compare with two readings (B may be LaTeX):\nA: {A}\nB: {B}\n"
                 "Last line exactly: VERDICT: A, B, BOTH, or NEITHER (matching the print character for character).", crop)
    vs = re.findall(r"VERDICT:\s*\**\s*(BOTH|NEITHER|A|B)\b", ans or "")   # longest alternatives first; last verdict wins
    head = vs[-1] if vs else "unparsed"
    pick = {"A": "pg" if swap else "model", "B": "model" if swap else "pg"}.get(head, head.lower())
    return dict(r, bs_band=[t, b], bs_answer=ans[-1500:], bs_pick=pick)
def main():
    par = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    src = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] != "test" else f"{H}/scan/pass3/blindspot_opus.json"
    dst = sys.argv[3] if len(sys.argv) > 3 else f"{H}/scan/pass3/blindspot_checked.json"
    rows = json.load(open(src))
    done = {}
    if os.path.exists(dst):
        for x in json.load(open(dst)):
            if x.get("bs_pick") not in ("error", "noloc", "unparsed"): done[(x["id"], x["djvu"], x["gutenberg"])] = x
    todo = [(i, r) for i, r in enumerate(rows) if (r["id"], r["djvu"], r["gutenberg"]) not in done]
    out = list(done.values()); lk = threading.Lock()
    with cf.ThreadPoolExecutor(par) as ex:
        for x in ex.map(one, todo):
            with lk:
                out.append(x); json.dump(out, open(dst + ".tmp", "w"), ensure_ascii=False, indent=1); os.replace(dst + ".tmp", dst)
    from collections import Counter; print(Counter(x["bs_pick"] for x in out))
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "test":
        r = json.load(open(f"{H}/scan/pass3/blindspot_opus.json"))[0]; x = one((0, r)); print(x["bs_band"] if "bs_band" in x else x.get("bs_loc"), x["bs_pick"]); print(x.get("bs_answer", "")[-900:])
    else: main()
