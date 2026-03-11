from __future__ import annotations

import pytest

from tree_ensemble_methods import (
    bootstrap_indices,
    boosting_residuals,
    class_probabilities,
    gini_impurity,
    gradient_boosting_step,
    split_gain,
    update_weights,
)


def test_gini_impurity() -> None:
    assert gini_impurity([0, 0, 1, 1]) == 0.5
    assert gini_impurity([]) == 0.0
    assert class_probabilities([0, 0, 1, 1]) == pytest.approx([0.5, 0.5])


def test_bootstrap_indices_len() -> None:
    assert len(bootstrap_indices(5, seed=1)) == 5
    with pytest.raises(ValueError, match="positive"):
        bootstrap_indices(0)


def test_update_weights_normalizes() -> None:
    out = update_weights([0.5, 0.5], [1, 0], 0.7)
    assert abs(sum(out) - 1.0) < 1e-6


def test_update_weights_validates_inputs() -> None:
    with pytest.raises(ValueError, match="same length"):
        update_weights([0.5], [1, 0], 0.7)
    with pytest.raises(ValueError, match="non-negative"):
        update_weights([-0.5, 1.5], [1, 0], 0.7)
    with pytest.raises(ValueError, match="0 or 1"):
        update_weights([0.5, 0.5], [2, 0], 0.7)


def test_gradient_boosting_step_updates_predictions_and_residuals() -> None:
    updated, residuals = gradient_boosting_step(
        targets=[3.0, 5.0],
        predictions=[1.0, 2.0],
        weak_learner_output=[2.0, 3.0],
        learning_rate=0.5,
    )
    assert updated == [2.0, 3.5]
    assert residuals == [1.0, 1.5]
    assert boosting_residuals([3.0, 5.0], updated) == [1.0, 1.5]


def test_split_gain_matches_formula() -> None:
    value = split_gain(
        left_grad=2.0,
        left_hess=1.0,
        right_grad=-1.0,
        right_hess=1.0,
        lambda_reg=1.0,
        gamma=0.1,
    )
    assert value == pytest.approx(0.9833333333)


def test_split_gain_validates_gamma() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        split_gain(1.0, 1.0, 1.0, 1.0, lambda_reg=1.0, gamma=-0.1)
