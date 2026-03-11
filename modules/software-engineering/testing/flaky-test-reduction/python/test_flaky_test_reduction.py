from __future__ import annotations

import pytest

from flaky_test_reduction import flake_risk, should_quarantine, stabilization_steps


def test_flake_risk_rises_with_uncontrolled_dependencies() -> None:
    assert flake_risk(uses_time=False, uses_network=False, shared_state=False) == "low"
    assert flake_risk(uses_time=True, uses_network=False, shared_state=False) == "medium"
    assert flake_risk(uses_time=True, uses_network=True, shared_state=False) == "high"


def test_stabilization_steps_target_the_source_of_flakiness() -> None:
    assert stabilization_steps(uses_time=True, uses_network=True, shared_state=False) == [
        "freeze time or inject clock",
        "replace network with stub",
    ]
    assert stabilization_steps(uses_time=False, uses_network=False, shared_state=False) == [
        "keep test deterministic"
    ]


def test_quarantine_is_last_resort_for_noncritical_flakes() -> None:
    assert should_quarantine(failure_rate=0.2, critical_path=False) is True
    assert should_quarantine(failure_rate=0.2, critical_path=True) is False

    with pytest.raises(ValueError):
        should_quarantine(failure_rate=1.5, critical_path=False)
