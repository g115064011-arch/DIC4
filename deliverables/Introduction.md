# Introduction

## I.A Widening Gap Between Threat Scale and Defender Capacity

Modern enterprise environments face an unprecedented deluge of cyber threats that far outstrips the analytical bandwidth of human defenders. According to official disclosures by Taiwan's National Security Bureau (NSB) in 2026, external adversaries launched approximately 2.63 million daily cyber probe and intrusion attempts against critical national infrastructure in 2025 — representing a 6% year-over-year escalation [NSB 2026]. Crucially, these figures quantify externally originating perimeter scans, port sweeps, and exploit attempts, which must be rigorously distinguished from internal alert queues processed by corporate Security Operations Centers (SOCs); confusing external probe volumes with internal SOC alert loads misrepresents operational queue burdens and may lead to under-resourcing of frontline analyst teams.

The economic and temporal damages inflicted by uncontained intrusions have reached catastrophic levels. The IBM Cost of a Data Breach Report 2026 records an all-time peak global average breach cost of $4.99 million (+12% YoY), with an average dwell and containment lifecycle spanning 247 days [IBM 2026]. Organizations deploying advanced AI and automation in security workflows reduced breach lifecycles by 65 days and saved an average of $1.93 million per incident [IBM 2026]. Simultaneously, Mandiant M-Trends 2026 reports a global median dwell time of 14 days, stretching to 122 days for cyber espionage operations [Mandiant 2026]. These empirical benchmarks demonstrate that detection and containment velocity serves as the paramount differentiator between minor security incidents and catastrophic institutional collapse.

## I.B Alert Fatigue and the Limits of Existing Automation

A modern SOC relies on Security Information and Event Management (SIEM) and Extended Detection and Response (XDR) systems to aggregate telemetry across endpoints, network perimeters, cloud tenants, and identity providers. Tier-1 analysts bear the frontline responsibility of rapid alert triage: determining whether incoming events represent a True Positive (TP, confirmed malicious intrusion), a Benign Positive (BP, authorized administrative activity triggering detection logic), or a False Positive (FP, sensor erroneous firing) [Alahmadi 2022].

The distinction between BP and FP is operationally critical: empirical studies by Alahmadi et al. [Alahmadi 2022] establish that the vast majority of dismissed alarms are benign positives rather than erroneous false alarms. Analysts map alerts against the MITRE ATT&CK matrix [Sadlek 2025] and adhere to standard incident handling frameworks such as NIST SP 800-61 Rev. 3 [NIST 2025], which mandates prioritized triage based on threat progression rather than chronological arrival order.

Statistical classifiers such as GBDT-based Copilot Guided Response (CGR) [Freitas 2024] achieve macro-F1 scores above 0.87 on the Microsoft GUIDE benchmark but inherently lack semantic comprehension of multi-stage attack kill-chains. Conversely, Large Language Model (LLM) agents provide natural language reasoning capabilities but suffer from a critical operational failure mode: when an initial log query returns an empty result set, five evaluated tool-using agent architectures [Tsegai 2026] prematurely conclude that no threat exists, yielding a false negative rate (FNR) of at least 40.4%. The ExCyTIn-Bench evaluation suite [Wu 2026] corroborates this finding, with investigation rewards plateauing at 0.606 across tested strategies. This gap between statistical accuracy and semantic investigation reliability constitutes the central research problem addressed in this work.

## I.C Research Contributions

This paper presents four primary contributions to the state of automated SOC alert triage:

1. **Spec-Driven Eight-Module Architecture:** An RFC 2119 behavioral specification governing eight decoupled functional components, ensuring auditability and reproducible deployment across heterogeneous SOC environments.

2. **Bounded ReAct+RAG Control Loop with Evidence Gate:** Algorithm 1 formalizes a planning loop with an explicit Evidence Gate: when tool queries return empty sets, the gate prevents premature FP closure and triggers conditional escalation, directly targeting the 40.4% FNR failure mode.

3. **Calibrated Asymmetric Escalation Policy:** A mathematically grounded cost-sensitive escalation policy that explicitly models the asymmetric costs between missed true-positive attacks and unnecessary human escalations, enabling operators to trace a Pareto frontier parameterized by the confidence threshold τ_conf.

4. **Dual-Benchmark Reproducible Evaluation Protocol:** A standardized evaluation protocol covering both Microsoft GUIDE (707k incidents, 6,100 tenants) and ExCyTIn-Bench (57 log tables, 8 attack chains), using GroupKFold partitioning grouped by customer tenant ID to prevent cross-institutional data leakage [Arp 2022].

The remainder of this paper is organized as follows. Section II surveys related work in automated SOC triage, LLM agent evaluation, and human-in-the-loop cybersecurity systems. Section III describes the system architecture. Section IV details the methodology. Section V presents the experimental setup. Section VI reports results. Section VII discusses threats to validity, and Section VIII concludes.

---

**Key References (Introduction):**
- [NSB 2026] National Security Bureau, Republic of China (Taiwan). *Analysis of Cyber Threats to Critical Infrastructure in 2025.* 2026.
- [IBM 2026] IBM Security. *Cost of a Data Breach Report 2026.*
- [Mandiant 2026] Google Cloud Mandiant. *M-Trends 2026.*
- [Alahmadi 2022] Alahmadi et al. "99% False Positives: A Qualitative Study of SOC Analysts' Perspectives." USENIX Security 2022.
- [Freitas 2024] Freitas et al. "AI-Driven Guided Response for SOC with Microsoft Copilot for Security." arXiv:2407.09017.
- [Tsegai 2026] Tsegai et al. "From Investigation Failures to Reliable SOC Agents." arXiv:2610.10608.
- [Wu 2026] Wu et al. "ExCyTIn-Bench." ICML 2026.
- [Arp 2022] Arp et al. "Dos and Don'ts of Machine Learning in Computer Security." USENIX Security 2022.
