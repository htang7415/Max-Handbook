from __future__ import annotations


def start_trace(run_id: str, goal: str) -> dict[str, object]:
    if not run_id.strip():
        raise ValueError("run_id must be non-empty")
    if not goal.strip():
        raise ValueError("goal must be non-empty")
    return {
        "run_id": run_id,
        "goal": goal,
        "spans": [],
    }


def add_span(trace: dict[str, object], name: str, latency_ms: float, status: str) -> dict[str, object]:
    if not name.strip():
        raise ValueError("name must be non-empty")
    if latency_ms < 0:
        raise ValueError("latency_ms must be non-negative")
    if not status.strip():
        raise ValueError("status must be non-empty")
    spans = list(trace.get("spans", []))
    spans.append(
        {
            "name": name,
            "latency_ms": latency_ms,
            "status": status,
        }
    )
    updated = dict(trace)
    updated["spans"] = spans
    return updated


def summarize_trace(trace: dict[str, object]) -> dict[str, object]:
    spans = list(trace.get("spans", []))
    total_latency_ms = sum(float(span.get("latency_ms", 0.0)) for span in spans)
    failed_spans = sum(1 for span in spans if str(span.get("status", "")).lower() != "ok")
    return {
        "span_count": len(spans),
        "total_latency_ms": total_latency_ms,
        "failed_spans": failed_spans,
    }
