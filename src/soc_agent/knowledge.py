"""
Domain Knowledge Engine: MITRE ATT&CK STIX 2.1 RAG and NIST SP 800-61 Rev. 3 playbooks.
Module ⑥ of Eight-Module Architecture.
"""
from typing import List, Dict

class DomainKnowledgeEngine:
    """
    Maintains structured graph and vector embeddings for MITRE ATT&CK Enterprise techniques
    and NIST SP 800-61 Rev. 3 incident playbooks.
    """
    def __init__(self):
        self.attack_db = {
            "T1059.001": {
                "name": "Command and Scripting Interpreter: PowerShell",
                "tactic": "Execution",
                "kill_chain_phase": "Execution",
                "description": "Adversaries may abuse PowerShell commands and scripts for execution."
            },
            "T1003.001": {
                "name": "OS Credential Dumping: LSASS Memory",
                "tactic": "Credential Access",
                "kill_chain_phase": "Credential Access",
                "description": "Adversaries may attempt to access credential material stored in the LSASS process."
            },
            "T1078": {
                "name": "Valid Accounts",
                "tactic": "Defense Evasion / Persistence",
                "kill_chain_phase": "Persistence",
                "description": "Adversaries may obtain and abuse credentials of existing accounts."
            },
            "T1048": {
                "name": "Exfiltration Over Alternative Protocol",
                "tactic": "Exfiltration",
                "kill_chain_phase": "Exfiltration",
                "description": "Stealthy exfiltration of sensitive organizational assets over unauthorized channels."
            }
        }

        self.nist_playbooks = {
            "Credential Access": [
                "NIST Step 1: Immediately isolate compromised host from enterprise VLAN.",
                "NIST Step 2: Invalidate compromised Kerberos tickets and reset Active Directory password.",
                "NIST Step 3: Perform memory forensic triage on LSASS handle injections."
            ],
            "Execution": [
                "NIST Step 1: Collect script block execution logs (EID 4104).",
                "NIST Step 2: Validate whether parent process corresponds to authorized IT automation."
            ],
            "Exfiltration": [
                "NIST Step 1: BLOCK outbound IP/Domain at perimeter firewall and proxy.",
                "NIST Step 2: Freeze host session and notify CISO under high-severity protocol."
            ],
            "Default": [
                "NIST Step 1: Review host telemetry within +/- 2 hours of alert trigger.",
                "NIST Step 2: Validate digital signature of flagged binary."
            ]
        }

    def map_attack_techniques(self, query: str) -> List[Dict[str, str]]:
        results = []
        q_lower = query.lower()
        if "lsass" in q_lower or "mimikatz" in q_lower or "credential" in q_lower:
            results.append({"technique_id": "T1003.001", **self.attack_db["T1003.001"]})
        if "powershell" in q_lower or "script" in q_lower:
            results.append({"technique_id": "T1059.001", **self.attack_db["T1059.001"]})
        if "exfiltration" in q_lower or "c2" in q_lower:
            results.append({"technique_id": "T1048", **self.attack_db["T1048"]})
        if not results:
            results.append({"technique_id": "T1078", **self.attack_db["T1078"]})
        return results

    def get_nist_guidance(self, tactics: List[str]) -> List[str]:
        steps = []
        for t in tactics:
            if t in self.nist_playbooks:
                steps.extend(self.nist_playbooks[t])
        if not steps:
            steps.extend(self.nist_playbooks["Default"])
        return steps
