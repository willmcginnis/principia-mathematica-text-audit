# Changelog

Newest first. Entries up to 2026-10-12 were moved here from the README; their text is unchanged, so their
links and section names refer to the README as it was then. Earlier numbers are as of their date.

- 2026-10-13: links to the Lean repository's docs moved to its new main, 672f6ab (after its Prove2Me export release 1.0.0).
- 2026-10-13: the Lean repository is now dual-licensed MIT OR Apache-2.0; links to its docs moved to its new main, 5b28a60.
- 2026-10-12: links to the Lean repository's docs moved to its new main, e3f64c3.
- 2026-10-12: README slimmed; details moved to docs/; Lean progress and the formalization comparison now live in the Lean repository (links); CHANGELOG, CITATION.cff and CONTRIBUTING added.
- 2026-10-12: the Lean repository was renamed principia-mathematica-lean; links updated (the old address redirects).
- 2026-10-12: Lean progress, our row and the Lean section updated to the Lean repository's main branch `e73ab2b`
  (adds ✱14·3 as a schema, one theorem per instance, not as printed: its printed form takes propositions as apparent
  variables, and the formalization has no type of propositions): all 47 of ✱14's assertions proved, ✱11–✱14
  123/123/123 (✱14 9/38); Vol I 456 of 3,230 assertions proved.
- 2026-10-12: Lean progress, our row and the Lean section updated to the Lean repository's main branch `ac0cdd1`
  (adds 51 of ✱20's 55 numbered propositions and 44 of ✱21's 48, with ledgers, and PM's displayed chains in ✱11·71, ✱13,
  ✱14 and ✱20 as `calc` blocks): Vol I 455 of 3,230 assertions proved; classes (✱20–✱24) in progress, with the eight ✱20/✱21 items not
  counted listed; ✱20–✱56 95/95/95. Fidelity counts are those the ledgers record; footnote 8 notes the Lean README's three
  readings without choosing among them.
- 2026-10-12: "Lean progress" section added (linked from the status at a glance): done versus remaining per
  volume and per Vol I range, with milestones, computed by a script from the Lean repository's main branch
  (`2cca9b6`) and PM's own lists of numbered items; it is re-run at every update. Vol II's total is an upper
  bound from the transcription's labels; Vol III is not yet counted.
- 2026-10-12: our row and the Lean section updated to the Lean repository's main branch `2cca9b6` (adds ✱13·3, 46 of ✱14's 47 assertions and per-proposition ledgers for ✱12–✱20, so F is now stated for ✱13, ✱14 and ✱20).
- 2026-10-11 (evening): our formalization-table row, its footnotes and the Lean section updated to the Lean
  repository's main branch `ac3fcf7` (adds ✱11, ✱12·1/✱12·11, ✱13 except ✱13·3, and parts of ✱14 and ✱20). The "Fits within PM"
  definition now says that an extra rule no proof counted in P uses is allowed (our row has one, a comprehension
  rule that no counted PM proposition uses).
- 2026-10-11: the Lean repository is now public ([principia-mathematica-lean](https://github.com/willmcginnis/principia-mathematica-lean), MIT); the
  README links it instead of calling it private. Its main branch covers ✱1–✱5 and ✱9–✱10, as described here.
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
- 2026-10-10: Vol I: both judges ran on 76 more blind-spot rows of kinds the reader does write; 5 kept,
  3 already listed, 2 new candidates (✱41·34 p. 332, ✱92·1 p. 602; errata/vol1.md §5, N9–N10), awaiting human
  check and loaded on the review page as report-check additions (113 report-check items). Of the 1,024
  single-reading hunks, 155 have now had both judges and 869 none. Vol III: after the artefact review, 161
  candidates on 111 DP pages and 33 set aside with reasons; checked against the printed Errata to Vol III, none
  of the rows is an already-printed erratum. The human check has started on a small first batch and is in
  progress. Methodology: a glyph-matching pilot is described; its results are not used for any list.
- 2026-10-09: Vol I body follow-up: the 1,024 single-reading hunks on 109 pages were triaged, and both judges
  ran on the 39 queued rows. 16 were kept: 7 already in the draft report, 1 page-marker placement and 8 new
  candidates, awaiting human check (errata/vol1.md §5); they and ✱4·42 are loaded on the review page as 9
  additions to the report check, with no answers recorded yet. A two-judge sample of 40 blind-spot rows found nothing
  new, and a triage bug fix leaves the 215 body rows unchanged. Disclosed that the public scripts do not yet
  include the Vol II follow-up step, and that `body_final.py`'s proposition labels can be wrong. Lean list of
  extra propositions completed with ✱4·3 and ✱2·54.
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
- 2026-10-04: wording fixes after a third round of two reviews. The 102-entry Vol I report check and the
  Vol II top-up (14 items withdrawn and replaced, seed 20261005) are now loaded on the review page; no answers
  are recorded yet. Effort-unset claim, coverage wording, the Vol III errata filter status and H18's context
  stated more carefully. The `ᗡ"`/`Rl` rows in Vol II are grouped under one note.
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
- 2026-10-04: "Status at a glance" matrix and work-in-progress banner added. The Vol I body coverage gap and
  the 6 unjudged Vol II hunks are now stated in the status tables.
- 2026-10-04: fix pass after two reviews. Vol II: 62 comparison artefacts set aside (222 → 160 candidates),
  rendering bug fixed. Vol I report: intro rewritten to describe the checks as they happened, 22 entries held back (102 → 80), contexts made unique.
  Methodology: Introduction reader, coverage gaps, effort settings, errata sources, sample design and open
  items corrected; glossary added.
- 2026-10-04: first public draft.
