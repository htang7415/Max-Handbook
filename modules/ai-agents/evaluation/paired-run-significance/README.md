# Paired Run Significance

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Paired run significance compares two agent variants on the same cases and checks whether their disagreement is large enough to treat as more than noise.

## Key Points

- Pairing matters because each variant sees the same cases.
- Discordant pairs carry the actual signal: cases where one variant succeeds and the other fails.
- A significance check should distinguish improvement, regression, and inconclusive results.

## Minimal Code Mental Model

```python
counts = paired_outcome_counts(baseline, candidate)
stat = mcnemar_statistic(counts["baseline_only"], counts["candidate_only"])
route = paired_significance_route(counts, threshold=3.84)
```

## Function

```python
def paired_outcome_counts(baseline: list[bool], candidate: list[bool]) -> dict[str, int]:
def mcnemar_statistic(baseline_only: int, candidate_only: int) -> float:
def paired_significance_route(counts: dict[str, int], threshold: float) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/paired-run-significance/python -q
```
