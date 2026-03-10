from __future__ import annotations

import pytest

from loss_functions import cross_entropy, focal_loss, hinge_loss, huber, mae, mse, rmse


def test_cross_entropy_is_low_for_confident_correct_logits() -> None:
    assert cross_entropy([3.0, 0.0], 0) < 0.1


def test_focal_loss_downweights_easy_examples() -> None:
    assert focal_loss(0.9, gamma=2.0) < focal_loss(0.6, gamma=2.0)


def test_hinge_loss_penalizes_margin_violations() -> None:
    assert hinge_loss(2.0, 1) == pytest.approx(0.0)
    assert hinge_loss(0.2, 1) == pytest.approx(0.8)


def test_huber_is_quadratic_near_zero() -> None:
    assert huber(1.0, 0.0, delta=1.0) == pytest.approx(0.5)


def test_regression_losses_cover_absolute_squared_and_root_error() -> None:
    assert mae([1.0, 2.0], [1.0, 3.0]) == pytest.approx(0.5)
    assert mse([1.0, 2.0], [1.0, 3.0]) == pytest.approx(0.5)
    assert rmse([1.0, 2.0], [1.0, 3.0]) == pytest.approx(0.5**0.5)
