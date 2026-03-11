# Phantom Reads Basics

> Track: `databases` | Topic: `transactions`

## Concept

A phantom read happens when the same range query sees a different set of matching rows because another transaction inserted or removed rows in that range.

## Key Points

- The problem is about a predicate range, not one row ID.
- A second read can return extra rows even if none of the original rows changed.
- Snapshot-style repeatable reads usually hold the earlier picture steady; weaker semantics may not.
- This is why “count rows where status = open” can be unstable across a transaction without stronger isolation.

## Minimal Code Mental Model

```python
summary = phantom_summary(
    initial_rows=[task_row(1, 8), task_row(2, 3)],
    inserted_row=task_row(3, 9),
    min_priority=8,
)
```

## Function

```python
def task_row(task_id: int, priority: int) -> dict[str, int]:
def matching_task_ids(rows: list[dict[str, int]], min_priority: int) -> list[int]:
def read_committed_counts(
    initial_rows: list[dict[str, int]],
    inserted_row: dict[str, int],
    min_priority: int,
) -> tuple[int, int]:
def repeatable_read_counts(
    initial_rows: list[dict[str, int]],
    inserted_row: dict[str, int],
    min_priority: int,
) -> tuple[int, int]:
```

## Run tests

```bash
pytest modules/databases/transactions/phantom-reads-basics/python -q
```
