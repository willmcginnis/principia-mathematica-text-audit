# Scripts

The code for the Vol I and Vol II pipeline, as it was run, with these edits for publication:

- Default paths now come from environment variables instead of a home directory. `PM_WORK` (default `./work`)
  is the working directory that holds page images, model readings and intermediate JSON; `GUTFILE` is the
  Gutenberg HTML file; `DJVU` is the DjVu file; `CODEX` is the Codex CLI binary (default `codex` on `PATH`).
- `normalize.py` is the shared normalizer and set-aside filter (`post()`, `blind()`). It is the same code the
  Vol III comparison uses, without that comparison's input handling (DP's unposted text is not published).
- Fixed on 2026-10-04: `fullpage_compare.py`'s Gutenberg renderer (a `<` inside a formula used to swallow text),
  and a small-capital roman-numeral class in `blind()`. `vol2_split_artefacts.py`, `fetch_vol1_pages.sh` and the
  held-back rule in `pg_errata_render.py` are new.
- Added later on 2026-10-04, after the second review: `notation()` in `normalize.py` and the
  `notation_representation` rule in `vol2_split_artefacts.py`, plus one widened `old`/`new` pair and one
  page note in `pg_errata_render.py`.

Not included: the Vol III scripts (they read DP's unpublished text); the control-group scoring scripts
(they read a third-party register that has no licence, see [METHODOLOGY.md §6](../METHODOLOGY.md#6-control-group-a-regression-benchmark));
the human-review tooling, which is still in use; and the scripts of the earlier Vol I proposition pass
(METHODOLOGY §2), whose outputs feed the Vol I report.

## Known gaps: the scripts do not run end to end from this repository

**Vol II follow-up step not included yet.** `vol2_split_artefacts.py` has the comparison-artefact rules (the 68
rows) only. It does not include the follow-up step of 2026-10-08: the p. 497 row (the script's comments still
call it "held for follow-up") and the 7 follow-up rows, including the 5 set aside as rejected by the judges
(METHODOLOGY §4.5). The script that selected and judged those rows is not public yet. Cleaned-up versions of
both will be published later. Until then the 73 set-aside rows and the 149 kept spans cannot be reproduced
from this repository alone.

**Vol I proposition labels.** `body_final.py` assigns each body row to the last proposition cited before it,
which is not always the proposition the row belongs to. The ✱4·42 row on p. 124 was filed under ✱2·11 that
way and relabelled by hand; re-running this `body_final.py` brings back the ✱2·11 label. Other labels may be
wrong too.

**Vol I triage fix not included yet.** The 2026-10-09 fix to the inverted-D test in `body_triage.py` (the
reading must be non-empty) is not in this copy (METHODOLOGY §7). The follow-up of the 1,024 single-reading
hunks is not public yet either.

**Inputs not included.** Download the Gutenberg HTML (#78050, #78255) and the Wikimedia Commons DjVu files
yourself (`fetch_vol1_pages.sh` gets the Vol I page images). Pipeline intermediates that the scripts read are
not shipped either:

| Script | Reads (not included) |
|---|---|
| `body_final.py` | `scan/full/body_conf2.cx.json` (the vetoed Vol I body rows), `data/our_errata_scan.tsv` and `scan/pass3/tier2_entries.txt` (the earlier Vol I lists), `data/errata_*.txt` (transcribed published errata) |
| `fullpage_compare.py` | `data/errata_v1page.txt`, `data/errata_v2page.txt`, `data/errata_010.txt` (transcribed published errata; a missing file silently disables the errata filter) |
| `vol2_build_final.py` | `scan2v/full/*_scanpicks.cx.json`, `fcq2_agree*.fc.json`, `data/errata_vol2_pages.txt` |
| `vol2_split_artefacts.py` | `data/vol2/v2_final.json` (and `v2_set_aside.json` if present), the blind readings under `scan2v/full/` |
| `sweep_eval.py` | `scan/full/intro_confirmed.json` |
| `dots.py` | `data/vol1.jsonl` |
| `bs_check.py` | `scan/pass3/blindspot_opus.json` (in its self-test) and the row file given on the command line |
| `pg_errata_items.py` | `vol1_errata_draft.txt` (the long-form draft) |
| `pg_errata_render.py` | `data/vol1/pg_report_units.json` (the formatter's output) and `data/vol1/report_provenance.json` |

**Paths.** `body_final.py`, `sweep_eval.py`, `dots.py`, `pg_errata_items.py` and `pg_errata_format.py` ignore
`PM_WORK` and read paths relative to the current directory. `read_page.sh` expects the prompt at
`$PM_WORK/scan/full/prompt_full.txt`, not in `scripts/`.

**Environment variables** not documented elsewhere:

| Variable | Used by | Meaning |
|---|---|---|
| `OFF` | `fullpage_compare.py`, `fc_full.py` | DjVu page minus printed page (22 for Vol I, 40 for Vol II) |
| `SECOND` | `fullpage_compare.py` | directory of Reader 2: default `opus` (the Vol I Introduction run); `codexhi` for the Vol I body and Vol II |
| `POSTNORM` | `fullpage_compare.py` | apply `normalize.post()` to both streams (set for Vol II) |
| `SCANBASE` | `fullpage_compare.py` | directory holding the readings (default `$PM_WORK/scan/full`) |
| `ERRFILES` | `fullpage_compare.py` | comma-separated published-errata files |
| `CODEX_EFFORT` | `read_page.sh` | effort for the `codex` reader; unset sends none (server default) |
| `JUDGE`, `IMGFMT`, `FCSUFFIX` | `fc_full.py` | judge (`opus` or `codex`), page-image path pattern, output suffix |
| `EFFORT` | `bs_check.py` | Opus effort for the crop check (default `high`) |
| `V2DATA` | `vol2_split_artefacts.py` | directory of the Vol II row files |
| `UNITS`, `OUT`, `SIGNATURE` | `pg_errata_render.py` | input units, output file, signature line of the email |

The model calls need the `claude` and `codex` command-line clients with a working login;
`CLAUDE_CODE_OAUTH_TOKEN` is optional. Python 3 with Pillow, and `ddjvu` from DjVuLibre.

| Script | Stage |
|---|---|
| `fetch_vol1_pages.sh` | Download Commons' 1920 px renders of the Vol I pages (what the Vol I readers and judges saw) |
| `render_djvu.sh` | Render one Vol II DjVu page to JPEG at native resolution |
| `read_page.sh`, `prompt_full.txt` | Blind full-page reading of one page by one model/effort |
| `dots.py` | PM dot-notation parser and truth-table check (propositional formulas) |
| `compare_scan.py` | Proposition-level comparison of blind readings with Gutenberg #78050 |
| `fullpage_compare.py` | Full-page comparison: normalize both sides, diff, label hunks (labels: METHODOLOGY §3) |
| `normalize.py` | Shared normalizer and set-aside classes (used for Vol II via `POSTNORM`) |
| `body_triage.py` | Vol I body: drop formatting noise, set aside blind-spot classes, queue the rest |
| `fc_full.py` | Forced choice: Opus (or Codex with `JUDGE=codex`) picks the reading that matches the print |
| `bs_check.py` | High-resolution crop check for blind-spot rows (renders the Vol I DjVu at native resolution) |
| `body_final.py` | Vol I body: classify judged rows (substantive, dot-only, number-dot, alignment, TeX residue) |
| `sweep_eval.py` | Codex effort-setting comparison on the Vol I Introduction (METHODOLOGY §5) |
| `vol2_build_final.py` | Vol II: merge both judges' picks into the candidate list |
| `vol2_split_artefacts.py` | Vol II: set aside comparison artefacts, with a reason per row (METHODOLOGY §4.5) |
| `pg_errata_items.py`, `pg_errata_format.py`, `pg_errata_render.py` | Build the Vol I report in Gutenberg's errata format, with deterministic acceptance checks and the held-back rule |
