import pytest

from throughput_per_dollar import throughput_per_dollar


def test_throughput_per_dollar_converts_rps_and_hourly_cost_to_requests_per_dollar() -> None:
    score = throughput_per_dollar(requests_per_second=10.0, dollars_per_hour=5.0)

    assert score == pytest.approx(7200.0)


def test_throughput_per_dollar_allows_zero_throughput() -> None:
    assert throughput_per_dollar(requests_per_second=0.0, dollars_per_hour=5.0) == pytest.approx(0.0)


def test_throughput_per_dollar_requires_positive_cost_rate() -> None:
    with pytest.raises(ValueError, match="positive"):
        throughput_per_dollar(requests_per_second=1.0, dollars_per_hour=0.0)
