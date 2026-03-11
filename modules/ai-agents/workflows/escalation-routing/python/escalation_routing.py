from __future__ import annotations


def escalation_reason(
    blocked: bool,
    confidence: float,
    threshold: float,
    attempt: int,
    max_attempts: int,
) -> str | None:
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must satisfy 0 <= value <= 1")
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("threshold must satisfy 0 <= value <= 1")
    if attempt < 0:
        raise ValueError("attempt must be non-negative")
    if max_attempts <= 0:
        raise ValueError("max_attempts must be positive")
    if blocked:
        return "policy_review"
    if confidence < threshold:
        return "low_confidence"
    if attempt >= max_attempts:
        return "retry_exhausted"
    return None


def escalation_target(reason: str | None, routing_table: dict[str, str]) -> str | None:
    if reason is None:
        return None
    return routing_table.get(reason)


def escalation_packet(task_id: str, reason: str, route: str) -> dict[str, str]:
    if not task_id.strip():
        raise ValueError("task_id must be non-empty")
    if not reason.strip():
        raise ValueError("reason must be non-empty")
    if not route.strip():
        raise ValueError("route must be non-empty")
    return {"task_id": task_id, "reason": reason, "route": route}
