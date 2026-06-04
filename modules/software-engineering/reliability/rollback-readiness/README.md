# Rollback Readiness

> Track: `software-engineering` | Topic: `reliability`

## Concept

A change is only truly deployable when the team can reverse it quickly under failure, with a clear rollback path for flags, configuration, and schema coupling.

## Use When

| Situation | Rollback Requirement |
| --- | --- |
| Code behavior can be disabled | Feature flag or config switch |
| Storage shape changes | Reversible or backward-compatible schema |
| Rollout risk is non-trivial | Canary and explicit stop criteria |

## First Principles

- A feature flag alone is not a rollback strategy if the schema is already irreversible.
- Rollback blockers should be explicit before deployment starts.
- The safest rollback is the one planned before the canary fails.

## Workflow

1. List flags, config changes, migrations, and dependent services.
2. Mark which pieces can be reversed independently.
3. Define canary metrics and rollback triggers.
4. Do not deploy until blockers are visible and accepted.

## Minimal Code Mental Model

```python
blockers = rollback_blockers(flagged=True, reversible_schema=False, canary=True)
ready = rollback_ready(flagged=True, reversible_schema=True, canary=True)
risk = rollback_risk(flagged=False, reversible_schema=True, canary=False)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Irreversible schema first | Code rollback cannot restore behavior |
| No canary | Bad changes reach too much traffic before detection |
| Blockers discovered during incident | Recovery becomes improvised |

## Function

```python
def rollback_blockers(flagged: bool, reversible_schema: bool, canary: bool) -> list[str]:
def rollback_ready(flagged: bool, reversible_schema: bool, canary: bool) -> bool:
def rollback_risk(flagged: bool, reversible_schema: bool, canary: bool) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/reliability/rollback-readiness/python -q
```
