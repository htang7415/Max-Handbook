from __future__ import annotations

import pytest

from decision_cost_matrices import (
    cost_matrix_decision,
    expected_action_cost,
    ranked_actions_by_cost,
)


def test_decision_cost_matrices_rank_actions_by_expected_cost() -> None:
    outcome_probs = {"safe": 0.7, "unsafe": 0.3}
    matrix = {
        "allow": {"safe": 0.0, "unsafe": 12.0},
        "review": {"safe": 2.0, "unsafe": 2.0},
        "block": {"safe": 5.0, "unsafe": 0.0},
    }

    assert expected_action_cost(outcome_probs, matrix["allow"]) == pytest.approx(3.6)
    assert ranked_actions_by_cost(matrix, outcome_probs) == [
        {"action": "review", "expected_cost": pytest.approx(2.0)},
        {"action": "block", "expected_cost": pytest.approx(3.5)},
        {"action": "allow", "expected_cost": pytest.approx(3.6)},
    ]
    assert cost_matrix_decision(matrix, outcome_probs) == "review"


def test_decision_cost_matrices_can_prefer_allow_when_unsafe_probability_is_low() -> None:
    outcome_probs = {"safe": 0.97, "unsafe": 0.03}
    matrix = {
        "allow": {"safe": 0.0, "unsafe": 12.0},
        "review": {"safe": 1.0, "unsafe": 1.0},
        "block": {"safe": 5.0, "unsafe": 0.0},
    }

    assert cost_matrix_decision(matrix, outcome_probs) == "allow"


def test_decision_cost_matrices_validation() -> None:
    with pytest.raises(ValueError):
        expected_action_cost({}, {"safe": 1.0})
    with pytest.raises(ValueError):
        expected_action_cost({"safe": 0.8}, {"safe": 1.0})
    with pytest.raises(ValueError):
        expected_action_cost({"safe": 1.0}, {})
    with pytest.raises(ValueError):
        ranked_actions_by_cost({}, {"safe": 1.0})
