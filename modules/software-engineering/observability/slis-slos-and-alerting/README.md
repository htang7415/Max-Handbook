# SLIs, SLOs, And Alerting

> Track: `software-engineering` | Topic: `observability`

## Concept

SLIs measure service behavior, SLOs set the target, and alerting decides when the remaining error budget is low enough that humans need to act.

## Key Points

- A service level indicator should reflect user-visible quality, not just machine counters.
- Error budget is the gap between the allowed failure rate and the current failure rate.
- Alerts should page for meaningful budget burn, not for every small dip.

## Minimal Code Mental Model

```python
sli = sli_rate(good_events=995, total_events=1000)
budget = error_budget_remaining(actual_sli=sli, target_slo=0.99)
state = alert_state(actual_sli=sli, target_slo=0.99, page_when_remaining_below=0.25)
```

## Function

```python
def sli_rate(good_events: int, total_events: int) -> float:
def error_budget_remaining(actual_sli: float, target_slo: float) -> float:
def alert_state(actual_sli: float, target_slo: float, page_when_remaining_below: float = 0.25) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/observability/slis-slos-and-alerting/python -q
```
