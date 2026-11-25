"""
AI SOC Analyst Agent: Bounded ReAct Planner & Reasoning Engine.
Module ③ of Eight-Module Architecture.
"""
import time
from typing import Dict, Any, List
from .models import Incident, TriageReport, Verdict
from .analytics import TriageClassifier
from .knowledge import DomainKnowledgeEngine
from .evidence import IncidentEvidenceStore
from .fusion import EvidenceFusionEngine

class AISOCAnalystAgent:
    def __init__(self, tau_confidence: float = 0.70, max_hops: int = 5):
        self.classifier = TriageClassifier()
        self.knowledge = DomainKnowledgeEngine()
        self.evidence_store = IncidentEvidenceStore()
        self.fusion = EvidenceFusionEngine(tau_confidence=tau_confidence)
        self.max_hops = max_hops

    def triage_incident(self, incident: Incident) -> TriageReport:
        start_time = time.time()
        trace = []
        token_count = 0

        # Step 1: Analytics prior (GBDT calibrated probabilities + TreeSHAP)
        probs = self.classifier.predict_probabilities(incident)
        shap_feats = self.classifier.explain_prediction(incident, probs)
        trace.append({"step": "ML_Prior", "probabilities": probs, "shap": shap_feats})
        token_count += 240

        # Step 2: Domain Knowledge Retrieval (MITRE ATT&CK RAG)
        context_str = " ".join([a.detector for a in incident.alerts])
        techniques = self.knowledge.map_attack_techniques(context_str)
        tactics = [t["tactic"] for t in techniques]
        playbook = self.knowledge.get_nist_guidance(tactics)
        trace.append({"step": "Domain_RAG", "techniques": techniques, "playbook_count": len(playbook)})
        token_count += 380

        # Step 3: Bounded ReAct Log Evidence Gathering
        evidence_chain = []
        hosts = list({a.host for a in incident.alerts})
        for host in hosts:
            ev_proc = self.evidence_store.query_logs(host, "process_tree")
            evidence_chain.append(ev_proc)
            ev_net = self.evidence_store.query_logs(host, "network_connections")
            evidence_chain.append(ev_net)
            trace.append({"step": "Tool_Call", "host": host, "findings": len(ev_proc.findings) + len(ev_net.findings)})
            token_count += 450

        # Step 4: Decision & Evidence Fusion (Escalation Gate)
        final_verdict, should_escalate, reasons = self.fusion.evaluate_verdict(
            probabilities=probs,
            evidence_chain=evidence_chain,
            attack_tactics=tactics
        )
        trace.append({"step": "Evidence_Fusion", "verdict": final_verdict.value, "escalate": should_escalate, "reasons": reasons})
        token_count += 210

        elapsed = time.time() - start_time
        return TriageReport(
            incident_id=incident.incident_id,
            verdict=final_verdict,
            confidence=probs[max(probs, key=probs.get)],
            probabilities=probs,
            shap_top_features=shap_feats,
            mitre_techniques=techniques,
            nist_playbook_steps=playbook,
            escalate_to_human=should_escalate,
            escalation_reasons=reasons,
            investigation_trace=trace,
            token_cost=token_count,
            execution_time_sec=round(elapsed, 3)
        )
