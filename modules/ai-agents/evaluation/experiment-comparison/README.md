# Experiment Comparison

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Experiment comparison summarizes two agent variants side by side so you can see which one is better on success, latency, and cost.

## Key Points

- A good comparison uses the same metrics for both variants.
- Success deltas are usually more important than raw counts.
- Latency and cost should be read together with quality, not in isolation.

## Minimal Code Mental Model

```python
delta = success_delta(0.72, 0.81)
winner = compare_variant_scores({"success": 0.81, "latency_ms": 140}, {"success": 0.72, "latency_ms": 120})
summary = comparison_summary("A", "B", 0.72, 0.81)
```

## Function

```python
def success_delta(baseline_success: float, candidate_success: float) -> float:
def compare_variant_scores(baseline: dict[str, float], candidate: dict[str, float]) -> str:
def comparison_summary(baseline_name: str, candidate_name: str, baseline_success: float, candidate_success: float) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/experiment-comparison/python -q
```
