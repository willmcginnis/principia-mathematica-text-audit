# Related work and credits

This audit stands on other people's work, and several of them found things first.

- **Project Gutenberg** and the **Distributed Proofreaders** volunteers, whose transcriptions are the object of study. Every error report here is offered as a contribution to their work, not a criticism of it.
- **Luc Pommeret**, [*Principia-Mathematica*](https://github.com/l-pommeret/Principia-Mathematica): a source-critical Lean 4 edition of PM. Its anomaly register (read at upstream commit `3fb187a`, 2026-08-24) is our regression benchmark. The repository has no licence, so nothing from it (code, text or register entries) is included here; we report only our aggregate result, and the facts and numbers in the [formalization comparison](https://github.com/willmcginnis/principia-mathematica-lean/blob/abbbcc1/docs/FORMALIZATION_COMPARISON.md) (now in the Lean repository).
- **Landon D. C. Elkind**: the [PM-MATS](https://github.com/LogicalAtomist/PM-MATS) project and the [*principia-rewrite*](https://github.com/LogicalAtomist/principia-rewrite) Coq formalization of ✱1–✱5 (GPL-3.0; used as an external oracle, not copied).
- **Travis / Impression Editions**, [Gerrata](https://github.com/Impression-Editions/Gerrata): semi-automated errata detection for Project Gutenberg prose, comparing Gutenberg texts with Internet Archive scans. It is independent prior art for the same idea. Our reports adopt the same Gutenberg-preferred "old ==> new" layout it emits. Gerrata does not handle mathematical notation, where most candidates found by this audit lie, and no code from it is used here.
- **Metamath** [set.mm](https://github.com/metamath/set.mm) `pm*` theorems (CC0): a statement oracle for ✱1–✱5.
- [Neo-Principia](https://github.com/MudroadWhite/Neo-Principia) (Rocq), [PrincipiaMathematica_Agda](https://github.com/yangg1g/PrincipiaMathematica_Agda), [ndrwnaguib/principia](https://github.com/ndrwnaguib/principia) (Lean) and [xamidi/luk-pmproofs](https://github.com/xamidi/luk-pmproofs).
- Page images: Wikimedia Commons (Vols I–II, 1910/1912) and the University of Michigan Historical Mathematics Collection via HathiTrust (Vol III, 1913).

## How far each formalization got

The comparison of formalizations of PM (one unit, with a defined "Fits within PM" column and its footnotes) now
lives in the Lean repository, in
[docs/FORMALIZATION_COMPARISON.md](https://github.com/willmcginnis/principia-mathematica-lean/blob/abbbcc1/docs/FORMALIZATION_COMPARISON.md).
There is no copy here.
