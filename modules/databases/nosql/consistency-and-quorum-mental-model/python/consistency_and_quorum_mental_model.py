"""consistency_and_quorum_mental_model - overlap rules for replicated reads and writes."""

from __future__ import annotations


def validate_quorums(
    read_quorum: int,
    write_quorum: int,
    replication_factor: int,
) -> None:
    if replication_factor <= 0:
        raise ValueError("replication_factor must be positive")
    if read_quorum <= 0 or read_quorum > replication_factor:
        raise ValueError("read_quorum must be between 1 and replication_factor")
    if write_quorum <= 0 or write_quorum > replication_factor:
        raise ValueError("write_quorum must be between 1 and replication_factor")


def majority_quorum(replication_factor: int) -> int:
    if replication_factor <= 0:
        raise ValueError("replication_factor must be positive")
    return replication_factor // 2 + 1


def quorums_overlap(
    read_quorum: int,
    write_quorum: int,
    replication_factor: int,
) -> bool:
    validate_quorums(read_quorum, write_quorum, replication_factor)
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
