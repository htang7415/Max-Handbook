import pytest

from mse_loss import mse


def test_mse():
    assert mse([1.0, 2.0], [1.0, 3.0]) == 0.5


def test_mse_zero_for_perfect_prediction():
    assert mse([1.0, 2.0], [1.0, 2.0]) == 0.0


def test_mse_rejects_length_mismatch():
    with pytest.raises(ValueError, match="same length"):
        mse([1.0], [1.0, 2.0])
