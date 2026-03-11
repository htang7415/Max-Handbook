from __future__ import annotations


def structured_log(
    service: str,
    level: str,
    message: str,
    context: dict[str, object] | None = None,
) -> dict[str, object]:
    cleaned_service = service.strip()
    cleaned_level = level.strip().lower()
    cleaned_message = message.strip()
    if not cleaned_service:
        raise ValueError("service must be non-empty")
    if cleaned_level not in {"debug", "info", "warn", "error"}:
        raise ValueError("level must be one of debug, info, warn, error")
    if not cleaned_message:
        raise ValueError("message must be non-empty")
    return {
        "service": cleaned_service,
        "level": cleaned_level,
        "message": cleaned_message,
        "context": dict(context or {}),
    }


def metric_summary(name: str, values: list[float]) -> dict[str, float]:
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("name must be non-empty")
    if not values:
        raise ValueError("values must be non-empty")
    total = sum(values)
    return {
        "count": float(len(values)),
        "min": min(values),
        "max": max(values),
        "avg": total / len(values),
    }


def trace_summary(spans: list[dict[str, object]]) -> dict[str, object]:
    total_latency = 0.0
    failed_spans = 0
    for span in spans:
        latency_ms = float(span.get("latency_ms", 0.0))
        if latency_ms < 0:
            raise ValueError("span latency must be non-negative")
        total_latency += latency_ms
        if str(span.get("status", "")).lower() != "ok":
            failed_spans += 1
    return {
        "span_count": len(spans),
        "failed_spans": failed_spans,
        "total_latency_ms": total_latency,
    }
