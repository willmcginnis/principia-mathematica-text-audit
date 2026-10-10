# Methodology

Everything here is provisional and will change as the review continues.

Parameters below are those used for the runs reported here. Numbers are labelled **MEASURED** (we ran it)
or **DOCUMENTED** (taken from someone's documentation and not independently checked). Unless a section says
otherwise, every count is a pipeline output that has **not yet been confirmed by the human review** and is
awaiting human review (§7).
"Checked by Claude" below means checked by the orchestrating model, not by a person. Terms are defined in
the [README glossary](README.md#glossary).

## 1. Sources

| Volume | Digital text under audit | Page images | Page alignment |
|---|---|---|---|
| I | Project Gutenberg #78050 (HTML, LaTeX in `data-tex`) | Commons `Russell, Whitehead - Principia Mathematica, vol. I, 1910.djvu`, 696 pp., 2720 × 4585 at native resolution | DjVu page = printed page + 22 (MEASURED) |
| II | Project Gutenberg #78255 | Commons Vol. II 1912 DjVu, 816 pp., rendered 2720 px wide and 4,324–4,442 px tall (MEASURED on 21 sampled pages), SHA-1 `09eb65c3…` verified | DjVu page = printed page + 40 (MEASURED on 18 sampled pages, all agree) |
| III | Distributed Proofreaders (DP) project, formatting round, not yet posted (third proofing round complete on all 501 pages) | UMich Historical Mathematics Collection `aat3201.0003.001`, 1913 first edition, 512 images, IIIF, resampled to 2720 px wide | image = DP page + 6 (e.g. DP page 12 is image 18; MEASURED by text similarity on all 496 matchable pages) |

Archive.org's Vol III copies are the **1927 second edition**, so they are the wrong witness and are not used.

Image resolution differs by volume and stage:

- **Vol I, reading and judging:** 1920 px wide JPEGs (`djvuN.jpg`, e.g. 1920 × 3236). These are Commons' own
  renders of the DjVu, downloaded with [`scripts/fetch_vol1_pages.sh`](scripts/fetch_vol1_pages.sh) (Commons caps
  page thumbnails at 1920 px). The blind readers and both judges saw these images, in both the proposition pass
  and the full-page pass.
- **Vol I, crop check:** the page is rendered from the DjVu at native resolution (2720 px wide) with `ddjvu`
  ([`scripts/bs_check.py`](scripts/bs_check.py)), and one line is cut out of it.
- **Vol II:** every page is rendered from the DjVu at native resolution
  ([`scripts/render_djvu.sh`](scripts/render_djvu.sh)); readers and judges saw the same 2720 px image.
- **Vol III:** IIIF images resampled to 2720 px wide.

DP's Volume III text is unpublished work in progress. It is not redistributed here, and no part of it is
quoted. For Volume III this repository gives only counts, method and page numbers; findings go to the DP
project team through DP's own process.

## 2. Blind reading

### Full-page pass (Vol I Introduction and body, Vols II and III)

Each page image is transcribed in full (prose, formulas, footnotes) by two runs that are never shown the
digital text:

- **Reader 1:** OpenAI Codex at the server's default reasoning effort. When effort is left unset the client sends nothing. On our §5 benchmark it performed similarly to `low`/`medium`; what the server does with an unset effort is not established.
- **Reader 2:** for the Vol I body and Vols II–III, the same Codex model at `high` effort. It is a deliberately
  different second witness, not a better one. For the **Vol I Introduction** (pp. 1–88), Reader 2 was
  **Claude Opus**. Claude's output filter blocked many of its full-page transcriptions, so Opus produced a
  reading for only 44 of the 88 pages. That is why Opus was later dropped as a reader. Since then it has
  been used only for one-line judgements (§4).

Coverage (MEASURED from the comparison record): Vols II and III have both readings on every page. In the Vol I
body (pp. 89–666), Reader 1's reading differed from Gutenberg on 536 compared pages. On 5 further pages
(pp. 90, 93, 344, 374, 487) Reader 1 produced a reading, but the Gutenberg text could not be split out at a
page marker, so they were not compared. Of the 536 compared pages,
Reader 2 was attempted on 433 and succeeded on 426 (7 failed). The other 103 were never attempted; the rule
that chose the attempted pages was not recorded. That leaves 110 compared pages with no second reading.
109 of them carry the 1,024 Reader-1 hunks that have only one reading (their follow-up is in §7). The 110th has only one hunk, and it
matched a published erratum.

The prompt ([`scripts/prompt_full.txt`](scripts/prompt_full.txt)) asks for a faithful transcription and says to ignore
handwriting. The Commons Vol I copy carries a reader's handwritten corrections that match PM's
own published errata. Each run gets an empty working directory and only the page image.

### Proposition pass (Vol I, earlier)

The Vol I report entries ([`errata/vol1.md`](errata/vol1.md)) come from this earlier, proposition-level check,
run in three batches on the same 1920 px page images. Readers were given only the page image, never the digital
text. They were not sandboxed, though, so this rests on the prompts and the working directory; no log shows a
reader opening the ebook.

- **Batch 1 (pp. 98–131).** One Claude reader read each page (the model was not recorded; the script's default
  was Claude Sonnet). For each disputed proposition, Claude Opus re-read it from the page, shown neither
  reading. A pilot Codex reading of two of these pages agrees with the print reading.
- **Batch 2 (pp. 132–250).** Claude Opus read each page. For each disputed proposition, Opus re-read it from
  the page, shown neither reading. Claude Sonnet was then shown the page and the two versions (the blind
  reading and Gutenberg's) unlabelled, in random order, and picked one; so this judge did see Gutenberg's
  version, as one of the two options. Codex read the page independently. Its logs record "reasoning effort:
none". We have not checked whether that is how the client reports an unset effort (compare §5).
- **Batch 3 (pp. 251–666, ✱31–✱97).** As batch 2, except that the Codex reading came first and was used as a
  filter: a row went on only if Codex agreed with Opus. The same Codex reading was then counted as the fourth
  witness, so it is not an extra check. **Tier 1** is rows where all four agree against Gutenberg (65 rows:
  52 are report entries 29–80, and 13 are held back). **Tier 2** is the 114 rows with weaker support, decided by the crop check
  (§4.3), which picked the print on 47. Rows that differ only in dots over relation or restriction signs
  (83 rows) went straight to the crop check, which picked the print on 4.
- **Proof replay.** Replaying the ✱1–✱5 proofs by machine found 5 further lines. Each was checked by one Opus
  reading of the line from the page.

None of the report entries went through the crop check. 49 of the 102 entries in the earlier draft were also
found independently by the later full-page pass, with both judges picking the print. The report's introduction
says which entries were checked which way. §5b explains why 22 entries are held back.

## 3. Comparison

Both sides are reduced to one normalized character stream per page:

1. LaTeX is mapped to Unicode with a shared symbol table: `\supset` → ⊃, Greek names → letters, `\text{…}` kept as words, array and alignment markup removed.
2. For Vol III, DP's in-round markup conventions (bracketed arrow and breve notation, small-capital tags and the like) are mapped to the same forms.
3. All whitespace is removed, so spacing never creates a difference. Word splits and joins are checked separately on a word stream.
4. Footnotes are re-attached to their page, and running heads and page numbers are dropped.

`difflib` then yields hunks (replace, insert, delete). [`scripts/fullpage_compare.py`](scripts/fullpage_compare.py)
labels each hunk by what Reader 2 did at the same place:

| Label in the script | Meaning |
|---|---|
| `agree` | Reader 2 made the same change. Only these go forward. |
| `opus_other` | Reader 2 made a different change at that place. |
| `opus_matches_pg` | Reader 2 agrees with the digital text. |
| `no_opus` | No Reader 2 text for that page. |
| `applied_erratum` | The hunk matches one of PM's published errata (§4.4). |

The `opus_*` names date from the Introduction run, where Reader 2 was Opus. The script reads Reader 2 from the
directory named by `SECOND` (default `opus`, which reproduces the Introduction run). The body and Vol II runs
set `SECOND=codexhi`, so for them the labels mean Codex at high effort.

Gutenberg's text is split into pages at its `[Pg N]` markers. Where a marker sits a line early or late, whole
lines show up as "missing" on one page and "extra" on the next. Vol II rows of this kind are now set aside by
rule (§4.5). A rendering bug also left LaTeX fragments in the Gutenberg stream wherever a formula contained `<`.
It is fixed in `fullpage_compare.py`, and the Vol II rows it produced are set aside (§4.5). The Vol I body
rows were classified before this was found, and the Vol I TeX-residue class (2 rows, discarded) is the same
artefact.

### Set-aside classes (not judged; reported separately)

Some differences are systematic reader blind spots, not evidence. Their pairs are set aside:

- PM's dot punctuation when only dots, colons or commas differ;
- the inverted D (ᗡ) read as C, Cl or D;
- E! vs ∃!;
- arrows and breves over letters;
- dotted operators (⊂̇, ∩̇);
- capital vs. small subscripts, which Unicode cannot express (P/p, S/s, C/c);
- ℩ vs 1;
- case-only differences in small-capital roman numerals (IV/iv);
- and, for Vol III, bracket residue from DP's in-round notation.

These classes are listed in [`scripts/normalize.py`](scripts/normalize.py) (`SETASIDE`, `PAIRS`, `blind()`) and,
for the Vol I body pass, [`scripts/body_triage.py`](scripts/body_triage.py). Some entries in the Vol I report
fall in these classes. They were not taken from the full-page pass, and each one's separate check is
stated in the report itself (§5b).

## 4. Adjudication

1. **Forced choice (Claude Opus 5.5, effort `high`).** The judge sees the full page image and two unlabelled readings, A and B, of one short span (about 35 characters either side), in random order. It answers with one line: A, B, BOTH or NEITHER, plus at most 15 words naming the printed difference. It does not transcribe, and it is told to judge only the print, not mathematical correctness.
2. **Veto (OpenAI Codex, effort `high`).** The same forced choice, run independently on rows Opus decided for the scan. A row is kept only if both judges pick the scan reading. In the Vol I body, Opus picked the scan on 495 rows. 29 of these were long whole-line rows (page-alignment shifts) and were removed before the veto. On the other 466, Codex picked the scan on 339, Gutenberg on 6, neither on 120 and both on 1. That sample was preselected for Opus scan wins, so the split does not measure Codex's own bias. Codex is the readers' model family, so its acceptance is never treated as confirmation on its own. It is used only to remove rows. **The 53 Vol I Introduction rows had no veto** (§6 and the README).
3. **High-resolution crop check (blind-spot rows only).** The proposition is located, the band is cropped from the native-resolution DjVu (left and right halves stacked), and Opus gives a mark-by-mark verdict.
4. **Published-errata filter.** PM printed its own errata. A hunk that matches a published correction is the digital edition correctly applying the author's errata, and it is not reported as an error. The lists used:
   - **Vol I:** Vol I's own errata slip (1910), the "Additional Errata to Volume I" printed in Vol II, and the "Additional Erratum to Volume I" printed in Vol III (p. x).
   - **Vol II:** Vol II's own errata list and the "Additional errata to Volume II" printed in Vol III. For Vol II, the 17 judged rows on pages that carry a published erratum were held out and classified one at a time against the erratum text and the page image, by Claude (not a person). Claude classified 8 as Gutenberg correctly applying an erratum, 7 as further candidate discrepancies the erratum does not touch, 1 as page-marker placement and 1 as small-capital typography. One of the 7 (S3) lies inside the p. 71 definition that an unapplied erratum replaces, so applying the erratum would probably supersede it.
   - **Vol III:** the Errata to Volume III printed in Vol III (pp. ix–x), transcribed from the scan. As for Vol II, the automatic matcher is not used: the 14 judged rows (10 distinct differences; 7 rows on p. 187 repeat 3 of them) on the 7 erratum pages that have judged rows were classified, one distinct difference at a time, against the erratum text and the page image, by Claude (not a person). None of the rows is an already-printed erratum, so this filter sets aside no rows.

   The automatic matcher has known gaps: it can both miss and over-match (§8).
5. **Vol II artefact split.** After both judges, [`scripts/vol2_split_artefacts.py`](scripts/vol2_split_artefacts.py) sets aside, with a written reason per row:
   - rows that disappear when the page is re-compared with the fixed renderer (10);
   - small-capital roman numerals (1);
   - notation representation (6, added after the second public-draft review): the same printed glyph written two ways. These are Gutenberg's ⇷ (normalized to ↦) vs the readers' ←+; Gutenberg's ʻʻ double inverted comma (normalized to `''`) vs `"`; Gutenberg's `↓_{.,}` subscript dots vs a combining diaeresis below; and a lone combining diaeresis on a dotted operator. The rule is `notation()` in [`scripts/normalize.py`](scripts/normalize.py). It is not yet part of `blind()`, so it has not been applied to the Vol I counts; the Vol III artefact review applies it (§4.6);
   - page-marker placement (51). This covers whole text on one side only, at the very start or end of a page, that is found again (similarity ≥ 0.85) at the end of the previous page's reading or the start of the next page's Gutenberg text. 48 rows meet the rule; the other 3 were decided by Claude looking at the page images.

   Re-comparing the 17 affected pages with the fixed renderer also found 6 reader-agreed hunks, on 6 of those pages, that had never been judged, and the set-aside p. 497 row hid a possible `*183-26` slip. Both models judged these 7 follow-up rows on 2026-10-08, and each row records both picks, the A/B order and the date. Both judges picked the print on 2 (p. 191: Gutenberg ⊢, print ⊣; p. 225: Gutenberg ✱, print ·), which are kept. The other 5 are set aside as rejected by the judges, each with a reason: two printer's signature marks (pp. 179, 227), a paragraph plus signature mark that Gutenberg places at the top of the next page (p. 275), and two where only Opus picked the print (p. 558 `<br>`, p. 497 `*183-26`).

   Of 222 judged rows, 149 remain, on 125 pages; 73 are set aside (68 comparison artefacts of the 215 original rows, and the 5 rejected follow-up rows). The renderer
   and notation rules are deterministic; the page-marker rule is a similarity test. **The public scripts do not yet reproduce the whole split.** The public
   [`scripts/vol2_split_artefacts.py`](scripts/vol2_split_artefacts.py) has the comparison-artefact rules (the 68 rows) only. It does not include the follow-up step: the
   handling of the p. 497 row (its comments still call it "held for follow-up") and of the 7 follow-up rows, including the 5 set aside as rejected by the judges.
   The script that selected and judged the follow-up rows is not public yet. Cleaned-up versions of both will be published later.
6. **Vol III artefact review (2026-10-10).** The same kind of review, adapted to DP's text, was run on the 194 Vol III rows that both judges kept: 161 remain, on 111 DP pages, and 33 are set aside, each with a written reason (14 notation representation, 12 residue of DP's in-round markup that our comparison failed to clean, 4 in set-aside classes, 3 not reproduced by a re-run of the current comparison). Every row must now be one that the current comparison script gives as a hunk on which both readers agree and that is not in a set-aside class; this replaces the earlier pp. 1–249 selection with one rule. §8 item 2 stays open, and readers cannot yet re-run the rule themselves. The Vol III split script is not among the public scripts.

**Glyph-matching pilot (not used for any list).** To reduce the number of items that need a person, we are piloting a matcher that compares each disputed mark with PM's own printed glyphs, cut from the Vol I and Vol II scans. It has been tried on the first batch of review items only. It is not calibrated, and its results are not used for any count or list here; the human check is unchanged.

## 5. Effort settings (MEASURED, 2026-10-02)

**Codex, full-page transcription of the Vol I Introduction (88 pages), measured against the 53 Introduction reference rows (the candidate rows of the Introduction pass; see the README):**

| effort | reference rows re-found | differences per page | median reasoning tokens per page |
|---|---|---|---|
| unset (default) | 48 / 53 | 2.3 | 155 |
| low | 46 / 53 | 2.0 | 99 |
| medium | 46 / 53 | 2.3 | 705 |
| high | 43 / 53 (2 pages failed) | 2.3 | 1972 |

Caveat: the 53 were identified using the unset-effort reads, which favours that row. Conclusion: on this
reference set, higher effort did not improve recovery. The reference set is not independent of the unset
condition, and recovery is measured as a local context match rather than end-to-end detection, so this is
indicative, not conclusive. OpenAI's documentation gives `medium` as the default (DOCUMENTED). On this
benchmark, unset requests performed similarly to `low`/`medium`. That does not establish what the server actually
does with an unset effort.

**Opus, crop check on 83 blind-spot rows:** `medium` and `high` gave the same verdict on 79 of 83.
The 4 disagreements included 2 of the 4 scan picks that `high` had made, so confirmation stays at `high`.

Claude's default effort for Opus 5.5 is `medium` (DOCUMENTED, Anthropic). The judging calls set the effort
explicitly: the forced choice ([`fc_full.py`](scripts/fc_full.py), `high`) and the crop check
([`bs_check.py`](scripts/bs_check.py), `high` unless `EFFORT` is set). Other Claude calls did not, so they ran
at the default:
- the Opus page reader in [`read_page.sh`](scripts/read_page.sh) (Reader 2 on the Vol I Introduction only);
- the proposition-pass readers, re-reads and Sonnet forced choice (§2), which predate the effort setting;
- the errata formatter [`pg_errata_format.py`](scripts/pg_errata_format.py), which only proposes `old`/`new`
  pairs that deterministic checks then accept or reject (§5b).

## 5b. Reporting format

Every report to Project Gutenberg uses Gutenberg's own preferred errata format
([gutenberg.org/help/errata.html](https://www.gutenberg.org/help/errata.html)):

- Name the title, author and eBook number, and the file reported against (the HTML file under "more files").
- For each error, give one context line copied verbatim from that file, long enough to be unique, then `old ==> new`.
- State how the changes were checked, and against which scan. Do not paste whole paragraphs or before-and-after blocks.

PM's formulas live in the HTML as LaTeX in each image's `data-tex` attribute, so for a formula the context line and the
`old ==> new` pair are LaTeX copied from that attribute. The image file name is given as the locator.
[`scripts/pg_errata_format.py`](scripts/pg_errata_format.py) (with `pg_errata_items.py` and `pg_errata_render.py`) builds each entry. A model proposes the minimal `old`/`new` pair; it never decides acceptance. An entry is accepted only after deterministic checks:

- the context occurs in the Gutenberg file;
- `old` occurs exactly once in the context;
- the change does something;
- the context contains no run of spaces (email collapses them).

A context that occurs more than once in the file is lengthened verbatim, a whole LaTeX token at a time, within its own
`data-tex` value until it is unique. In the earlier draft, all 102 entries passed these checks, 4 of them after a hand fix where the formatter gave no
usable change. 10 contexts occurred more than once; 9 were lengthened to be unique, and the tenth belongs to a
held-back entry (draft entry 72, H18). Its context is not yet unique: inside its own `data-tex` it could only
be lengthened across a run of spaces, which the rule above forbids, so it needs a different context before it
can be sent. After the second review, one more `old`/`new` pair (report entry 48) was
widened by hand so that it starts at a whole LaTeX token instead of inside `\text{Cls}`. It still occurs
exactly once in its context.

Of those 102, **22 are held back** from the report until they are checked further
([`scripts/pg_errata_render.py`](scripts/pg_errata_render.py) applies the rule and lists the reasons):
- **20** change only marks in a set-aside class (§3: dots, E! for ∃!, breves and arrows, the inverted D) and
  have had neither a crop check nor a later pick of the print by both full-page judges. The other 13 entries in
  these classes do have that two-judge pick; the report names them and says that none has had a close-up check.
- **1** (✱25·56): the Sonnet judge answered "neither", and no later check picked the print.
- **1** (✱1·5, a missing ✱ in the label): no dedicated scan check.

The draft report now has 80 entries. Its introduction says, entry by entry, which checks each one had.
[`errata/vol1.md`](errata/vol1.md) lists all 102 entries: the 80 with the status "in draft report — awaiting
human check" and the 22 in full with "held back — awaiting human check" and the reason. Nothing has been sent.
All 102 are loaded on a private review page, where a person will check each entry against the scan; the human
check has started on a small first batch and is in progress. That check decides what is sent, and nothing is sent until it is done.

## 6. Control group: a regression benchmark

Luc Pommeret's Lean edition of PM ([l-pommeret/Principia-Mathematica](https://github.com/l-pommeret/Principia-Mathematica))
keeps an anomaly register of errors in the digital witnesses that were found independently. We use it as an
**external regression benchmark**, not as a recall estimate: the register is small and selected, and some of
its items helped guide the development of the pipeline (missed Introduction items are why the full-page pass
exists). That repository has no licence, so nothing from the register (entries, identifiers or our per-item
matching table) is reproduced here, and the scoring scripts that read it are not included. Only the
aggregate result is reported. As of 2026-10-02 (MEASURED):

- **Errors in the Gutenberg text, Vol I:** all 14 in-scope register items are matched **at the error level**: one of our rows records the same span with the same direction of change. 10 match automatically in a space-free character diff. 4 were judged by Claude reading both records, because the register writes the error differently from our records. 13 were caught by the full-page pass and 1 by the earlier proposition pass, which never covered the Introduction, where 13 of the register's Gutenberg items lie.
- One further register item turned out to be Gutenberg correctly applying one of PM's own published errata. Our own matching item was withdrawn.
- 20 register items concern Wikisource, not Gutenberg, and are out of scope.

Proof-structure findings (citations PM omits, gaps in reconstruction) are compared separately
against our ✱1–✱5 Lean formalization and are outside the scope of this text audit.

## 7. Limitations

- **No result of the human check is used yet; precision is not yet measured.** Everything here is awaiting human review. The two-judge filter removes most noise, but artefacts remain: a spot check of Vol I body candidates found bracket, subscript and shifted-line artefacts, and 68 of the 215 originally judged Vol II rows were classified as comparison artefacts (§4.5); on Vol III the same kind of review set aside 33 of 194 (§4.6). A blind human review of a stratified 120-item sample is loaded on a private review page (see the [README](README.md#human-review)). Separately, all 102 Vol I report entries are loaded on the same page, and a person will check each one against the scan before anything is reported. The human check has started on a small first batch and is in progress.
- **Coverage gaps.** In the Vol I body, 1,024 Reader-1 hunks on 109 pages had no second reading, and 5 pages were not compared (§2). The Vol I Introduction had Reader 2 on 44 of 88 pages, and no veto.
- **Follow-up of the 1,024 single-reading hunks (2026-10-08/09; candidates, awaiting human check).** The body triage ([`scripts/body_triage.py`](scripts/body_triage.py)) dropped 292 as formatting, set aside 654 in blind-spot classes and dropped 39 long alignment blocks. Both judges ran on the other 39, on 7 pages. 16 were kept: 7 are already in the draft report, 1 is page-marker placement, and 8 are new candidates, listed in [`errata/vol1.md`](errata/vol1.md) §5. These rows had one blind reading plus two judges, not two readings. A stratified two-judge sample of 40 of the 654 blind-spot rows kept 3: 2 page-marker rows misrouted into the blind-spot class, and 1 (✱72·61) already in the earlier lists. None was new; for 0 new in 38 real blind-spot rows, the one-sided 95% upper bound on the new-hit rate is 7.6% (unweighted, small stratified sample, so not a rate for the whole blind-spot class). The 8 new candidates and ✱4·42 are loaded on the private review page as additions to the report check, awaiting human check.
- **Blind-spot rows of kinds the reader writes (2026-10-10; candidates, awaiting human check).** Of the rows still set aside as blind-spot after the triage fix below, 76 are of kinds the reader does write (breves, arrows and overlines; inverted commas, ! and ↓; restriction signs on pages where the reader writes them) and were not in the 40-row sample. Both judges ran on them: 5 kept, 3 of them already in the earlier lists and 2 new candidates (✱41·34, p. 332; ✱92·1, p. 602), listed in [`errata/vol1.md`](errata/vol1.md) §5 as N9–N10. Claude looked at the scan crop of each; no result of the human check is used for them yet. Both are loaded on the private review page as report-check additions.
- **Triage fix (2026-10-09).** The inverted-D blind-spot test in `body_triage.py` did not require a non-empty reading, so it also set aside spans present only in Gutenberg. With the fix, 14 rows of the body pass move (10 to alignment blocks, 4 to the queue); 3 of them are among the 1,024 (now 651 blind-spot, 40 blocks, 41 queued). The 215 body rows and the 8 new candidates are unchanged. Of the 4 newly queued rows, 3 are page-marker placements and 1 (p. 340, ✱43·411, not among the 1,024) was judged by both models and rejected: both picked Gutenberg's text. Counting the 40-row sample and the 76 rows above, 155 of the 1,024 have had both judges and 869 have had no judge (292 formatting, 537 blind-spot, 40 alignment blocks). The public `body_triage.py` does not have this fix yet.
- **Proposition labels.** [`scripts/body_final.py`](scripts/body_final.py) labels each body row with the last proposition cited before it, which is not always the one the row belongs to. ✱4·42 was filed under ✱2·11 that way and relabelled by hand; re-running the public script brings back the ✱2·11 label. Other labels may be wrong too, so the counts of 163 propositions and of 50 rows on already-listed propositions are approximate.
- **The set-aside classes are real error classes too.** A dropped dot can change PM's meaning. They are excluded because the readers cannot be trusted on them, not because they don't matter. Crop checks were used for designated blind-spot rows (§4.3). Some report entries in these classes instead have later full-page checks by both model judges, without a crop check (§5b). Those full-page checks have the limitations described here, and the entries are awaiting human review.
- **Shared blind spots.** Except on the Vol I Introduction, both readers are the same model at different efforts. An error the model systematically misreads would be missed by both. A different model family as one reader would reduce this, and it is on the plan.
- **Judge independence.** Opus and Codex are different families, but both see the same full-page image at the same resolution. Fine marks may need the crop check regardless.
- **Edition.** Findings are against the first edition only. Where the second edition (1925–27) differs, that is out of scope.

## 8. External review and corrections

An external model review of the methodology (2026-10-02; the review itself is not included in this
repository) found the following, which are fixed:

- **Verdict parsing.** The crop-check parser matched `B` before `BOTH`. 18 tier-2 answers were re-parsed from the saved text, with no new model calls: tier 2 now has 47 scan picks, not 54, and 7 items that had been listed are held as uncertain.
- **Normalization.** LaTeX macro names were also replaced inside ordinary words (e.g. "capital" became "∩ital"). Macros are now replaced only where written as macros, or inside math segments for names of four letters or more. Vol II and Vol III comparisons were re-run, and only rows not already judged were sent to adjudication.
- **Reproducibility of the body counts.** `body_final.py` now contains the alignment and TeX-residue reclassification step that produced the published 215.

Two later public-draft reviews (2026-10-04) led to the Vol II artefact split (§4.5), the renderer fix (§3), and
corrections to this document and the Vol I report. A second round of two reviews (also 2026-10-04) led to:
the notation-representation class (§4.5); body coverage figures reconciled with the comparison record (§2);
S3 marked as probably superseded (§4.4); one report entry's `old`/`new` widened to whole LaTeX tokens (§5b);
and the full list of 102 Vol I entries with their status. The decision to list the held-back entries rather
than omit them was the author's. A third round of two reviews (also 2026-10-04) led to wording fixes only,
made after the human-review page was loaded with the Vol I report check and the Vol II top-up.

**Open items**, in priority order:

1. The human checks (loaded on the review page; started on a small first batch, in progress): all 102 Vol I report entries against the scan, plus 11 draft additions (the 10 new body follow-up candidates and ✱4·42), and the precision sample. 14 of the 32 Vol II items in the pipeline-kept stratum had been drawn from rows that the two artefact splits set aside (8 page-marker, 3 LaTeX fragments, 3 notation). They were withdrawn before any answer was recorded, kept in the record as withdrawn, and replaced by fresh draws from the 147 kept rows with seed 20261005, so the sample is still 120 items.
2. **Vol III review sample.** Applying the current `blind()` to the 139 judged Vol III rows (pp. 1–249) would set aside 45 of them, although all are stored as `agree`; the artefact review now applies one rule to every row (§4.6), and only 3 of those 45 had reached the 194. 9 of the 32 sampled Vol III pipeline-kept items are on rows now set aside; they have not been withdrawn from the review page yet.
3. **Published-errata matching can both miss and over-match.** One-character changes are never matched, and other matches use substring containment without a line or proposition anchor. This can miss "delete π" while accepting an unrelated short change on the same page, and a missing errata file silently disables the filter. The Vol II and Vol III errata-page rows were instead each classified by Claude against the erratum text (§4.4). Vol I still relies on the automatic matcher.
4. The Vol I body rows with no second reading (triaged and partly judged, §7; 869 have had no judge), and the 5 pages that were not compared (§2).
5. A lossless comparison record with every exclusion reason; recording both judges' answers and the A/B order on every row; reproducible paths and a dependency manifest.
