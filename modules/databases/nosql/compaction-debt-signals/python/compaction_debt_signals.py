"""compaction_debt_signals - combine backlog signals into a compaction recommendation."""

from __future__ import annotations


def read_amplification(level_sstables: list[int]) -> int:
    return sum(max(count, 0) for count in level_sstables)


def debt_signals(
    level_sstables: list[int],
    tombstone_ratio: float,
    pending_bytes_mb: int,
) -> dict[str, bool]:
    return {
        "high_read_amp": read_amplification(level_sstables) >= 14,
        "high_tombstones": tombstone_ratio >= 0.2,
        "high_pending_bytes": pending_bytes_mb >= 512,
    }


def recommended_action(
    level_sstables: list[int],
    tombstone_ratio: float,
    pending_bytes_mb: int,
) -> str:
    signals = debt_signals(level_sstables, tombstone_ratio, pending_bytes_mb)
    signal_count = sum(1 for value in signals.values() if value)
    if signal_count >= 2:
        return "compact-now"
    if signal_count == 1:
        return "compact-soon"
    return "observe"


def compaction_summary(
    level_sstables: list[int],
    tombstone_ratio: float,
    pending_bytes_mb: int,
) -> dict[str, object]:
    signals = debt_signals(level_sstables, tombstone_ratio, pending_bytes_mb)
    return {
        "read_amplification": read_amplification(level_sstables),
        "tombstone_ratio": max(tombstone_ratio, 0.0),
        "pending_bytes_mb": max(pending_bytes_mb, 0),
        "signals": signals,
        "recommended_action": recommended_action(
            level_sstables,
            tombstone_ratio,
            pending_bytes_mb,
        ),
    }
