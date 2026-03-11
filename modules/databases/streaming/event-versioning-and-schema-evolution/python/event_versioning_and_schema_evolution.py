"""event_versioning_and_schema_evolution - normalize multiple event versions into one internal shape."""

from __future__ import annotations


def order_event_v1(order_id: str, status: str) -> dict[str, object]:
    return {
        "event_name": "order.status-changed",
        "version": 1,
        "order_id": order_id,
        "status": status,
    }


def order_event_v2(order_id: str, status: str, workspace_id: int) -> dict[str, object]:
    return {
        "event_name": "order.status-changed",
        "version": 2,
        "order_id": order_id,
        "status": status,
        "workspace_id": workspace_id,
    }


def normalize_order_event(event: dict[str, object]) -> dict[str, object]:
    version = int(event["version"])
    if version == 1:
        return {
            "order_id": str(event["order_id"]),
            "status": str(event["status"]),
            "workspace_id": None,
        }
    if version == 2:
        return {
            "order_id": str(event["order_id"]),
            "status": str(event["status"]),
            "workspace_id": int(event["workspace_id"]),
        }
    raise ValueError(f"unsupported event version: {version}")


def normalized_stream(events: list[dict[str, object]]) -> list[dict[str, object]]:
    return [normalize_order_event(event) for event in events]
