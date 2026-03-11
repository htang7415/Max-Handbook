# OR Predicate Plan Shapes

> Track: `databases` | Topic: `query-plans`

## Concept

`OR` predicates are awkward because they can match rows from multiple branches. Optimizers often choose between scanning the whole table or probing multiple indexes and unioning the results.

## Key Points

- `OR` can be harder to optimize than a selective `AND`.
- Narrow OR branches can justify separate index probes plus union.
- Broad OR predicates often collapse into “just scan it.”
- Overlap between branches matters because duplicate candidates still cost work.

## Minimal Code Mental Model

```python
summary = or_plan_summary(
    total_rows=1_000_000,
    left_selectivity=0.002,
    right_selectivity=0.003,
    overlap_selectivity=0.0001,
)
```

## Function

```python
def matching_rows(total_rows: int, selectivity: float) -> int:
def union_rows(
    total_rows: int,
    left_selectivity: float,
    right_selectivity: float,
    overlap_selectivity: float,
) -> int:
def index_union_cost(
    total_rows: int,
    left_selectivity: float,
    right_selectivity: float,
    overlap_selectivity: float,
    probe_overhead: int = 8,
    row_fetch_cost: int = 2,
) -> int:
def recommended_path(
    total_rows: int,
    left_selectivity: float,
    right_selectivity: float,
    overlap_selectivity: float,
) -> str:
def or_plan_summary(
    total_rows: int,
    left_selectivity: float,
    right_selectivity: float,
    overlap_selectivity: float,
) -> dict[str, int | float | str]:
```

## Run tests

```bash
pytest modules/databases/query-plans/or-predicate-plan-shapes/python -q
```
