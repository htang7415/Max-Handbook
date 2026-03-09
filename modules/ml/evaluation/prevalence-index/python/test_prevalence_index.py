import math

import pytest

from prevalence_index import prevalence_index


def test_prevalence_index_normalizes_positive_rate_by_baseline() -> None:
    score = prevalence_index([1, 0, 1, 1], baseline_rate=0.25)

    assert score == pytest.approx(3.0)


def test_prevalence_index_returns_infinity_for_positive_rate_over_zero_baseline() -> None:
    assert math.isinf(prevalence_index([1, 1], baseline_rate=0.0))


def test_prevalence_index_returns_zero_for_empty_input() -> None:
    assert prevalence_index([], baseline_rate=0.5) == pytest.approx(0.0)


def test_prevalence_index_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="0 or 1"):
        prevalence_index([1, 2], baseline_rate=0.5)
