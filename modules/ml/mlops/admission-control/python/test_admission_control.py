import pytest

from admission_control import admit_requests


def test_admit_requests_accepts_all_requests_when_capacity_exists() -> None:
    assert admit_requests(current_outstanding=6, incoming_requests=3, max_outstanding=10) == (3, 0)


def test_admit_requests_rejects_requests_beyond_capacity() -> None:
    assert admit_requests(current_outstanding=8, incoming_requests=5, max_outstanding=10) == (2, 3)


def test_admit_requests_rejects_everything_when_already_over_capacity() -> None:
    assert admit_requests(current_outstanding=12, incoming_requests=4, max_outstanding=10) == (0, 4)


def test_admit_requests_requires_non_negative_counts() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        admit_requests(current_outstanding=-1, incoming_requests=1, max_outstanding=5)
