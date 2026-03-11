# Hybrid Retrieval Evaluation

> Track: `databases` | Topic: `vector-db`

## Concept

Hybrid retrieval should be judged by retrieval metrics, not intuition. The useful question is whether lexical, vector, or hybrid ranking returns relevant results higher in the list.

## Key Points

- Precision at `k` tells you how many top results are relevant.
- Duplicate result ids should not get extra precision credit.
- Reciprocal rank tells you how quickly the first relevant result appears.
- A hybrid system should beat or justify itself against lexical-only and vector-only baselines.
- Evaluation should happen per query set, not by staring at one anecdotal search result.

## Minimal Code Mental Model

```python
relevant = {"q1": {"a"}, "q2": {"d"}}
runs = {
    "lexical": {"q1": ["a", "b"], "q2": ["x", "d"]},
    "hybrid": {"q1": ["a", "b"], "q2": ["d", "x"]},
}
scores = evaluate_runs(runs, relevant, k=1)
```

## Function

```python
def precision_at_k(
    ranked_ids: list[str],
    relevant_ids: set[str],
    k: int,
) -> float:
def reciprocal_rank(
    ranked_ids: list[str],
    relevant_ids: set[str],
) -> float:
def evaluate_run(
    ranked_by_query: dict[str, list[str]],
    relevant_by_query: dict[str, set[str]],
    k: int,
) -> dict[str, float]:
def evaluate_runs(
    runs: dict[str, dict[str, list[str]]],
    relevant_by_query: dict[str, set[str]],
    k: int,
) -> dict[str, dict[str, float]]:
def best_run_name(
    scores: dict[str, dict[str, float]],
    metric: str,
) -> str:
```

## Run tests

```bash
pytest modules/databases/vector-db/hybrid-retrieval-evaluation/python -q
```
