#!/usr/bin/env python3
"""Forced choice for full-page hunks: Opus sees the page image and two unlabeled readings of one short span
(PG vs blind reader, random order) and picks the one that matches the print. Output is one line, no transcription.
Usage: fc_full.py CANDIDATES_JSON [PAR]   -> <same>.fc.json"""
import json, sys, random, subprocess, os, tempfile, shutil, concurrent.futures as cf
H = os.environ.get("PM_WORK", "work")
JUDGE = os.environ.get("JUDGE", "opus"); IMGFMT = os.environ.get("IMGFMT", H + "/scan/djvu{d}.jpg"); OFFS = int(os.environ.get("OFF", "22"))
TOK = os.environ.get("CLAUDE_CODE_OAUTH_TOKEN", "")  # optional; a normal claude login also works
PROMPT = ("Read only the file {img} and nothing else. It is a page of Principia Mathematica (first edition). "
          "Below are two readings, A and B, of the same short passage on this page (spaces around symbols and punctuation are removed). "
          "Find the passage on the page and decide which reading matches the PRINT exactly, character for character, including dots, commas, brackets and symbols. "
          "Do not judge which is more correct mathematically; judge only what is printed.\n"
          "A: {a}\nB: {b}\n"
          "Answer with exactly one line: A, B, BOTH, or NEITHER, then a colon and at most 15 words naming the printed difference.")
import threading
_AUTH = {"fail": 0, "ok": 0}; _AL = threading.Lock()
def ask(row, seed):
    with _AL:
        if _AUTH["fail"] >= 5 and _AUTH["ok"] == 0:
            return dict(row, fc_answer="SKIPPED: judge login failing", fc_pick="skipped")
    rnd = random.Random(seed)
    pgv, rdv = row["ctx_pg"], row["ctx_read"]
    swap = rnd.random() < 0.5
    a, b = (rdv, pgv) if swap else (pgv, rdv)
    img = IMGFMT.format(d=row.get("seq", row["page"] + OFFS), d3="%03d" % row.get("seq", row["page"] + OFFS))
    w = tempfile.mkdtemp(); shutil.copy(img, f"{w}/page.jpg")
    try:
        if JUDGE == "codex":
            q = PROMPT.format(img="the attached image", a=a, b=b).replace("Read only the file the attached image and nothing else. ", "Look only at the attached image. ")
            p = subprocess.run([os.environ.get("CODEX", "codex"), "exec", "--skip-git-repo-check", "-c", 'model_reasoning_effort="high"', q, "-i", f"{w}/page.jpg"],
                               capture_output=True, text=True, cwd=w, timeout=900, stdin=subprocess.DEVNULL)
        else:
            p = subprocess.run(["claude", "-p", "--model", "claude-opus-5-5", "--effort", "high", "--allowedTools=Read"],
                               input=PROMPT.format(img=f"{w}/page.jpg", a=a, b=b), capture_output=True, text=True,
                               cwd=w, timeout=600, env=dict(os.environ, **({"CLAUDE_CODE_OAUTH_TOKEN": TOK} if TOK else {})))
        ans = p.stdout.strip().splitlines()[-1] if p.stdout.strip() else "ERR " + p.stderr[-200:]
    except Exception as e:
        ans = f"ERR {e}"
    finally:
        shutil.rmtree(w, ignore_errors=True)
    with _AL:
        _AUTH["fail" if ("authenticate" in ans.lower() or "oauth" in ans.lower()) else "ok"] += 1
    head = ans.split(":")[0].strip().strip("*").upper()
    pick = {"A": ("read" if swap else "pg"), "B": ("pg" if swap else "read")}.get(head, head.lower())
    return dict(row, fc_answer=ans, fc_pick=pick)
def main():
    path = sys.argv[1]; par = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    rows = [r for r in json.load(open(path)) if r.get("ctx_pg")]
    out = []
    with cf.ThreadPoolExecutor(par) as ex:
        for r in ex.map(lambda t: ask(t[1], t[0]), enumerate(rows)): out.append(r)
    json.dump(out, open(path.replace(".json", os.environ.get("FCSUFFIX", ".fc.json")), "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    print(Counter(r["fc_pick"] for r in out))
    if _AUTH["ok"] == 0 and _AUTH["fail"]: sys.exit("judge login failed on every call; output marked skipped — refresh the login and re-run")
if __name__ == "__main__": main()
