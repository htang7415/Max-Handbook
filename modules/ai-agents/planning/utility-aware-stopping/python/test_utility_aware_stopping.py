from __future__ import annotations

import pytest

from utility_aware_stopping import (
    expected_step_utility,
    plan_utility,
    utility_stop_route,
)


def test_utility_aware_stopping_scores_steps_and_plan_value() -> None:
    utility = expected_step_utility(
        success_probability=0.7,
        success_value=10.0,
        step_cost=2.0,
        risk_penalty=1.0,
    )

    assert utility == pytest.approx(4.0)
    assert plan_utility([utility, 1.5, -0.5]) == pytest.approx(5.0)
    assert utility_stop_route(utility, min_continue_utility=1.0, max_stop_loss=-1.0) == "continue"


def test_utility_aware_stopping_distinguishes_review_and_stop() -> None:
    assert utility_stop_route(0.25, min_continue_utility=1.0, max_stop_loss=-1.0) == "review"
    assert utility_stop_route(-1.5, min_continue_utility=1.0, max_stop_loss=-1.0) == "stop"


def test_utility_aware_stopping_validation() -> None:
    with pytest.raises(ValueError):
        expected_step_utility(1.2, 10.0, 2.0)
    with pytest.raises(ValueError):
        expected_step_utility(0.5, -1.0, 2.0)
    with pytest.raises(ValueError):
        plan_utility([])
    with pytest.raises(ValueError):
        utility_stop_route(0.0, min_continue_utility=-2.0, max_stop_loss=-1.0)
