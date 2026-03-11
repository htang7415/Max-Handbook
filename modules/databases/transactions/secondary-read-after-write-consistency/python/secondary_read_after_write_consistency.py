"""secondary_read_after_write_consistency - a lagging secondary can miss the latest committed write."""

from __future__ import annotations


def version(lsn: int, value: str) -> dict[str, object]:
    return {
        "lsn": lsn,
        "value": value,
    }


def visible_value(versions: list[dict[str, object]], applied_lsn: int) -> str | None:
    visible = [row for row in versions if int(row["lsn"]) <= applied_lsn]
    if not visible:
        return None
    return str(visible[-1]["value"])


def can_secondary_serve(last_write_lsn: int, secondary_applied_lsn: int) -> bool:
    return secondary_applied_lsn >= last_write_lsn


def read_after_write_summary(
    versions: list[dict[str, object]],
    last_write_lsn: int,
    secondary_applied_lsn: int,
) -> dict[str, object]:
    secondary_value = visible_value(versions, secondary_applied_lsn)
    primary_value = visible_value(versions, last_write_lsn)
    return {
        "secondary_value": secondary_value,
        "primary_value": primary_value,
        "secondary_is_safe": can_secondary_serve(last_write_lsn, secondary_applied_lsn),
        "recommended_target": "secondary" if can_secondary_serve(last_write_lsn, secondary_applied_lsn) else "primary",
    }
