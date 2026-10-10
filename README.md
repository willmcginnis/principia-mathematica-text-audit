# Principia Mathematica text audit: errata tracker

> **Work in progress — awaiting human review.** The human check has started on a small first batch and is in
> progress; no result from it is used here yet. Everything below is a model-pipeline output and is awaiting human
> review. Nothing has been reported upstream.

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
| **Vol I** (Gutenberg #78050), body and drafted report | 🟡 2nd reading missing on 110 of 536 pages (109 of them carry 1,024 hunks); 5 pages not compared | 🟡 215 body rows pass both judges; of the 1,024 single-reading hunks, 155 have been judged by both models (2026-10-08/10): 10 new candidates | 🟡 automatic matcher only; known gaps | 🟡 all 102 report entries loaded on the review page; the 10 new candidates and ✱4·42 loaded as 11 additions to that check; body sample loaded; the human check has started on a small first batch and is in progress | ⬜ not sent (80 in draft report, 22 held back) | 🟡 all 102 report entries and the 10 new candidates listed, each awaiting human review; other candidates counts only |
| **Vol I Introduction** (pp. 1–88) | 🟡 2nd reader (Opus) on 44 of 88 pages | 🟡 Opus only (53 rows), no veto | 🟡 automatic matcher only; known gaps | 🟡 in sample, in progress; no results yet | ⬜ not reported | ⬜ count only |
| **Vol II** (Gutenberg #78255) | ✅ all 816 pages, both readings | ✅ both judges done, including the 7 follow-up rows judged on 2026-10-08 (2 kept, 5 set aside) | 🟡 17 rows classified by Claude; 3 apparently unapplied errata, awaiting confirmation | 🟡 sample loaded (14 items withdrawn and replaced); in progress | ⬜ not reported (156 candidates, 3 errata) | ✅ full list, all rows awaiting human review |
| **Vol III** (DP, in progress) | ✅ all 512 images, both readings | 🟡 194 spans pass both judges; after the artefact review, 161 kept on 111 DP pages and 33 set aside with reasons | 🟡 checked against the Errata to Vol III (pp. ix–x) by Claude, not by a person: none of the rows is an already-printed erratum | 🟡 in sample, in progress; no results yet | ⬜ not yet; will go to DP through their process | — counts only (DP text unpublished) |
| **Lean formalization (✱1–✱5)** | — statements read from the 1910 scan | — proofs checked by Lean, not judged | — | — | ⬜ not sent: ✱1·4 (Vol I draft entry 1) and ✱4·42 (already one of the 215 Vol I body rows) | 🟡 summary only; ✱4·42 in [errata/vol1.md §4](errata/vol1.md#4-found-by-the-lean-replay--awaiting-human-check); Lean repo not yet published |

✅ done · 🟡 partial / in progress · ⬜ not started · — not applicable

*Lean row:* the columns are the text-audit stages, so most do not apply. The results are reported by the
author: all 188 ✱2–✱5 propositions are proved from PM's primitive propositions, with no added axioms. The
replay also independently re-found one Vol I transcription candidate (✱4·42, p. 124). It is not new: it is
already one of the 215 body rows from the full-page pass, but it never reached the draft report. It is
awaiting human check. The results become verifiable once that repository is published ([details](#lean-formalization)).

## Status

Counts are pipeline outputs. A **candidate** is a row that passed the automated checks described for its
volume below. **No result of the human check is used here yet; every candidate and report entry is awaiting
human review.** The pipeline stages overlap, so the counts within a volume are **not** added together. Terms are
defined in the [glossary](#glossary).

### Volume I: 1910 print, Gutenberg #78050

| | |
|---|---|
| Drafted report | **102 entries, all awaiting human review**: 80 in the draft report and 22 held back. [errata/vol1.md](errata/vol1.md) lists every one with its status, in Gutenberg's preferred errata layout (one held-back entry, H18, still needs a unique context). They come from the proposition pass, proof replay and an extended scan check over ✱31–✱97. The 22 held-back entries have weaker model support. 20 change only marks that machine readers often get wrong (dots, E! for ∃!, breves and arrows, the inverted D). 19 of them have had neither a close-up crop check nor a later pick of the print by both full-page judges; the 20th (H21) has since been picked as the print by both judges and looked at in a scan crop by Claude, not yet by a person, and stays held back. In 1 the forced-choice judge answered "neither". 1 (a missing ✱ in a label) has had no dedicated scan check. All 102 are loaded on a private review page, where a person will check each one against the scan; that check has started on a small first batch and is in progress. Nothing is sent to Project Gutenberg until that check is finished. |
| Full-page pass, body (pp. 89–666) | **215** substantive candidate rows on 163 identified propositions (27 rows not attributed to a proposition). Each has two blind Codex readings that agree against Gutenberg; both judges (Opus, then the Codex veto) picked the print. 50 of the 215 are on propositions already in the earlier lists (independent re-discovery). Both counts rest on proposition labels assigned by `body_final.py`, which takes the last proposition cited before the row, not always the one the row belongs to: ✱4·42 was filed under ✱2·11 that way and corrected by hand, other labels may be wrong too, and re-running the public `body_final.py` brings back the ✱2·11 label. Also 74 dot-only and 39 number-dot rows (low priority). **Coverage gap:** Reader 1 differed from Gutenberg on 536 comparable pages. Reader 2 was attempted on 433 of them and succeeded on 426. That leaves 110 pages without a second reading. 109 of them carry 1,024 Reader-1 hunks, which have one reading only (see the follow-up below); the 110th has only a hunk matched to a published erratum. 5 further pages had no Gutenberg page marker to split on, so they were not compared at all. |
| Body follow-up, single-reading pages (2026-10-08/10) | **8 new candidates, awaiting human check.** The 1,024 single-reading hunks on 109 pages went through the same triage as the body pass: 292 dropped as formatting, 654 set aside in blind-spot classes and 39 long alignment blocks dropped, so 985 were not queued. Both model judges ran on the other 39 (on 7 pages): 16 kept, 23 rejected. (A triage fix made later changes these counts to 651, 40 and 41. The 2 newly queued rows are page-marker placements, so the 8 candidates are unchanged; [METHODOLOGY §7](METHODOLOGY.md#7-limitations).) Of the 16, 7 are already in the draft report and 1 is page-marker placement, not a text error. The other **8 are new candidates**, listed in [errata/vol1.md §5](errata/vol1.md#5-new-candidates-from-the-body-follow-up-2026-10-09--awaiting-human-check). 6 of them are "Cls ex² excl" in ✱84, where the ebook drops "ex". They had one blind reading plus two judges, which is weaker support than the 215 body rows. They are loaded on the private review page as additions to the report check, awaiting human check. ✱4·42 (below) is a body row, not one of these. A two-judge sample of 40 of the 654 blind-spot rows found nothing new ([METHODOLOGY §7](METHODOLOGY.md#7-limitations)). **2 more new candidates (2026-10-10), awaiting human check.** Both judges then ran on the 76 other blind-spot rows of kinds the reader does write (breves, arrows and overlines; inverted commas, ! and ↓; restriction signs on pages where the reader writes them): 5 kept, 3 of them already in the earlier lists, and 2 new: ✱41·34 (p. 332) and ✱92·1 (p. 602), listed in §5 as N9–N10. They are loaded on the private review page as report-check additions. In all, 155 of the 1,024 single-reading hunks have now had both judges and 869 have had no judge. |
| Full-page pass, Introduction (pp. 1–88) | **53** candidate rows. Checked less strictly than the body: Reader 1 (Codex) differed from Gutenberg and Opus picked the print in the forced choice. On 37 of them the second reader (Opus) agreed; on 16 there was no second reading. No Codex veto. |
| Further candidates | Proposition pass, tier 2: 47 rows where the crop check picked the print. Crop check of 83 blind-spot rows: 4 picks for the print (✱34·84, ✱35·01, ✱61·391, ✱80·41; the first and last are also held as uncertain). Awaiting human review, and not yet in either human check (outside the precision sample's population and outside the 102 report entries). The Lean replay independently re-found ✱4·42 (p. 124), where the ebook omits the citation `⊢ . ✱3·26 .` that the print has on *Dem.* line (2). This is not an additional candidate: it is already one of the 215 body rows above (it was first filed there under ✱2·11 by the labelling rule described above; the label was corrected by hand), so it is not counted again here. It never reached the draft report. It is listed in [errata/vol1.md §4](errata/vol1.md#4-found-by-the-lean-replay--awaiting-human-check), awaiting human check. It is loaded on the private review page as an addition to the report check, awaiting human check. |
| Held as uncertain | Two separate sets, 11 rows in all, none of them in the drafted report. 7 tier-2 items, whose answers were re-read as BOTH after a parsing fix; these are not counted in the 47 above. And 4 crop-check rows whose verdict changes with the effort setting, on 3 propositions: ✱34·84, ✱80·41 (twice, pp. 505 and 510) and ✱90·31. |

### Volume II: 1912 print, Gutenberg #78255

| | |
|---|---|
| Candidates | **156 candidates, all awaiting human review**: 149 spans on 125 printed pages where both judges (Claude Opus and Codex) pick the print over Gutenberg's text, plus 7 further candidate discrepancies among the 17 judged rows on pages that carry a published erratum. Those 17 were classified one at a time against the erratum text by Claude, not by a person. One of the 7 (S3) lies inside a definition that an unapplied erratum replaces, so it is probably superseded. All 816 pages have both blind readings; the Opus forced choice ran on 997 rows. |
| Set aside | 73 judged rows. 68 classified as comparison artefacts, not text differences: 51 page-marker placements, 10 LaTeX fragments left by a rendering bug (now fixed), 1 small-capital typography, and 6 notation-representation rows (the same glyph written two ways; set aside after the second review). Listed in [errata/vol2.md](errata/vol2.md#4-set-aside-classified-as-comparison-artefacts-68-rows). And 5 follow-up rows that the judges did not both pick as the print ([errata/vol2.md §5](errata/vol2.md#5-set-aside-follow-up-rows-rejected-by-the-judges-5-rows)). |
| Published errata | **3 published errata that appear not to have been applied** (pp. 11, 71, 82). The transcriber's note says the published errata were applied; these three appear to have been missed. Two are in the "Additional errata" printed in Vol III, so they are easy to overlook. Awaiting human confirmation. |
| Follow-up | Re-comparing the 17 pages affected by the renderer fix found 6 reader-agreed hunks (on 6 of those pages), and a set-aside row on p. 497 hid Gutenberg's `*183-26`. Both judges ran on these 7 on 2026-10-08: 2 kept (pp. 191, 225; included in the 149 spans above), 5 set aside ([METHODOLOGY §4](METHODOLOGY.md#4-adjudication)). |
| Reporting | Not yet reported. See [errata/vol2.md](errata/vol2.md). |

### Volume III: 1913 print, Distributed Proofreaders project in progress

DP's Volume III text is unpublished work in progress, so this repository gives counts only. No DP text is
quoted or redistributed here.

| | |
|---|---|
| Candidates | All 512 images of the 1913 print have both blind readings. **161 candidates on 111 DP pages**, awaiting human review. They are what remains of 194 spans on 128 DP pages where Opus and Codex both pick the 1913 print over DP's text (table-of-contents leader dots excluded, because DP's guidelines omit them), after an artefact review like the one for Vol II ([METHODOLOGY §4](METHODOLOGY.md#4-adjudication)). Earlier sub-count, pages 1–249: the Opus forced choice ran on 139 rows and picked DP's reading on 79, the print on 50 and neither on 8 (plus 1 "both" and 1 malformed answer); the Codex veto kept 31 of the 50. |
| Set aside | 33 of the 194, each with a written reason: 14 notation representation (the same printed sign written two ways), 12 residue of DP's in-round markup that our comparison failed to clean, 4 in set-aside classes, and 3 that a re-run of the current comparison does not reproduce. They are classed as comparison artefacts or as rows in set-aside classes (marks the readers cannot be trusted on), and are not counted as candidates. |
| Published errata | The Errata to Vol III printed in the volume (pp. ix–x) were transcribed from the scan and checked, by Claude, not by a person: the 14 judged rows (10 distinct differences) on the 7 erratum pages that have judged rows were classified, one distinct difference at a time, and none of the rows is an already-printed erratum. |
| Open | 9 of the 32 sampled Vol III pipeline-kept items in the precision sample are on rows now set aside; they have not been withdrawn yet ([METHODOLOGY §8](METHODOLOGY.md#8-external-review-and-corrections)). |
| Reporting | Will be reported to DP through their process, while the formatting round is open, so corrections land before the book is posted. |

## Human review

**In progress.** The human check has started on a small first batch of items on the private review page. Every
count above is a pipeline output and is awaiting human review. Two checks are loaded on that page (233 active
items in all):

1. **Vol I report check (113 items).** All 102 Vol I report entries (80 in the draft report, 22 held back) are
   on the page, and a person will check each one against the scan. This checks every entry, not a sample.
   The check also has 11 draft additions, not yet in the report: the 10 new candidates from the body follow-up
   (8 added on 2026-10-09, 2 on 2026-10-10) and ✱4·42 ([errata/vol1.md](errata/vol1.md) §4 and §5). Nothing
   goes to Project Gutenberg until it is finished.
2. **Precision sample.** A blind review of a stratified sample measures the pipeline's **precision**: how
   many of its candidates a person agrees with.

Details of the precision sample:

- **Sample:** 120 items, 40 per volume, **stratified**. Each volume contributes 32 items from the
  **pipeline-kept** stratum (both judges picked the print; for the Vol I Introduction rows, Opus only, no veto;
  called "reported" in the data files, although nothing has been reported upstream) and 8 from the **rejected** stratum (Opus picked the digital text). That
  is 96 and 24 overall. Within the pipeline-kept stratum, items are allocated by kind of difference
  (insertion or omission, look-alike characters, ✱ for the centred dot, dots, other) in proportion to the
  population, with at least 3 per kind (all rows if fewer), so rare kinds are over-sampled. Not every kind
  occurs in every volume. Vols II and III have no "dots" rows in this stratum, and Vol II had a single
  "other" row. Precision will be reweighted to the population. The draw uses a fixed seed (20261004).
  Redrawing it also needs the sampling frame (the candidate lists in file order), the kind rule and the
  allocation code. These are in the private source repository and will be published with the results,
  except for Vol III rows, which contain DP text.
- **Top-up (Vol II, done):** 14 of the 32 Vol II pipeline-kept items had been drawn from rows that the two
  artefact splits later set aside: 8 page-marker placements, 3 LaTeX fragments and 3 notation-representation
  rows (pp. 482, 483 and 489). Vol II's only "other" row is among them, and no kept row is of that kind. All
  14 were withdrawn before any answer was recorded and replaced by fresh draws from the 147 kept rows, using
  the same kind-stratified procedure and a new fixed seed (20261005). The withdrawn items stay in the record,
  marked as such, and are not shown to the reviewer. Vol II's pipeline-kept stratum is again 32 items (18
  original and 14 replacements), so the sample is still 120 items.
- **Populations covered:** Vol I samples the 215 body rows plus the 53 Introduction rows. Its estimate does
  not cover the Vol I report entries, which are checked one by one instead. Vol II samples the 147 kept rows
  (after the top-up), not the 7 errata-page items and not the 2 follow-up rows kept on 2026-10-08, which came
  after the draw. Vol III samples the 194 spans; 9 of its 32 pipeline-kept items are on rows that the Vol III
  artefact review later set aside, and they have not been withdrawn yet.
- **Blind:** for each item the reviewer sees a crop of the page around the disputed line (the full page is one
  click away), about 35 characters of context, and two versions of the span, A and B, in random order. One is
  the digital edition and the other the blind readers' version; the reviewer is not told which. The one
  question is which version matches what is printed: A, B, both look the same, neither, or can't tell.
- **Precision** is computed on the **pipeline-kept stratum only**, per volume and per kind: the share of
  answered items where the reviewer picks the print reading the pipeline proposed. "Neither" (the print
  matches neither version) counts against precision. "Both look the same" and "can't tell" are left out of
  the denominator and reported separately, with their counts. Per-kind intervals are Wilson 95%. The
  per-volume figure is reweighted across kinds, so an ordinary Wilson interval does not describe it. Its
  interval will use a method that accounts for the stratification and the weights, and that method will be
  stated, with its code, before any answers are scored. A volume whose result is borderline may get 32 more
  items. What counts as borderline is not yet defined; it will be stated with the interval method, before
  any answers are scored. Agreement with the print is not the same as a reportable error: items that match one of PM's
  published errata are filtered before reporting.
- **Human disagreement with sampled Opus rejections:** in the rejected stratum, the share of answered items
  where the reviewer sides with the print. The denominator is the 8 rejected-stratum items per volume, less
  any "both look the same" or "can't tell" answers. The population is only the rows that reached the forced choice
  and on which Opus picked the digital text (235, 281 and 595 rows in Vols I, II and III). It is not an overall judge error rate and not a recall estimate. An agreement table compares the
  reviewer, Opus and Codex on every sampled item.
- **Reporting the result:** raw candidate counts stay as they are. A precision-adjusted estimate is given
  separately, with its interval, and only for the population the sample covers.

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
- **Candidate.** A row that passed the pipeline's automatic checks. Not yet confirmed by a person.
- **Awaiting human review.** No result of a person's check against the scan is used for it yet. This applies to everything in
  this repository for now.
- **Deep embedding** (Lean section). PM's formulas are represented as a data type inside Lean, and PM's own
  primitive propositions are the only rules of proof. Lean's logic is not used to prove PM's theorems directly.

## Lean formalization

A companion project formalizes the propositional part of PM (✱1–✱5) in Lean 4, with statements read from the
1910 printed scan. It is a **deep embedding**: PM's formulas are a data type inside Lean, and a formula counts
as a theorem only if it can be derived from PM's primitive propositions ✱1·1–✱1·6 (the definitions ✱1·01,
✱3·01 and ✱4·01 are abbreviations). These results are reported by the author. The Lean repository is not yet
public, so they cannot yet be checked independently.

- All 188 ✱2–✱5 propositions are proved. Lean's `#print axioms` reports "does not depend on any axioms" for
  every theorem. That means the proofs use none of Lean's own axioms, such as choice. PM's primitive
  propositions are not Lean axioms but the rules of the embedded proof system. There is no `sorry`, no
  `native_decide` and no added axiom.
- 103 of them are replayed as explicit proof terms that follow PM's own cited propositions. The other 85
  used derived rules. 74 of the 85 have been rewritten to follow PM's own proof: one Lean line per *Dem.*
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
  - ✱4·42 (p. 124): the print cites `⊢ . ✱3·26 .` on line (2); the ebook omits it. This appears to be a
    transcription error; awaiting human check. It is an independent re-discovery: the full-page pass had
    already found it, and it is one of the 215 Vol I body rows, but it never reached the draft report. It is
    listed in [errata/vol1.md §4](errata/vol1.md#4-found-by-the-lean-replay--awaiting-human-check).

  No published erratum touches pp. 123–125. The 1925 second edition has not been checked.
- A Kalmár-style completeness theorem (every tautology is a theorem), also without axioms. No replay depends on it.
- The author reports that Gutenberg #78050's transcription of ✱1·4 (`p ∨ q . ⊃ . p ∨ p`) is not derivable in
  the embedded proof system. This rests on a checked countervaluation, not on a failed proof attempt: the
  formula is false when p is false and q is true, and a machine-checked soundness theorem shows that every
  theorem of the system is true under every valuation. The 1910 print has `q ∨ p` (draft entry 1 in
  [errata/vol1.md](errata/vol1.md), awaiting human review).

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
- **Luc Pommeret**, [*Principia-Mathematica*](https://github.com/l-pommeret/Principia-Mathematica): a source-critical Lean 4 edition of PM. Its anomaly register (read at upstream commit `3fb187a`, 2026-08-24) is our regression benchmark. The repository has no licence, so nothing from it (code, text or register entries) is included here; we report only our aggregate result.
- **Landon D. C. Elkind**: the [PM-MATS](https://github.com/LogicalAtomist/PM-MATS) project and the [*principia-rewrite*](https://github.com/LogicalAtomist/principia-rewrite) Coq formalization of ✱1–✱5 (GPL-3.0; used as an external oracle, not copied).
- **Travis / Impression Editions**, [Gerrata](https://github.com/Impression-Editions/Gerrata): semi-automated errata detection for Project Gutenberg prose, comparing Gutenberg texts with Internet Archive scans. It is independent prior art for the same idea. Our reports adopt the same Gutenberg-preferred "old ==> new" layout it emits. Gerrata does not handle mathematical notation, where most candidates found by this audit lie, and no code from it is used here.
- **Metamath** [set.mm](https://github.com/metamath/set.mm) `pm*` theorems (CC0): a statement oracle for ✱1–✱5.
- [Neo-Principia](https://github.com/MudroadWhite/Neo-Principia) (Rocq), [PrincipiaMathematica_Agda](https://github.com/yangg1g/PrincipiaMathematica_Agda), [ndrwnaguib/principia](https://github.com/ndrwnaguib/principia) (Lean) and [xamidi/luk-pmproofs](https://github.com/xamidi/luk-pmproofs).
- Page images: Wikimedia Commons (Vols I–II, 1910/1912) and the University of Michigan Historical Mathematics Collection via HathiTrust (Vol III, 1913).

## Repository layout

```
README.md         this file: the tracker
METHODOLOGY.md    the pipeline, its parameters, the control group, and the limitations
errata/vol1.md    Vol I: all 102 drafted entries (80 in the draft report, 22 held back), with status, 1 body row re-found by the Lean replay, and 10 new candidates from the body follow-up; awaiting human review, not sent
errata/vol2.md    Vol II: unapplied published errata, the 156 candidates, and the 73 set-aside rows; awaiting human review
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
