from __future__ import annotations


def _validate_rate(value: float, name: str) -> None:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must satisfy 0 <= value <= 1")


def success_delta(baseline_success: float, candidate_success: float) -> float:
    _validate_rate(baseline_success, "baseline_success")
    _validate_rate(candidate_success, "candidate_success")
    return candidate_success - baseline_success


def compare_variant_scores(baseline: dict[str, float], candidate: dict[str, float]) -> str:
    baseline_success = float(baseline.get("success", 0.0))
    candidate_success = float(candidate.get("success", 0.0))
    _validate_rate(baseline_success, "baseline.success")
    _validate_rate(candidate_success, "candidate.success")
    if candidate_success > baseline_success:
        return "candidate"
    if candidate_success < baseline_success:
        return "baseline"

    baseline_latency = float(baseline.get("latency_ms", 0.0))
    candidate_latency = float(candidate.get("latency_ms", 0.0))
    if candidate_latency < baseline_latency:
        return "candidate"
    if candidate_latency > baseline_latency:
        return "baseline"
    return "tie"


def comparison_summary(
    baseline_name: str,
    candidate_name: str,
    baseline_success: float,
    candidate_success: float,
) -> str:
    _validate_rate(baseline_success, "baseline_success")
    _validate_rate(candidate_success, "candidate_success")
    delta = candidate_success - baseline_success
    return (
        f"{candidate_name} vs {baseline_name}: "
        f"success {candidate_success:.2f} vs {baseline_success:.2f} "
        f"(delta {delta:+.2f})"
    )
