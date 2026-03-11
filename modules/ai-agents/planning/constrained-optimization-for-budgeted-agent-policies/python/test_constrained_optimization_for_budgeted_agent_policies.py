from __future__ import annotations

import pytest

from constrained_optimization_for_budgeted_agent_policies import (
    budgeted_policy_choice,
    feasible_policies,
    policy_objective,
)


def test_constrained_optimization_for_budgeted_agent_policies_selects_best_feasible_policy() -> None:
    policy_to_metrics = {
        "fast-policy": {"expected_reward": 7.0, "cost": 1.0, "latency_ms": 200.0, "risk": 0.04},
        "balanced-policy": {"expected_reward": 8.5, "cost": 2.0, "latency_ms": 400.0, "risk": 0.05},
        "deep-policy": {"expected_reward": 10.0, "cost": 4.0, "latency_ms": 800.0, "risk": 0.08},
    }

    assert policy_objective(8.5, 2.0, 400.0, cost_weight=1.0, latency_weight=0.002) == pytest.approx(5.7)
    assert feasible_policies(policy_to_metrics, max_cost=3.0, max_latency_ms=500.0, max_risk=0.06) == [
        "balanced-policy",
        "fast-policy",
    ]
    assert (
        budgeted_policy_choice(
            policy_to_metrics,
            max_cost=3.0,
            max_latency_ms=500.0,
            max_risk=0.06,
            cost_weight=1.0,
            latency_weight=0.002,
        )
        == "balanced-policy"
    )


def test_constrained_optimization_for_budgeted_agent_policies_reviews_when_nothing_is_feasible() -> None:
    assert (
        budgeted_policy_choice(
            {
                "deep-policy": {"expected_reward": 10.0, "cost": 4.0, "latency_ms": 800.0, "risk": 0.08},
            },
            max_cost=3.0,
            max_latency_ms=500.0,
            max_risk=0.06,
        )
        == "review"
    )


def test_constrained_optimization_for_budgeted_agent_policies_validation() -> None:
    with pytest.raises(ValueError):
        policy_objective(-1.0, 1.0, 100.0)
    with pytest.raises(ValueError):
        feasible_policies({}, max_cost=1.0, max_latency_ms=100.0, max_risk=0.1)
    with pytest.raises(ValueError):
        feasible_policies({"policy": {"cost": -1.0, "latency_ms": 10.0, "risk": 0.0}}, 1.0, 100.0, 0.1)
