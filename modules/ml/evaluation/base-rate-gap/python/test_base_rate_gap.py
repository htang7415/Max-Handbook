import pytest

from base_rate_gap import base_rate_gap


def test_base_rate_gap_returns_signed_difference_between_positive_rates() -> None:
    gap = base_rate_gap([1, 0, 1, 1], [0, 1, 0, 0])

    assert gap == pytest.approx(0.5)


def test_base_rate_gap_handles_empty_groups_as_zero_rate() -> None:
    assert base_rate_gap([], [1, 0]) == pytest.approx(-0.5)


def test_base_rate_gap_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="0 or 1"):
        base_rate_gap([1, 2], [0, 1])
