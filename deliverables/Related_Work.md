# Related Work

Automated SOC alert triage sits at the intersection of machine learning-based anomaly detection, natural language-driven autonomous agents, and operational cybersecurity practice. We survey these three dimensions and identify the research gaps motivating our design.

## II.A Machine Learning for Alert Prioritization

Early large-scale automation of SOC workflows deployed tabular statistical classifiers over structured endpoint and network log features. Freitas et al. [Freitas 2024] introduced Copilot Guided Response (CGR), deploying Gradient Boosted Decision Trees (GBDT) with Shapley Additive Explanations (SHAP) across Microsoft enterprise tenants, achieving a macro-F1 score above 0.87 on the GUIDE dataset. The key advantage of GBDT-based approaches lies in their calibrated probabilistic outputs and computational efficiency (<0.04s per incident), making them suitable for high-throughput production environments. However, CGR and similar statistical models lack semantic comprehension of kill-chain attack progressions: they classify individual alert feature vectors without reasoning across correlated multi-step activity sequences.

Garcia et al. [Garcia 2025] proposed ROSCA, integrating alert correlation with MITRE ATT&CK technique mapping to rank alert severity. ROSCA demonstrated scalability advantages over graph-based correlation engines but required manually curated MITRE mappings for each deployment environment. Freitas et al. [Freitas 2026] subsequently introduced Adaptive Incident Prioritization (AIP), dynamically re-ranking queued incidents based on evolving threat context, reducing analyst queue overflow by approximately 23% in production. Ndichu et al. [Ndichu 2026] provide a comprehensive survey of AI-driven alert screening approaches, cataloguing 47 methods and identifying that high false-positive tolerance remains the predominant unresolved challenge across systems.

## II.B LLM Agents for Autonomous Cyber Investigation

The emergence of tool-augmented LLMs enabled a qualitative shift from passive classification to active evidence gathering. Wei et al. [Wei 2025] proposed CORTEX, a multi-agent debate architecture in which independent LLM instances challenge each other's threat hypotheses before converging on a verdict. CORTEX improved investigation consensus quality but introduced substantial per-alert API costs (approximately $24 per complex multi-hop investigation), limiting deployment to Tier-2 escalation workflows.

Habibzadeh et al. [Habibzadeh 2025] survey LLM integration patterns across SOC workflows, identifying five operational models: prompt-only, RAG-augmented, tool-using ReAct, multi-agent debate, and hybrid human-AI handoff. Their analysis finds that tool-using ReAct variants offer the best cost-accuracy tradeoff under standard enterprise budgets, but are most vulnerable to premature investigation termination on empty query returns.

Tsegai et al. [Tsegai 2026] provide the most rigorous empirical characterization of this vulnerability through AIDA (Automated Intrusion Detection Agent), evaluating five distinct tool-using agent architectures across diverse enterprise alert corpora. All five strategies exhibited a true-positive false negative rate of at least 40.4%, with the dominant failure mode being premature termination: when an initial log query returns an empty result set, the LLM incorrectly infers absence of malicious activity and closes the investigation without further evidence gathering. This failure mode is structurally absent from pure-classifier approaches and represents the critical gap exploited in our Evidence Gate design.

## II.C Benchmark Evaluation Frameworks

Realistic evaluation of autonomous cyber investigation agents requires multi-hop log environments reflecting authentic enterprise attack chains. Wu et al. [Wu 2026] introduce ExCyTIn-Bench, comprising 57 relational log tables and 8 complete attack chain scenarios sourced from authentic breach investigations, with an investigation reward metric measuring the fraction of correctly identified attacker steps. The state-of-the-art investigation reward plateaus at 0.606, indicating that existing agents correctly trace only approximately 60% of attack activities even under ideal laboratory conditions.

Deason et al. [Deason 2025] develop CyberSOCEval, extending LLM evaluation to malware analysis and threat intelligence reasoning tasks. TechniqueRAG, proposed by Lekssays et al. [Lekssays 2025], addresses knowledge hallucination in ATT&CK technique annotation by retrieving structured STIX 2.1 objects from curated CTI corpora, demonstrating 19% improvement in technique mapping accuracy over zero-shot LLM baselines.

## II.D Operational Human-in-the-Loop Considerations

Deployment of automated triage in production SOCs introduces human-factor risks independent of classification accuracy. Tilbury and Flowerday [Tilbury 2026] conducted a longitudinal field study across four enterprise SOC deployments, finding that sustained automation reliance induces vigilance decrements: analysts who routinely approve automated verdicts without independent verification exhibit a 31% reduction in anomaly detection sensitivity over six months. This "automation complacency" effect mandates explicit, calibrated human escalation boundaries rather than unrestricted automation.

Alahmadi et al. [Alahmadi 2022] established through qualitative interviews with 20 SOC practitioners that 99% of raised security alarms are ultimately classified as non-actionable, with the majority constituting benign positives (legitimate administrative activity) rather than sensor false positives. Sadlek et al. [Sadlek 2025] demonstrate that severity-based triage integrating kill-chain attack graph reasoning reduces analyst mean-time-to-respond (MTTR) by 38% over threshold-based alert filtering alone.

## II.E Research Gap and Positioning

The analysis of related literature reveals a consistent tripartite gap:

1. **Statistical classifiers** (CGR, AIP, ROSCA) lack kill-chain semantic reasoning, achieving high classification accuracy but generating no investigative context for analyst handoff.

2. **LLM agents** (CORTEX, AIDA strategies) suffer from the empty-query premature termination failure mode, with all evaluated architectures exhibiting ≥40.4% TP miss rates.

3. **No existing system** jointly addresses probabilistic calibration, structured knowledge retrieval, bounded investigation planning, and empirically validated human escalation thresholds within a single deployable architecture.

The proposed AI SOC Analyst Agent addresses all four dimensions through a single integrated spec-driven architecture validated across two complementary benchmarks.

| System | Year | Core Approach | Key Limitation |
|--------|------|---------------|----------------|
| CGR [Freitas 2024] | 2024 | GBDT + SHAP | No kill-chain semantics |
| CORTEX [Wei 2025] | 2025 | Multi-LLM Debate | $24/alert API cost |
| AIDA [Tsegai 2026] | 2026 | Tool ReAct | ≥40.4% FNR |
| ExCyTIn [Wu 2026] | 2026 | Multi-hop Logs | Reward plateau 0.606 |
| Vigilance [Tilbury 2026] | 2026 | SOC Field Study | Complacency trap |
| Alahmadi [2022] | 2022 | Field Survey | BP vs. FP conflation |
| **Ours** | 2026 | GBDT+RAG+ReAct+Gate | (This work) |

---

**Key References (Related Work):**
- [Freitas 2024] Freitas et al. "AI-Driven Guided Response." arXiv:2407.09017.
- [Freitas 2026] Freitas et al. "Adaptive Incident Prioritization." arXiv:2607.16963.
- [Garcia 2025] Garcia et al. "ROSCA." WATCH'25. DOI: 10.1145/3733826.3762680.
- [Ndichu 2026] Ndichu et al. "AI-Driven Security Alert Screening." arXiv:2605.08316.
- [Wei 2025] Wei et al. "CORTEX." arXiv:2510.00311.
- [Habibzadeh 2025] Habibzadeh et al. "LLMs for SOCs: A Comprehensive Survey." arXiv:2509.10858.
- [Tsegai 2026] Tsegai et al. "AIDA." arXiv:2610.10608.
- [Wu 2026] Wu et al. "ExCyTIn-Bench." ICML 2026.
- [Deason 2025] Deason et al. "CyberSOCEval." arXiv:2509.20166.
- [Lekssays 2025] Lekssays et al. "TechniqueRAG." ACL Findings 2025.
- [Tilbury 2026] Tilbury & Flowerday. "The Vigilance Paradox." ICS 34(4):639–662. DOI: 10.1108/ICS-08-2025-0318.
- [Alahmadi 2022] Alahmadi et al. "99% False Positives." USENIX Security 2022.
- [Sadlek 2025] Sadlek et al. "Severity-Based Triage." JISA 89:103956. DOI: 10.1016/j.jisa.2024.103956.
