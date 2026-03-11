# Delegation Budgets

> Track: `ai-agents` | Topic: `multi-agent`

## Concept

Delegation budgets split a shared worker budget across agents, detect which workers exceed their share, and decide whether the coordinator can execute, rebalance, or should review.

## Key Points

- Delegation should be bounded by explicit budgets, not only by task text.
- Worker budgets should be proportional to role importance or expected workload.
- If only some workers exceed budget, rebalancing is better than failing the whole plan.

## Minimal Code Mental Model

```python
budgets = proportional_worker_budgets({"research": 2.0, "writer": 1.0}, total_budget=6.0, reserve_budget=1.0)
over_budget = over_budget_workers({"research": 3.5, "writer": 1.0}, budgets)
route = delegation_budget_route({"research": 3.5, "writer": 1.0}, budgets)
```

## Function

```python
def proportional_worker_budgets(worker_weights: dict[str, float], total_budget: float, reserve_budget: float = 0.0) -> dict[str, float]:
def over_budget_workers(worker_costs: dict[str, float], worker_budgets: dict[str, float]) -> list[str]:
def delegation_budget_route(worker_costs: dict[str, float], worker_budgets: dict[str, float]) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/multi-agent/delegation-budgets/python -q
```
