import pytest

from retry_rate import retry_rate


def test_retry_rate_counts_requests_with_any_retry() -> None:
    retried, rate = retry_rate([0, 2, 0, 1, 3])

    assert retried == 3
    assert rate == pytest.approx(3 / 5)


def test_retry_rate_returns_zero_for_empty_input() -> None:
    assert retry_rate([]) == (0, 0.0)


def test_retry_rate_requires_non_negative_counts() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        retry_rate([0, -1, 2])
