# Developer Experience As Leverage

> Track: `software-engineering` | Topic: `platform-and-delivery`

## Concept

Developer experience matters because slow setup, testing, or deployment feedback multiplies across every engineer and every change.

## Use When

| Signal | DX Lever |
| --- | --- |
| Slow local setup | Better bootstrap path |
| Slow tests | Faster focused feedback |
| Slow deploy feedback | Clearer pipeline status and smaller gates |
| Repeated manual steps | Automation or templates |

## First Principles

- Small per-engineer delays become large org-wide waste.
- Setup time, test feedback time, and deploy feedback time are high-signal DX metrics.
- DX work is leverage when it saves repeated minutes across many engineers every week.

## Workflow

1. Measure setup, test, and deploy feedback time.
2. Multiply repeated delay by engineers and frequency.
3. Prioritize the bottleneck that affects the most changes.
4. Keep the improvement visible so teams trust the path.

## Minimal Code Mental Model

```python
risk = feedback_loop_risk(setup_minutes=20, test_minutes=15, deploy_feedback_minutes=10)
worth_it = dx_investment_worth_it(engineers=10, minutes_saved_per_week=30)
focus = dx_priority(setup_minutes=20, test_minutes=5, deploy_feedback_minutes=8)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Optimizing rare tasks first | Little leverage for the organization |
| No baseline measurement | DX work is hard to justify or compare |
| Automation hides failures | Engineers lose trust in the toolchain |

## Function

```python
def feedback_loop_risk(setup_minutes: int, test_minutes: int, deploy_feedback_minutes: int) -> str:
def dx_investment_worth_it(engineers: int, minutes_saved_per_week: int) -> bool:
def dx_priority(setup_minutes: int, test_minutes: int, deploy_feedback_minutes: int) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/platform-and-delivery/developer-experience-as-leverage/python -q
```
