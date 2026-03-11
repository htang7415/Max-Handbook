# Utility-Aware Stopping

> Track: `ai-agents` | Topic: `planning`

## Concept

Utility-aware stopping decides whether an agent should continue, review, or stop by comparing the expected value of the next step against its cost and risk.

## Key Points

- Planning should stop when the next step is no longer worth its expected value.
- Expected utility is a compact way to combine success probability, reward, cost, and risk.
- A review band is useful when a step is neither clearly worth doing nor clearly not worth doing.

## Minimal Code Mental Model

```python
utility = expected_step_utility(success_probability=0.7, success_value=10.0, step_cost=2.0, risk_penalty=1.0)
total = plan_utility([utility, 1.5, -0.5])
route = utility_stop_route(utility, min_continue_utility=1.0, max_stop_loss=-1.0)
```

## Function

```python
def expected_step_utility(
    success_probability: float,
    success_value: float,
    step_cost: float,
    risk_penalty: float = 0.0,
) -> float:
def plan_utility(step_utilities: list[float]) -> float:
def utility_stop_route(
    expected_utility: float,
    min_continue_utility: float,
    max_stop_loss: float = 0.0,
) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/planning/utility-aware-stopping/python -q
```
