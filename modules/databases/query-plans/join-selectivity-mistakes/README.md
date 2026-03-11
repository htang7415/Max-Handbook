# Join Selectivity Mistakes

> Track: `databases` | Topic: `query-plans`

## Concept

Join plans depend on how many rows the optimizer thinks will survive each filter. If that selectivity estimate is badly wrong, the chosen join strategy can be wrong too.

## Key Points

- Nested loops are fine when the outer side is tiny.
- Hash joins are usually better once the filtered side gets larger.
- A small estimated row count can make a nested loop look cheap even when the real result is much larger.
- This is why stale stats and correlated predicates can cause sudden plan regressions.

## Minimal Code Mental Model

```python
summary = plan_outcome(
    base_outer_rows=1_000,
    estimated_selectivity=0.005,
    actual_selectivity=0.5,
    inner_rows=10_000,
)
```

## Function

```python
def filtered_rows(base_rows: int, selectivity: float) -> int:
def join_work(strategy: str, outer_rows: int, inner_rows: int) -> int:
def choose_join_strategy(estimated_outer_rows: int, nested_loop_outer_threshold: int = 10) -> str:
def plan_outcome(
    base_outer_rows: int,
    estimated_selectivity: float,
    actual_selectivity: float,
    inner_rows: int,
    nested_loop_outer_threshold: int = 10,
) -> dict[str, int | str]:
```

## Run tests

```bash
pytest modules/databases/query-plans/join-selectivity-mistakes/python -q
```
