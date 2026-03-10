from __future__ import annotations

import pytest

from regression_metrics import mae_mse, r2_score


def test_mae_mse_returns_absolute_and_squared_error_views() -> None:
    mae, mse = mae_mse([1.0, 2.0], [1.0, 3.0])
    assert mae == pytest.approx(0.5)
    assert mse == pytest.approx(0.5)


def test_r2_score_returns_one_for_perfect_fit() -> None:
    assert r2_score([1.0, 2.0], [1.0, 2.0]) == pytest.approx(1.0)


def test_regression_metrics_validate_lengths() -> None:
    with pytest.raises(ValueError):
        mae_mse([1.0], [1.0, 2.0])
    with pytest.raises(ValueError):
        r2_score([1.0], [1.0, 2.0])
