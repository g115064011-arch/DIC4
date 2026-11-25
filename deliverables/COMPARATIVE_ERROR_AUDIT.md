# COMPARATIVE ERROR AUDIT
## DIC4 — Good Final vs. Bad Draft LaTeX Differences

**Document:** This audit lists all intentional differences between `DIC4_Good_Final_IEEE_Conference.pdf` and `DIC4_Bad_Draft_Erroneous.pdf`.  
**Purpose:** Verification reference for the instructor. This document is **NOT** embedded in either PDF.  
**Generated:** 2026-11-25  

---

## 1. Overfull \hbox — Text Overflow

| # | Location | Good Final | Bad Draft |
|---|----------|-----------|-----------|
| 1 | `sections/01_introduction.tex`, para 1 | No URL in paragraph — normal prose only | Long unbreakable `\texttt{https://soc-telemetry-cluster...}` causes **257.54pt** Overfull overflow into adjacent column |
| 2 | `sections/04_methodology.tex`, equation | Multi-line `aligned` environment with proper `\\` linebreaks | Single-line equation without `aligned` env → **154.83pt** Overfull |

## 2. Figure Errors

| # | Location | Good Final | Bad Draft |
|---|----------|-----------|-----------|
| 3 | `sections/03_system_architecture.tex` | `\includegraphics[width=\columnwidth]` — fits column exactly | `\includegraphics[width=1.4\columnwidth]` — overflows by **100.80pt** |
| 4 | `sections/03_system_architecture.tex` | `\ref{fig:arch}` resolves → "Fig. 1" | `\ref{fig:arch_missing}` undefined → prints **"Fig. ??"** |

## 3. Table Errors

| # | Location | Good Final | Bad Draft |
|---|----------|-----------|-----------|
| 5 | `sections/02_related_work.tex`, Table literature | Wrapped in `\resizebox{\columnwidth}{!}` with `llll` columns | NOT wrapped; wide `p{}` columns → **49.70pt** Overfull |
| 6 | `sections/04_methodology.tex`, Table contracts | Wrapped in `\resizebox{\columnwidth}{!}` | NOT wrapped; wide `p{}` columns → **8.78pt** Overfull |

## 4. Undefined Citation Errors — [?] in PDF

| # | Location | Good Final | Bad Draft |
|---|----------|-----------|-----------|
| 7 | Intro para 2 | `\cite{tsegai2026aida}` — defined | `\cite{tsegai2026aida_missing}` — NOT in bib → **[?]** |
| 8 | Intro para 2 | `\cite{wu2026excytin}` — defined | `\cite{wu2026excytin_missing}` — NOT in bib → **[?]** |
| 9 | Related Work | `\cite{tsegai2026aida}` correct | `\cite{tsegai2026aida_missing}` again → **[?]** |

## 5. Typographic Errors

| # | Location | Good Final | Bad Draft |
|---|----------|-----------|-----------|
| 10 | Abstract | `alert fatigue` | `alret fatigue` |
| 11 | Abstract | `strategies` | `strageties` |
| 12 | Intro | `revealed` | `revelaed` |
| 13 | Intro | `strategies` | `strageties` |
| 14 | Intro | `hallucinates` | `hallucianates` |
| 15 | Intro | `asymmetric` | `assymetric` |
| 16 | Methodology | `evidence` | `evidance` |

## 6. LaTeX Syntax Errors

| # | Location | Good Final | Bad Draft |
|---|----------|-----------|-----------|
| 17 | Abstract | All `%` escaped as `\%` | Bare unescaped `%` truncates abstract line |

---

## Summary

| Category | Count |
|----------|-------|
| Overfull hbox (text/equation overflow) | 2 |
| Figure errors | 2 |
| Table overflow | 2 |
| Undefined citations -> [?] | 3 |
| Typos | 7 |
| LaTeX syntax | 1 |

> All errors are introduced through LaTeX source code modifications only.  
> No red boxes, annotations, Chinese text, or error labels appear in either PDF.  
> Both PDFs compiled with Tectonic 0.17.0 using `\documentclass[conference]{IEEEtran}`.
