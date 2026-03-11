from __future__ import annotations

import pytest

from cost_quality_tradeoffs import best_tradeoff_index, cost_per_success, quality_per_cost


def test_cost_quality_tradeoffs_compare_runs() -> None:
    assert quality_per_cost([0.8, 0.9], [0.2, 0.5]) == pytest.approx(1.7 / 0.7)
    assert cost_per_success([True, False, True], [0.2, 0.3, 0.5]) == pytest.approx(0.5)
    assert best_tradeoff_index([0.7, 0.9], [0.1, 0.4]) == 0


def test_cost_quality_tradeoffs_validation() -> None:
    with pytest.raises(ValueError):
        quality_per_cost([], [])
    with pytest.raises(ValueError):
        quality_per_cost([0.8], [0.0])
    with pytest.raises(ValueError):
        cost_per_success([False, False], [0.2, 0.3])
    with pytest.raises(ValueError):
        best_tradeoff_index([0.7], [-0.1])
