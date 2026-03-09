import pytest

from mae_loss import mae


def test_mae():
    assert mae([1.0, 2.0], [1.0, 3.0]) == 0.5


def test_mae_zero_for_perfect_prediction():
    assert mae([1.0, 2.0], [1.0, 2.0]) == 0.0


def test_mae_rejects_length_mismatch():
    with pytest.raises(ValueError, match="same length"):
        mae([1.0], [1.0, 2.0])
