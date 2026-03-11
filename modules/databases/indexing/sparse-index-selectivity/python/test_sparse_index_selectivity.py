import pytest

from sparse_index_selectivity import selectivity_summary, sparse_index_entries


def test_sparse_index_is_much_smaller_when_few_rows_populate_the_column() -> None:
    assert selectivity_summary(total_rows=1_000_000, populated_fraction=0.01, matching_rows=100) == {
        "full_index_entries": 1_000_000,
        "sparse_index_entries": 10_000,
        "entries_saved": 990_000,
        "match_fraction_within_sparse_index": 0.01,
    }


def test_dense_column_saves_little_with_a_sparse_index() -> None:
    summary = selectivity_summary(total_rows=1_000_000, populated_fraction=0.9, matching_rows=90_000)

    assert summary["sparse_index_entries"] == 900_000
    assert summary["entries_saved"] == 100_000


def test_invalid_fraction_is_rejected() -> None:
    with pytest.raises(ValueError):
        sparse_index_entries(100, 1.5)
