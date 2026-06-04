# Runbooks And Dashboards

> Track: `software-engineering` | Topic: `observability`

## Concept

Runbooks tell operators what to do during an incident, and dashboards tell them whether the system is moving toward or away from recovery.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Incident response | Humans need repeatable action under pressure | The service has no operational owner |
| Dashboard review | Panels should support decisions, not decoration | The signal is not tied to a runbook action |
| Rollback or mitigation | Operators need health checks and ownership data | The system cannot be changed during an incident |

## First Principles

- A dashboard without a runbook leaves responders guessing what action to take.
- A runbook without current service signals is hard to trust under pressure.
- Missing owner, rollback, or health-check information usually turns incidents into improvisation.

## Workflow

1. Write required runbook fields: owner, symptoms, checks, mitigation, rollback.
2. Add dashboard panels for latency, error rate, traffic, and saturation as needed.
3. Compare required panels with present panels.
4. Check whether runbook and dashboard are both complete.
5. Use the combined result as operator readiness.

## Minimal Code Mental Model

```python
missing = missing_runbook_fields(runbook)
coverage = missing_dashboard_panels(["latency", "error-rate", "traffic"], ["latency", "traffic"])
ready = operator_ready(runbook, ["latency", "error-rate", "traffic"], ["latency", "error-rate", "traffic"])
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Missing owner or rollback | Incident response turns into guessing | `missing_runbook_fields` reports absent fields |
| Missing dashboard panel | Operator cannot verify recovery | `missing_dashboard_panels` reports gaps |
| Runbook and dashboard drift | Steps do not match current service signals | `operator_ready` requires both to pass |

## Function

```python
def missing_runbook_fields(runbook: dict[str, str], required_fields: list[str] | None = None) -> list[str]:
def missing_dashboard_panels(required_panels: list[str], present_panels: list[str]) -> list[str]:
def operator_ready(runbook: dict[str, str], required_panels: list[str], present_panels: list[str]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/observability/runbooks-and-dashboards/python -q
```
