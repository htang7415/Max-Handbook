import pytest

from overflow_peak import overflow_peak


def test_overflow_peak_returns_maximum_excess_length() -> None:
    assert overflow_peak([64, 120, 80, 200], max_length=100) == 100


def test_overflow_peak_returns_zero_when_nothing_overflows() -> None:
    assert overflow_peak([20, 30, 40], max_length=50) == 0


def test_overflow_peak_requires_non_negative_lengths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        overflow_peak([10, -1], max_length=64)
