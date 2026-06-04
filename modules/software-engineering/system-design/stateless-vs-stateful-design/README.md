# Stateless Vs Stateful Design

> Track: `software-engineering` | Topic: `system-design`

## Concept

Stateless components are easier to scale and replace, while stateful components can provide stronger locality or coordination at the cost of harder recovery.

## Use When

| Need | Bias |
| --- | --- |
| Easy horizontal scaling | Stateless component |
| Durable session or coordination | Stateful component |
| Fast local reads with acceptable rebuild | Local cache |
| Correct recovery after failure | Explicit state owner |

## First Principles

- Stateless services are usually easier to load-balance horizontally.
- Local mutable state makes failover and scaling more complicated.
- State should live where recovery and consistency rules are explicit.

## Workflow

1. Identify which data must survive process loss.
2. Decide whether state is source-of-truth, cache, or session data.
3. Place state behind explicit recovery and consistency rules.
4. Keep request handlers stateless when durable state is not required.

## Minimal Code Mental Model

```python
style = component_style(needs_durable_session=True, requires_local_cache_consistency=False)
scaling = horizontal_scaling_ease(style)
recovery = recovery_complexity(style)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Hidden local state | Failover loses user-visible progress |
| Stateless label with sticky sessions | Scaling and recovery assumptions are false |
| No state owner | Consistency bugs move between services |

## Function

```python
def component_style(needs_durable_session: bool, requires_local_cache_consistency: bool) -> str:
def horizontal_scaling_ease(style: str) -> str:
def recovery_complexity(style: str) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/system-design/stateless-vs-stateful-design/python -q
```
