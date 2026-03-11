from __future__ import annotations


def flake_risk(uses_time: bool, uses_network: bool, shared_state: bool) -> str:
    risk_count = sum([uses_time, uses_network, shared_state])
    if risk_count == 0:
        return "low"
    if risk_count == 1:
        return "medium"
    return "high"


def stabilization_steps(uses_time: bool, uses_network: bool, shared_state: bool) -> list[str]:
    steps: list[str] = []
    if uses_time:
        steps.append("freeze time or inject clock")
    if uses_network:
        steps.append("replace network with stub")
    if shared_state:
        steps.append("isolate state per test")
    if not steps:
        steps.append("keep test deterministic")
    return steps


def should_quarantine(failure_rate: float, critical_path: bool) -> bool:
    if not 0 <= failure_rate <= 1:
        raise ValueError("failure_rate must be between 0 and 1")
    return failure_rate >= 0.1 and not critical_path
