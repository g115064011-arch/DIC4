"""
CLI Entry point for AI SOC Analyst Agent demonstration.
Module 8: Output & Interaction.
"""
import sys
import json
from .models import Incident, Alert
from .agent import AISOCAnalystAgent

def main():
    print("=" * 70)
    print("   AI SOC Analyst Agent - Spec-Driven OpenSpec Implementation (DIC4)")
    print("=" * 70)

    # Sample Incident 1: Suspicious credential dump
    inc1 = Incident(
        incident_id="INC-2026-0891",
        tenant_id="TENANT-MICROSOFT-GUIDE-6102",
        alerts=[
            Alert("ALT-01", "Detector_Suspicious_PowerShell", "High", "2026-11-25T10:00:00", "WS-01", "user_admin", {"cmd": "powershell -enc ..."}),
            Alert("ALT-02", "Detector_LSASS_Access", "Critical", "2026-11-25T10:01:15", "WS-01", "user_admin", {"target": "lsass.exe"})
        ],
        created_at="2026-11-25T10:02:00"
    )

    agent = AISOCAnalystAgent(tau_confidence=0.75)
    report1 = agent.triage_incident(inc1)

    print(f"\n[+] Triage Completed for Incident: {report1.incident_id}")
    print(f"    - Final Verdict: {report1.verdict.value}")
    print(f"    - Calibrated Probabilities: {report1.probabilities}")
    print(f"    - Escalation to Human Tier-2/3: {report1.escalate_to_human}")
    if report1.escalation_reasons:
        print(f"    - Escalation Triggers: {report1.escalation_reasons}")
    print("    - MITRE ATT&CK Mappings:")
    for m in report1.mitre_techniques:
        print(f"      * [{m['technique_id']}] {m['name']} ({m['tactic']})")
    print("    - NIST Incident Handling Playbook:")
    for step in report1.nist_playbook_steps[:2]:
        print(f"      * {step}")
    print(f"    - Execution Cost: {report1.token_cost} tokens, Latency: {report1.execution_time_sec}s")
    print("=" * 70)

if __name__ == "__main__":
    main()
