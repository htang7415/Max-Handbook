# When Postgres Is Enough

> Track: `databases` | Topic: `nosql`

## Concept

Teams often reach for NoSQL too early. If the product still needs joins, transactions, ad hoc filters, and moderate scale, a relational system like Postgres is often simpler and more correct.

## Key Points

- Many products need relational features more than a narrow scale optimization.
- Joins and transactions are strong signals to stay relational.
- NoSQL becomes more attractive when access paths are extremely simple and scale pressure is unusually high.
- “Enough” means operationally simpler for the real workload, not theoretically perfect.
- If the signals are balanced, treat the result as `depends` instead of forcing a fake winner.

## Minimal Code Mental Model

```python
decision = recommend_store(
    needs_joins=True,
    needs_transactions=True,
    simple_key_access=False,
    extreme_write_scale=False,
)
```

## Function

```python
def store_scores(
    needs_joins: bool,
    needs_transactions: bool,
    simple_key_access: bool,
    extreme_write_scale: bool,
    ad_hoc_queries: bool = True,
) -> tuple[int, int]:
def recommend_store(
    needs_joins: bool,
    needs_transactions: bool,
    simple_key_access: bool,
    extreme_write_scale: bool,
    ad_hoc_queries: bool = True,
) -> str:
def decision_summary(
    needs_joins: bool,
    needs_transactions: bool,
    simple_key_access: bool,
    extreme_write_scale: bool,
    ad_hoc_queries: bool = True,
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/nosql/when-postgres-is-enough/python -q
```
