from compaction_debt_signals import compaction_summary, recommended_action


def test_low_backlog_stays_in_observe_mode() -> None:
    assert recommended_action([2, 1, 0], tombstone_ratio=0.05, pending_bytes_mb=64) == "observe"


def test_multiple_signals_trigger_compact_now() -> None:
    summary = compaction_summary([7, 6, 4], tombstone_ratio=0.24, pending_bytes_mb=900)

    assert summary["recommended_action"] == "compact-now"
    assert summary["signals"] == {
        "high_read_amp": True,
        "high_tombstones": True,
        "high_pending_bytes": True,
    }
