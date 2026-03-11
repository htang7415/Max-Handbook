from __future__ import annotations


def run_success_rate(runs: list[dict[str, object]]) -> float:
    if not runs:
        raise ValueError("runs must be non-empty")
    successes = sum(1 for run in runs if bool(run.get("success")))
    return successes / len(runs)


def mean_run_latency_ms(runs: list[dict[str, object]]) -> float:
    if not runs:
        raise ValueError("runs must be non-empty")
    latencies = [float(run.get("latency_ms", 0.0)) for run in runs]
    if any(latency < 0 for latency in latencies):
        raise ValueError("latency_ms must be non-negative")
    return sum(latencies) / len(latencies)


def failed_span_counts(traces: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for trace in traces:
        spans = trace.get("spans", [])
        if not isinstance(spans, list):
            continue
        for span in spans:
            if not isinstance(span, dict):
                continue
            status = str(span.get("status", "")).strip().lower()
            if status == "ok":
                continue
            name = str(span.get("name", "")).strip()
            if not name:
                continue
            counts[name] = counts.get(name, 0) + 1
    return counts
