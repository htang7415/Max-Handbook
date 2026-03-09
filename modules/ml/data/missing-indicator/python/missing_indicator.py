from __future__ import annotations


def missing_indicators(table: list[list[float | None]]) -> list[list[int]]:
    if not table:
        return []

    width = len(table[0])
    for row in table:
        if len(row) != width:
            raise ValueError("all rows must have the same length")

    return [[1 if value is None else 0 for value in row] for row in table]
