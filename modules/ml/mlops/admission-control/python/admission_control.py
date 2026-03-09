from __future__ import annotations


def admit_requests(
    current_outstanding: int,
    incoming_requests: int,
    max_outstanding: int,
) -> tuple[int, int]:
    if current_outstanding < 0 or incoming_requests < 0:
        raise ValueError("request counts must be non-negative")
    if max_outstanding <= 0:
        raise ValueError("max_outstanding must be positive")

    available = max(0, max_outstanding - current_outstanding)
    admitted = min(incoming_requests, available)
    rejected = incoming_requests - admitted
    return admitted, rejected
