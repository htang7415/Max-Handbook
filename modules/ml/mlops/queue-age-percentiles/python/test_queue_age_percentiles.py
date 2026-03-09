import pytest

from queue_age_percentiles import queue_age_percentiles


def test_queue_age_percentiles_returns_p50_and_p95() -> None:
    p50, p95 = queue_age_percentiles([5.0, 1.0, 3.0, 7.0, 9.0])

    assert p50 == pytest.approx(5.0)
    assert p95 == pytest.approx(8.6)


def test_queue_age_percentiles_returns_zeroes_for_empty_input() -> None:
    assert queue_age_percentiles([]) == (0.0, 0.0)


def test_queue_age_percentiles_requires_non_negative_ages() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        queue_age_percentiles([1.0, -2.0])
