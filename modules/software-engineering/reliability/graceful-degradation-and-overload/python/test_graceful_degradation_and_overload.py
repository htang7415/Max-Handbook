from __future__ import annotations

import pytest

from graceful_degradation_and_overload import (
    capacity_state,
    degradation_actions,
    requests_to_shed,
)


def test_capacity_state_distinguishes_healthy_degraded_and_overloaded() -> None:
    assert capacity_state(current_rps=650, safe_rps=700, hard_rps=900) == "healthy"
    assert capacity_state(current_rps=850, safe_rps=700, hard_rps=900) == "degraded"
    assert capacity_state(current_rps=950, safe_rps=700, hard_rps=900) == "overloaded"


def test_overload_controls_disable_optional_features_and_shed_excess_requests() -> None:
    assert requests_to_shed(current_rps=950, hard_rps=900) == 50
    assert degradation_actions("degraded", ["personalization", "analytics"]) == [
        "disable:personalization",
        "disable:analytics",
    ]
    assert degradation_actions("overloaded", ["personalization"]) == [
        "disable:personalization",
        "rate-limit",
    ]


def test_capacity_validation_rejects_invalid_ranges() -> None:
    with pytest.raises(ValueError):
        capacity_state(current_rps=-1, safe_rps=700, hard_rps=900)
    with pytest.raises(ValueError):
        degradation_actions("unknown", [])
