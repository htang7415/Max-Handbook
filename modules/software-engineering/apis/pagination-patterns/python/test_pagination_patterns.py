from __future__ import annotations

import pytest

from pagination_patterns import cursor_page, offset_page, pagination_strategy


ITEMS = [
    {"id": 1, "title": "a"},
    {"id": 2, "title": "b"},
    {"id": 3, "title": "c"},
    {"id": 4, "title": "d"},
]


def test_offset_page_returns_requested_slice() -> None:
    assert offset_page(ITEMS, offset=1, limit=2) == [
        {"id": 2, "title": "b"},
        {"id": 3, "title": "c"},
    ]


def test_cursor_page_returns_stable_page_and_next_cursor() -> None:
    first_page, next_cursor = cursor_page(ITEMS, cursor=None, limit=2)
    second_page, final_cursor = cursor_page(ITEMS, cursor=next_cursor, limit=2)

    assert first_page == [{"id": 1, "title": "a"}, {"id": 2, "title": "b"}]
    assert next_cursor == "2"
    assert second_page == [{"id": 3, "title": "c"}, {"id": 4, "title": "d"}]
    assert final_cursor is None


def test_pagination_strategy_prefers_cursor_for_churn_and_offset_for_random_access() -> None:
    assert pagination_strategy(high_churn=True, needs_random_access=False) == "cursor"
    assert pagination_strategy(high_churn=False, needs_random_access=True) == "offset"

    with pytest.raises(ValueError):
        cursor_page(ITEMS, cursor="missing", limit=2)
