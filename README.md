# DIC4: AI SOC Analyst Agent — IEEE Conference Paper & OpenSpec Repository

> **Project**: AI SOC Analyst Agent: A Spec-Driven Multi-Tier System Orchestrating Machine Learning Triage, MITRE ATT&CK Reasoning, and Bounded LLM Planning  
> **Related Project (DIC3)**: [DIC3-AI-SOC-Agent](https://github.com/g115064011-arch/DIC3-AI-SOC-Agent.git)  
> **Repository (DIC4)**: [DIC4](https://github.com/g115064011-arch/DIC4.git)  
> **Group 16**: 蘇恩平 (En-Ping Su)、周妤 (Yu Chou)、袁靖淇 (Ching-Chi Yuan)、蕭宥瑄 (Yu-Hsuan Hsiao)  
> **Updated**: 2026-11-25  

---

## Executive Summary

This repository contains the complete **DIC4** deliverables for an IEEE Conference Paper built upon the DIC3 **AI SOC Analyst Agent** research project:

1. **Two Genuine LaTeX-Compiled IEEEtran Conference PDFs** (`\documentclass[conference]{IEEEtran}`, compiled with Tectonic 0.17.0 / XeTeX):
   - **[`DIC4_Good_Final_IEEE_Conference.pdf`](DIC4_Good_Final_IEEE_Conference.pdf)**: Proofread, submission-ready IEEE double-column conference paper with zero `Overfull \hbox` warnings, zero undefined citations/references, properly broken multi-line equations, and `booktabs` tables fitted within column width.
   - **[`DIC4_Bad_Draft_Erroneous.pdf`](DIC4_Bad_Draft_Erroneous.pdf)**: Unproofread draft generated purely from modified LaTeX source code, exhibiting natural typesetting defects (column text overflow, oversized figure, table overflow, `[?]` undefined citations, `Fig. ??` undefined reference, typos, and unescaped `%` syntax truncation) without any artificial error boxes or annotations.
2. **Modular LaTeX Source Projects** (`paper_good/` and `paper_bad/`): Split into per-section `.tex` files (`sections/00_abstract.tex` through `sections/08_conclusion.tex`) assembled via `\input{}` in `main.tex`, accompanied by `references.bib` (18 verified references), `fig1_architecture.png`, and compilation logs (`main.log`).
3. **Standalone Academic Chapters** (`deliverables/`):
   - [`deliverables/Abstract.md`](deliverables/Abstract.md)
   - [`deliverables/Introduction.md`](deliverables/Introduction.md)
   - [`deliverables/Related_Work.md`](deliverables/Related_Work.md)
4. **Independent Comparative Error Audit**: [`deliverables/COMPARATIVE_ERROR_AUDIT.md`](deliverables/COMPARATIVE_ERROR_AUDIT.md) documenting every intentional source-level difference between the Good Final and Bad Draft versions.
5. **OpenSpec Spec-Driven Development (SDD) Structure** (`openspec/`): Preserved RFC 2119 specifications and change proposals (`000-abstract` to `006-reference`).
6. **Overleaf Upload Package**: [`DIC4_Paper_Overleaf_Package.zip`](DIC4_Paper_Overleaf_Package.zip) ready for direct upload via Overleaf (`Create a new project -> Existing project (.zip)`).

---

## Good Final vs. Bad Draft Comparison

All differences in `DIC4_Bad_Draft_Erroneous.pdf` originate naturally from LaTeX source code rather than visual callouts. See [`deliverables/COMPARATIVE_ERROR_AUDIT.md`](deliverables/COMPARATIVE_ERROR_AUDIT.md) for the full line-by-line audit.

| Defect Category | Good Final (`paper_good/`) | Bad Draft (`paper_bad/`) |
|---|---|---|
| **Overfull `\hbox` (Text)** | Clean prose; `0` Overfull warnings | Long unbreakable `\texttt{...}` URL in Section I (`257.54pt` overflow) |
| **Formula Formatting** | Multi-line `aligned` environment | Unbroken single-line equation in Section IV (`154.83pt` overflow) |
| **Figure Sizing & Ref** | `\includegraphics[width=\columnwidth]` + `\ref{fig:arch}` -> `Fig. 1` | `\includegraphics[width=1.4\columnwidth]` (`100.80pt` overflow) + `\ref{fig:arch_missing}` -> `Fig. ??` |
| **Table Layout** | Wrapped in `\resizebox{\columnwidth}{!}{...}` | Unconstrained `p{...}` columns in Tables I & II (`49.70pt` / `8.78pt` overflow) |
| **Undefined Citations** | All 18 keys resolved in `references.bib` | Missing keys (`tsegai2026aida_missing`, `wu2026excytin_missing`) -> `[?]` |
| **Typos** | Proofread academic English | Natural misspellings (`alret`, `strageties`, `revelaed`, `hallucianates`, `assymetric`, `evidance`) |
| **LaTeX Syntax** | Properly escaped `\%` | Unescaped `%` in Abstract truncating trailing text |

---

## Repository Structure

```text
DIC4/
├── DIC4_Good_Final_IEEE_Conference.pdf   # Proofread IEEEtran Conference PDF (Good Final)
├── DIC4_Bad_Draft_Erroneous.pdf          # Erroneous IEEEtran Conference PDF (Bad Draft)
├── DIC4_Paper_Overleaf_Package.zip       # Ready-to-upload Overleaf project archive
├── COMPARATIVE_ERROR_AUDIT.md            # Root copy of error audit
├── README.md                             # This file
├── paper_good/                           # Modular LaTeX source (Good Final)
│   ├── main.tex
│   ├── references.bib
│   ├── fig1_architecture.png
│   ├── main.pdf / main.log
│   └── sections/
│       ├── 00_abstract.tex
│       ├── 01_introduction.tex
│       ├── 02_related_work.tex
│       ├── 03_system_architecture.tex
│       ├── 04_methodology.tex
│       ├── 05_experimental_setup.tex
│       ├── 06_results.tex
│       ├── 07_discussion.tex
│       └── 08_conclusion.tex
├── paper_bad/                            # Modular LaTeX source (Bad Draft)
│   ├── main.tex
│   ├── references.bib
│   ├── fig1_architecture.png
│   ├── main.pdf / main.log
│   └── sections/                         # Same 9 section files with natural LaTeX defects
├── deliverables/                         # Final submission bundle
│   ├── DIC4_Good_Final_IEEE_Conference.pdf
│   ├── DIC4_Bad_Draft_Erroneous.pdf
│   ├── DIC4_Good_Final.log
│   ├── DIC4_Bad_Draft.log
│   ├── Abstract.md
│   ├── Introduction.md
│   ├── Related_Work.md
│   └── COMPARATIVE_ERROR_AUDIT.md
├── openspec/                             # OpenSpec SDD specifications and changes
├── src/                                  # AI SOC Analyst Agent implementation
└── docs/                                 # Proposal and supporting documentation
```

---

## Local Compilation (Tectonic)

Both papers can be compiled locally using the bundled Tectonic engine:

```powershell
# Compile Good Final
Set-Location paper_good
..\bin\tectonic.exe --keep-intermediates --keep-logs main.tex

# Compile Bad Draft
Set-Location ..\paper_bad
..\bin\tectonic.exe --keep-intermediates --keep-logs main.tex
```

## Overleaf Deployment

1. Open Overleaf and select **Create a new project -> Existing project (.zip)**.
2. Upload `DIC4_Paper_Overleaf_Package.zip`.
3. Click **Recompile** to build the IEEEtran PDF on Overleaf.
