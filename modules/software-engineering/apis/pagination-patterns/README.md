# Pagination Patterns

> Track: `software-engineering` | Topic: `apis`

## Concept

Pagination controls how large result sets are split into stable pages, usually with either offset-based access or cursor-based continuation.

## Key Points

- Offset pagination is simple but can drift when rows are inserted or deleted between requests.
- Cursor pagination is better for append-heavy feeds because it resumes from a stable item boundary.
- Random page access and high-churn feeds usually want different strategies.

## Minimal Code Mental Model

```python
page = offset_page(items, offset=2, limit=2)
cursor_items, next_cursor = cursor_page(items, cursor=None, limit=2)
strategy = pagination_strategy(high_churn=True, needs_random_access=False)
```

## Function

```python
def offset_page(items: list[dict[str, object]], offset: int, limit: int) -> list[dict[str, object]]:
def cursor_page(
    items: list[dict[str, object]],
    cursor: str | None,
    limit: int,
    sort_key: str = "id",
) -> tuple[list[dict[str, object]], str | None]:
def pagination_strategy(high_churn: bool, needs_random_access: bool) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/apis/pagination-patterns/python -q
```
