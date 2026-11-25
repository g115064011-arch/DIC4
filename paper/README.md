# AI SOC Analyst Agent — IEEE Conference Paper Package (DIC4)

This repository contains the complete, verified LaTeX source code, OpenSpec SDD specifications, and runnable Python agent implementation for the **AI SOC Analyst Agent** project.

## Overleaf Compilation & Synchronization

This project is 100% compliant with standard IEEE Conference formatting (`IEEEtran`).

### Project Structure
```text
paper/
├── main.tex                  # Primary LaTeX root file
├── preamble.tex              # Math macros & package configurations
├── authors.tex               # Author affiliations (Group 16)
├── references.bib            # 16 verified, non-hallucinated citations
├── IEEEtran.cls              # Official IEEE conference class
├── sections/
│   ├── 00_abstract.tex       # Checkpoints A through F verified
│   ├── 01_introduction.tex   # Threat telemetry & research contributions
│   ├── 02_related_work.tex   # 50% AI / 50% Domain literature & Table I
│   ├── 03_domain_analysis.tex# 5 mindsets & 3 controversies
│   ├── 04_system_architecture.tex # 8 modules, Table II contracts, Alg 1
│   ├── 05_experimental_design.tex # GUIDE & ExCyTIn-Bench protocols
│   ├── 06_expected_outcomes.tex   # Pareto frontier & threats to validity
│   └── 07_conclusion.tex     # Synthesis & IoT/ICS outlook
└── README.md
```

### Steps to Sync to Overleaf:
1. Open your Overleaf project: `https://www.overleaf.com/project/6afafb3ef4ed8b43cc1d222`
2. You can upload the contents of the `paper/` folder directly via Overleaf Web UI (`Upload` -> Zip or folder) or copy the modular files.
3. If syncing via Overleaf MCP (`netique/overleaf-mcp` or `GhoshSrinjoy/Overleaf-mcp`), point the tool to `paper/main.tex`.
4. Click **Recompile** in Overleaf (Engine: pdfLaTeX). It will compile cleanly with 0 errors and 0 bibentry warnings.

## Academic Checkpoint Verification (A through F)
- **Checkpoint A (Attention Getter)**: 2026 empirical metrics (IBM Cost of Breach $4.99M, 247-day lifecycle; Mandiant 14-day dwell time; Taiwan NSB 2.63M daily cyber probes vs internal SOC alerts).
- **Checkpoint B (But / Gap)**: Alert fatigue, 20.6% TP vs 49% BP vs 30.4% FP (GUIDE dataset), 40.4% LLM false negative rate, ExCyTIn-Bench 0.606 reward.
- **Checkpoint C (Cure)**: AI SOC Analyst Agent combining ML triage, MITRE ATT&CK STIX RAG, and bounded ReAct planning.
- **Checkpoint D (Development)**: 8-module architecture, TreeSHAP feature explanations, Algorithm 1 Bounded ReAct with Evidence Gate.
- **Checkpoint E (Experiments)**: Microsoft GUIDE (~1M incidents, 6.1k tenants) and ExCyTIn-Bench (57 log tables, 8 attack chains).
- **Checkpoint F (Expected Outcomes)**: Miss Rate vs Escalation Rate Pareto frontier.
