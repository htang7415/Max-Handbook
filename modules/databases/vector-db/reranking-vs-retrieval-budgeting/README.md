# Reranking Vs Retrieval Budgeting

> Track: `databases` | Topic: `vector-db`

## Concept

Reranking can improve result quality, but it adds cost and latency. Budgeting means deciding when the quality gain is worth the extra stage.

## Key Points

- Retrieval-only pipelines are cheaper because they stop after the first stage.
- Reranking reads more candidates and scores them again, so it costs more.
- If reranking fits the budget and meaningfully improves quality, it is often worth it.
- If the budget is tight or the quality gain is tiny, retrieval-only may be the better system choice.

## Minimal Code Mental Model

```python
summary = pipeline_summary(
    budget_ms=120,
    retrieve_k=50,
    rerank_candidates=20,
    retrieval_cost_per_doc=1,
    rerank_cost_per_doc=2,
    expected_retrieval_mrr=0.62,
    expected_rerank_mrr=0.72,
)
```

## Function

```python
def validate_pipeline_inputs(
    budget_ms: int,
    retrieve_k: int,
    rerank_candidates: int,
    retrieval_cost_per_doc: int,
    rerank_cost_per_doc: int,
    expected_retrieval_mrr: float,
    expected_rerank_mrr: float,
) -> None:
def retrieval_only_cost(retrieve_k: int, retrieval_cost_per_doc: int) -> int:
def rerank_pipeline_cost(
    retrieve_k: int,
    rerank_candidates: int,
    retrieval_cost_per_doc: int,
    rerank_cost_per_doc: int,
) -> int:
def fits_budget(cost: int, budget_ms: int) -> bool:
def choose_pipeline(
    budget_ms: int,
    retrieve_k: int,
    rerank_candidates: int,
    retrieval_cost_per_doc: int,
    rerank_cost_per_doc: int,
    expected_retrieval_mrr: float,
    expected_rerank_mrr: float,
) -> str:
def pipeline_summary(
    budget_ms: int,
    retrieve_k: int,
    rerank_candidates: int,
    retrieval_cost_per_doc: int,
    rerank_cost_per_doc: int,
    expected_retrieval_mrr: float,
    expected_rerank_mrr: float,
) -> dict[str, int | float | str | bool]:
```

`rerank_candidates` should be a subset of the retrieved set, so it should not exceed `retrieve_k`.

## Run tests

```bash
pytest modules/databases/vector-db/reranking-vs-retrieval-budgeting/python -q
```
