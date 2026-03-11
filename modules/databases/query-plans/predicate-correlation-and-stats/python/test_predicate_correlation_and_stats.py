import pytest

from predicate_correlation_and_stats import correlation_summary, independent_estimate


def test_independence_assumption_can_severely_underestimate_correlated_filters() -> None:
    summary = correlation_summary(table_rows=1_000_000, selectivities=[0.2, 0.2])

    assert summary == {
        "independent_estimate": 40_000,
        "correlated_actual_rows": 200_000,
        "q_error": 5.0,
        "needs_extended_stats": True,
    }


def test_less_extreme_correlation_still_reduces_the_gap() -> None:
    summary = correlation_summary(table_rows=1_000_000, selectivities=[0.4, 0.4])

    assert summary["independent_estimate"] == 160_000
    assert summary["correlated_actual_rows"] == 400_000
    assert summary["needs_extended_stats"] is False


def test_invalid_selectivity_is_rejected() -> None:
    with pytest.raises(ValueError):
        independent_estimate(1_000, [0.4, 1.5])
