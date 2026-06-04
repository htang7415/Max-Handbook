from __future__ import annotations


def _require_unit_interval(name: str, value: float) -> float:
    value = float(value)
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must satisfy 0 <= value <= 1")
    return value


def _require_positive(name: str, value: float) -> float:
    value = float(value)
    if value <= 0.0:
        raise ValueError(f"{name} must be positive")
    return value


def composite_quality_score(
    task_success: float,
    judge_win_rate: float,
    calibration_error: float,
    regression_rate: float = 0.0,
) -> float:
    task_success = _require_unit_interval("task_success", task_success)
    judge_win_rate = _require_unit_interval("judge_win_rate", judge_win_rate)
    calibration_error = _require_unit_interval("calibration_error", calibration_error)
    regression_rate = _require_unit_interval("regression_rate", regression_rate)

    score = (
        0.5 * task_success
        + 0.3 * judge_win_rate
        + 0.2 * (1.0 - calibration_error)
        - 0.4 * regression_rate
    )
    return max(0.0, min(1.0, score))


def serving_fit(
    p95_latency_ms: float,
    cost_per_1k: float,
    latency_budget_ms: float,
    cost_budget_per_1k: float,
) -> float:
    p95_latency_ms = _require_positive("p95_latency_ms", p95_latency_ms)
    cost_per_1k = _require_positive("cost_per_1k", cost_per_1k)
    latency_budget_ms = _require_positive("latency_budget_ms", latency_budget_ms)
    cost_budget_per_1k = _require_positive("cost_budget_per_1k", cost_budget_per_1k)
    return min(latency_budget_ms / p95_latency_ms, cost_budget_per_1k / cost_per_1k)


def release_gate(metrics: dict[str, float], budgets: dict[str, float]) -> dict[str, object]:
    quality = composite_quality_score(
        metrics["task_success"],
        metrics["judge_win_rate"],
        metrics["calibration_error"],
        metrics.get("regression_rate", 0.0),
    )
    fit = serving_fit(
        metrics["p95_latency_ms"],
        metrics["cost_per_1k"],
        budgets["max_latency_ms"],
        budgets["max_cost_per_1k"],
    )

    reasons: list[str] = []
    if quality < float(budgets["min_quality"]):
        reasons.append("quality-below-threshold")
    if metrics["p95_latency_ms"] > budgets["max_latency_ms"]:
        reasons.append("latency-over-budget")
    if metrics["cost_per_1k"] > budgets["max_cost_per_1k"]:
        reasons.append("cost-over-budget")
    if metrics.get("regression_rate", 0.0) > budgets.get("max_regression_rate", 0.03):
        reasons.append("regression-risk")
    if metrics["calibration_error"] > budgets.get("max_calibration_error", 0.15):
        reasons.append("calibration-risk")

    decision = "ship" if not reasons else "hold"
    if "regression-risk" in reasons or "calibration-risk" in reasons:
        decision = "rollback"

    return {
        "decision": decision,
        "quality": round(quality, 4),
        "serving_fit": round(fit, 4),
        "reasons": reasons,
    }
