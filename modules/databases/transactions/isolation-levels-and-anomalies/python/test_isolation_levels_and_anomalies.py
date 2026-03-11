import pytest

from isolation_levels_and_anomalies import allowed_anomalies, minimum_isolation_for, prevents


def test_read_committed_blocks_dirty_reads_but_allows_some_read_instability() -> None:
    assert prevents("read-committed", "dirty-read") is True
    assert "nonrepeatable-read" in allowed_anomalies("read-committed")


def test_serializable_is_needed_when_write_skew_must_be_blocked() -> None:
    assert minimum_isolation_for(["write-skew"]) == "serializable"


def test_unknown_level_is_rejected() -> None:
    with pytest.raises(ValueError, match="unsupported isolation level"):
        allowed_anomalies("snapshot-ish")
