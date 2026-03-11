from __future__ import annotations


RISK_ORDER = {"low": 0, "medium": 1, "high": 2}


def dependency_risk(version_pinned: bool, known_vulnerabilities: int, executes_install_script: bool) -> str:
    if known_vulnerabilities < 0:
        raise ValueError("known_vulnerabilities must be non-negative")
    if known_vulnerabilities > 0:
        return "high"
    if executes_install_script or not version_pinned:
        return "medium"
    return "low"


def dependency_gate(risk: str, in_production_path: bool) -> str:
    normalized = risk.strip().lower()
    if normalized not in RISK_ORDER:
        raise ValueError("risk must be low, medium, or high")
    if normalized == "high":
        return "block"
    if normalized == "medium" and in_production_path:
        return "review"
    return "allow"


def portfolio_risk(risks: list[str]) -> str:
    if not risks:
        raise ValueError("risks must be non-empty")
    normalized = [risk.strip().lower() for risk in risks]
    for risk in normalized:
        if risk not in RISK_ORDER:
            raise ValueError("risk must be low, medium, or high")
    return max(normalized, key=RISK_ORDER.get)
