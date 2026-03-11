from __future__ import annotations


def route_task(request: str, routes: dict[str, list[str]]) -> str | None:
    lowered = request.lower()
    scored: list[tuple[int, str]] = []
    for target, keywords in routes.items():
        matches = sum(1 for keyword in keywords if keyword.strip().lower() in lowered)
        if matches:
            scored.append((matches, target))
    if not scored:
        return None
    scored.sort(reverse=True)
    return scored[0][1]


def build_handoff(task_id: str, target: str, payload: dict[str, object]) -> dict[str, object]:
    if not task_id.strip():
        raise ValueError("task_id must be non-empty")
    if not target.strip():
        raise ValueError("target must be non-empty")
    return {
        "task_id": task_id,
        "target": target,
        "payload": payload,
    }


def should_retry(attempt: int, max_attempts: int, retryable: bool) -> bool:
    if attempt < 0:
        raise ValueError("attempt must be non-negative")
    if max_attempts <= 0:
        raise ValueError("max_attempts must be positive")
    return retryable and attempt < max_attempts
