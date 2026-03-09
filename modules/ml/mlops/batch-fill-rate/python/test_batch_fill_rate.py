import pytest

from batch_fill_rate import batch_fill_rate


def test_batch_fill_rate_reports_average_utilization() -> None:
    rate = batch_fill_rate(batch_sizes=[4, 8, 6], max_batch_size=8)

    assert rate == pytest.approx(0.75)


def test_batch_fill_rate_returns_zero_for_no_batches() -> None:
    assert batch_fill_rate(batch_sizes=[], max_batch_size=8) == pytest.approx(0.0)


def test_batch_fill_rate_rejects_oversized_batches() -> None:
    with pytest.raises(ValueError, match="cannot exceed"):
        batch_fill_rate(batch_sizes=[9], max_batch_size=8)
