from __future__ import annotations

import pytest

from latency_budgeting import (
    largest_latency_contributor,
    latency_budget_exceeded,
    remaining_latency_budget_ms,
)


def test_latency_budget_tracks_remaining_headroom() -> None:
    assert remaining_latency_budget_ms(total_budget_ms=300, observed_steps_ms=[40, 80, 60]) == 120
    assert latency_budget_exceeded(total_budget_ms=300, observed_steps_ms=[40, 80, 60, 150]) is True


def test_largest_latency_contributor_finds_the_bottleneck() -> None:
    assert largest_latency_contributor({"api": 40, "db": 120, "cache": 20}) == "db"


def test_latency_validation_rejects_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        remaining_latency_budget_ms(total_budget_ms=-1, observed_steps_ms=[10])
    with pytest.raises(ValueError):
        largest_latency_contributor({})
