from __future__ import annotations

import pytest

from regularization_methods import dropout, l1_penalty, l2_penalty, should_stop, weight_decay_step


def test_l1_and_l2_penalties_capture_sparse_and_smooth_shrinkage() -> None:
    assert l1_penalty([1.0, -2.0], 0.1) == pytest.approx(0.3)
    assert l2_penalty([1.0, -2.0], 0.1) == pytest.approx(0.5)


def test_weight_decay_step_shrinks_parameter() -> None:
    assert weight_decay_step(1.0, 0.0, 0.1, 0.1) == pytest.approx(0.99)


def test_dropout_is_deterministic_for_same_seed() -> None:
    assert dropout([1.0, 2.0, 3.0], p=0.5, seed=1) == dropout([1.0, 2.0, 3.0], p=0.5, seed=1)


def test_early_stopping_triggers_after_patience_runs_out() -> None:
    assert should_stop([1.0, 0.9, 0.91, 0.92], patience=2) is True
