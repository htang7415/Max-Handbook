# Key Value Patterns

> Track: `databases` | Topic: `nosql`

## Concept

Key-value stores are best when the application already knows the exact lookup key. They are excellent for predictable point reads and writes, but weak when the product needs secondary queries or joins.

## Key Points

- The hot path should be `get(key)` or `put(key, value)`.
- Keys should be predictable from the request itself.
- Secondary lookups usually require extra indexes or a full scan outside the core pattern.
- This model fits sessions, feature flags, counters, and cached aggregates.

## Minimal Code Mental Model

```python
put_value(store, "session:s1", {"user_id": 42})
session = get_value(store, "session:s1")
```

## Function

```python
def put_value(store: dict[str, object], key: str, value: object) -> None:
def get_value(store: dict[str, object], key: str) -> object | None:
def user_session_keys(store: dict[str, object], user_id: int) -> list[str]:
def access_summary(store: dict[str, object], key: str, user_id: int) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/nosql/key-value-patterns/python -q
```
