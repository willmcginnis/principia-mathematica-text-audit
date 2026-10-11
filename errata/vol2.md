# Volume II (Gutenberg #78255): candidates, sample-checked, rows awaiting human check

**Status: rows awaiting human check. Nothing on this page has been reported to Project Gutenberg.**
No row on this page has been checked one by one by a person, and statements below about what the print has
are the models' readings of the page image. A blind human check of a stratified sample (2026-10-11) measured
the precision of the 147 pipeline spans kept after both artefact splits at 94% (80–98%): about 138 of the 147
(117–144) are expected to be real differences from the print (see the [README](../README.md#human-review)).
The sample does not cover the 2 follow-up spans or the 7 errata-page items, and this page does not say which
sampled rows were confirmed. Expect some rows to be wrong and the list to change.

Total: **156 candidates** = 149 spans on 125 printed pages from the pipeline (section 3), plus 7 further
candidate discrepancies on pages that carry a published erratum (section 2). A further 73 judged rows are set
aside: 68 that the pipeline produced were classified as comparison artefacts (section 4), and 5 follow-up rows
were rejected by the judges (section 5).

## 1. Published errata that Gutenberg appears not to have applied (awaiting human review)

The transcriber's note says the published errata were applied; these three appear to have been missed.
Two are in the "Additional errata to Volume II" printed in Volume III, so they are easy to overlook. Each
erratum text was compared with the Gutenberg HTML by Claude. A person still has to confirm each one, and
none has been reported.

1. **p. 11**, line 13 from below: for 'Nc‘α ∩ t₀¹‘α' read 'Nc‘α ∩ t‘t₀¹‘α' (Additional errata, Vol III)  
   Gutenberg has: N₀¹‘α = Nc‘α ∩ t₀¹‘α
2. **p. 71**, last line: replace the definition by (Nc‘α)^ν = (N₀c‘α)^ν Df and μ^{Nc‘β} = μ^{N₀c‘β} Df (Additional errata, Vol III)  
   Gutenberg has: Nc‘α^{N_c c‘β} = N₀c‘α^{N₀c‘β} Df (the uncorrected definition, with a further difference, row S3 below)
3. **p. 82**, last line but one: for 'Λ_α' and 'Λ_β' read 'Λ ∩ α' and 'Λ ∩ β' (Vol II's own errata list)  
   Gutenberg has: Λ_β ↓ “ι“α ∪ ↓ Λ_α “ι“β in *110·5 Dem. (the models read the page image as showing this uncorrected form, so the erratum is a correction to the print, not a transcription slip)

## 2. Seven additional candidate discrepancies on published-errata pages

On a page that carries a published erratum, a difference from the print can be Gutenberg correctly applying
that erratum. So the 17 pipeline rows on such pages (both judges had picked the print) were held out of
section 3 and classified one at a time against the erratum text and the page image. That classification
was done by Claude, the model that orchestrates the pipeline, not by a person. Claude classified these 7 as
differences that the erratum does not touch. S3 is the exception to watch: it lies inside the definition that
the p. 71 erratum replaces, so applying that erratum would probably supersede it (see its note). The other 10
were classified as 8 errata that Gutenberg correctly applied, 1 page-marker placement and 1 small-capital
typography difference, and all 10 are set aside.

| # | Page | Gutenberg reads | Model-proposed print reading | Note |
|---|---|---|---|---|
| S1 | 11 | *(nothing)* | `0` | The models read the print as t‘t₀₀‘α in the N₀₀c‘α definition; Gutenberg has t‘t₀‘α. Not the line the erratum corrects. |
| S2 | 11 | *(nothing)* | `c` | The models read the print as N₀¹c‘α; the ebook omits the c. Separate from the erratum, which appears not to have been applied (section 1). |
| S3 | 71 | `c` | *(nothing)* | Gutenberg has N_c c‘β in the exponent where the models read the print as Nc‘β. **Potentially superseded:** this is inside the definition that the p. 71 erratum replaces (section 1), and the corrected text has no N_c c‘β. It is a difference from the uncorrected print, not an independent correction. If the erratum is applied, S3 needs no separate change. |
| S4 | 82 | *(nothing)* | `⊢` | The models read the print as ⊃ ⊢ . Prop at the end of *110·41 Dem.; the ebook omits ⊢. Not the line the erratum corrects. |
| S5 | 101 | *(nothing)* | `)` | *112·22: the models read the print as closing (ε↧“λ) before ∩; the ebook omits ). The erratum concerns *112·23. |
| S6 | 101 | `.` | `=` | *112·17: the models read the print as ΣNc‘κ = ΣNc‘λ; Gutenberg has a dot. The erratum concerns *112·23. |
| S7 | 101 | `ᗡ"` | `Rl` | *112·17 Dem.: the models read the print as ∩ Rl‘sm; Gutenberg has ᗡ“‘sm. The erratum concerns *112·23. Same pattern as six section 3 rows (see the note there). |

## 3. Pipeline candidates (149 spans on 125 pages)

Each row here has two blind machine readings of the 1912 page that agree with each other and differ from
Gutenberg's text. Both model judges (Claude Opus and Codex), shown the page image and the two readings
unlabelled, picked the readers' version as the print. No row has been checked one by one by a person; a sample of them gave the precision above.

How to read the table:

- **Page** is the printed page of the 1912 first edition.
- **Gutenberg reads** and **Model-proposed print reading** are the disputed span in the comparator's normalized
  form: all whitespace removed, LaTeX mapped to Unicode, ✱ written as `*` and the centred dot as `.`.
  *(nothing)* means that side has nothing at that point (an insertion or omission).
- **Context** is about 20 characters either side of the span on the Gutenberg side, in the same normalized
  form, with the Gutenberg span marked 【like this】.

**One recurring pattern: `ᗡ"` for `Rl`.** Rows 13, 15, 17, 127, 130 and 144 here, and S7 in section 2, are the
same difference: where the models read the print as Rl‘ (e.g. Rl‘sm, Rl‘J), Gutenberg has the inverted D with
a double inverted comma, `\text{ᗡ}ʻʻʻ` in its LaTeX. They can be checked, and if confirmed fixed, together.
Across the whole file, Gutenberg writes `\text{Rl}` in 131 formulas and `\text{ᗡ}ʻʻʻ` in 17 (23 occurrences). The
`\text{ᗡ}ʻʻʻ` occurrences outside these 7 rows have not been flagged either way: some may be the same slip and
some may be correct as they stand.

| # | Page | Gutenberg reads | Model-proposed print reading | Context (Gutenberg) |
|---|---|---|---|---|
| 1 | 21 | `=` | `≡` | `c'α=1.≡.Nc'α=Nc'1'x.【=】.αε1Dem.⊢.*100.31.32` |
| 2 | 27 | `1` | `I` | `guousconstant,suchas【1】orΛorsg,R(x,y)isatyp` |
| 3 | 30 | `:.` | `≡` | `1]*102.5.⊢:μεNCβ(α).【:.】.(∃δ).μ=Nc(αβ)'δ[*10` |
| 4 | 30 | `*` | `.` | `εNCα(α)(1)⊢.(1).*102【*】5.⊃⊢.Prop*102.54.⊢:δ` |
| 5 | 30 | `*` | `.` | `*100.22.*71.41.(*102【*】01)]Inusingpropositi` |
| 6 | 35 | *(nothing)* | `s` | `oreasonshypothetical【】concerningtypesareof` |
| 7 | 37 | `α` | `ᵃ` | `member.*103.301.⊢.NC【α】(α)=N0C(α)*103.34.⊢.` |
| 8 | 43 | `-` | `.` | `'α.β⊂t'α[*63.5.(*104【-】01)]*104.101.⊢:βεN1c` |
| 9 | 44 | `1` | *(nothing)* | `≡.(∃α).μ=N1c'α[*100.【1】22.*71.41.(*104.02)]` |
| 10 | 61 | *(nothing)* | `0` | `t01'αDfetc.*106.02.N【】1c'α=Nc'α∩t't01'αDfe` |
| 11 | 61 | *(nothing)* | `0` | `efined.*106.12.⊢:βεN【】1c'α.≡.βεNc'α.βεt't0` |
| 12 | 61 | *(nothing)* | `ε` | `:βεN01c'α.≡.βεNc'α.β【】t't01'α.≡.βsmα.βεt't` |
| 13 | 65 | `ᗡ"` | `Rl` | `εᗡ'R.[*13.14]⊃.ᗡ'R≠【ᗡ"】'(α↑α)(1)⊢.(1).*22.4` |
| 14 | 73 | *(nothing)* | `ex` | `.S⊂sm.⊃.Crp(S)"λεCls【】2excl.ConsequentlyMu` |
| 15 | 91 | `ᗡ"` | `Rl` | `εκsmsmλ.⊃.Tε↾λεκsmλ∩【ᗡ"】'sm[*111.11.111]Thet` |
| 16 | 94 | `ex` | *(nothing)* | `*111.3.⊢:λεCls【ex】2excl.⊃.s"D"εΔ'αsm"λ` |
| 17 | 96 | `ᗡ"` | `Rl` | `κ,λεCls2excl.∃!κsmλ∩【ᗡ"】'sm.⊃.s'κsms'λ[*111.` |
| 18 | 102 | `Λ` | `λ` | `calsum.*112.303.⊢:κ∩【Λ】=Λ.⊃.Σ'κ∩Σ'λ=ΛDem.⊢.` |
| 19 | 106 | `y` | `γ` | `embers.*113.127.⊢:R↾【y】εαsmγ.S↾δεβsmδ.⊃.(R‖` |
| 20 | 112 | `3` | `1` | `s'D"μ.β=s'ᗡ"μ(1)⊢.*1【3】3.101.143.⊃⊢:.Hp.Pεμ` |
| 21 | 119 | `⊃` | `β` | `.⊃⊢:∃!×α'β∩×α'γ.⊃.∃!【⊃】∩γ(1)⊢.(1).*84.11.⊃⊢` |
| 22 | 125 | `λ` | `Λ` | `zero.*114.301.⊢:κ∩λ=【λ】.⊃.εΔ'(κ∪λ)smεΔ'κ×εΔ` |
| 23 | 131 | `4` | `1` | `⊢.*43.122.*71.166.*1【4】4.601.602.⊃⊢:Hp.⊃.Pε` |
| 24 | 149 | `*` | `.` | `⊃.μν=Λ[*116.203]*116【*】21.⊢:.μ,νεNC.⊃:ξεμν.` |
| 25 | 150 | `1` | `3` | `2).(3).⊃⊢.Prop*116.3【1】1.⊢:μεNC-1'Λ.⊃.1μ=1D` |
| 26 | 154 | `"` | *(nothing)* | `.⊃α.M'αεαsmγ:T=s'M"κ【"】:⊃.T"γsmsmκ↓,,"γ.T"γ` |
| 27 | 157 | *(nothing)* | `)` | `γsmεΔ'(α↓,,"β∪α↓,,"γ【】.[*116.14.*113.13]⊃.` |
| 28 | 160 | `ω` | `w` | `εγ.∃!D'M'z∩D'M'w.⊃z,【ω】.z=w:zεγ.⊃z.M'zε1→1.` |
| 29 | 166 | `ν` | `v` | `κ.⊃:∃!(M'w)"εΔ'κ∩(M'【ν】)"εΔ'κ.⊃.w=vDem.⊢.*1` |
| 30 | 167 | `k` | `κ` | `κ.∃!s'κ.⊃.εΔ'(expγ)"【k】sm(εΔ'κ)expγ(2)⊢.*53` |
| 31 | 182 | `O` | `0` | `:[*117.581.591]⊃:δ≠【O】.⊃.αδ≥21.[*116.321.*` |
| 32 | 185 | *(nothing)* | `,or` | `atedclassesW'κandW'λ【】wherewearegivencorre` |
| 33 | 196 | *(nothing)* | `R.` | `⊃.(∃R).Rε1(ξ)→1.α⊂ᗡ'【】R"α=R"α.[*73.12]⊃.(∃` |
| 34 | 200 | *(nothing)* | `×` | `]*118.47.⊢:π≠0.⊃.(μ【】cν)πξ=[(μ×cν)ξπ]ξ[Pr` |
| 35 | 209 | `1` | *(nothing)* | `soisα+cβ(*120.45.450【1】),andifα+cβisaninduc` |
| 36 | 209 | `*120` | *(nothing)* | `ecardinalsorΛ(*120.5【*120】.52),whileconversely` |
| 37 | 212 | `i` | `I` | `.∃!α.⊃.sm"αεNCinduct【i】.e.acardinalwhichisn` |
| 38 | 213 | *(nothing)* | `1` | `.⊃:Nc'(η∪1'y)=Nc'η+c【】[(*110.03)]=N0c'η+c1` |
| 39 | 213 | `p` | `ρ` | `0.511.⊃⊢:Hp.⊃.sm"Nc'【p】=N0c'ρ.[*120.15]⊃.N0` |
| 40 | 214 | `μ` | `η` | `sinduct.⊃:.ηεμ.⊃η,y.【μ】∪1'yεμ:Λεμ:⊃.ρεμ(1)⊢` |
| 41 | 214 | `μ` | `η` | `5.Insteadofηεμ.⊃η,y.【μ】∪1'yεμ,intheabovepro` |
| 42 | 214 | `*` | `.` | `*90.172.*120.25]*120【*】26.⊢:.ρεClsinduct:φη` |
| 43 | 228 | `p` | `ρ` | `]⊃:(∃γ,ρ,σ,ξ,x).N0c'【p】=α.N0c'σ=γ.ξsmρ.xεσ-` |
| 44 | 228 | `p` | `ρ` | `.1]⊃:(∃γ,ρ,σ,ξ).N0c'【p】=α.N0c'σ=γ.ξsmρ.ξ⊂σ.` |
| 45 | 235 | `l` | `1` | `.⊃.P1⊂P*121.31.⊢:Pε(【l】→Cls)∪(Cls→1).Ppo⊂J.` |
| 46 | 235 | *(nothing)* | `i` | `for(Pμ)ν,which=Pμxcν【】nthesamecircumstance` |
| 47 | 236 | `*121` | *(nothing)* | `propositions(*121.7-【*121】.72)onR'x,ofwhichthe` |
| 48 | 236 | `*` | `.` | `'B'P)[(*121.04)]*121【*】131.⊢:E!Pν-c1'B'P.⊃.` |
| 49 | 237 | `*` | `.` | `y=P(x-y)∪1'x∪1'y*121【*】25.⊢.Ppo(x-y)=P(x-y)` |
| 50 | 237 | `*` | `.` | `x-y)[*121.2.201]*121【*】21.⊢:xPpoy.≡.yεP(x⊣y` |
| 51 | 238 | `1` | `I` | `:⊃⊢.Prop*121.3.⊢.P0⊂【1】↾C'PDem.⊢.*121.11.⊃⊢` |
| 52 | 244 | *(nothing)* | `)` | `herR(z↦z)=1'zorR(z↦z【】=Λ.ButwhenzRpoz,itis` |
| 53 | 251 | `*` | `.` | `.(3).(2).⊃⊢.Prop*121【*】64.⊢:PεCls→1.Ppo⊂J.ν` |
| 54 | 264 | `*` | `.` | `*122【*】442.⊢:Hp*122.44.⊃.P=` |
| 55 | 264 | `*` | `.` | `α∩Rpo'y∩Rpo'z):[*122【*】28.Transp]⊃:(∃y).yεR` |
| 56 | 265 | *(nothing)* | `ε` | `∼εClsinduct.⊃.D'R-α∼【】Clsinduct(1)⊢.(1).*1` |
| 57 | 268 | `3` | `2` | `∩t3'xεℵ0whence,by*12【3】.36,*123.27.⊢:∃!ℵ0(x` |
| 58 | 269 | `0` | `3` | `3'x)Alsowehave,by*12【0】.322above,∃!ℵ0.⊃.ℵ0ε` |
| 59 | 274 | `*` | `.` | `+cℵ0=2×cℵ0Dem.⊢.*123【*】42.⊃⊢:αεℵ0.⊃.(∃β,γ).` |
| 60 | 277 | `O` | `0` | `3.53.⊢:νεNCinduct-1'【O】.⊃.ℵ0ν=ℵ0[*123.52.*1` |
| 61 | 284 | `*` | `.` | `*100.43]⊃μ,ν.μ=ν[*71【*】55]⊃:(∩Cl'ρ)↾NCinduc` |
| 62 | 284 | *(nothing)* | `ex` | `l'ρ)"NCinductεℵ0∩Cls【】2excl[*124.51.15.*12` |
| 63 | 285 | `p` | `ρ` | `Nc'(∩Cl'ρ)"NCinduct.【p】∼εClsinduct.[*124.51` |
| 64 | 285 | `ν` | *(nothing)* | `0.2]⊃.αεClsinduct.αε【ν】Cl'ρ.(3)⊢.(2).(3).⊃⊢` |
| 65 | 285 | *(nothing)* | `)` | `-s'Rpo'γ)∩(δ-s'Rpo'δ【】=Λ(3)Similarly⊢:.Hp.` |
| 66 | 286 | `*` | `.` | `γ.s'Rpo'β⊂s'R'γ:[*22【*】81]⊃:(∃β).γRpoβ.∃!β-` |
| 67 | 291 | `-` | *(nothing)* | `.*63.102.⊃⊢:∃!(1→1)∩【-】D't'x-ᗡ't'x.≡.(∃R).R` |
| 68 | 292 | *(nothing)* | `ε` | `⊃⊢.Prop*125.35.⊢:.ℵ0【】NCmult.⊃:∃!ℵ0(x).≡.I` |
| 69 | 294 | `*116` | *(nothing)* | `4,*113.04.05,*116.03【*116】.04,*117.02.03,` |
| 70 | 307 | `y` | `γ` | `alogueof(P\|Q)"γ=P"Q"【y】(*37.33),isveryoften` |
| 71 | 312 | *(nothing)* | `43` | `!S'Q.≡.∃!QDem.⊢.*37.【】.*150.22.⊃⊢:.Hp.⊃:∃!` |
| 72 | 315 | `5` | `8` | `Q.⊃.S'(P\|Q)εPot'S'Q(【5】)⊢.(1).(8).*91.373fr` |
| 73 | 322 | *(nothing)* | `(3)` | `T'R[*150.13]=(S\|T)'R【】⊢.(1).(2).(3).*151.1` |
| 74 | 323 | `l` | `1` | `'QεPsmorQ.⊃.S↾C'Qε1→【l】.P=S'Q(2)⊢.*151.11.⊃` |
| 75 | 332 | `P` | `R` | `Rεsmor"μ.≡.(∃Q).Qεμ.【P】smorQ(1)⊢.*152.5.⊃⊢:` |
| 76 | 337 | `1` | `4` | `ldbecontrastedwith*5【1】.411.*153.24.⊢.2r=Nr` |
| 77 | 345 | `=` | `≡` | `Df*155.11.⊢:QεN0r'P.【=】.QsmorP.Qεt'P.≡.QεNr` |
| 78 | 353 | `*` | `.` | `s'P⨣"λ[Proofasin*160【*】41]*160.412.⊢:∃!λ.∃!` |
| 79 | 353 | `*` | `.` | `[*33.265.*160.1]*160【*】34.⊢:R⊂S.⊃.Q⨣R⊂Q⨣S[*` |
| 80 | 354 | `-` | `=` | `.*150.22.⊃⊢:Hp.⊃.C'P【-】S"C'P'.C'Q=S"C'Q'.[H` |
| 81 | 361 | *(nothing)* | `⊢` | `xSy(1)⊢.(1).*150.1.⊃【】:.Hp.⊃:uS↾(-1'y)'Qv.` |
| 82 | 363 | `=` | `≡` | `]*162.14.⊢:.x(Σ'P)y.【=】:(∃Q).QFP.xQy.∨.(∃Q,` |
| 83 | 377 | `*` | `.` | `'PsmorΣ'Q.PsmorQ*164【*】18.⊢:S↾C'Σ'QεPsmorsm` |
| 84 | 386 | *(nothing)* | `as` | `nrelation-arithmetic【】α↓,,"βhasincardinala` |
| 85 | 395 | `*` | `.` | `rsmorP↓.,'Q(2)⊢.*165【*】242.⊃⊢:P=Λ.∃!Q.⊃.P↓.` |
| 86 | 397 | `=` | `≡` | `.1]*166.13.⊢:.P×Q=Λ.【=】:P=Λ.∨.Q=Λ[*166.12.*` |
| 87 | 402 | `(` | *(nothing)* | `⨣P↓.,y.[*166.52]⊃.Σ'【(】P↓.,'(Q↦y)=Σ'P↓.,'Q⨣` |
| 88 | 416 | `y` | `γ` | `γ,δ).γ,δεCl'ᗡ'S.α=S"【y】.β=S"δ.∃!γ-δ-Q"(δ-γ)` |
| 89 | 424 | *(nothing)* | `⊃.` | `.15.⊢:β⊂C'P.zεC'P-β.【】(β∪1'z)PdfβDem.⊢.*51` |
| 90 | 425 | `1` | `2` | `'P.α≠C'P.⊃.αεᗡ'Pdf(【1】)⊢.(1).(2).⊃⊢:αεCl'C` |
| 91 | 436 | `P` | `R` | `P↦Z)Q.R≠Q.⊃R.M'R=N'【P】:.[*51.239.(3).*161.` |
| 92 | 442 | *(nothing)* | `or` | `42.421]*172.44.⊢:Psm【】smorQ.⊃.Π'PsmorΠ'Q[*` |
| 93 | 463 | `.w↓y'` | *(nothing)* | `xPx':y'Qy.y'≠y.w↓y'【.w↓y'】εμ.⊃y',w.w↓y'εν:.[*5` |
| 94 | 463 | *(nothing)* | `)` | `80.3]≡:.S,Tε(C'P↑C'Q【】Δ'C'Q:.(∃y):yεC'Q.(S` |
| 95 | 464 | `P` | `R` | `smorS.⊃.(PexpQ)smor(【P】expS).PQsmorRS[*176.` |
| 96 | 464 | `P` | `R` | `l∩Nr'Q.C'R⊂Nr'P.⊃.Π'【P】smor(PexpQ)[*165.38.` |
| 97 | 470 | `P` | `R` | `⊢:.P=Λ.∨.Q=Λ:⊃.Pexp(【P】×Q)=Λ(2)⊢.(1).(2).*1` |
| 98 | 478 | `P` | `Q` | `Prop*180.12.⊢.↓(Λ∩C'【P】)'1'PsmorP.(Λ∩C'P)↓'` |
| 99 | 478 | `1` | *(nothing)* | `Q)"1"C'P.C'(Λ∩C'P)↓'【1】1'Q=(Λ∩C'P)↓"1"C'Q[*` |
| 100 | 479 | `⊃` | `'` | `*180.151.⊢:.C'P∩C【⊃】Q=Λ.⊃:Zsmor(P⨣Q).≡.(` |
| 101 | 481 | *(nothing)* | `)` | `μ=Nr'P.ν=Nr'Q.C"(μ+ν【】=C"Nr'P+cC"Nr'Q.[*13` |
| 102 | 484 | `*` | `.` | `[*181.2.*155.26]*181【*】22.⊢.N0r'P+1=Nr'(P↦x` |
| 103 | 487 | *(nothing)* | `.In` | `umbersofmembersofC'P【】thenextnumber,weshal` |
| 104 | 502 | *(nothing)* | `⊃.` | `⊃⊢:νεNR.C'P⊂ν.SεC'P.【】ν=Nr'S.C'P⊂Nr'S(2)⊢.` |
| 105 | 508 | `)` | *(nothing)* | `r(π×ν)=(μexprν)exprπ【)】Dem.⊢.*186.111.*184.` |
| 106 | 509 | `O` | `0` | `11.*181.4.⊃⊢:∼(α,βεN【O】R).⊃.αexpr(β+1)=Λ.(α` |
| 107 | 524 | `or` | *(nothing)* | `cingthehypothesis∃!α【or】inproofsinwhichitisn` |
| 108 | 528 | `*` | `.` | `∩trans[Proofasin*200【*】22]*201.3.⊢.ΛεtransD` |
| 109 | 537 | `1` | `l` | `202.161.⊢:Pεconnex∩R【1】'J.⊃.P↾C'Pε1→1.P↾C'P` |
| 110 | 546 | *(nothing)* | `or` | `P,smor,Q.⊃.(P↾S"β)sm【】Q↾βDem.⊢.*202.8.⊃⊢:H` |
| 111 | 552 | `r` | *(nothing)* | `!B'Q.⊃:PsmorQ.≡.P↾ᗡ'【r】PsmorQ↾ᗡ'QDem.⊢.*151` |
| 112 | 556 | *(nothing)* | `1` | `'PεconnexDem.⊢.*172.【】1.*33.45.Transp.⊃⊢::` |
| 113 | 563 | `)` | *(nothing)* | `.*37.105.⊃⊢:Hp.⊃.x∼ε【)】P"(1'x∪1'y).yεP"(1'x` |
| 114 | 572 | `α` | *(nothing)* | `rop*205.66.⊢:Pεtrans【α】∩connex.E!minP'α.⊃.p` |
| 115 | 572 | `α` | *(nothing)* | `rop*205.65.⊢:Pεtrans【α】∩connex.E!minP'α.⊃.p` |
| 116 | 579 | `*206` | *(nothing)* | `propositions(*206.3-【*206】.38)onthesequentofP"` |
| 117 | 586 | *(nothing)* | `∼` | `)⊢.*206.34.⊃⊢:.Hp.⊃:【】E!seqP'P"α.⊃.∼E!maxP` |
| 118 | 598 | `*` | `.` | `=Λ(2)⊢.*205.193.*207【*】12.⊃⊢:Hp.maxP'α=Λ.⊃.` |
| 119 | 600 | `1` | `l` | `⊃⊢.Prop*207.35.⊢:PεR【1】'J∩connex.⊃.D'ltP=C'` |
| 120 | 616 | *(nothing)* | `∩` | `λ).λε(ᗡ'maxQ∪ᗡ'seqQ)【】(ᗡ'minQ∪ᗡ'precQ)Thus` |
| 121 | 616 | *(nothing)* | `εκ` | `3.⊢:Hp*210.2.λ⊂κ.p'λ【】-λ.⊃.p'λ=precQ'λ=tlQ` |
| 122 | 621 | `⊃` | `⊂` | `0.2:λ⊂κ.⊃λ.s'λεκ:⊃:λ【⊃】κ.⊃.s'λε(maxQ'λ∪seqQ` |
| 123 | 632 | `I` | `1` | `Ser.QεD'P↾.C'P-C'Q∼ε【I】.⊃:C'Qεsect'P.≡.(∃R)` |
| 124 | 635 | `ε` | `E` | `x).xεC'P.α=P'x∪1'x.∼【ε】!P1'x:.⊃⊢.Prop*211.3` |
| 125 | 639 | `*` | `.` | `xP'α.∨.E!seqP'α.*211【*】54.⊢:.P⊂J:∃!maxP'α.⊃` |
| 126 | 639 | `⊃` | *(nothing)* | `'P"β.[*40.682]⊃.β⊂P"【⊃】α(1)⊢.(1).*24.55.⊃⊢.` |
| 127 | 647 | `ᗡ"` | `Rl` | `11.74]*211.756.⊢:.Pε【ᗡ"】'J∩connex.α⊂C'P.Q=P.` |
| 128 | 650 | *(nothing)* | `⊂` | `sect'(P⨣Q).α⊂C'P.≡.α【】C'P.P"α⊂α.[*211.1]≡.` |
| 129 | 650 | `*` | `.` | `ect'Q-1'Λ.C'P⊂α.[*22【*】92]≡.αε(C'P∪)"(sect'` |
| 130 | 654 | `ᗡ"` | `Rl` | `212.122.⊢.s'P,sgm'Pε【ᗡ"】'J[*170.17]*212.123.` |
| 131 | 658 | `1` | `I` | `sect'P,D'Pε,orD'(Pε∩【1】),andtheQisreplacedb` |
| 132 | 670 | `D` | `⊃` | `122.⊢:PpoεSer.∃!B'P.【D】.B'(s'P)↾(-1'Λ)=1'B'` |
| 133 | 674 | *(nothing)* | `-` | `P=Λ.⊃.C'Ps=P↾"sect'P【】1'ΛDem.⊢.*213.156.⊃⊢` |
| 134 | 676 | `P` | `R` | `Hp.⊃:αεsect'R.⊃.α⊂C'【P】.α⊂C'P.(P↾β)"α⊂α(3)⊢` |
| 135 | 677 | `P` | `R` | `ct'P.γεsect'R.Q=P↾α=【P】↾γ.⊃.α=γ(2)⊢.(1).(2)` |
| 136 | 681 | `R` | *(nothing)* | `'Q-1'Λ).S=(P⨣Q)↾β.≡:【R】(∃β).βε(C'P∪)"(sect'` |
| 137 | 702 | *(nothing)* | `P` | `p*216.14.⊢:PεSer.⊃.δ【】2'α⊂δP'αDem.⊢.*71.47` |
| 138 | 707 | `ε` | `E` | `2]≡.(∃κ).κ⊂P"α.∃!κ.∼【ε】!max(s'P)'κ.γ=s'κ.[*` |
| 139 | 724 | `k` | `κ` | `⊃⊢.Prop*230.321.⊢:∃!【k】.⊃.RQcn(p'κ)=p'RQcn"` |
| 140 | 730 | `P` | `R` | `2)⊢.(1).(2).⊃⊢:Hp.yε【P】Qcn(P'x).zεC'Q∩ᗡ'R.⊃` |
| 141 | 735 | `e` | *(nothing)* | `scQ).limaxP'(PRscQ)∼【e】εD'P1.⊃.limaxP'(PRsc` |
| 142 | 738 | *(nothing)* | `)sc` | `RQ)sc'Q"(α∩ᗡ'R).(PRQ【】'α=(PRQ)sc'Q"(α∩ᗡ'R)` |
| 143 | 746 | `e` | `s` | `rational【e】foritsarguments,this` |
| 144 | 750 | `ᗡ"` | `Rl` | `01.101]*233.421.⊢:Pε【ᗡ"】'J∩trans.Qεtrans∩con` |
| 145 | 758 | `ο` | `o` | `n(Ppο'w):≡:xεC'P:xPp【ο】w.⊃w.(∃y).yεC'Q∩ᗡ'R.` |
| 146 | 761 | `ε` | `⊃` | `.*22.41]⊃.P'x=PRscQ:【ε】⊢.Prop*234.162.⊢:Ppo` |
| 147 | 765 | `P` | `R` | `202.⊃⊢:Hp.⊃.os(P,Q)'【P】ε1∪2(1)⊢.(1).*234.24` |

**Follow-up rows (judged 2026-10-08).** Comparing the 17 pages affected by the renderer fix again (section 4)
exposed 6 reader-agreed hunks that had never been judged, and the set-aside p. 497 row hid a seventh possible
slip. Both judges ran on all 7. They both picked the print on these 2, which are kept and numbered after the
others; the other 5 are in section 5. Like every row here, both await human review.

| # | Page | Gutenberg reads | Model-proposed print reading | Context (Gutenberg) |
|---|---|---|---|---|
| 148 | 191 | `⊢` | `⊣` | `ndlessthany,whileP(x【⊢】y)willbethesenumbers` |
| 149 | 225 | `*` | `.` | `26]⊃.Nc'ρ<Nc'σ:[*100【*】321]⊃:ρsmξ.ρ⊂σ.∃!σ-ρ` |

## 4. Set aside: classified as comparison artefacts (68 rows)

These rows passed both judges but were classified as artefacts of the comparison, not differences in the
text. They are listed so that the split can be checked, and like every row here they await human review. The
rules are in [`scripts/vol2_split_artefacts.py`](../scripts/vol2_split_artefacts.py), and each row in the
private data carries its own reason. Two classes rest on a deterministic check rather than a model's
judgement. The LaTeX rows are set aside because the difference disappears when the page is compared again
with the fixed renderer. The notation rows are set aside because the two spans are known spellings of the
same glyph. The page-marker rule is a text-similarity test, and 3 page-marker rows were decided from the
page images by Claude.

- **Page-marker placement (51 rows).** The comparison works page by page, using Gutenberg's `[Pg N]` markers.
  Where a marker sits one line or proposition early or late, the same text shows up as "missing" on one page
  and "extra" on the next. Rule: whole text present on one side only, at the very start or end of a page,
  and found again (similarity ≥ 0.85) at the end of the previous page's reading or the start of the next
  page's Gutenberg text. 48 rows meet this rule. The other 3 (pp. 3, 308, 497) were decided by Claude looking at
  the page images. The p. 497 row also contains Gutenberg's `*183-26` with a hyphen where the readers have
  ✱183·26 with a centred dot. That separate possible slip was judged on its own on 2026-10-08 and set aside (section 5).
- **LaTeX left in the comparison stream (10 rows).** A bug in the comparator's HTML rendering let a `<`
  inside a formula swallow text up to the next `>`, leaving fragments such as `[beginalign`, `[l` and
  `upharpoonright`, or stray brackets. When the pages are compared again with the fixed renderer, these 10
  differences disappear (a deterministic check, not a judgement). This is the
  same artefact class as the two "infty" rows dropped earlier.
- **Small-capital typography (1 row).** "Vol. IV" printed in small capitals, read as "iv"; the same case on
  p. 753 was already set aside.
- **Notation representation (6 rows, added after the second review).** The same printed glyph is written two
  ways, Gutenberg's notation on one side and the readers' Unicode on the other. These are not text
  differences:
  - pp. 482, 483: Gutenberg's `\unicode{x21f7}` (⇷, a leftward arrow with a stroke), which the normalizer maps
    to ↦, vs the readers' ←+;
  - pp. 488, 489: Gutenberg's ʻʻ double inverted comma (normalized to `''`) vs the readers' `"`;
  - p. 429: Gutenberg's `↓_{.,}` subscript dots vs the readers' combining diaeresis below;
  - p. 458: a dotted operator (Gutenberg `\dot{s}`), where the normalizer strips the dot above but not the
    readers' diaeresis. Dotted operators are a set-aside class.

  The rule is `notation()` in [`scripts/normalize.py`](../scripts/normalize.py). It is not yet part of
  `blind()`, so the Vol I counts are unchanged until that comparison is re-run; the Vol III artefact review
  applies it (METHODOLOGY §4.6).

| Page | Class | Side | Span (normalized, truncated) |
|---|---|---|---|
| 3 | page-marker placement | Gutenberg only | `PARTIII.CARDINALARITHMETIC.` |
| 6 | page-marker placement | print only | `"NCβ(α)."` |
| 9 | page-marker placement | print only | `N3C(t3'α)etc.` |
| 43 | page-marker placement | Gutenberg only | `*104.2.⊢."αεN1c'α` |
| 44 | page-marker placement | Gutenberg only | `*104.112.⊢.N2c'α=Nc(t2'α)'α=Nc(t2'α)α'…` |
| 56 | page-marker placement | Gutenberg only | `*105.317.⊢:∃!N2c'α.N2c'α=N2c'β.⊃.N0c'α…` |
| 59 | page-marker placement | Gutenberg only | `*105.42.⊢:N1c'α=Λ.⊃.N2c'α=Λ[*105.41]` |
| 61 | page-marker placement | Gutenberg only | `*106.4.41.411.⊢:μ=N0c'α.⊃.μ(00)=N00c'α…` |
| 65 | page-marker placement | Gutenberg only | `*106.44.⊢:μ,νεN00C.t'μ=t'ν.⊃.(∃γ,δ).γε…` |
| 73 | page-marker placement | Gutenberg only | `κ1smλ1.κ2smλ2.etc.` |
| 88 | page-marker placement | print only | `λ.IfwewriteS` |
| 89 | page-marker placement | Gutenberg only | `λ.IfwewriteS` |
| 109 | page-marker placement | Gutenberg only | `*113.104.⊢.E!α↓,,'y[*38.12]` |
| 111 | page-marker placement | Gutenberg only | `Dem.⊢.*55.261.*2.02.⊃⊢:yεβ.⊃.D"α↓,,y=1…` |
| 133 | page-marker placement | print only | `Theaboveisoneofthetwovariantsoftheasso…` |
| 139 | page-marker placement | Gutenberg only | `*115.25.⊢:κεCls3arithm.⊃.εΔ'κ⊂1→1.εΔ's…` |
| 153 | page-marker placement | Gutenberg only | `thenumbersofthecolumns,isequalto` |
| 172 | page-marker placement | Gutenberg only | `*117.24.⊢:μ≥ν.≡.(∃α,β).μ=N0c'α.ν=N0c'β…` |
| 177 | comparator artefact (LaTeX left in the stream) | Gutenberg only | `[beginalign` |
| 179 | comparator artefact (LaTeX left in the stream) | Gutenberg only | `(` |
| 190 | page-marker placement | Gutenberg only | `suffice,sofarasweknow,to` |
| 191 | comparator artefact (LaTeX left in the stream) | both | `upharpoonright` |
| 191 | small-capital typography | both | `IV` |
| 195 | page-marker placement | Gutenberg only | `*118.24.⊢:νεNC.⊃.(μ+cν)ξ=(μ+csmξ"ν)ξ` |
| 207 | page-marker placement | print only | `*120.21.⊢:ρεClsinduct.≡.N0c'ρεNCinduct` |
| 210 | page-marker placement | Gutenberg only | `κ)onthesubjectofεΔ'κ.` |
| 225 | comparator artefact (LaTeX left in the stream) | Gutenberg only | `[l` |
| 227 | comparator artefact (LaTeX left in the stream) | Gutenberg only | `[l` |
| 227 | comparator artefact (LaTeX left in the stream) | Gutenberg only | `[l` |
| 227 | comparator artefact (LaTeX left in the stream) | print only | `<(Nc'σ)Nc'ξ` |
| 237 | page-marker placement | Gutenberg only | `*121.201.⊢:∼(yPpoy).⊃.y∼εP(x-y)` |
| 238 | page-marker placement | Gutenberg only | `*121.271.⊢:∼(ν,ν+c1εNC-1'Λ).⊃.Pν=Λ[*12…` |
| 256 | page-marker placement | Gutenberg only | `Inadditiontothepropositionsalreadyment…` |
| 281 | page-marker placement | Gutenberg only | `*124.13.⊢:ρεClsrefl.⊃.∃!ℵ0∩Cl'ρ[*124.1…` |
| 283 | comparator artefact (LaTeX left in the stream) | Gutenberg only | `(` |
| 283 | comparator artefact (LaTeX left in the stream) | Gutenberg only | `[beginalign` |
| 283 | comparator artefact (LaTeX left in the stream) | Gutenberg only | `)` |
| 290 | page-marker placement | print only | `*125.2.⊢:.Infinax(x).≡:αεNCinduct.⊃α.∃…` |
| 306 | page-marker placement | print only | `We` |
| 307 | page-marker placement | Gutenberg only | `We` |
| 308 | page-marker placement | Gutenberg only | `sinceitisverifiedwhenSisacorrelatorofS…` |
| 332 | page-marker placement | Gutenberg only | `*152.43.⊢.NRεCls2excl[*152.42]` |
| 337 | page-marker placement | Gutenberg only | `*153.212.⊢.C"2r=2[*55.15.*56.11.*54.101]` |
| 345 | page-marker placement | Gutenberg only | `*155.22.⊢:μεN0R.⊃.∃!μ` |
| 346 | page-marker placement | Gutenberg only | `*155.41.⊢.smor"N0r'P∩t'Q=Nr(Q)'P` |
| 349 | page-marker placement | print only | `analogoustothoseof` |
| 372 | page-marker placement | Gutenberg only | `*163.16.⊢:PεRel2excl.⊃.C"C'PεCls2excl[…` |
| 398 | page-marker placement | Gutenberg only | `Theabovepropositionisusedintheordinalt…` |
| 412 | page-marker placement | Gutenberg only | `generatedbyPlc.` |
| 429 | notation representation | both | `.,` vs combining diaeresis below |
| 444 | page-marker placement | Gutenberg only | `*173.12.⊢.C'Prod'P⊂D"FΔ'C'P[*172.12.*1…` |
| 458 | notation representation | print only | combining diaeresis (dotted operator) |
| 461 | page-marker placement | Gutenberg only | `*176.181.⊢.PQsmor(PexpQ)` |
| 482 | notation representation | both | `↦` (⇷) vs `←+` |
| 483 | notation representation | both | `↦` (⇷) vs `←+` |
| 488 | notation representation | both | `''` (ʻʻ) vs `"` |
| 489 | page-marker placement | Gutenberg only | `NowΣ'↓'P=P∪I↾C'P(*182.413),andΠ'(P∪I↾C…` |
| 489 | notation representation | both | `''` (ʻʻ) vs `"` |
| 490 | page-marker placement | Gutenberg only | `*182.05.⊢.↓.,'Q=↓Q'Q=Q↓.,Q[*182.021.*1…` |
| 497 | page-marker placement | Gutenberg only | `25.⊢.ΣNr'P↓.,'Q=Nr'(Q×P)*183-` |
| 526 | page-marker placement | Gutenberg only | `Wehaveaseriesofpropositions(*201.5-.56…` |
| 563 | page-marker placement | Gutenberg only | `*205.123.⊢:maxP'α=Λ.≡.α∩C'P⊂P"α` |
| 565 | page-marker placement | Gutenberg only | `*205.195.⊢:xmaxPα.⊃.∼(xPx)` |
| 578 | page-marker placement | Gutenberg only | `*206.14.⊢:α∩C'P=Λ.⊃.seqP'α=B'P` |
| 597 | page-marker placement | Gutenberg only | `*207.12.⊢:maxP'α=Λ.⊃.ltP'α=seqP'α[*207…` |
| 613 | page-marker placement | Gutenberg only | `D'(Pε∩I).` |
| 702 | page-marker placement | Gutenberg only | `*216.1.⊢:xεδp'α.≡.(∃β).β⊂α∩C'P.∃!β.xlt…` |
| 750 | page-marker placement | Gutenberg only | `Dem.⊢.*232.352.⊃⊢:Hp.xε(PRQ)sc'α.⊃.x=(…` |

## 5. Set aside: follow-up rows rejected by the judges (5 rows)

Of the 7 follow-up rows (see the end of section 3), these 5 were set aside because the two judges did not
both pick the print. Each row in the private data records both picks, the A/B order, the date and a reason.
Like every row here, they await human review.

| Page | What differs | Picks | Reason set aside |
|---|---|---|---|
| 179 | the printer's signature mark `12-2`, print only | Opus Gutenberg, Codex neither | signature marks are omitted by Gutenberg on purpose |
| 227 | the printer's signature mark `15-2`, print only | both Gutenberg | signature marks are omitted by Gutenberg on purpose |
| 275 | a paragraph at the page edge, plus the signature mark `18-2` (print only) | both Gutenberg | Gutenberg places the paragraph at the top of p. 276 |
| 558 | a `<br>` left in Gutenberg's TeX | Opus print, Codex neither | only one judge picked the print |
| 497 | Gutenberg's `*183-26` (hyphen) where the readers have ✱183·26 | Opus print, Codex neither | only one judge picked the print (Codex saw the centred dot but did not accept "." for it) |
