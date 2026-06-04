# SLIs, SLOs, And Alerting

> Track: `software-engineering` | Topic: `observability`

## Concept

SLIs measure service behavior, SLOs set the target, and alerting decides when the remaining error budget is low enough that humans need to act.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Service health | You can count good and total user-visible events | The signal is only host-level noise |
| Alert design | Human action should depend on budget burn | The condition is informational only |
| Reliability review | You need to explain why a page should happen | No target SLO exists |

## First Principles

- A service level indicator should reflect user-visible quality, not just machine counters.
- Error budget is the gap between the allowed failure rate and the current failure rate.
- Alerts should page for meaningful budget burn, not for every small dip.

## Workflow

1. Count good and total events for the SLI.
2. Choose a target SLO below perfect reliability.
3. Compute remaining error budget.
4. Page when the SLO is missed.
5. Ticket when budget is low but the SLO still holds.

## Minimal Code Mental Model

```python
sli = sli_rate(good_events=995, total_events=1000)
budget = error_budget_remaining(actual_sli=sli, target_slo=0.99)
state = alert_state(actual_sli=sli, target_slo=0.99, page_when_remaining_below=0.25)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Invalid event counts | SLI exceeds possible range | `sli_rate` validates good and total events |
| Invalid SLO threshold | Error budget math breaks | `error_budget_remaining` validates `0 < target_slo < 1` |
| Paging on every dip | Alert fatigue | `alert_state` distinguishes `page`, `ticket`, and `ok` |

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
