from __future__ import annotations

import pytest

from race_conditions_and_shared_state import (
    apply_versioned_update,
    optimistic_write_allowed,
    shared_state_risk,
)


def test_version_checks_allow_fresh_updates_and_increment_version() -> None:
    assert optimistic_write_allowed(4, 4) is True
    assert apply_versioned_update(10, delta=5, current_version=4, expected_version=4) == (15, 5)


def test_stale_version_is_rejected() -> None:
    assert optimistic_write_allowed(4, 3) is False
    with pytest.raises(ValueError):
        apply_versioned_update(10, delta=5, current_version=4, expected_version=3)


def test_shared_state_risk_rises_without_coordination() -> None:
    assert shared_state_risk(concurrent_writers=1, uses_coordination=False) == "low"
    assert shared_state_risk(concurrent_writers=3, uses_coordination=True) == "medium"
    assert shared_state_risk(concurrent_writers=3, uses_coordination=False) == "high"
