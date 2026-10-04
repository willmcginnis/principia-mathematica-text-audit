#!/usr/bin/env python3
"""Parse the Vol I draft into items, attach the exact Gutenberg source string for each image."""
import re, json, html
G = open(__import__("os").environ.get("GUTFILE", "work/gutenberg/vol1-pg78050.html"), encoding="utf8").read()
TEX = {m.group(2): html.unescape(m.group(1)) for m in re.finditer(r'<img[^>]*?data-tex="([^"]*)"[^>]*?src="images/(\d+\.svg)"', G)}
t = open("vol1_errata_draft.txt").read()
head, rest = t.split("\n1. ", 1); rest = "1. " + rest
body, tail = rest.rsplit("\n\nThank you", 1)
items = []
for blk in re.split(r"\n\n(?=\d+(?:–\d+)?\. )", body):
    m = re.match(r"(\d+(?:–\d+)?)\. (.*)", blk, re.S)
    if not m: continue
    first = m.group(2).split("\n   ")[0]
    f = {"n": m.group(1), "hdr": first.strip()}
    for k in ("Current", "Scan", "Change", "Note"):
        mm = re.search(rf"^   {k}:\s*(.*?)(?=\n   [A-Z][a-z]+:|\Z)", blk, re.M | re.S)
        if mm: f[k.lower()] = mm.group(1).strip()
    trailer = blk.split("\n   ")[-1]
    imgs = re.findall(r"(?:images/)?(\d{3,5})\.svg", first)
    f["images"] = [i + ".svg" for i in imgs]
    f["source"] = {i: TEX.get(i) for i in f["images"]}
    items.append(f)
# a trailing prose line inside a block (e.g. "The following five were found by...") stays with the previous block; capture section notes
json.dump({"head": head, "tail": "Thank you" + tail, "items": items}, open("vol1_items.json", "w"), ensure_ascii=False, indent=1)
print(len(items), "items;", sum(len(i["images"]) for i in items), "images;", sum(1 for i in items for v in i["source"].values() if v is None), "images without data-tex")
for i in items:
    if not i["images"] or any(v is None for v in i["source"].values()): print("  check:", i["n"], i["hdr"][:90])
