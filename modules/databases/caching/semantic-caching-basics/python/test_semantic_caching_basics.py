from semantic_caching_basics import lookup_semantic_cache, store_semantic_entry


def build_entries():
    entries: list[dict[str, object]] = []
    store_semantic_entry(
        entries,
        "find failed runs",
        "3 failed runs",
        workspace_id=7,
        version="v1",
        now=100,
    )
    store_semantic_entry(
        entries,
        "find active alerts",
        "2 active alerts",
        workspace_id=8,
        version="v1",
        now=100,
    )
    return entries


def test_similar_query_can_hit_within_same_workspace_and_version() -> None:
    entries = build_entries()

    assert lookup_semantic_cache(
        entries,
        "show failed runs",
        workspace_id=7,
        version="v1",
        now=120,
    ) == "3 failed runs"


def test_cross_workspace_or_version_scope_blocks_a_semantic_hit() -> None:
    entries = build_entries()

    assert lookup_semantic_cache(
        entries,
        "show failed runs",
        workspace_id=8,
        version="v1",
        now=120,
    ) is None
    assert lookup_semantic_cache(
        entries,
        "show failed runs",
        workspace_id=7,
        version="v2",
        now=120,
    ) is None


def test_stale_entry_does_not_hit_even_if_semantically_similar() -> None:
    entries = build_entries()

    assert lookup_semantic_cache(
        entries,
        "show failed runs",
        workspace_id=7,
        version="v1",
        now=500,
    ) is None
