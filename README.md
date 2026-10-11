# Principia Mathematica text audit: errata tracker

> **Work in progress.** The first human check is complete (2026-10-11): one person checked every Vol I report
> entry, and a stratified sample of the pipeline's candidates, against the scan, blind (one sample answer was
> not; see below). Its results are below.
> Rows that were not in that check are model-pipeline output, awaiting human check. Nothing has been reported
> upstream yet.

This project checks the digital texts of Whitehead & Russell's *Principia Mathematica* (first edition,
1910–1913) against page images of the printed books. Project Gutenberg published Volume I (#78050) and
Volume II (#78255) in 2026, and Distributed Proofreaders (DP) is still preparing Volume III. They are careful
LaTeX transcriptions of a very hard typesetting job: dense dot-punctuated logic, arrows over letters, inverted
glyphs, hand-set subscripts. Small discrepancies can remain despite careful proofreading. This audit tries to
find them systematically. Each page is read blind by AI models and compared with the digital text, after
applying the normalization rules described in [METHODOLOGY.md](METHODOLOGY.md). Selected disagreements are
then judged against the print. What survives, once a person has checked it, goes back to the people who
maintain the texts. This repository tracks what has been found so far.

**Everything here is provisional and will change as the review continues.**

## Status at a glance

| | Blind scan reading | Model judging | Published-errata filter | Human review | Reported upstream | Public list here |
|---|---|---|---|---|---|---|
| **Vol I** (Gutenberg #78050), body and drafted report | 🟡 2nd reading missing on 110 of 536 pages (109 of them carry 1,024 hunks); 5 pages not compared | 🟡 215 body rows pass both judges; of the 1,024 single-reading hunks, 155 have been judged by both models (2026-10-08/10): 10 new candidates | 🟡 automatic matcher only; known gaps | ✅ all 102 report entries and 11 additions checked one by one (2026-10-11): 96 entries confirmed, 1 removed, 5 held; the 11 additions confirmed. Body rows: sample only, precision 93% (78–98%) | ⬜ not sent (revised draft: 96 entries) | ✅ all 102 report entries with their human-check status, the revised draft, and the 11 confirmed additions; other candidates counts only |
| **Vol I Introduction** (pp. 1–88) | 🟡 2nd reader (Opus) on 44 of 88 pages | 🟡 Opus only (53 rows), no veto | 🟡 automatic matcher only; known gaps | 🟡 in the Vol I sample (precision above); rows not checked one by one | ⬜ not reported | ⬜ count only |
| **Vol II** (Gutenberg #78255) | ✅ all 816 pages, both readings | ✅ both judges done, including the 7 follow-up rows judged on 2026-10-08 (2 kept, 5 set aside) | 🟡 17 rows classified by Claude; 3 apparently unapplied errata, awaiting confirmation | 🟡 sample checked: precision 94% (80–98%); rows not checked one by one | ⬜ not reported (156 candidates, 3 errata) | ✅ full list; rows outside the sample awaiting human check |
| **Vol III** (DP, in progress) | ✅ all 512 images, both readings | 🟡 194 spans pass both judges; after the artefact review, 161 kept on 111 DP pages and 33 set aside with reasons | 🟡 checked against the Errata to Vol III (pp. ix–x) by Claude, not by a person: none of the rows is an already-printed erratum | 🟡 sample checked: precision 91% (72–98%); rows not checked one by one | ⬜ not yet; will go to DP through their process | — counts only (DP text unpublished) |
| **Lean formalization (✱1–✱5, ✱9–✱10)** | — statements read from the 1910 scan | — proofs checked by Lean, not judged | — | ✅ ✱1·4 and ✱4·42 confirmed by the human check | ⬜ not sent: ✱1·4 (entry 1 of the revised Vol I draft) and ✱4·42 (already one of the 215 Vol I body rows; an addition, not yet merged) | 🟡 summary only; ✱4·42 in [errata/vol1.md §4](errata/vol1.md#4-found-by-the-lean-replay--confirmed-by-the-human-check); Lean repo not yet published |

✅ done · 🟡 partial / in progress · ⬜ not started · — not applicable

*Lean row:* the columns are the text-audit stages, so most do not apply. The results are reported by the
author: all 188 ✱2–✱5 propositions are proved from PM's primitive propositions, with no added axioms. The
replay also independently re-found one Vol I transcription candidate (✱4·42, p. 124). It is not new: it is
already one of the 215 body rows from the full-page pass, but it never reached the draft report. The human
check confirmed it (2026-10-11); it is not yet merged into the report. The Lean results become verifiable once
that repository is published ([details](#lean-formalization)).

## Status

Counts are pipeline outputs unless marked otherwise. A **candidate** is a row that passed the automated checks
described for its volume below. **The human check (2026-10-11) decided each Vol I report entry one by one. For
the other candidates it measured precision on a blind sample ([Human review](#human-review)); rows outside the
sample are still awaiting human check.** The pipeline stages overlap, so the counts within a volume are **not**
added together. Terms are defined in the [glossary](#glossary).

### Volume I: 1910 print, Gutenberg #78050

| | |
|---|---|
| Drafted report | **Human check complete (2026-10-11): 96 entries in the revised draft report, not yet sent.** The earlier draft had 102 entries: 80 in the draft report and 22 held back with weaker model support. One person checked each one against the scan, blind ([Human review](#human-review)). 96 were confirmed: 76 of the 80, and 20 of the 22 held-back entries, which were moved into the report. 1 was removed, because the print agrees with the ebook. 5 are held, because the reviewer could not confirm them. [errata/vol1.md](errata/vol1.md) lists every entry with its status and gives the revised draft in Gutenberg's preferred errata layout. The entries come from the proposition pass, proof replay and an extended scan check over ✱31–✱97. The 11 draft additions (✱4·42 and the 10 new candidates below) were checked the same way and all were confirmed; they are not yet merged into the report. Will McGinnis sends the report; it has not been sent. |
| Full-page pass, body (pp. 89–666) | **215** substantive candidate rows on 163 identified propositions (27 rows not attributed to a proposition). Each has two blind Codex readings that agree against Gutenberg; both judges (Opus, then the Codex veto) picked the print. 50 of the 215 are on propositions already in the earlier lists (independent re-discovery). Both counts rest on proposition labels assigned by `body_final.py`, which takes the last proposition cited before the row, not always the one the row belongs to: ✱4·42 was filed under ✱2·11 that way and corrected by hand, other labels may be wrong too, and re-running the public `body_final.py` brings back the ✱2·11 label. Also 74 dot-only and 39 number-dot rows (low priority). **Coverage gap:** Reader 1 differed from Gutenberg on 536 comparable pages. Reader 2 was attempted on 433 of them and succeeded on 426. That leaves 110 pages without a second reading. 109 of them carry 1,024 Reader-1 hunks, which have one reading only (see the follow-up below); the 110th has only a hunk matched to a published erratum. 5 further pages had no Gutenberg page marker to split on, so they were not compared at all. |
| Body follow-up, single-reading pages (2026-10-08/10) | **8 new candidates, confirmed by the human check (2026-10-11).** The 1,024 single-reading hunks on 109 pages went through the same triage as the body pass: 292 dropped as formatting, 654 set aside in blind-spot classes and 39 long alignment blocks dropped, so 985 were not queued. Both model judges ran on the other 39 (on 7 pages): 16 kept, 23 rejected. (A triage fix made later changes these counts to 651, 40 and 41. The 2 newly queued rows are page-marker placements, so the 8 candidates are unchanged; [METHODOLOGY §7](METHODOLOGY.md#7-limitations).) Of the 16, 7 are already in the draft report and 1 is page-marker placement, not a text error. The other **8 are new candidates**, listed in [errata/vol1.md §5](errata/vol1.md#5-new-candidates-from-the-body-follow-up-2026-10-0910--confirmed-by-the-human-check). 6 of them are "Cls ex² excl" in ✱84, where the ebook drops "ex". They had one blind reading plus two judges, which is weaker support than the 215 body rows. They were checked with the report entries and all confirmed; they are not yet merged into the report. ✱4·42 (below) is a body row, not one of these. A two-judge sample of 40 of the 654 blind-spot rows found nothing new ([METHODOLOGY §7](METHODOLOGY.md#7-limitations)). **2 more new candidates (2026-10-10), also confirmed by the human check.** Both judges then ran on the 76 other blind-spot rows of kinds the reader does write (breves, arrows and overlines; inverted commas, ! and ↓; restriction signs on pages where the reader writes them): 5 kept, 3 of them already in the earlier lists, and 2 new: ✱41·34 (p. 332) and ✱92·1 (p. 602), listed in §5 as N9–N10. In all, 155 of the 1,024 single-reading hunks have now had both judges and 869 have had no judge. |
| Full-page pass, Introduction (pp. 1–88) | **53** candidate rows. Checked less strictly than the body: Reader 1 (Codex) differed from Gutenberg and Opus picked the print in the forced choice. On 37 of them the second reader (Opus) agreed; on 16 there was no second reading. No Codex veto. |
| Further candidates | Proposition pass, tier 2: 47 rows where the crop check picked the print. Crop check of 83 blind-spot rows: 4 picks for the print (✱34·84, ✱35·01, ✱61·391, ✱80·41; the first and last are also held as uncertain). Awaiting human review: they were not in either part of the human check (outside the precision sample's population and outside the 102 report entries). The Lean replay independently re-found ✱4·42 (p. 124), where the ebook omits the citation `⊢ . ✱3·26 .` that the print has on *Dem.* line (2). This is not an additional candidate: it is already one of the 215 body rows above (it was first filed there under ✱2·11 by the labelling rule described above; the label was corrected by hand), so it is not counted again here. It never reached the draft report. It is listed in [errata/vol1.md §4](errata/vol1.md#4-found-by-the-lean-replay--confirmed-by-the-human-check); the human check confirmed it (2026-10-11). |
| Held as uncertain | Two separate sets, 11 rows in all, none of them in the drafted report. 7 tier-2 items, whose answers were re-read as BOTH after a parsing fix; these are not counted in the 47 above. And 4 crop-check rows whose verdict changes with the effort setting, on 3 propositions: ✱34·84, ✱80·41 (twice, pp. 505 and 510) and ✱90·31. |

### Volume II: 1912 print, Gutenberg #78255

| | |
|---|---|
| Candidates | **156 candidates, not checked one by one**: a blind sample of 32 of the 147 kept spans gave a precision of 94% (80–98%) ([Human review](#human-review)); the other rows are awaiting human check. 149 spans on 125 printed pages where both judges (Claude Opus and Codex) pick the print over Gutenberg's text, plus 7 further candidate discrepancies among the 17 judged rows on pages that carry a published erratum. Those 17 were classified one at a time against the erratum text by Claude, not by a person. One of the 7 (S3) lies inside a definition that an unapplied erratum replaces, so it is probably superseded. All 816 pages have both blind readings; the Opus forced choice ran on 997 rows. |
| Set aside | 73 judged rows. 68 classified as comparison artefacts, not text differences: 51 page-marker placements, 10 LaTeX fragments left by a rendering bug (now fixed), 1 small-capital typography, and 6 notation-representation rows (the same glyph written two ways; set aside after the second review). Listed in [errata/vol2.md](errata/vol2.md#4-set-aside-classified-as-comparison-artefacts-68-rows). And 5 follow-up rows that the judges did not both pick as the print ([errata/vol2.md §5](errata/vol2.md#5-set-aside-follow-up-rows-rejected-by-the-judges-5-rows)). |
| Published errata | **3 published errata that appear not to have been applied** (pp. 11, 71, 82). The transcriber's note says the published errata were applied; these three appear to have been missed. Two are in the "Additional errata" printed in Vol III, so they are easy to overlook. Awaiting human confirmation. |
| Follow-up | Re-comparing the 17 pages affected by the renderer fix found 6 reader-agreed hunks (on 6 of those pages), and a set-aside row on p. 497 hid Gutenberg's `*183-26`. Both judges ran on these 7 on 2026-10-08: 2 kept (pp. 191, 225; included in the 149 spans above), 5 set aside ([METHODOLOGY §4](METHODOLOGY.md#4-adjudication)). |
| Reporting | Not yet reported. See [errata/vol2.md](errata/vol2.md). |

### Volume III: 1913 print, Distributed Proofreaders project in progress

DP's Volume III text is unpublished work in progress, so this repository gives counts only. No DP text is
quoted or redistributed here.

| | |
|---|---|
| Candidates | All 512 images of the 1913 print have both blind readings. **161 candidates on 111 DP pages**, not checked one by one: a blind sample gave a precision of 91% (72–98%) on these rows ([Human review](#human-review)); the other rows are awaiting human check. They are what remains of 194 spans on 128 DP pages where Opus and Codex both pick the 1913 print over DP's text (table-of-contents leader dots excluded, because DP's guidelines omit them), after an artefact review like the one for Vol II ([METHODOLOGY §4](METHODOLOGY.md#4-adjudication)). Earlier sub-count, pages 1–249: the Opus forced choice ran on 139 rows and picked DP's reading on 79, the print on 50 and neither on 8 (plus 1 "both" and 1 malformed answer); the Codex veto kept 31 of the 50. |
| Set aside | 33 of the 194, each with a written reason: 14 notation representation (the same printed sign written two ways), 12 residue of DP's in-round markup that our comparison failed to clean, 4 in set-aside classes, and 3 that a re-run of the current comparison does not reproduce. They are classed as comparison artefacts or as rows in set-aside classes (marks the readers cannot be trusted on), and are not counted as candidates. |
| Published errata | The Errata to Vol III printed in the volume (pp. ix–x) were transcribed from the scan by Claude; no person has checked the transcript, which marks 3 readings as uncertain. They were then checked, again by Claude, not by a person: the 14 judged rows (10 distinct differences) on the 7 erratum pages that have judged rows were classified, one distinct difference at a time, and none of the rows is an already-printed erratum. |
| Sample items on set-aside rows | 9 of the 32 sampled Vol III pipeline-kept items turned out to be on rows the artefact review set aside. 6 of them were withdrawn before scoring (our conversion artefacts and DP placeholders, see [Human review](#human-review)); the other 3 were answered and scored, but are kept out of the Vol III estimate. |
| Reporting | Will be reported to DP through their process, while the formatting round is open, so corrections land before the book is posted. |

## Human review

**Complete (2026-10-11).** One person answered all 224 active items on a private review page. The check was
blind, with one exception (below): the reviewer was never told which version was the digital edition and
which the blind readers', and no machine pick or score was shown. Items were asked in one of two ways:

- **A/B question (95 answers).** The reviewer saw a crop of the page around the disputed line (the full page
  one click away), about 35 characters of context, and two versions of the span, A and B, in random order: one
  is the digital edition, the other the blind readers' version. The question was which version matches what is
  printed (A, B, both look the same, neither, or can't tell; a "garbled" answer was also possible). On 58 of
  these answers the crop also showed a box, placed by our glyph matcher, at the disputed spot.
- **Glyph picker (129 answers).** Where the two versions differ in a single character and the matcher could
  locate the spot, the reviewer saw the printed line with that spot boxed and tapped what is printed there,
  from 10 tiles of glyphs cut from PM's own pages ("none of these", "garbled" and "can't tell" were also
  possible). The matcher chose the tiles, but both versions' glyphs were always among them. The tiles were in a
  fixed grouped order (marks, digits, Latin, Greek, other symbols), never ranked; 6 sample answers were given on
  an earlier version of the page, whose tiles were shuffled by item id. The tap was mapped to A, B or neither
  afterwards ([METHODOLOGY §4](METHODOLOGY.md#4-adjudication)).

**An item-level note on 3 items.** Late in the check, a "[sic]" heads-up was added to 3 items (2 report-check
items and 1 sample item; two on p. 117, one on p. 110). It said that one of the two versions has odd-looking
characters that really are in its source text, checked by hand, without saying which version. It is not a
machine pick. It was added 13 minutes after the reviewer, answering the p. 110 item, noted that its
options looked like a LaTeX bug. Two of the three items had already been answered when the note was
added, so the reviewer can have seen it on at most one answer.

**One scored answer is not blind.** On one sample item (✱50·72, p. 355) the reviewer's blind answer was
"neither". In a discussion afterwards, which was not blind, Claude suggested comparing the mark with ✱50·74 and
re-answering if it is a single bar, which is the proposed correction (so the suggestion pointed toward the
proposed reading), and said, wrongly (later retracted), that the Michigan copy independently showed the same
mark; it is the same scan ([METHODOLOGY §7](METHODOLOGY.md#7-limitations)). 44 minutes after the blind answer,
the reviewer described the mark as a misprint (all they could make out was a dot, like a ghost image), and
Claude entered "garbled" at the reviewer's request. That answer replaced the blind one and is the one scored.
"Neither" and "garbled" both count against precision, so the figures below are the same either way.

Detailed results are in the private source repository; this page gives the summary and, apart from
✱50·72 above, no per-item answers. The outcome of each Vol I report-check entry is in
[errata/vol1.md](errata/vol1.md). The page had two checks:

1. **Vol I report check (113 items; 64 answered with the picker, 49 with A/B):** all 102 entries of the earlier
   Vol I draft and 11 draft additions, each checked one by one. 96 entries were confirmed, 1 removed and 5 held;
   the 11 additions were all confirmed ([Volume I](#volume-i-1910-print-gutenberg-78050), [errata/vol1.md](errata/vol1.md)).
2. **Precision sample (111 items; 65 picker, 46 A/B):** a stratified sample of the pipeline's candidates and of
   rows the first judge rejected, which measures how many candidates a person agrees with.

**Withdrawn items.** 23 loaded items were withdrawn before scoring, each with a written reason:

- **14** Vol II items had been drawn from rows that the two artefact splits later set aside (7 page-marker
  placements, 4 LaTeX fragments, 3 notation representation). They were withdrawn before any answer was recorded
  and replaced by fresh draws from the 147 kept rows (seed 20261005).
- **6** were false items created by **our own text conversion**: LaTeX command names left as letters (for
  example "infty" where the source has ∞), so the two versions differed only because of our conversion, not
  in the source. The reviewer found them. A guard (`latex_leak.py`, with a regression test, in the private
  review tooling) now refuses to load such items.
- **2** were DP's own bracketed placeholders (for example [Del] for ∇). That is DP's convention for a sign that
  is converted later, not an error.
- **1** was DP's placeholder for ∂ written without brackets inside a subscript; the print's ∂ is encoded, so
  there is no print difference.

The 9 items withdrawn on 2026-10-11 were not replaced, and answers already given to 6 of them are not used.

### Results

**Precision** is the share of scored pipeline-kept items where the reviewer picked the print reading the
pipeline proposed. "Neither" and "garbled" count against it; "both look the same" and "can't tell" are left
out (none occurred in this stratum). Each volume is reweighted across kinds of difference to the population it
covers, because the sample over-represents rare kinds. The 95% interval is Wilson's at the effective (Kish)
sample size. **This interval method was chosen when the answers were scored, not before.** The earlier version
of this page promised to state the method, with its code, before any answers were scored; that did not happen.
It first appears in the private commit that scored the answers (2026-10-11), after the answers were in. The
**expected real differences** (expected to be real differences from the print, in our one scan) are the rows
the pipeline reports times precision, only for the population the sample covers; the raw candidate counts above
are unchanged.

| Volume | Population the sample covers | Items scored | Precision | 95% interval | Expected real differences |
|---|---|---|---|---|---|
| Vol I | the 215 body rows and 53 Introduction rows (268); not the report entries, which were checked one by one | 31 | **93%** | 78–98% | about 249 of 268 (209–263) |
| Vol II | the 147 spans kept after both artefact splits; not the 2 follow-up spans kept on 2026-10-08 (after the draw) or the 7 errata-page items | 32 | **94%** | 80–98% | about 138 of 147 (117–144) |
| Vol III | the 161 rows kept by the artefact review; 2 of them, of a kind with no scored item, are not covered | 23 | **91%** | 72–98% | about 145 of 159 (115–155) |
| All three | 574 rows | 86 | **93%** | 85–97% | |

**Judges' miss rate (rejected stratum).** In the rows where the first judge (Opus) picked the digital text,
which are not candidates (235, 281 and 595 rows in Vols I, II and III), the reviewer sided with the print on
1 of 6, 1 of 7 and 1 of 7 scored items. Pooled, weighted by pool size: **15% (5–38%)**. This is a miss rate
for that stratum only, from 20 scored items, not an overall recall estimate. The three rows are not added to
any list here yet.

**What the check does not cover.**

- One reviewer, and one scan per volume. The University of Michigan copy we tried as a second witness is the
  same scan as our page images, so where a mark is faint or broken, whether it is in the print or only in the
  scan is open ([METHODOLOGY §7](METHODOLOGY.md#7-limitations)).
- The check measures the precision of the **differences** the pipeline reported. It does not look for errors
  that the digital text and our readings share, and our readings agreeing with Gutenberg may not be
  independent evidence: Gutenberg's credits say its text was produced from HathiTrust images, and which
  HathiTrust scan is not yet known ([METHODOLOGY §7](METHODOLOGY.md#7-limitations)).
- Rows outside the sample, and the candidates outside the sample's populations (for example the Vol I tier-2
  rows), are still awaiting human check.

### Sample design

- **Sample:** 120 items, 40 per volume, **stratified**. Each volume contributed 32 items from the
  **pipeline-kept** stratum (both judges picked the print; for the Vol I Introduction rows, Opus only, no veto;
  called "reported" in the data files, although nothing has been reported upstream) and 8 from the **rejected**
  stratum (Opus picked the digital text). Within the pipeline-kept stratum, items were allocated by kind of
  difference (insertion or omission, look-alike characters, ✱ for the centred dot, dots, other) in proportion to
  the population, with at least 3 per kind (all rows if fewer), so rare kinds are over-sampled. The draw used a
  fixed seed (20261004); the Vol II top-up used seed 20261005. Redrawing it also needs the sampling frame (the
  candidate lists in file order), the kind rule and the allocation code. These are in the private source
  repository and will be published, except for Vol III rows, which contain DP text.
- **Vol III frame:** the sample was drawn from the 194 spans that passed both judges. After the artefact review,
  the estimate covers the 161 kept rows: of the 32 pipeline-kept items, 6 were withdrawn and 3 are on set-aside
  rows and scored outside the estimate, which leaves 23.
- **Top-up:** the plan allowed 32 more items for a volume with a borderline result. The earlier version of this
  page promised to define "borderline", with the interval method, before any answers were scored; it was never
  defined. No top-up items were drawn.

## How it works

The full-page pipeline aims to transcribe each printed page **blind** twice, without the existing digital text.
Coverage is complete for Vols II–III and partial for Vol I (see the status tables above). For most of the audit the
two readers are the same Codex model at two effort settings; the Vol I Introduction used Claude Opus as the
second reader. A comparator lines their readings up against the digital text after applying the normalization
rules described in [METHODOLOGY.md](METHODOLOGY.md) (LaTeX mapped to Unicode, whitespace removed, and some
notation differences set aside). Those rules have known gaps. Where both blind readers agree with each other
and disagree with the digital text, Claude Opus is shown the page image and the two competing readings in
random order. It answers in one line which one matches the print (the **forced choice**). A second judge,
Codex, then answers the same question independently and can **veto** the row. Known systematic blind spots
(PM's dots, the inverted D, arrows over letters, capital vs. small subscripts) are **set aside** rather than
guessed at. Coverage gaps, also described there, leave some disagreements unjudged. As an external
**regression benchmark**, all 14 in-scope Gutenberg items in Luc Pommeret's independently compiled anomaly
register for Vol I are matched at the error level. The register is too small, and too involved in the
pipeline's development, to give a recall estimate. Details and limitations: [METHODOLOGY.md](METHODOLOGY.md).

## Glossary

- **Scan image / printed page / DP page.** A *scan image* is one page image of the printed book (a DjVu page for
  Vols I–II, an image in the UMich sequence for Vol III). A *printed page* is the page number printed in the book.
  A *DP page* is one page file of Distributed Proofreaders' Vol III project. The offsets between them are in
  [METHODOLOGY §1](METHODOLOGY.md#1-sources).
- **Blind reading.** A model transcribes a page image without being shown the digital text.
- **Proposition pass.** The first Vol I check: blind readings of each page compared with Gutenberg one
  proposition (formula) at a time. The Vol I report comes from it ([METHODOLOGY §2](METHODOLOGY.md#2-blind-reading)).
- **Full-page pass.** The later check of every page in full (prose, formulas, footnotes): two blind readings of
  the whole page, compared with the digital text of that page.
- **Hunk / span / row.** The comparison yields *hunks*: places where a reading and the digital text differ. A
  *span* is the disputed text of one hunk. A *row* is one hunk as it moves through the pipeline (one line in a
  data file or table). Several rows can fall in one proposition, and one proposition can carry several rows.
- **Set-aside class.** A kind of difference that the readers get wrong so often that it is not judged at all
  (e.g. PM's dots, the inverted D, arrows over letters). Set aside does not mean unimportant
  ([METHODOLOGY §3](METHODOLOGY.md#3-comparison)).
- **Forced choice.** The judging step: a model is shown the page image and two unlabelled versions of one span
  (A and B, in random order; one is the digital text, the other the blind reading) and must say which one is
  printed: A, B, BOTH or NEITHER.
- **Veto.** A second, independent forced choice by a model from a different family (Codex). A row is kept only
  if both judges pick the print; the veto can only remove rows, never add them.
- **Crop check.** For selected rows (197 in the Vol I proposition pass: 114 tier-2 and 83 blind-spot rows): the line is cut out of the full-resolution scan, enlarged, and
  judged mark by mark by Opus.
- **Tier 2.** In the Vol I proposition pass, rows with weaker support than tier 1: three of four readings agreed
  against Gutenberg, or the row was unresolved and re-run. They were decided by the crop check.
- **Candidate.** A row that passed the pipeline's automatic checks. Not confirmed by a person unless its status
  says so.
- **Awaiting human review / awaiting human check.** No person has checked this row against the scan. After the
  2026-10-11 check, this applies to every row except the Vol I report entries, the 11 Vol I additions and the
  sampled items; for the sampled populations a measured precision is given instead.
- **Deep embedding** (Lean section). PM's formulas are represented as a data type inside Lean, and PM's own
  primitive propositions are the only rules of proof. Lean's logic is not used to prove PM's theorems directly.

## Lean formalization

A companion project formalizes the propositional part of PM (✱1–✱5), and ✱9–✱10, in Lean 4, with statements
read from the 1910 printed scan. It is a **deep embedding**: PM's formulas are a data type inside Lean, and a formula counts
as a theorem only if it can be derived from PM's primitive propositions ✱1·1–✱1·6 (the definitions ✱1·01,
✱3·01 and ✱4·01 are abbreviations). These results are reported by the author. The Lean repository is not yet
public, so they cannot yet be checked independently.

- All 188 ✱2–✱5 propositions are proved. Lean's `#print axioms` reports "does not depend on any axioms" for
  every PM theorem (✱2–✱5 and ✱9–✱10). That means the proofs use none of Lean's own axioms, such as choice. PM's primitive
  propositions are not Lean axioms but the rules of the embedded proof system. There is no `sorry`, no
  `native_decide` and no added axiom.
- 103 of them are replayed as explicit proof terms built from PM's own cited propositions: 72 use only the
  propositions PM cites, and 31 also need at least one proposition PM does not cite (each one listed in the
  ledger). The other 85 used derived rules. 74 of the 85 have been rewritten to follow PM's own proof: one Lean line per *Dem.*
  line, or, where PM prints only a bracketed hint, one per hinted proposition in PM's order. The only steps
  done silently are ones PM itself leaves tacit (such as Syll, ✱3·03, using ≡ as ⊃, and chains of ≡).
  - 40 use only the propositions PM cites. Many of them (37) also use tacit steps, and 28 of the 40 follow
    only a bracketed hint, because PM prints no *Dem.* lines for them.
  - 34 also need a proposition PM does not cite. The kinds include: joining two halves into a
    product or an equivalence (Comp, ✱3·43); supplying the trivial half `p ⊃ p` of such a join or of a
    replacement (Id, ✱2·08); removing a double negation inside a larger formula (✱4·11); swapping the
    halves of an equivalence or taking an implication out of it (✱3·22, ✱3·26, ✱3·27); moving brackets or
    permuting a sum (✱2·31, ✱2·32, Perm); commuting a product (✱4·3); turning `∼p ⊃ q` into `p ∨ q`
    (✱2·54); and replacing one factor of a product (✱3·47).
  - 11 are unchanged: the transcription has neither *Dem.* lines nor a bracketed hint for them, so there is
    no PM proof to follow, and the earlier derived-rule proof is kept.
- Three anomalies in PM's *Dem.* lines turned up by the rewrite were checked against the 1910 print:
  - ✱4·32 (p. 123): line (1) cites ✱4·12 for a step that is in fact ✱2·03 taken both ways. This appears to
    be a slip in the 1910 print (the ebook follows the print); awaiting human check.
  - ✱4·43 (p. 125): ✱2·65 (∼p/p) yields `∼(∼p)`, but the line prints `p`. PM drops the double negation
    without citing ✱2·14; the ebook follows the print. Awaiting human check.
  - ✱4·42 (p. 124): the print cites `⊢ . ✱3·26 .` on line (2); the ebook omits it. The human check confirmed
    this transcription error (2026-10-11). It is an independent re-discovery: the full-page pass had
    already found it, and it is one of the 215 Vol I body rows, but it never reached the draft report. It is
    listed in [errata/vol1.md §4](errata/vol1.md#4-found-by-the-lean-replay--confirmed-by-the-human-check).

  No published erratum touches pp. 123–125. The 1925 second edition has not been checked.
- A Kalmár-style completeness theorem (every tautology is a theorem), also without axioms. No replay depends on it.
- **✱9–✱10 (2026-10-11).** These follow ✱10's "alternative method" (PM pp. 143–144): ∼, ∨ and (x) are
  primitive, ✱1's primitive propositions hold for all formulas, and ✱10·1, ✱10·11 and ✱10·12 are added as
  primitive, as PM says this method requires. 60 numbered items are stated and proved: 10 from ✱9 (✱9·1,
  ✱9·11, ✱9·12, ✱9·13 and ✱9·2–✱9·25) and 50 from ✱10, which is every numbered ✱10 item from ✱10·1 to ✱10·57
  except ✱10·121, ✱10·122 and ✱10·221, PM's rules about significance, which are built into the syntax. 7 of the
  60 only restate a primitive rule of the embedding (their proof is the rule itself): ✱10·1, ✱10·11 and
  ✱10·12, and ✱9·2, ✱9·12 (detachment), ✱9·13 and ✱9·25, which are the same rules under their ✱9 numbers. The
  other 53 are derived. In the table [below](#how-far-each-formalization-got) only PM's assertions count, so
  ✱9 reads 6/4 against PM's 28 assertions in ✱9: we state 6 of them (✱9·2–✱9·25; ✱9·3 onward are not stated),
  and ✱9·2 and ✱9·25 are not counted as proved because here they are primitive (✱9·1–✱9·13 are primitive
  propositions in PM's ✱9, not assertions). ✱10
  reads 48/46: all 48 assertions are stated, and ✱10·1 and ✱10·12 are primitive (✱10·11 and ✱10·13 are rules,
  not assertions). `#print axioms` reports "does not depend on any
  axioms" for all 460 declarations in the project's axiom check (the 188 ✱2–✱5 theorems, the completeness
  theorem, and the ✱9–✱10 theorems and models). A soundness theorem shows that every ✱9–✱10 theorem is true
  in every model. There is no adequacy theorem yet: the syntax also admits terms that correspond to no finite
  PM formula. PM's ramified hierarchy (✱12 on) is not formalized. Two findings, reported by the author:
  - Six ✱10 proofs (✱10·25, ✱10·251, ✱10·33, ✱10·34, ✱10·36, ✱10·37) use a real variable, so they assume
    that an individual exists; without one they fail in the empty model. A counter-model in the empty model is
    machine-checked for ✱10·25 only; for the other five this was checked by hand.
  - ✱10·27 (p. 150): the print cites ✱10·1 for the step that turns y into an apparent variable, which is
    ✱10·11. This is possibly a citation slip in PM; it has not been checked against the 1925 edition.
- 13 declarations use Lean's standard axioms `propext` and `Quot.sound`, never choice: three metatheorems about
  the embedding (among them the ✱1–✱5 soundness theorem), some compiler-generated lemmas, and a `Repr`
  instance (for printing formulas). None of them is a PM derivation.
- The author reports that Gutenberg #78050's transcription of ✱1·4 (`p ∨ q . ⊃ . p ∨ p`) is not derivable in
  the embedded proof system. This rests on a checked countervaluation, not on a failed proof attempt: the
  formula is false when p is false and q is true, and a machine-checked soundness theorem shows that every
  theorem of the system is true under every valuation. The 1910 print has `q ∨ p` (entry 1 in
  [errata/vol1.md](errata/vol1.md), confirmed by the human check).

## How this was made

This is a human-directed project carried out with heavy AI assistance, and it says so plainly.
Will McGinnis set the goals, made the judgement calls, and reviews what goes out. The
transcription, comparison, adjudication and most of the code were done by AI models working
under that direction:

- **Claude (Anthropic)**, Opus 5.5: orchestration, code, the forced-choice image checks, the readings of the
  earlier Vol I proposition pass, and these documents. Claude Sonnet 5.5 was a judge in that earlier pass.
- **OpenAI Codex**: the blind page readings and the independent veto judge.

The methodology was also checked by an external model review. Model output is treated as evidence, not as truth.

## Related work and credits

This audit stands on other people's work, and several of them found things first.

- **Project Gutenberg** and the **Distributed Proofreaders** volunteers, whose transcriptions are the object of study. Every error report here is offered as a contribution to their work, not a criticism of it.
- **Luc Pommeret**, [*Principia-Mathematica*](https://github.com/l-pommeret/Principia-Mathematica): a source-critical Lean 4 edition of PM. Its anomaly register (read at upstream commit `3fb187a`, 2026-08-24) is our regression benchmark. The repository has no licence, so nothing from it (code, text or register entries) is included here; we report only our aggregate result, and the facts and numbers in the table below.
- **Landon D. C. Elkind**: the [PM-MATS](https://github.com/LogicalAtomist/PM-MATS) project and the [*principia-rewrite*](https://github.com/LogicalAtomist/principia-rewrite) Coq formalization of ✱1–✱5 (GPL-3.0; used as an external oracle, not copied).
- **Travis / Impression Editions**, [Gerrata](https://github.com/Impression-Editions/Gerrata): semi-automated errata detection for Project Gutenberg prose, comparing Gutenberg texts with Internet Archive scans. It is independent prior art for the same idea. Our reports adopt the same Gutenberg-preferred "old ==> new" layout it emits. Gerrata does not handle mathematical notation, where most candidates found by this audit lie, and no code from it is used here.
- **Metamath** [set.mm](https://github.com/metamath/set.mm) `pm*` theorems (CC0): a statement oracle for ✱1–✱5.
- [Neo-Principia](https://github.com/MudroadWhite/Neo-Principia) (Rocq), [PrincipiaMathematica_Agda](https://github.com/yangg1g/PrincipiaMathematica_Agda), [ndrwnaguib/principia](https://github.com/ndrwnaguib/principia) (Lean) and [xamidi/luk-pmproofs](https://github.com/xamidi/luk-pmproofs).
- Page images: Wikimedia Commons (Vols I–II, 1910/1912) and the University of Michigan Historical Mathematics Collection via HathiTrust (Vol III, 1913).

### How far each formalization got

Measured by us on 2026-10-11 from each project's own files. Only facts and numbers are given here; no code or
text from the projects is included.

**How to read it.** The unit is one of PM's own numbered propositions (✱N·M). Only *assertions* count: numbered
items that PM prints with the assertion sign ⊢ and that are neither a definition (Df), a primitive proposition
(Pp), nor a rule stated in words. Each cell reads **S / P / F**:

- **S**: the number of PM assertions in that range for which the project states a formal statement labelled
  with that PM number. Several declarations for one number count once.
- **P**: of those, the number with a complete proof. That means no `sorry`, `Admitted`, `postulate` or `axiom`
  stands in for the proof, and the proof does not depend on another unproved PM item. An assertion that a
  project takes as an axiom is not counted in P.
- **F**: of those proved, the number where the project itself records, *for that proposition*, that the proof
  follows PM's own proof. The record can be a ledger entry or a per-declaration tag. It need not say whether the
  proof also uses propositions PM does not cite, so F means the same for every project, ours included. **ns**
  means "not stated" per proposition. Project-wide claims, and PM's Dem. quoted beside a proof, do not count.

The denominator row gives how many assertions PM prints in each range (counted from the Gutenberg text with a
few corrections; for ✱20–✱97 our counts agree with the PM-MATS citation graph's to within about 2%, which is
agreement between two counts, not a measured error bound). Read every cell against it, and against the
**Emb.** and **Check** columns. In a *deep* embedding, P means the statement was derived from the project's
primitive rules. In a *shallow* one, P means the statement holds in the host logic (for example classical Coq
or Lean), which says nothing about PM's deductive system. **Check** says how P was established: `build` means
we compiled the project; `static` means P comes from reading and searching the source, with nothing compiled;
`D-recheck` means we re-ran the condensed-detachment proofs with our own checker. **Fits within PM**:

- **yes**: the embedding is deep; its formulas are built from PM's own primitive ideas (∼ and ∨, and (x) from
  ✱9 on); every rule of its proof system is one of PM's own primitive propositions for the method it follows
  (✱1·1–✱1·6 with ✱1·11; for ✱9–✱10 those of ✱9 or those of ✱10's alternative method; from ✱12 on also ✱12·1
  and ✱12·11), and we have checked this against the source; and no proof counted in P takes an extra
  assumption.
- **partly**: deep, and the rules are PM's ✱1 primitive propositions, but the formulas are built from other
  primitive signs.
- **not verified**: deep, but we have not checked that the rules are exactly PM's primitive propositions.
- **no**: shallow, or the rules are another axiom system.

| Project | Prim. | Emb. | Check | Fits within PM | ✱2–✱5 | ✱9 | ✱10 | ✱11–✱14 | ✱20–✱56 | ✱60–✱97 |
|---|---|---|---|---|---|---|---|---|---|---|
| **PM assertions (denominator)** | | | | | **188** | **28** | **48** | **123** | **1366** | **1477** |
| ours (Lean 4; repository not yet public) | PM ✱1·1–✱1·6; ✱10 alt. method | deep | build | yes (✱1–✱5, ✱9–✱10)⁶ | 188/188/177¹ | 6/4/ns | 48/46/ns | – | – | – |
| [l-pommeret](https://github.com/l-pommeret/Principia-Mathematica) (Lean 4) | PM ✱1·1–✱1·6, ✱1·11; ramified system | deep (shallow from ✱70) | build⁴ | yes for ✱1–✱5; not verified for its ramified ranges; no for its shallow ones⁵ | 188/188/171 | 28/26/21 | 35/34/34 | 71/68/66 | 183/128/88 | 160/151/98 (6 deep) |
| [Neo-Principia](https://github.com/MudroadWhite/Neo-Principia) (Rocq) | host logic (classical Coq); ✱9+ Pps admitted | shallow | static | no | 186/186/ns² | 28/28‡/ns | 48/47‡/ns | 123/66‡/ns | 51/1‡/ns | – |
| [PrincipiaMathematica_Agda](https://github.com/yangg1g/PrincipiaMathematica_Agda) (Agda) | Sheffer stroke; PM ✱1·1–✱1·6 | deep | static | partly (its primitive connective is the Sheffer stroke) | 188/188/ns | 28/0/ns | – | – | – | – |
| [principia-rewrite](https://github.com/LogicalAtomist/principia-rewrite) (Coq, PL.v) | host logic (classical Coq) | shallow | static | no | 188/188/ns | – | – | – | – | – |
| [luk-pmproofs](https://github.com/xamidi/luk-pmproofs) | Łukasiewicz's 3 axioms + condensed detachment | CD text | D-recheck | no | 188/188/ns | – | – | – | – | – |
| [Metamath pmproofs.txt](https://us.metamath.org/mmsolitaire/pmproofs.txt) | ax-1–ax-3 + condensed detachment | CD text | D-recheck | no | 188/188/ns | – | – | – | – | – |
| [Metamath set.mm](https://github.com/metamath/set.mm) (pm\* theorems) | ax-1–ax-3 + ax-mp | – | – | no | not measured³ | | | | | |
| [ndrwnaguib/principia](https://github.com/ndrwnaguib/principia) (Lean 4) | host logic (Lean + Mathlib) | shallow | static | no | 47/47/ns | – | – | – | – | – |
| [Lacrimae-Angeli](https://github.com/MudroadWhite/Lacrimae-Angeli) (Rocq) | none yet | sketch | static | – | – | – | – | – | – | – |
| [PM-MATS](https://github.com/LogicalAtomist/PM-MATS) | not a formalization (a citation graph) | – | – | – | – | – | – | – | – | – |

"–" means nothing in that range. CD text: a text file of condensed-detachment proofs.

‡ The proof is complete relative to the project's admitted primitive propositions, but by our reading of the
source (not compiled) those admitted primitives are jointly inconsistent: its admitted stand-in for ✱9·13 yields
`∀ x : Prop, x`, so that stand-in alone is inconsistent. Treat these as unproved.

¹ ✱2–✱5 F = 177 proofs that our ledgers record as following PM's proof: 112 use only the propositions PM cites,
and 65 also need at least one proposition PM does not cite (listed per proof in our ledgers). The other 11 have no
PM proof to follow (the transcription has no Dem. or hint for them). 112 + 65 + 11 = 188.

² The two missing assertions, ✱4·8 and ✱4·81, are probably present under names that lack the chapter number;
they are not counted.

³ set.mm was not measured.

⁴ Built by us on 2026-10-11 (Lean v4.30.0, upstream commit `3fb187a`, 319 jobs, no errors). P was mapped
statically from names and proof status; the build confirms they compile. F comes from the project's own
per-declaration tags, which we did not verify. The project also states 404 assertions from Vols II–III, 375
of them with proofs, all in its shallow part (no denominator here).

⁵ For ✱1–✱5 its rules are ✱1·1, ✱1·11 and ✱1·2–✱1·6. Its ramified system has 20 rules, each labelled with a PM
number, among them ✱12·1 and ✱12·11 (the axiom of reducibility); we have not checked them against PM's own list
of primitive propositions. 59 PM numbers have deep proofs that take an extra hypothesis that is never discharged,
such as an assumption about carrying reducibility across scopes; those are counted as not proved, unless the
same number has another, unconditional proof.

⁶ Our ✱10 formula type also contains terms that correspond to no finite PM formula; there is no adequacy theorem
yet (see the [Lean section](#lean-formalization)).

**l-pommeret is the furthest deep formalization in the table:** a deep ramified system whose rules include
✱12·1 and ✱12·11, with deep proofs into ✱11–✱56. We built it ourselves. Like ours, it records per proposition
whether a proof follows PM's. What our ledgers add, and what we have not found in the other projects' files, is
a list, for each of the 188 ✱2–✱5 proofs, of the propositions it needs that PM does not cite (l-pommeret's status
document reports how many of its proofs reach a proposition by a route PM does not print). Our Lean repository
is not yet public, so its row cannot yet be checked independently.

## Repository layout

```
README.md         this file: the tracker
METHODOLOGY.md    the pipeline, its parameters, the control group, and the limitations
errata/vol1.md    Vol I: all 102 drafted entries with their human-check status, the revised draft report (96 entries), the 6 not in it, and the 11 confirmed additions (1 body row re-found by the Lean replay, 10 new candidates); not sent
errata/vol2.md    Vol II: unapplied published errata, the 156 candidates, and the 73 set-aside rows; sample-checked, rows awaiting human check
scripts/          the code for the Vol I and Vol II pipeline (see scripts/README.md for what is missing)
```

## How to cite

> Will McGinnis, *Principia Mathematica text audit: errata tracker*, first public draft, 2026-10-04.
> https://github.com/willmcginnis/principia-mathematica-text-audit

Because everything here will change, please cite a specific commit.

## License

Code is under the [MIT License](LICENSE). Our own documentation and data are released into the public domain
under [CC0 1.0](LICENSE-DOCS). The Gutenberg text quoted in the errata lists is from public-domain ebooks.
*Principia Mathematica* itself (1910–1913) is in the public domain in the United States.

## Changelog

- 2026-10-04: first public draft.
- 2026-10-04: fix pass after two reviews. Vol II: 62 comparison artefacts set aside (222 → 160 candidates),
  rendering bug fixed. Vol I report: intro rewritten to describe the checks as they happened, 22 entries held back (102 → 80), contexts made unique.
  Methodology: Introduction reader, coverage gaps, effort settings, errata sources, sample design and open
  items corrected; glossary added.
- 2026-10-04: "Status at a glance" matrix and work-in-progress banner added. The Vol I body coverage gap and
  the 6 unjudged Vol II hunks are now stated in the status tables.
- 2026-10-04: second fix pass after two more reviews.
  - Vol I: all 102 draft entries are now listed, each with its status. The 22 held-back entries are shown in
    full rather than hidden. Every entry is checked against the scan by a person before anything is sent.
  - Vol II: 6 notation-representation rows set aside (160 → 154 candidates; 147 spans on 123 pages). S3 is
    marked as probably superseded by the p. 71 erratum.
  - Vol I body coverage figures reconciled with the data. Vol III count flagged as expected to fall.
  - Human-review section: per-volume strata spelled out, Vol II top-up (seed 20261005) described, interval
    method and the rejected-stratum measure stated more carefully.
  - Lean claim attributed to the author, with its basis. Model identifiers replaced by product names.
  - Everything not yet checked by a person is now marked "awaiting human review".
- 2026-10-04: wording fixes after a third round of two reviews. The 102-entry Vol I report check and the
  Vol II top-up (14 items withdrawn and replaced, seed 20261005) are now loaded on the review page; no answers
  are recorded yet. Effort-unset claim, coverage wording, the Vol III errata filter status and H18's context
  stated more carefully. The `ᗡ"`/`Rl` rows in Vol II are grouped under one note.
- 2026-10-08: Lean section updated. 74 of the 85 proofs that used derived rules were rewritten to follow
  PM's own proofs (40 using only the propositions PM cites, 34 also needing one PM does not cite); 11 are
  unchanged. Three anomalies were checked against the 1910 print, awaiting human check: ✱4·32 appears to be
  a slip in the 1910 print (the ebook follows the print); at ✱4·43 PM drops a double negation without citing
  ✱2·14, and the ebook follows the print; ✱4·42 appears to be an ebook transcription error. ✱4·42 is not a
  new candidate: it is already one of the 215 Vol I body rows, re-found independently by the Lean replay. It
  is listed in errata/vol1.md §4, awaiting human check, and is not counted again. Its body-row label was
  corrected by hand from ✱2·11 to ✱4·42, so the body rows now fall on 163 identified propositions (was 162).
  Vol II: the 7 follow-up rows (6 hunks exposed by the renderer fix and the p. 497 `*183-26`) were judged
  by both models; 2 kept (pp. 191, 225), 5 set aside, so 156 candidates (149 spans on 125 pages + 7
  errata-page items) and 73 set-aside rows.
- 2026-10-09: Vol I body follow-up: the 1,024 single-reading hunks on 109 pages were triaged, and both judges
  ran on the 39 queued rows. 16 were kept: 7 already in the draft report, 1 page-marker placement and 8 new
  candidates, awaiting human check (errata/vol1.md §5); they and ✱4·42 are loaded on the review page as 9
  additions to the report check, with no answers recorded yet. A two-judge sample of 40 blind-spot rows found nothing
  new, and a triage bug fix leaves the 215 body rows unchanged. Disclosed that the public scripts do not yet
  include the Vol II follow-up step, and that `body_final.py`'s proposition labels can be wrong. Lean list of
  extra propositions completed with ✱4·3 and ✱2·54.
- 2026-10-10: Vol I: both judges ran on 76 more blind-spot rows of kinds the reader does write; 5 kept,
  3 already listed, 2 new candidates (✱41·34 p. 332, ✱92·1 p. 602; errata/vol1.md §5, N9–N10), awaiting human
  check and loaded on the review page as report-check additions (113 report-check items). Of the 1,024
  single-reading hunks, 155 have now had both judges and 869 none. Vol III: after the artefact review, 161
  candidates on 111 DP pages and 33 set aside with reasons; checked against the printed Errata to Vol III, none
  of the rows is an already-printed erratum. The human check has started on a small first batch and is in
  progress. Methodology: a glyph-matching pilot is described; its results are not used for any list.
- 2026-10-11: the first human check is complete. One person answered all 224 active items, blind except one sample
  answer: 95 through the A/B question and 129 through a glyph picker (tap what is printed in a box, from 10 tiles of PM's own
  glyphs; both versions always among them; no machine pick shown), described in the Human review section and
  METHODOLOGY §4. The weighted-interval method was chosen when the answers were scored, not before as this page
  had promised, and "borderline" was never defined. Vol I report:
  96 entries in a revised draft (76 kept, 20 moved in from held back), 1 removed (the print agrees with the
  ebook), 5 held; not sent. The 11 Vol I additions (✱4·42 and the 10 new candidates) were confirmed. Precision
  of the reported differences: Vol I 93%, Vol II 94%, Vol III 91%, all three 93%, with intervals and
  precision-adjusted estimates for the populations covered; judges' miss rate in the rejected stratum 15%.
  23 loaded items were withdrawn before scoring, 6 of them false items from our own text conversion (now
  guarded against). The count of withdrawn Vol II items by class is corrected to 7 page-marker, 4 LaTeX
  fragments and 3 notation (was 8, 3 and 3). Methodology: caveats added on the second copy (the same scan) and
  on Gutenberg's HathiTrust source; Vol III errata wording made more careful; glyph-matcher result updated
  (its picks still not used for any list). Lean: ✱9–✱10 added in the companion repository (still private): 60
  numbered items, 53 derived and 7 restating the embedding's primitive rules; the 103 explicit ✱2–✱5 replays
  are now split into 72 that use only the propositions PM cites and 31 that also need one PM does not cite.
  New table: how far each formalization of PM got, in one unit, with a defined "Fits within PM" column.
