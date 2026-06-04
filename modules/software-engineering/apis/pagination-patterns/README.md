# Pagination Patterns

> Track: `software-engineering` | Topic: `apis`

## Concept

Pagination controls how large result sets are split into stable pages, usually with either offset-based access or cursor-based continuation.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Offset pagination | Users need random page access and data churn is low | Rows are frequently inserted or deleted between requests |
| Cursor pagination | Feeds are append-heavy or high-churn | Users require arbitrary page numbers |
| Strategy choice | API behavior must stay stable as result sets grow | The result set is always tiny |

## First Principles

- Offset pagination is simple but can drift when rows are inserted or deleted between requests.
- Cursor pagination is better for append-heavy feeds because it resumes from a stable item boundary.
- Random page access and high-churn feeds usually want different strategies.

## Workflow

1. Decide whether callers need random page access.
2. Estimate how often rows are inserted or deleted during traversal.
3. Use offset for low-churn random access.
4. Use cursor continuation for high-churn feeds.
5. Validate cursor and limit inputs before slicing.

## Minimal Code Mental Model

```python
page = offset_page(items, offset=2, limit=2)
cursor_items, next_cursor = cursor_page(items, cursor=None, limit=2)
strategy = pagination_strategy(high_churn=True, needs_random_access=False)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Invalid offset or limit | Pages are empty for the wrong reason | `offset_page` validates non-negative offset and positive limit |
| Missing cursor | Client resumes from an unknown item | `cursor_page` rejects unknown cursors |
| Wrong strategy | High-churn feed skips or duplicates items | `pagination_strategy` prefers cursor under churn |

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
