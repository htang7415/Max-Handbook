from llm_eval_serving_gate import (
    composite_quality_score,
    release_gate,
    serving_fit,
)


def test_release_gate_ships_when_quality_and_serving_fit_budget():
    decision = release_gate(
        metrics={
            "task_success": 0.88,
            "judge_win_rate": 0.64,
            "calibration_error": 0.06,
            "regression_rate": 0.01,
            "p95_latency_ms": 900,
            "cost_per_1k": 0.45,
        },
        budgets={
            "min_quality": 0.78,
            "max_latency_ms": 1000,
            "max_cost_per_1k": 0.50,
            "max_regression_rate": 0.03,
            "max_calibration_error": 0.12,
        },
    )

    assert decision["decision"] == "ship"
    assert decision["reasons"] == []
    assert decision["quality"] >= 0.78


def test_release_gate_rolls_back_regression_or_calibration_risk():
    decision = release_gate(
        metrics={
            "task_success": 0.89,
            "judge_win_rate": 0.70,
            "calibration_error": 0.20,
            "regression_rate": 0.05,
            "p95_latency_ms": 850,
            "cost_per_1k": 0.40,
        },
        budgets={
            "min_quality": 0.75,
            "max_latency_ms": 1000,
            "max_cost_per_1k": 0.50,
            "max_regression_rate": 0.03,
            "max_calibration_error": 0.12,
        },
    )

    assert decision["decision"] == "rollback"
    assert "regression-risk" in decision["reasons"]
    assert "calibration-risk" in decision["reasons"]


def test_quality_and_serving_fit_validate_ranges():
    assert 0.0 <= composite_quality_score(0.8, 0.6, 0.1) <= 1.0
    assert serving_fit(800, 0.25, latency_budget_ms=1000, cost_budget_per_1k=0.50) > 1.0

    try:
        composite_quality_score(1.2, 0.6, 0.1)
    except ValueError as exc:
        assert "task_success" in str(exc)
    else:
        raise AssertionError("expected invalid unit interval to fail")
