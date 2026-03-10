import pytest

from uncertainty_intervals import (
    bootstrap_percentile_interval,
    mean_confidence_interval,
    sample_mean_and_std,
    standard_error,
    wilson_interval,
)


def test_mean_confidence_interval_brackets_the_sample_mean() -> None:
    lower, upper = mean_confidence_interval([1.0, 2.0, 3.0, 4.0])
    assert lower < 2.5 < upper


def test_bootstrap_percentile_interval_returns_requested_percentiles() -> None:
    lower, upper = bootstrap_percentile_interval([1.0, 2.0, 3.0, 4.0], alpha=0.5)
    assert lower == pytest.approx(1.75)
    assert upper == pytest.approx(3.25)


def test_sample_mean_and_standard_error_match_basic_statistics() -> None:
    mean, std = sample_mean_and_std([1.0, 2.0, 3.0, 4.0])
    assert mean == pytest.approx(2.5)
    assert std == pytest.approx(1.2909944487)
    assert standard_error([1.0, 2.0, 3.0, 4.0]) == pytest.approx(std / 2.0)


def test_wilson_interval_stays_inside_unit_interval() -> None:
    lower, upper = wilson_interval(successes=3, trials=10)
    assert 0.0 <= lower <= upper <= 1.0


def test_invalid_inputs_raise() -> None:
    with pytest.raises(ValueError, match="at least two"):
        mean_confidence_interval([1.0])

    with pytest.raises(ValueError, match="0 < alpha < 1"):
        bootstrap_percentile_interval([1.0, 2.0], alpha=1.0)
