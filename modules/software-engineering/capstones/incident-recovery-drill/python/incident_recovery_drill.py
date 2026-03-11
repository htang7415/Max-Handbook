from __future__ import annotations


def error_budget_state(
    actual_sli: float,
    target_slo: float,
    page_when_remaining_below: float = 0.25,
) -> str:
    if not 0 <= actual_sli <= 1:
        raise ValueError("actual_sli must be between 0 and 1")
    if not 0 < target_slo < 1:
        raise ValueError("target_slo must be between 0 and 1")
    if not 0 <= page_when_remaining_below <= 1:
        raise ValueError("page_when_remaining_below must be between 0 and 1")

    allowed_failure_rate = 1 - target_slo
    actual_failure_rate = 1 - actual_sli
    remaining = (allowed_failure_rate - actual_failure_rate) / allowed_failure_rate
    remaining = max(0.0, min(1.0, remaining))
    if actual_sli < target_slo:
        return "page"
    if remaining <= page_when_remaining_below:
        return "ticket"
    return "ok"


def drill_severity(user_impacting: bool, duration_minutes: int, data_loss: bool) -> str:
    if duration_minutes < 0:
        raise ValueError("duration_minutes must be non-negative")
    if data_loss:
        return "sev1"
    if user_impacting and duration_minutes >= 30:
        return "sev1"
    if user_impacting:
        return "sev2"
    return "sev3"


def recovery_actions(
    alert_state: str,
    rollback_ready: bool,
    degraded_mode_available: bool,
    data_loss: bool,
) -> list[str]:
    if data_loss:
        return ["freeze-writes", "engage-data-recovery"]
    if alert_state == "page" and rollback_ready:
        return ["rollback"]
    if alert_state == "page" and degraded_mode_available:
        return ["degrade-noncritical-features"]
    if alert_state == "ticket":
        return ["investigate", "watch-metrics"]
    return ["monitor"]


def postmortem_followups(rollback_used: bool, missing_runbook: bool, data_loss: bool) -> list[str]:
    actions: list[str] = []
    if rollback_used:
        actions.append("reduce-rollback-latency")
    if missing_runbook:
        actions.append("write-runbook")
    if data_loss:
        actions.append("add-data-recovery-drill")
    if not actions:
        actions.append("verify-alert-thresholds")
    return actions


def incident_recovery_decision(
    user_impacting: bool,
    duration_minutes: int,
    data_loss: bool,
    actual_sli: float,
    target_slo: float,
    rollback_ready: bool,
    degraded_mode_available: bool,
) -> str:
    severity = drill_severity(user_impacting, duration_minutes, data_loss)
    alert = error_budget_state(actual_sli, target_slo)
    actions = recovery_actions(alert, rollback_ready, degraded_mode_available, data_loss)

    if actual_sli >= target_slo:
        return "stabilized"
    if "freeze-writes" in actions:
        return "declare-sev1"
    if "rollback" in actions:
        return "rollback-now"
    if "degrade-noncritical-features" in actions:
        return "degrade-service"
    if severity == "sev1":
        return "escalate-incident"
    return "investigate"
