from __future__ import annotations

import pytest

from incident_recovery_drill import (
    drill_severity,
    error_budget_state,
    incident_recovery_decision,
    postmortem_followups,
    recovery_actions,
)


def test_error_budget_state_and_severity_detect_user_harming_incidents() -> None:
    assert error_budget_state(actual_sli=0.94, target_slo=0.99) == "page"
    assert drill_severity(user_impacting=True, duration_minutes=40, data_loss=False) == "sev1"


def test_incident_recovery_decision_prefers_rollback_or_data_protection_actions() -> None:
    assert recovery_actions("page", rollback_ready=True, degraded_mode_available=False, data_loss=False) == [
        "rollback"
    ]
    assert incident_recovery_decision(
        user_impacting=True,
        duration_minutes=40,
        data_loss=False,
        actual_sli=0.94,
        target_slo=0.99,
        rollback_ready=True,
        degraded_mode_available=False,
    ) == "rollback-now"
    assert incident_recovery_decision(
        user_impacting=True,
        duration_minutes=5,
        data_loss=True,
        actual_sli=0.97,
        target_slo=0.99,
        rollback_ready=True,
        degraded_mode_available=False,
    ) == "declare-sev1"


def test_postmortem_followups_capture_recovery_gaps() -> None:
    assert postmortem_followups(rollback_used=True, missing_runbook=True, data_loss=False) == [
        "reduce-rollback-latency",
        "write-runbook",
    ]
    assert postmortem_followups(rollback_used=False, missing_runbook=False, data_loss=False) == [
        "verify-alert-thresholds"
    ]
    assert incident_recovery_decision(
        user_impacting=False,
        duration_minutes=5,
        data_loss=False,
        actual_sli=0.995,
        target_slo=0.99,
        rollback_ready=False,
        degraded_mode_available=False,
    ) == "stabilized"

    with pytest.raises(ValueError):
        error_budget_state(actual_sli=1.2, target_slo=0.99)
