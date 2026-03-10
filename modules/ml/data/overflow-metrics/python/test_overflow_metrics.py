import pytest

from overflow_metrics import (
    budget_overrun_share,
    overflow_cutoff_rate,
    overflow_cutoff_tail_mass,
    overflow_quantile,
    truncation_rate,
)


def test_truncation_rate_counts_budget_violations() -> None:
    truncated, rate = truncation_rate([4, 8, 10, 3], max_length=6)

    assert truncated == 2
    assert rate == pytest.approx(0.5)


def test_budget_overrun_share_normalizes_by_total_length() -> None:
    share = budget_overrun_share([4, 8, 10], max_length=6)

    assert share == pytest.approx(6 / 22)


def test_overflow_quantile_looks_at_overflow_amount_not_raw_length() -> None:
    quantile = overflow_quantile([6, 7, 10, 14], max_length=6, quantile=0.5)

    assert quantile == pytest.approx(2.5)


def test_cutoff_metrics_focus_on_large_failures() -> None:
    lengths = [6, 9, 11, 18]

    assert overflow_cutoff_rate(lengths, max_length=6, cutoff=4) == pytest.approx(0.5)
    assert overflow_cutoff_tail_mass(lengths, max_length=6, cutoff=2, quantile=0.5) == pytest.approx(0.85)


def test_invalid_inputs_raise() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        truncation_rate([1, -1], max_length=4)

    with pytest.raises(ValueError, match="quantile"):
        overflow_quantile([1], max_length=1, quantile=1.5)

    with pytest.raises(ValueError, match="cutoff"):
        overflow_cutoff_rate([1], max_length=1, cutoff=-1)
