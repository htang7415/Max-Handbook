from __future__ import annotations


def _validate_rate(value: float, name: str) -> None:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must satisfy 0 <= value <= 1")


def risk_adjusted_score(success_rate: float, high_risk_failure_rate: float, risk_penalty: float) -> float:
    _validate_rate(success_rate, "success_rate")
    _validate_rate(high_risk_failure_rate, "high_risk_failure_rate")
    if risk_penalty < 0.0:
        raise ValueError("risk_penalty must be non-negative")
    return success_rate - risk_penalty * high_risk_failure_rate


def benchmark_risk_summary(
    name: str,
    success_rate: float,
    high_risk_failure_rate: float,
    risk_penalty: float,
) -> dict[str, object]:
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("name must be non-empty")
    score = risk_adjusted_score(success_rate, high_risk_failure_rate, risk_penalty)
    return {
        "name": cleaned_name,
        "success_rate": success_rate,
        "high_risk_failure_rate": high_risk_failure_rate,
        "risk_penalty": risk_penalty,
        "risk_adjusted_score": score,
    }


def risk_adjusted_route(
    candidate_score: float,
    baseline_score: float,
    min_score: float,
    max_drop: float,
) -> str:
    if max_drop < 0.0:
        raise ValueError("max_drop must be non-negative")
    if candidate_score < min_score:
        return "fail"
    if baseline_score - candidate_score > max_drop:
        return "review"
    return "pass"
