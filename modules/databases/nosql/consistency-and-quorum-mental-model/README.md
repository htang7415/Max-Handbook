# Consistency And Quorum Mental Model

> Track: `databases` | Topic: `nosql`

## Concept

Quorum reads and writes rely on overlapping replica sets so a read is likely to intersect the latest successful write.

## Key Points

- Replication factor `N` is the number of replicas for a value.
- Write quorum `W` is how many replicas must acknowledge a write.
- Read quorum `R` is how many replicas a read consults.
- `R` and `W` must each stay between `1` and `N`.
- The classic overlap rule is `R + W > N`.

## Math

$$
R + W > N
$$

## Minimal Code Mental Model

```python
majority = majority_quorum(3)
overlap = quorums_overlap(read_quorum=2, write_quorum=2, replication_factor=3)
safe = read_your_write_possible(read_quorum=2, write_quorum=2, replication_factor=3)
```

## Function

```python
def validate_quorums(
    read_quorum: int,
    write_quorum: int,
    replication_factor: int,
) -> None:
def majority_quorum(replication_factor: int) -> int:
def quorums_overlap(
    read_quorum: int,
    write_quorum: int,
    replication_factor: int,
) -> bool:
def read_your_write_possible(
    read_quorum: int,
    write_quorum: int,
    replication_factor: int,
) -> bool:
def stale_read_risk(
    read_quorum: int,
    write_quorum: int,
    replication_factor: int,
) -> bool:
```

## Run tests

```bash
pytest modules/databases/nosql/consistency-and-quorum-mental-model/python -q
```
