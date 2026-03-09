import pytest

from queue_delay import queue_delay


def test_queue_delay_returns_per_request_delays_and_mean() -> None:
    delays, average = queue_delay(
        enqueued_at=[1.0, 2.0, 4.0],
        started_at=[1.5, 3.0, 5.0],
    )

    assert delays == pytest.approx([0.5, 1.0, 1.0])
    assert average == pytest.approx(5.0 / 6.0)


def test_queue_delay_returns_zero_for_empty_input() -> None:
    assert queue_delay([], []) == ([], 0.0)


def test_queue_delay_requires_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        queue_delay([1.0], [1.0, 2.0])


def test_queue_delay_rejects_negative_waiting_time() -> None:
    with pytest.raises(ValueError, match="at or after"):
        queue_delay([3.0], [2.0])
