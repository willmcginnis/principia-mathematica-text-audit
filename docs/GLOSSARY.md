# Glossary

- **Scan image / printed page / DP page.** A *scan image* is one page image of the printed book (a DjVu page for
  Vols I–II, an image in the UMich sequence for Vol III). A *printed page* is the page number printed in the book.
  A *DP page* is one page file of Distributed Proofreaders' Vol III project. The offsets between them are in
  [METHODOLOGY §1](../METHODOLOGY.md#1-sources).
- **Blind reading.** A model transcribes a page image without being shown the digital text.
- **Proposition pass.** The first Vol I check: blind readings of each page compared with Gutenberg one
  proposition (formula) at a time. The Vol I report comes from it ([METHODOLOGY §2](../METHODOLOGY.md#2-blind-reading)).
- **Full-page pass.** The later check of every page in full (prose, formulas, footnotes): two blind readings of
  the whole page, compared with the digital text of that page.
- **Hunk / span / row.** The comparison yields *hunks*: places where a reading and the digital text differ. A
  *span* is the disputed text of one hunk. A *row* is one hunk as it moves through the pipeline (one line in a
  data file or table). Several rows can fall in one proposition, and one proposition can carry several rows.
- **Set-aside class.** A kind of difference that the readers get wrong so often that it is not judged at all
  (e.g. PM's dots, the inverted D, arrows over letters). Set aside does not mean unimportant
  ([METHODOLOGY §3](../METHODOLOGY.md#3-comparison)).
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
- **Deep embedding** (Lean section). PM's formulas are represented as a data type inside Lean, and every PM
  proposition counted is derived only from PM's own primitive propositions (the system also has an opt-in
  comprehension rule that no counted proposition uses; footnote 6 of the Lean repository's
  [formalization comparison](https://github.com/willmcginnis/principia-mathematica-lean/blob/d8ae7df/docs/FORMALIZATION_COMPARISON.md)). Lean's logic is not used to prove PM's theorems directly.
