# Human review

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
  afterwards ([METHODOLOGY §4](../METHODOLOGY.md#4-adjudication)).

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
mark; it is the same scan ([METHODOLOGY §7](../METHODOLOGY.md#7-limitations)). 44 minutes after the blind answer,
the reviewer described the mark as a misprint (all they could make out was a dot, like a ghost image), and
Claude entered "garbled" at the reviewer's request. That answer replaced the blind one and is the one scored.
"Neither" and "garbled" both count against precision, so the figures below are the same either way.

Detailed results are in the private source repository; this page gives the summary and, apart from
✱50·72 above, no per-item answers. The outcome of each Vol I report-check entry is in
[errata/vol1.md](../errata/vol1.md). The page had two checks:

1. **Vol I report check (113 items; 64 answered with the picker, 49 with A/B):** all 102 entries of the earlier
   Vol I draft and 11 draft additions, each checked one by one. 96 entries were confirmed, 1 removed and 5 held;
   the 11 additions were all confirmed ([Volume I](STATUS.md#volume-i-1910-print-gutenberg-78050), [errata/vol1.md](../errata/vol1.md)).
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

## Results

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
  scan is open ([METHODOLOGY §7](../METHODOLOGY.md#7-limitations)).
- The check measures the precision of the **differences** the pipeline reported. It does not look for errors
  that the digital text and our readings share, and our readings agreeing with Gutenberg may not be
  independent evidence: Gutenberg's credits say its text was produced from HathiTrust images, and which
  HathiTrust scan is not yet known ([METHODOLOGY §7](../METHODOLOGY.md#7-limitations)).
- Rows outside the sample, and the candidates outside the sample's populations (for example the Vol I tier-2
  rows), are still awaiting human check.

## Sample design

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
