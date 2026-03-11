# Constrained Optimization for Budgeted Agent Policies

> Track: `ai-agents` | Topic: `planning`

## Concept

Constrained optimization for budgeted agent policies chooses the best feasible policy by maximizing objective value while enforcing hard limits on cost, latency, and risk.

## Key Points

- A policy is only a valid candidate if it satisfies all hard budgets.
- Among feasible policies, objective value should stay explicit and comparable.
- If nothing is feasible, the planner should review instead of silently violating constraints.

## Minimal Code Mental Model

```python
feasible = feasible_policies(policy_to_metrics, max_cost=3.0, max_latency_ms=500.0, max_risk=0.06)
choice = budgeted_policy_choice(
    policy_to_metrics,
    max_cost=3.0,
    max_latency_ms=500.0,
    max_risk=0.06,
    cost_weight=1.0,
    latency_weight=0.002,
)
```

## Function

```python
def policy_objective(expected_reward: float, cost: float, latency_ms: float, cost_weight: float = 1.0, latency_weight: float = 0.0) -> float:
def feasible_policies(
    policy_to_metrics: dict[str, dict[str, float]],
    max_cost: float,
    max_latency_ms: float,
    max_risk: float,
) -> list[str]:
def budgeted_policy_choice(
    policy_to_metrics: dict[str, dict[str, float]],
    max_cost: float,
    max_latency_ms: float,
    max_risk: float,
    cost_weight: float = 1.0,
    latency_weight: float = 0.0,
) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/planning/constrained-optimization-for-budgeted-agent-policies/python -q
```
