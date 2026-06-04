# Incident Recovery Drill

> Track: `software-engineering` | Topic: `capstones`

## Concept

This capstone combines SLO breach detection, incident severity, mitigation choice, and postmortem follow-up into one compact recovery workflow.

## Use When

| Drill Signal | Response |
| --- | --- |
| SLO or error budget breach | Declare alert state |
| User-visible degradation | Pick mitigation by recovery option |
| Data loss risk | Escalate severity immediately |
| Service is stable again | Write follow-up actions |

## First Principles

- Incident response starts from user-visible degradation, not internal suspicion.
- Mitigation choice depends on rollback readiness, degraded-mode options, and data risk.
- Data-loss scenarios should escalate faster than ordinary availability incidents.
- Recovery is incomplete until follow-up actions are explicit.

## Workflow

1. Compare actual SLI to target SLO.
2. Classify severity from user impact, duration, and data risk.
3. Choose rollback, degraded mode, or escalation based on available options.
4. Close the drill only after postmortem follow-ups are named.

## Minimal Code Mental Model

```python
state = error_budget_state(actual_sli=0.94, target_slo=0.99)
actions = recovery_actions(state, rollback_ready=True, degraded_mode_available=False, data_loss=False)
decision = incident_recovery_decision(
    user_impacting=True,
    duration_minutes=40,
    data_loss=False,
    actual_sli=0.94,
    target_slo=0.99,
    rollback_ready=True,
    degraded_mode_available=False,
)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Starting from internal suspicion only | User impact is detected late |
| No degraded-mode option | Recovery has fewer safe choices |
| Treating data loss like availability | Severity is too low |
| No follow-up actions | The drill does not reduce future risk |

## Function

```python
def error_budget_state(
    actual_sli: float,
    target_slo: float,
    page_when_remaining_below: float = 0.25,
) -> str:
def drill_severity(user_impacting: bool, duration_minutes: int, data_loss: bool) -> str:
def recovery_actions(
    alert_state: str,
    rollback_ready: bool,
    degraded_mode_available: bool,
    data_loss: bool,
) -> list[str]:
def postmortem_followups(rollback_used: bool, missing_runbook: bool, data_loss: bool) -> list[str]:
def incident_recovery_decision(
    user_impacting: bool,
    duration_minutes: int,
    data_loss: bool,
    actual_sli: float,
    target_slo: float,
    rollback_ready: bool,
    degraded_mode_available: bool,
) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/capstones/incident-recovery-drill/python -q
```
