from __future__ import annotations

import pytest

from delegation_budgets import (
    delegation_budget_route,
    over_budget_workers,
    proportional_worker_budgets,
)


def test_delegation_budgets_split_shared_budget_and_detect_overruns() -> None:
    budgets = proportional_worker_budgets(
        {"research": 2.0, "writer": 1.0},
        total_budget=6.0,
        reserve_budget=1.0,
    )
    assert budgets == {
        "research": pytest.approx(3.3333333333),
        "writer": pytest.approx(1.6666666667),
    }
    assert over_budget_workers({"research": 3.5, "writer": 1.0}, budgets) == ["research"]
    assert delegation_budget_route({"research": 3.5, "writer": 1.0}, budgets) == "rebalance"


def test_delegation_budgets_distinguish_execute_and_review() -> None:
    budgets = {"research": 2.0, "writer": 1.0}
    assert delegation_budget_route({"research": 1.5, "writer": 0.5}, budgets) == "execute"
    assert delegation_budget_route({"research": 2.5, "writer": 1.5}, budgets) == "review"


def test_delegation_budgets_validation() -> None:
    with pytest.raises(ValueError):
        proportional_worker_budgets({}, total_budget=1.0)
    with pytest.raises(ValueError):
        proportional_worker_budgets({"research": 0.0}, total_budget=1.0)
    with pytest.raises(ValueError):
        over_budget_workers({}, {"research": 1.0})
    with pytest.raises(ValueError):
        over_budget_workers({"research": 1.0}, {})
