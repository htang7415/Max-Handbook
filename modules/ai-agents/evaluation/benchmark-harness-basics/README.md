# Benchmark Harness Basics

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Benchmark harness basics turn a fixed set of cases, bucket labels, and a frozen baseline into one repeatable evaluation suite for agent variants.

Use this after `agent-evaluation-basics`: that module defines the metrics, while this module defines the repeatable suite and release gate.

## Key Points

- A benchmark harness should keep the task set stable while variants change.
- Bucket counts help you see whether coverage is balanced across failure modes or task types.
- A frozen baseline turns benchmark runs into an auditable gate instead of a moving target.
- This module does not define raw success or latency metrics; it packages those metrics into a repeatable comparison.

## Minimal Code Mental Model

```python
manifest = benchmark_manifest(["tool-use", "tool-use", "planning", "guardrails"])
baseline = baseline_snapshot("agent-v1", {"success": 0.78, "latency_ms": 140.0})
gate = benchmark_gate(candidate_success=0.76, baseline_success=0.78, min_success=0.75, max_drop=0.03)
```

## Function

```python
def benchmark_manifest(case_buckets: list[str]) -> dict[str, object]:
def baseline_snapshot(name: str, metrics: dict[str, float]) -> dict[str, object]:
def benchmark_gate(
    candidate_success: float,
    baseline_success: float,
    min_success: float,
    max_drop: float,
) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/benchmark-harness-basics/python -q
```
