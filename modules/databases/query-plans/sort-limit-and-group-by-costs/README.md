# Sort Limit And Group By Costs

> Track: `databases` | Topic: `query-plans`

## Concept

Sorts, limits, and group-by operations add work because the database has to organize rows, keep state, or both.

## Key Points

- A full sort usually costs more than a top-N sort for a small limit.
- An index that already matches the order can avoid sort work entirely.
- Group-by cost grows with both input rows and the number of groups that must be tracked.
- Sort and aggregation operators often become the bottleneck after filtering is already selective.

## Minimal Code Mental Model

```python
full = full_sort_work_units(100000)
top_n = top_n_sort_work_units(100000, limit=20)
group = hash_group_by_work_units(100000, distinct_groups=500)
plan = choose_order_plan(100000, limit=20, has_covering_index=False)
```

## Function

```python
def full_sort_work_units(row_count: int) -> float:
def top_n_sort_work_units(row_count: int, limit: int) -> float:
def hash_group_by_work_units(row_count: int, distinct_groups: int) -> int:
def choose_order_plan(row_count: int, limit: int, has_covering_index: bool) -> str:
def plan_cost_summary(
    row_count: int,
    limit: int,
    distinct_groups: int,
    has_covering_index: bool,
) -> dict[str, float | int | str]:
```

## Run tests

```bash
pytest modules/databases/query-plans/sort-limit-and-group-by-costs/python -q
```
