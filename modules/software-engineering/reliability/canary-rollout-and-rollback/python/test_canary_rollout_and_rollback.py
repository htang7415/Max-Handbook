from __future__ import annotations

import pytest

from canary_rollout_and_rollback import (
    canary_healthy,
    next_canary_percentage,
    rollout_decision,
)


def test_canary_health_uses_baseline_plus_allowed_increase() -> None:
    assert canary_healthy(baseline_error_rate=0.01, canary_error_rate=0.015, max_increase=0.01) is True
    assert canary_healthy(baseline_error_rate=0.01, canary_error_rate=0.03, max_increase=0.01) is False


def test_rollout_expands_when_healthy_and_rolls_back_when_not() -> None:
    assert next_canary_percentage(current_percentage=10, healthy=True) == 25
    assert next_canary_percentage(current_percentage=10, healthy=False) == 0
    assert rollout_decision(current_percentage=10, healthy=True) == "expand"
    assert rollout_decision(current_percentage=10, healthy=False) == "rollback"
    assert rollout_decision(current_percentage=50, healthy=True) == "complete"


def test_validation_rejects_unknown_steps() -> None:
    with pytest.raises(ValueError):
        next_canary_percentage(current_percentage=7, healthy=True)
