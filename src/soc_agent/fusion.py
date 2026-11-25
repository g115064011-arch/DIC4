"""
Decision & Evidence Fusion Engine: Escalation Policy & Confidence Thresholding.
Module ⑦ of Eight-Module Architecture.
Enforces RFC 2119 SHALL/MUST escalation rules and Asymmetric Error Cost doctrine.
"""
from typing import Dict, List, Tuple
from .models import Verdict, ToolEvidence

class EvidenceFusionEngine:
    def __init__(self, tau_confidence: float = 0.70):
        self.tau = tau_confidence

    def evaluate_verdict(
        self,
        probabilities: Dict[str, float],
        evidence_chain: List[ToolEvidence],
        attack_tactics: List[str]
    ) -> Tuple[Verdict, bool, List[str]]:
        """
        Fuses ML predictions, evidence store telemetry, and ATT&CK domain knowledge.
        Applies 4 RFC 2119 Escalation triggers:
        1. Low Confidence (< tau)
        2. Conclusion Conflict (ML says FP/BP, but logs show high-risk actions)
        3. Investigation Insufficiency (Zero logs found or empty query)
        4. Late-stage Attack Tactics (Exfiltration / Impact detected)
        """
        escalate = False
        reasons = []

        max_class = max(probabilities, key=probabilities.get)
        max_conf = probabilities[max_class]

        # Trigger 1: Confidence below threshold
        if max_conf < self.tau:
            escalate = True
            reasons.append(f"Prediction confidence {max_conf:.2f} falls below threshold tau={self.tau}")

        # Trigger 2: Empty log results (Anti-premature-closure safeguard)
        has_empty_logs = any(e.is_empty for e in evidence_chain)
        if has_empty_logs and max_class != "TP":
            escalate = True
            reasons.append("Empty log queries detected: cannot rule out stealthy living-off-the-land intrusion.")

        # Trigger 3: Late stage tactics
        critical_tactics = {"Credential Access", "Exfiltration", "Lateral Movement", "Impact"}
        detected_crit = set(attack_tactics).intersection(critical_tactics)
        if detected_crit:
            if max_class != "TP":
                escalate = True
                reasons.append(f"Late-stage attack tactics detected ({', '.join(detected_crit)}) contradicting non-TP classification.")

        # Trigger 4: Evidence of credential dumping in logs
        has_credential_dump = any("lsass" in str(f).lower() for e in evidence_chain for f in e.findings)
        if has_credential_dump and max_class != "TP":
            escalate = True
            reasons.append("Evidence Store confirmed LSASS handle access; overrides ML Benign/False prior.")

        if escalate:
            return Verdict.ESCALATE, True, reasons
        
        verdict_map = {
            "TP": Verdict.TRUE_POSITIVE,
            "BP": Verdict.BENIGN_POSITIVE,
            "FP": Verdict.FALSE_POSITIVE
        }
        return verdict_map[max_class], False, []
