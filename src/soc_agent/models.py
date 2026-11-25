"""
Data models for AI SOC Analyst Agent.
RFC 2119 and OpenSpec compliant schema.
"""
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Any
import time

class Verdict(str, Enum):
    TRUE_POSITIVE = "TP"
    BENIGN_POSITIVE = "BP"
    FALSE_POSITIVE = "FP"
    ESCALATE = "ESCALATE"

class KillChainPhase(str, Enum):
    INITIAL_ACCESS = "Initial Access"
    EXECUTION = "Execution"
    PERSISTENCE = "Persistence"
    PRIVILEGE_ESCALATION = "Privilege Escalation"
    DEFENSE_EVASION = "Defense Evasion"
    CREDENTIAL_ACCESS = "Credential Access"
    DISCOVERY = "Discovery"
    LATERAL_MOVEMENT = "Lateral Movement"
    COLLECTION = "Collection"
    COMMAND_AND_CONTROL = "Command and Control"
    EXFILTRATION = "Exfiltration"
    IMPACT = "Impact"

@dataclass
class Alert:
    alert_id: str
    detector: str
    severity: str
    timestamp: str
    host: str
    user: str
    raw_event: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Incident:
    incident_id: str
    tenant_id: str
    alerts: List[Alert]
    created_at: str
    status: str = "QUEUED"

@dataclass
class ToolEvidence:
    tool_name: str
    query: str
    result_count: int
    findings: List[str]
    is_empty: bool

@dataclass
class TriageReport:
    incident_id: str
    verdict: Verdict
    confidence: float
    probabilities: Dict[str, float]
    shap_top_features: List[Dict[str, Any]]
    mitre_techniques: List[Dict[str, str]]
    nist_playbook_steps: List[str]
    escalate_to_human: bool
    escalation_reasons: List[str]
    investigation_trace: List[Dict[str, Any]]
    token_cost: int
    execution_time_sec: float
