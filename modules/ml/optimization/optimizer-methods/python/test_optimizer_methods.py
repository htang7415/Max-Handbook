from __future__ import annotations

import pytest

from optimizer_methods import (
    adagrad_step,
    adam_step,
    adamw_step,
    momentum_step,
    momentum_velocity,
    nesterov_step,
    rmsprop_step,
    sgd_step,
    weight_decay_term,
)


def test_sgd_step_moves_against_gradient() -> None:
    assert sgd_step(1.0, 0.5, 0.1) == pytest.approx(0.95)


def test_momentum_and_nesterov_return_updated_weight_and_velocity() -> None:
    w_m, v_m = momentum_step(1.0, 1.0, 0.0, 0.1, 0.9)
    w_n, v_n = nesterov_step(1.0, 1.0, 0.0, 0.1, 0.9)
    assert w_m < 1.0 and w_n < 1.0
    assert v_m == pytest.approx(1.0)
    assert v_n == pytest.approx(1.0)
    assert momentum_velocity(1.0, 0.0, 0.9) == pytest.approx(1.0)


def test_adaptive_optimizers_accumulate_state() -> None:
    _, g2 = adagrad_step(1.0, 1.0, 0.0, 0.1, 1e-8)
    _, v_r = rmsprop_step(1.0, 1.0, 0.0, 0.1, 0.9, 1e-8)
    _, m_a, v_a = adam_step(1.0, 1.0, 0.0, 0.0, 0.1, 0.9, 0.999, 1e-8)
    _, m_w, v_w = adamw_step(1.0, 1.0, 0.0, 0.0, 0.1, 0.1, 0.9, 0.999, 1e-8)
    assert g2 > 0.0 and v_r > 0.0
    assert m_a > 0.0 and v_a > 0.0
    assert m_w > 0.0 and v_w > 0.0
    assert weight_decay_term(1.0, 0.1, 0.1) == pytest.approx(0.01)


def test_optimizer_methods_validate_hyperparameters() -> None:
    with pytest.raises(ValueError, match="0 <= mu <= 1"):
        momentum_velocity(1.0, 0.0, 1.5)
    with pytest.raises(ValueError, match="non-negative"):
        sgd_step(1.0, 1.0, -0.1)
    with pytest.raises(ValueError, match="positive"):
        adagrad_step(1.0, 1.0, 0.0, 0.1, 0.0)
    with pytest.raises(ValueError, match="0 <= beta <= 1"):
        rmsprop_step(1.0, 1.0, 0.0, 0.1, 1.2, 1e-8)
    with pytest.raises(ValueError, match="beta1 and beta2"):
        adam_step(1.0, 1.0, 0.0, 0.0, 0.1, -0.1, 0.999, 1e-8)
    with pytest.raises(ValueError, match="non-negative"):
        adamw_step(1.0, 1.0, 0.0, 0.0, 0.1, -0.1, 0.9, 0.999, 1e-8)
