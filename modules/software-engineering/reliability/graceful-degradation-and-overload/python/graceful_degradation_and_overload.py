from __future__ import annotations


def capacity_state(current_rps: int, safe_rps: int, hard_rps: int) -> str:
    if current_rps < 0 or safe_rps <= 0 or hard_rps < safe_rps:
        raise ValueError("capacity inputs must be non-negative and ordered")
    if current_rps <= safe_rps:
        return "healthy"
    if current_rps <= hard_rps:
        return "degraded"
    return "overloaded"


def requests_to_shed(current_rps: int, hard_rps: int) -> int:
    if current_rps < 0 or hard_rps <= 0:
        raise ValueError("rps values must be positive")
    return max(0, current_rps - hard_rps)


def degradation_actions(state: str, optional_features: list[str]) -> list[str]:
    normalized_state = state.strip().lower()
    if normalized_state == "healthy":
        return []
    if normalized_state == "degraded":
        return [f"disable:{feature}" for feature in optional_features if feature.strip()]
    if normalized_state == "overloaded":
        actions = [f"disable:{feature}" for feature in optional_features if feature.strip()]
        actions.append("rate-limit")
        return actions
    raise ValueError("state must be healthy, degraded, or overloaded")
