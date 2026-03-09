import pytest

from budget_overrun_share import budget_overrun_share


def test_budget_overrun_share_normalizes_overflow_by_total_length() -> None:
    share = budget_overrun_share([64, 120, 80, 200], max_length=100)

    assert share == pytest.approx(120 / 464)


def test_budget_overrun_share_returns_zero_for_empty_input() -> None:
    assert budget_overrun_share([], max_length=64) == pytest.approx(0.0)


def test_budget_overrun_share_requires_non_negative_lengths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        budget_overrun_share([10, -1], max_length=64)
