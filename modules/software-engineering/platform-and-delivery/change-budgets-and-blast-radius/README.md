# Change Budgets And Blast Radius

> Track: `software-engineering` | Topic: `platform-and-delivery`

## Concept

Teams should size rollout plans to the blast radius of the change instead of spending the same deployment budget on every diff.

## Use When

| Signal | Release Control |
| --- | --- |
| Write path or multi-region change | Smaller rollout and stronger gates |
| Large user percentage affected | Progressive delivery |
| Many risky changes already open | Spend less change budget |

## First Principles

- Big write-path changes deserve stricter release controls than tiny read-only fixes.
- Blast radius comes from who is affected, how fast the effect propagates, and whether rollback is cheap.
- Change budgets help teams avoid stacking too many risky changes into one window.

## Workflow

1. Estimate user impact, write-path risk, and regional scope.
2. Check current on-call load and other high-risk changes.
3. Pick rollout controls that match the blast radius.
4. Delay or split the change when the budget is already consumed.

## Minimal Code Mental Model

```python
radius = blast_radius(users_affected_percent=40, touches_write_path=True, multi_region=False)
budget = change_budget_available(open_high_risk_changes=1, oncall_load="medium")
rollout = progressive_delivery_required(radius, budget)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Same process for every diff | High-risk changes ship with weak controls |
| Ignoring concurrent changes | Incidents become harder to attribute and recover |
| No blast-radius estimate | Rollout plan is based on optimism |

## Function

```python
def blast_radius(users_affected_percent: int, touches_write_path: bool, multi_region: bool) -> str:
def change_budget_available(open_high_risk_changes: int, oncall_load: str) -> bool:
def progressive_delivery_required(radius: str, budget_available: bool) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/platform-and-delivery/change-budgets-and-blast-radius/python -q
```
