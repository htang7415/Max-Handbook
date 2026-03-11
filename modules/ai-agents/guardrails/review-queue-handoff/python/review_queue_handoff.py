from __future__ import annotations


def review_priority(reason: str, confidence: float) -> str:
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must satisfy 0 <= value <= 1")
    cleaned_reason = reason.strip()
    if not cleaned_reason:
        raise ValueError("reason must be non-empty")
    if cleaned_reason == "policy_block":
        return "high"
    if cleaned_reason == "policy_review" or confidence < 0.5:
        return "medium"
    return "low"


def review_packet(task_id: str, reason: str, route: str, priority: str) -> dict[str, str]:
    if not task_id.strip():
        raise ValueError("task_id must be non-empty")
    if not reason.strip():
        raise ValueError("reason must be non-empty")
    if not route.strip():
        raise ValueError("route must be non-empty")
    if priority not in {"high", "medium", "low"}:
        raise ValueError("priority must be high, medium, or low")
    return {
        "task_id": task_id,
        "reason": reason,
        "route": route,
        "priority": priority,
    }


def send_to_review_queue(packet: dict[str, str]) -> bool:
    required = {"task_id", "reason", "route", "priority"}
    return required.issubset(packet.keys())
