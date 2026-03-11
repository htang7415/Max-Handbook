from __future__ import annotations


def offset_page(items: list[dict[str, object]], offset: int, limit: int) -> list[dict[str, object]]:
    if offset < 0 or limit <= 0:
        raise ValueError("offset must be non-negative and limit must be positive")
    return items[offset : offset + limit]


def cursor_page(
    items: list[dict[str, object]],
    cursor: str | None,
    limit: int,
    sort_key: str = "id",
) -> tuple[list[dict[str, object]], str | None]:
    if limit <= 0:
        raise ValueError("limit must be positive")
    if not sort_key.strip():
        raise ValueError("sort_key must be non-empty")

    ordered_items = sorted(items, key=lambda item: str(item[sort_key]))
    start_index = 0
    if cursor is not None:
        matches = [index for index, item in enumerate(ordered_items) if str(item[sort_key]) == cursor]
        if not matches:
            raise ValueError("cursor not found")
        start_index = matches[0] + 1

    page = ordered_items[start_index : start_index + limit]
    if not page or start_index + limit >= len(ordered_items):
        return page, None
    return page, str(page[-1][sort_key])


def pagination_strategy(high_churn: bool, needs_random_access: bool) -> str:
    if needs_random_access:
        return "offset"
    if high_churn:
        return "cursor"
    return "offset"
