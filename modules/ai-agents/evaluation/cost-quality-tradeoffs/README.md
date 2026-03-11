# Cost-Quality Tradeoffs

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Cost-quality tradeoffs compare runs by balancing output quality or success against their monetary or token cost.

## Key Points

- A better agent is not always the one with the highest raw quality.
- Cost per successful run is often a better operational metric than mean cost alone.
- Simple ratios are enough for first comparisons.

## Minimal Code Mental Model

```python
ratio = quality_per_cost([0.8, 0.9], [0.2, 0.5])
cost = cost_per_success([True, False, True], [0.2, 0.3, 0.5])
best = best_tradeoff_index([0.7, 0.9], [0.1, 0.4])
```

## Function

```python
def quality_per_cost(qualities: list[float], costs: list[float]) -> float:
def cost_per_success(successes: list[bool], costs: list[float]) -> float:
def best_tradeoff_index(qualities: list[float], costs: list[float]) -> int:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/cost-quality-tradeoffs/python -q
```
