# Storage Choice Basics

> Track: `software-engineering` | Topic: `system-design`

## Concept

Storage choice should follow the access pattern and correctness requirements instead of defaulting every workload to the same database.

## Use When

| Requirement | Storage Bias |
| --- | --- |
| Transactions and constraints | Relational database |
| Flexible document lookup | Document store or search index |
| Text search | Search index |
| Embedding similarity | Vector index |
| Multiple access patterns | Hybrid with a clear source of truth |

## First Principles

- Transaction-heavy source-of-truth data usually belongs in a relational store.
- Search and vector retrieval are access patterns, not replacements for core transactional state.
- Multiple requirements often justify a hybrid design rather than forcing one store to do everything.

## Workflow

1. Start with correctness and source-of-truth needs.
2. List primary read and write access patterns.
3. Choose the transactional store first when invariants matter.
4. Add search or vector indexes as derived access paths when needed.

## Minimal Code Mental Model

```python
store = primary_storage(needs_transactions=True, document_search=False, vector_similarity=False)
hybrid = hybrid_needed(needs_transactions=True, document_search=True, vector_similarity=False)
tradeoff = storage_tradeoff("vector")
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Picking storage by popularity | Access pattern or correctness gap appears later |
| Treating an index as source of truth | Rebuilds and drift become dangerous |
| Forcing one store for every query | Complexity moves into application code |

## Function

```python
def primary_storage(needs_transactions: bool, document_search: bool, vector_similarity: bool) -> str:
def hybrid_needed(needs_transactions: bool, document_search: bool, vector_similarity: bool) -> bool:
def storage_tradeoff(storage: str) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/system-design/storage-choice-basics/python -q
```
