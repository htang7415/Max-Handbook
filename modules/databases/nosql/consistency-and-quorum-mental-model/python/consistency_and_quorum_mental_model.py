"""consistency_and_quorum_mental_model - overlap rules for replicated reads and writes."""

from __future__ import annotations


def majority_quorum(replication_factor: int) -> int:
    if replication_factor <= 0:
        raise ValueError("replication_factor must be positive")
    return replication_factor // 2 + 1


def quorums_overlap(
    read_quorum: int,
    write_quorum: int,
    replication_factor: int,
) -> bool:
    return read_quorum + write_quorum > replication_factor


def read_your_write_possible(
    read_quorum: int,
    write_quorum: int,
    replication_factor: int,
) -> bool:
    return quorums_overlap(read_quorum, write_quorum, replication_factor)


def stale_read_risk(
    read_quorum: int,
    write_quorum: int,
    replication_factor: int,
) -> bool:
    return not quorums_overlap(read_quorum, write_quorum, replication_factor)
