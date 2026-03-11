from read_amplification_in_lsm_trees import (
    point_lookup_cost,
    tables_checked_with_bloom,
    tables_checked_without_bloom,
)
import pytest


def test_bloom_filters_reduce_but_do_not_remove_read_amplification():
    assert tables_checked_without_bloom([3, 5, 10]) == 18
    assert tables_checked_with_bloom([3, 5, 10], false_positive_tables=1) == 4

    summary = point_lookup_cost([3, 5, 10], false_positive_tables=1, table_read_ms=2)
    assert summary["latency_with_bloom_ms"] < summary["latency_without_bloom_ms"]


def test_more_levels_mean_more_point_read_work():
    shallow = point_lookup_cost([2, 3], false_positive_tables=0)
    deep = point_lookup_cost([2, 3, 4, 5], false_positive_tables=0)

    assert deep["tables_without_bloom"] > shallow["tables_without_bloom"]
    assert deep["tables_with_bloom"] > shallow["tables_with_bloom"]


def test_invalid_lsm_inputs_are_rejected():
    with pytest.raises(ValueError, match="level_sstables"):
        tables_checked_without_bloom([3, -1, 10])

    with pytest.raises(ValueError, match="false_positive_tables"):
        point_lookup_cost([3, 5, 10], false_positive_tables=-1)
