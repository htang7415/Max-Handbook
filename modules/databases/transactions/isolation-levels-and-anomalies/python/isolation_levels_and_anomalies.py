"""isolation_levels_and_anomalies - Postgres-style mapping from isolation levels to anomalies."""

from __future__ import annotations


_ORDERED_LEVELS = [
    "read-uncommitted",
    "read-committed",
    "repeatable-read",
    "serializable",
]

_ALLOWED = {
    "read-uncommitted": {
        "dirty-read",
        "nonrepeatable-read",
        "phantom-read",
        "write-skew",
    },
    "read-committed": {
        "nonrepeatable-read",
        "phantom-read",
        "write-skew",
    },
    "repeatable-read": {
        "write-skew",
    },
    "serializable": set(),
}


def allowed_anomalies(level: str) -> set[str]:
    normalized = level.strip().lower()
    if normalized not in _ALLOWED:
        raise ValueError(f"unsupported isolation level: {level}")
    return set(_ALLOWED[normalized])


def prevents(level: str, anomaly: str) -> bool:
    return anomaly not in allowed_anomalies(level)


def minimum_isolation_for(required_preventions: list[str]) -> str:
    for level in _ORDERED_LEVELS:
        if all(prevents(level, anomaly) for anomaly in required_preventions):
            return level
    return "serializable"
