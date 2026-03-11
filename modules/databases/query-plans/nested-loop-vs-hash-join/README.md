# Nested Loop Vs Hash Join

> Track: `databases` | Topic: `query-plans`

## Concept

Join strategy depends on how many rows arrive at the join and whether the inner side can be probed efficiently. Nested loops are great when the outer side is small and the inner side is indexed; hash joins are usually better for larger equality joins.

## Key Points

- Nested loops get expensive when they must rescan a large inner input.
- Hash joins pay upfront build cost, then probe cheaply.
- Equality joins are the usual case for hash joins.
- A small filtered outer input can still make nested loops the right choice.

## Minimal Code Mental Model

```python
strategy = choose_join_strategy(outer_rows=20, inner_rows=100_000, indexed_lookup=True)
```

## Function

```python
def nested_loop_cost(outer_rows: int, inner_rows: int, indexed_lookup: bool) -> int:
def hash_join_cost(left_rows: int, right_rows: int) -> int:
def choose_join_strategy(
    outer_rows: int,
    inner_rows: int,
    indexed_lookup: bool,
    equality_join: bool = True,
) -> str:
def join_cost_summary(
    outer_rows: int,
    inner_rows: int,
    indexed_lookup: bool,
    equality_join: bool = True,
) -> dict[str, int | str]:
```

## Run tests

```bash
pytest modules/databases/query-plans/nested-loop-vs-hash-join/python -q
```
