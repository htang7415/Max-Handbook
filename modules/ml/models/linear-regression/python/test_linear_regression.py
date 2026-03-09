import pytest

from linear_regression import predict


def test_predict():
    assert predict([1.0, 2.0], [0.5, 1.0], 0.0) == 2.5


def test_predict_includes_bias():
    assert predict([1.0, 2.0], [0.5, 1.0], 1.5) == 4.0


def test_predict_rejects_length_mismatch():
    with pytest.raises(ValueError, match="same length"):
        predict([1.0], [1.0, 2.0], 0.0)
