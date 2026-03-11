# Exact Vs ANN Search

> Track: `databases` | Topic: `vector-db`

## Concept

Exact search scores every vector, while approximate nearest neighbor search prunes the candidate set to trade some recall for lower latency.

## Key Points

- Exact search is the correctness baseline.
- ANN is a candidate-pruning strategy, not a different similarity metric.
- ANN usually evaluates fewer vectors than exact search.
- Lower candidate count can lower latency, but it can also miss a true nearest neighbor.
- Query and document vectors should be real non-empty vectors, and `k` should not be negative.

## Minimal Code Mental Model

```python
exact = exact_top_k(query, docs, k=2)
ann, candidates = ann_top_k(query, docs, k=2, threshold=0.8)
recall = recall_at_k(exact, ann)
```

## Function

```python
def validate_vector(vector: list[float]) -> None:
def validate_k(k: int) -> None:
def cosine_similarity(left: list[float], right: list[float]) -> float:
def bucket_key(vector: list[float], threshold: float = 0.8) -> str:
def exact_top_k(
    query_vector: list[float],
    documents: list[dict[str, object]],
    k: int,
) -> list[tuple[str, float]]:
def ann_top_k(
    query_vector: list[float],
    documents: list[dict[str, object]],
    k: int,
    threshold: float = 0.8,
) -> tuple[list[tuple[str, float]], int]:
def recall_at_k(
    exact_results: list[tuple[str, float]],
    ann_results: list[tuple[str, float]],
) -> float:
```

## Run tests

```bash
pytest modules/databases/vector-db/exact-vs-ann-search/python -q
```
