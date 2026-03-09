import pytest

from dropout import dropout


def test_dropout_preserves_values_when_p_zero():
    assert dropout([1.0, 2.0, 3.0], p=0.0, seed=1) == [1.0, 2.0, 3.0]


def test_dropout_is_deterministic_for_same_seed():
    out1 = dropout([1.0, 2.0, 3.0], p=0.5, seed=1)
    out2 = dropout([1.0, 2.0, 3.0], p=0.5, seed=1)
    assert out1 == out2


def test_dropout_rejects_invalid_probability():
    with pytest.raises(ValueError, match="0 <= p < 1"):
        dropout([1.0], p=1.0, seed=0)
