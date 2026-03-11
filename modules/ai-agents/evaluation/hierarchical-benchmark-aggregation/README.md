# Hierarchical Benchmark Aggregation

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Hierarchical benchmark aggregation rolls fine-grained bucket scores up into group scores and then into one overall score without losing the intermediate structure.

## Key Points

- Benchmark trees are easier to interpret when child buckets keep explicit weights.
- Group scores should be visible before the overall score so weak areas do not disappear.
- Overall pass decisions should consider both total score and weakest-group quality.

## Minimal Code Mental Model

```python
group = weighted_group_score(buckets)
summary = hierarchical_benchmark_summary(tree)
route = hierarchical_benchmark_route(summary, min_overall_score=0.75, min_group_score=0.7)
```

## Function

```python
def weighted_group_score(bucket_to_metrics: dict[str, dict[str, float]]) -> dict[str, float]:
def hierarchical_benchmark_summary(group_to_buckets: dict[str, dict[str, dict[str, float]]]) -> dict[str, object]:
def hierarchical_benchmark_route(
    summary: dict[str, object],
    min_overall_score: float,
    min_group_score: float,
) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/hierarchical-benchmark-aggregation/python -q
```
