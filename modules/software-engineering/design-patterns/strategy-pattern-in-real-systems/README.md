# Strategy Pattern In Real Systems

> Track: `software-engineering` | Topic: `design-patterns`

## Concept

Strategy is useful when one stable interface needs multiple policy choices, such as selecting a deployment region by latency or by cost.

## Use When

| Situation | Strategy Fit |
| --- | --- |
| One interface has multiple policies | Strong fit |
| Policies optimize different constraints | Strong fit |
| Only one ordinary branch exists | Probably too much abstraction |

## First Principles

- The caller should not change when the policy changes.
- Different strategies often optimize different production constraints.
- Use strategy for policy selection, not for hiding ordinary conditionals.

## Workflow

1. Define the stable policy interface.
2. Implement each policy with one clear optimization goal.
3. Keep callers unaware of policy internals.
4. Remove the abstraction if variation never appears.

## Minimal Code Mental Model

```python
candidates = [
    {"name": "us-east", "latency_ms": 40, "monthly_cost": 200},
    {"name": "eu-west", "latency_ms": 60, "monthly_cost": 120},
]
assert select_region(candidates, lowest_latency) == "us-east"
assert select_region(candidates, lowest_cost) == "eu-west"
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Strategy for one branch | Indirection without flexibility |
| Broad strategy contract | Every implementation depends on unrelated data |
| Caller knows policy details | Changing strategy still changes callers |

## Function

```python
def lowest_latency(candidates: list[dict[str, int | str]]) -> dict[str, int | str]:
def lowest_cost(candidates: list[dict[str, int | str]]) -> dict[str, int | str]:
def select_region(candidates: list[dict[str, int | str]], strategy) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/design-patterns/strategy-pattern-in-real-systems/python -q
```
