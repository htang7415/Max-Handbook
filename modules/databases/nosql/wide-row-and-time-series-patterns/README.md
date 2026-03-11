# Wide Row And Time Series Patterns

> Track: `databases` | Topic: `nosql`

## Concept

Wide-row and time-series models group many related events under one partition key so recent reads stay local to the entity and time bucket that matters.

## Key Points

- Partition keys usually combine entity identity with a time bucket like day or hour.
- Appends are cheap when writes land in one ordered row family or partition.
- Reads stay efficient when they target a narrow key range instead of scanning the whole dataset.
- Time buckets prevent one entity from creating an unbounded hot partition.

## Minimal Code Mental Model

```python
store = {}
write_point(store, "sensor-1", "2026-03-11T10:00:00Z", 18.2)
write_point(store, "sensor-1", "2026-03-11T10:05:00Z", 18.7)
day_points = points_for_day(store, "sensor-1", "2026-03-11")
recent = recent_points(store, "sensor-1", ["2026-03-10", "2026-03-11"], limit=2)
```

## Function

```python
def partition_key(series_id: str, timestamp: str) -> tuple[str, str]:
def write_point(
    store: dict[tuple[str, str], list[dict[str, object]]],
    series_id: str,
    timestamp: str,
    value: float,
) -> None:
def points_for_day(
    store: dict[tuple[str, str], list[dict[str, object]]],
    series_id: str,
    day: str,
) -> list[dict[str, object]]:
def recent_points(
    store: dict[tuple[str, str], list[dict[str, object]]],
    series_id: str,
    day_buckets: list[str],
    limit: int,
) -> list[dict[str, object]]:
```

## Run tests

```bash
pytest modules/databases/nosql/wide-row-and-time-series-patterns/python -q
```
