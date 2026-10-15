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

| Volume | Digital text | Candidates | Checked by a person | Sent upstream | List |
|---|---|---|---|---|---|
| **I** (1910) | Gutenberg #78050 | revised draft report of 96 entries, plus 11 confirmed additions not yet merged; other candidates counted in [docs/STATUS.md](docs/STATUS.md) | all 102 entries of the earlier draft and the 11 additions, one by one (2026-10-11): 96 confirmed, 1 removed, 5 held. Body and Introduction rows: sample only, precision 93% (78–98%); the other rows are awaiting human check | not sent | [errata/vol1.md](errata/vol1.md) |
| **II** (1912) | Gutenberg #78255 | 156 candidates; 3 published errata that appear not to have been applied | sample only, precision 94% (80–98%); the other rows are awaiting human check, and the 3 errata await human confirmation | not reported | [errata/vol2.md](errata/vol2.md) |
| **III** (1913) | DP, in progress | 161 candidates on 111 DP pages | sample only, precision 91% (72–98%); the other rows are awaiting human check | not yet; will go to DP through their process | counts only (DP text unpublished) |

The full status, stage by stage and with every count and caveat, is in [docs/STATUS.md](docs/STATUS.md).

## Where to find things

- **Errata lists:** [errata/vol1.md](errata/vol1.md) (every Vol I report entry with its human-check status, the
  revised draft report and the confirmed additions) and [errata/vol2.md](errata/vol2.md) (Vol II candidates,
  unapplied published errata and set-aside rows).
- **The human check:** [docs/HUMAN_REVIEW.md](docs/HUMAN_REVIEW.md) (procedure, results, withdrawn items, sample design).
- **Detailed status:** [docs/STATUS.md](docs/STATUS.md). **Terms:** [docs/GLOSSARY.md](docs/GLOSSARY.md).
- **Method and limitations:** [METHODOLOGY.md](METHODOLOGY.md); the code is in [scripts/](scripts/) (see
  [scripts/README.md](scripts/README.md) for what is missing).
- **Related work and credits:** [docs/RELATED_WORK.md](docs/RELATED_WORK.md). **History:** [CHANGELOG.md](CHANGELOG.md).
- **Lean formalization:** the companion repository [principia-mathematica-lean](https://github.com/willmcginnis/principia-mathematica-lean).

## How it works

The full-page pipeline aims to transcribe each printed page **blind** twice, without the existing digital text.
Coverage is complete for Vols II–III and partial for Vol I (see [docs/STATUS.md](docs/STATUS.md)). For most of the audit the
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

## Human review

**Complete (2026-10-11).** One person answered all 224 active items on a private review page, checking every
Vol I report entry and addition one by one and a stratified sample of the pipeline's candidates, against the
scan. The check was blind, with one exception: one scored sample answer (✱50·72, p. 355) is not blind. The
interval method below was chosen when the answers were scored; an earlier version of this page had promised to
state it before any answers were scored, and that did not happen. Both are described in full, with the
procedure, the withdrawn items and the sample design, in [docs/HUMAN_REVIEW.md](docs/HUMAN_REVIEW.md).

| Volume | Population the sample covers | Items scored | Precision | 95% interval | Expected real differences |
|---|---|---|---|---|---|
| Vol I | the 215 body rows and 53 Introduction rows (268); not the report entries, which were checked one by one | 31 | **93%** | 78–98% | about 249 of 268 (209–263) |
| Vol II | the 147 spans kept after both artefact splits; not the 2 follow-up spans kept on 2026-10-08 (after the draw) or the 7 errata-page items | 32 | **94%** | 80–98% | about 138 of 147 (117–144) |
| Vol III | the 161 rows kept by the artefact review; 2 of them, of a kind with no scored item, are not covered | 23 | **91%** | 72–98% | about 145 of 159 (115–155) |
| All three | 574 rows | 86 | **93%** | 85–97% | |

Rows outside the sample, and the candidates outside the sample's populations (for example the Vol I tier-2
rows), are still awaiting human check.

## Lean formalization

A companion project formalizes part of PM in Lean 4 as a deep embedding (PM's formulas are a data type inside
Lean). It is public at [principia-mathematica-lean](https://github.com/willmcginnis/principia-mathematica-lean) (MIT OR Apache-2.0), so its proofs can be checked by building it;
its results are reported by the author. What it proves and from which rules, how closely its proofs follow PM's,
and a comparison with other formalizations of PM are kept there, in one copy (moved from this README on
2026-10-12; links at commit `a31630c`):
[docs/PROGRESS.md](https://github.com/willmcginnis/principia-mathematica-lean/blob/a31630c/docs/PROGRESS.md), [docs/FIDELITY.md](https://github.com/willmcginnis/principia-mathematica-lean/blob/a31630c/docs/FIDELITY.md) and
[docs/FORMALIZATION_COMPARISON.md](https://github.com/willmcginnis/principia-mathematica-lean/blob/a31630c/docs/FORMALIZATION_COMPARISON.md).

What it contributed to this audit:

- **✱1·4.** The author reports that Gutenberg #78050's transcription (`p ∨ q . ⊃ . p ∨ p`) is not derivable in
  the embedded proof system, on the basis of a checked countervaluation. The 1910 print has `q ∨ p` (entry 1 in
  [errata/vol1.md](errata/vol1.md), confirmed by the human check; not sent).
- **✱4·42 (p. 124).** The replay independently re-found the citation `⊢ . ✱3·26 .` that the print has on *Dem.*
  line (2) and the ebook omits. It is already one of the 215 Vol I body rows, so it is not counted again. The
  human check confirmed it (2026-10-11); it is not yet merged into the report
  ([errata/vol1.md §4](errata/vol1.md#4-found-by-the-lean-replay--confirmed-by-the-human-check)).

Apparent slips in the 1910 print itself, which the ebook follows, are noted in the Lean repository's
[docs/FIDELITY.md](https://github.com/willmcginnis/principia-mathematica-lean/blob/a31630c/docs/FIDELITY.md#what-the-proofs-found-in-the-text) (✱4·32 and ✱4·43, awaiting human check;
✱10·27, possibly a citation slip).

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

This audit stands on other people's work, and several of them found things first. Above all, **Project
Gutenberg** and the **Distributed Proofreaders** volunteers, whose transcriptions are the object of study. Every
error report here is offered as a contribution to their work, not a criticism of it. Luc Pommeret's independently
compiled anomaly register is our regression benchmark, and Travis / Impression Editions' Gerrata is independent
prior art for the same idea. Page images: Wikimedia Commons (Vols I–II) and the University of Michigan Historical
Mathematics Collection via HathiTrust (Vol III). The full list, with links, is in
[docs/RELATED_WORK.md](docs/RELATED_WORK.md).

## Contributing

To report a discrepancy against the scans, see [CONTRIBUTING.md](CONTRIBUTING.md). Every errata entry is checked
by a person against the scan before it is submitted, and please do not paste unposted Distributed Proofreaders
text into issues.

## Repository layout

```
README.md             this file: what the audit is, status, links
CHANGELOG.md          dated changes
CONTRIBUTING.md       how to report a discrepancy
CITATION.cff          how to cite
METHODOLOGY.md        the pipeline, its parameters, the control group, and the limitations
docs/STATUS.md        the detailed status, volume by volume
docs/HUMAN_REVIEW.md  the human check: procedure, results, withdrawn items, sample design
docs/GLOSSARY.md      terms used on these pages
docs/RELATED_WORK.md  related work and credits
errata/vol1.md        Vol I: all 102 drafted entries with their human-check status, the revised draft report (96 entries), the 6 not in it, and the 11 confirmed additions (1 body row re-found by the Lean replay, 10 new candidates); not sent
errata/vol2.md        Vol II: unapplied published errata, the 156 candidates, and the 73 set-aside rows; sample-checked, rows awaiting human check
scripts/              the code for the Vol I and Vol II pipeline (see scripts/README.md for what is missing)
```

## How to cite

See [CITATION.cff](CITATION.cff) (GitHub offers it as "Cite this repository"):

> Will McGinnis, *Principia Mathematica text audit: errata tracker*.
> https://github.com/willmcginnis/principia-mathematica-text-audit

Because everything here will change, please cite a specific commit.

## License

Code is under the [MIT License](LICENSE). Our own documentation and data are released into the public domain
under [CC0 1.0](LICENSE-DOCS). The Gutenberg text quoted in the errata lists is from public-domain ebooks.
*Principia Mathematica* itself (1910–1913) is in the public domain in the United States.

## Changelog

Moved to [CHANGELOG.md](CHANGELOG.md).

## Moved sections

These headings are kept so that older links still work.

### Status

Moved to [docs/STATUS.md](docs/STATUS.md).

### Volume I: 1910 print, Gutenberg #78050

Moved to [docs/STATUS.md](docs/STATUS.md#volume-i-1910-print-gutenberg-78050).

### Volume II: 1912 print, Gutenberg #78255

Moved to [docs/STATUS.md](docs/STATUS.md#volume-ii-1912-print-gutenberg-78255).

### Volume III: 1913 print, Distributed Proofreaders project in progress

Moved to [docs/STATUS.md](docs/STATUS.md#volume-iii-1913-print-distributed-proofreaders-project-in-progress).

### Results

The human check's results are in [docs/HUMAN_REVIEW.md](docs/HUMAN_REVIEW.md#results).

### Sample design

Moved to [docs/HUMAN_REVIEW.md](docs/HUMAN_REVIEW.md#sample-design).

### Glossary

Moved to [docs/GLOSSARY.md](docs/GLOSSARY.md).

### Lean progress

Now in the Lean repository: [docs/PROGRESS.md](https://github.com/willmcginnis/principia-mathematica-lean/blob/a31630c/docs/PROGRESS.md).

### How far each formalization got

Now in the Lean repository: [docs/FORMALIZATION_COMPARISON.md](https://github.com/willmcginnis/principia-mathematica-lean/blob/a31630c/docs/FORMALIZATION_COMPARISON.md).
