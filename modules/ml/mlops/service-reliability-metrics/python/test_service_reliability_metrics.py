from __future__ import annotations

import pytest

from service_reliability_metrics import (
    queue_age_percentiles,
    queue_backlog_ratio,
    queue_delay,
    queue_delay_values,
    queue_utilization,
    request_sla_compliance,
    retry_rate,
    sla_violations,
    saturation_rate,
    violation_rate,
)


def test_request_sla_compliance_counts_requests_under_threshold() -> None:
    compliant, fraction = request_sla_compliance([80.0, 120.0, 220.0], sla_ms=150.0)
    assert compliant == 2
    assert fraction == pytest.approx(2 / 3)
    assert sla_violations([80.0, 120.0, 220.0], sla_ms=150.0) == [0, 0, 1]


def test_request_sla_compliance_validates_inputs() -> None:
    with pytest.raises(ValueError, match="positive"):
        request_sla_compliance([1.0], sla_ms=0.0)


def test_violation_rate_handles_empty_total() -> None:
    assert violation_rate(0, 0) == 0.0


def test_violation_rate_validates_counts() -> None:
    with pytest.raises(ValueError, match="must not exceed total"):
        violation_rate(3, 2)


def test_retry_rate_returns_fraction_of_requests_with_retries() -> None:
    retried, fraction = retry_rate([0, 2, 0, 1])
    assert retried == 2
    assert fraction == 0.5


def test_queue_delay_returns_per_item_delays_and_mean() -> None:
    delays, mean_delay = queue_delay([1.0, 4.0], [3.0, 5.0])
    assert delays == [2.0, 1.0]
    assert mean_delay == 1.5
    assert queue_delay_values([1.0, 4.0], [3.0, 5.0]) == [2.0, 1.0]


def test_queue_delay_rejects_negative_timestamps() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        queue_delay_values([-1.0], [1.0])


def test_queue_utilization_returns_fraction_and_flag() -> None:
    utilization, saturated = queue_utilization(queue_depth=12, queue_capacity=10)
    assert utilization == 1.2
    assert saturated is True


def test_queue_age_percentiles_returns_p50_and_p95() -> None:
    p50, p95 = queue_age_percentiles([1.0, 2.0, 3.0, 9.0])
    assert p50 == pytest.approx(2.5)
    assert p95 == pytest.approx(8.1)


def test_queue_backlog_ratio_normalizes_age_against_target() -> None:
    ratios, mean_ratio = queue_backlog_ratio([1.0, 3.0], target_age=2.0)
    assert ratios == [0.5, 1.5]
    assert mean_ratio == 1.0


def test_saturation_rate_counts_steps_over_threshold() -> None:
    saturated, fraction = saturation_rate([0.7, 1.0, 1.4], threshold=1.0)
    assert saturated == 2
    assert fraction == pytest.approx(2 / 3)
