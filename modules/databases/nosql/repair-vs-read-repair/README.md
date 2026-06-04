# Repair Vs Read-Repair

> Track: `databases` | Topic: `nosql`

## Concept

Read-repair fixes divergence only for keys that happen to be read. Background repair fixes all divergent keys whether clients read them or not.

## Key Points

- Read-repair piggybacks on a normal read path.
- Background repair scans for divergence even when no client read arrives.
- Read-repair can leave cold divergent keys broken for a long time.
- Background repair costs extra work but converges the whole replica set.

## Boundary

Use `anti-entropy-and-repair` for the basic convergence mechanism. Use this module when the design question is which trigger should repair divergence: a client read of a key or a background scan over all keys.

## Minimal Code Mental Model

```python
left = empty_replica("left")
right = empty_replica("right")
write_value(left, "doc:1", "v2", version=2)
write_value(right, "doc:1", "v1", version=1)
value, repaired = read_with_repair(left, right, "doc:1")
remaining = background_repair(left, right)
```

## Function

```python
def read_with_repair(
    left: dict[str, object],
    right: dict[str, object],
    key: str,
) -> tuple[object | None, bool]:
def background_repair(
    left: dict[str, object],
    right: dict[str, object],
) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/nosql/repair-vs-read-repair/python -q
```
