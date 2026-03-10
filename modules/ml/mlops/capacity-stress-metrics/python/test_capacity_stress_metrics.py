import math

import pytest

from capacity_stress_metrics import (
    breach_bucket_entropy,
    breach_bucket_share,
    breach_bucket_slope,
    breach_bucket_tail,
    capacity_breach_rate,
    excess_ratios,
    headroom_gap,
    overload_margin,
    pressure_score,
    surge_pressure,
)


def test_capacity_breach_and_headroom_capture_basic_capacity_state() -> None:
    breaches, rate = capacity_breach_rate([6.0, 9.0, 11.0], capacity=10.0)
    gaps, average_gap = headroom_gap([6.0, 9.0, 11.0], ceiling=10.0)

    assert breaches == 1
    assert rate == pytest.approx(1 / 3)
    assert gaps == [4.0, 1.0, -1.0]
    assert average_gap == pytest.approx(4 / 3)


def test_overload_and_pressure_distinguish_mild_from_severe_excess() -> None:
    observations = [8.0, 12.0, 15.0]

    assert overload_margin(observations, capacity=10.0) == pytest.approx(7 / 3)
    assert excess_ratios(observations, capacity=10.0) == pytest.approx([0.0, 0.2, 0.5])
    assert pressure_score(observations, capacity=10.0) == pytest.approx((1.2 + 1.5) / 3)
    assert surge_pressure(observations, capacity=10.0) == pytest.approx((0.2**2 + 0.5**2) / 3)


def test_bucket_metrics_summarize_breach_distribution() -> None:
    observations = [9.0, 11.0, 13.0, 18.0]
    cutoffs = [0.2, 0.5]

    assert breach_bucket_share(observations, 10.0, cutoffs) == pytest.approx([1 / 3, 1 / 3, 1 / 3])
    assert breach_bucket_entropy(observations, 10.0, cutoffs) == pytest.approx(math.log(3))
    assert breach_bucket_slope(observations, 10.0, cutoffs) == pytest.approx(0.0)
    assert breach_bucket_tail(observations, 10.0, cutoffs) == pytest.approx(1 / 3)


def test_invalid_inputs_raise() -> None:
    with pytest.raises(ValueError, match="positive"):
        capacity_breach_rate([1.0], capacity=0.0)

    with pytest.raises(ValueError, match="sorted"):
        breach_bucket_share([1.0], 1.0, [0.4, 0.2])

    with pytest.raises(ValueError, match="tail_buckets"):
        breach_bucket_tail([2.0], 1.0, [0.5], tail_buckets=0)
