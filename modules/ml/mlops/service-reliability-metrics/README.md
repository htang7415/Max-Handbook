# Service Reliability Metrics

> Track: `ml` | Topic: `mlops`

## Purpose

Use this module to learn the core metrics that tell you whether an online ML
service is meeting its latency and queueing obligations.

## First Principles

- Reliability is not just average latency; tail behavior and queue buildup matter.
- Queue metrics often degrade before full request latency collapses.
- Retries are an operational smell because they mean the first attempt often failed.
- SLA and saturation metrics should be read together, not in isolation.

## Core Math

Request SLA compliance:

$$
\mathrm{compliance} = \frac{\#\{t_i \le \tau\}}{N}
$$

Queue delay:

$$
d_i = s_i - a_i
$$

Saturation rate:

$$
\mathrm{SaturationRate} = \frac{\sum_{i=1}^{N} \mathbf{1}[u_i \ge \tau]}{N}
$$

## From Math To Code

- Turn each request into a binary SLA violation indicator first.
- Count compliant requests by subtracting total violations from the request count.
- Compute queue delay per request before averaging it into one service-level summary.
- Convert utilization into thresholded saturation events only after the raw ratios are visible.

## Minimal Code Mental Model

```python
violations = sla_violations(latencies_ms, sla_ms=200.0)
compliant, compliance = request_sla_compliance(latencies_ms, sla_ms=200.0)
delays = queue_delay_values(enqueued_at, started_at)
_, mean_delay = queue_delay(enqueued_at, started_at)
retried, retry_fraction = retry_rate(retry_counts)
utilization, saturated_now = queue_utilization(queue_depth, queue_capacity)
```

## Functions

```python
def sla_violations(latencies_ms: list[float], sla_ms: float) -> list[int]:
def request_sla_compliance(latencies_ms: list[float], sla_ms: float) -> tuple[int, float]:
def violation_rate(violations: int, total: int) -> float:
def retry_rate(retry_counts: list[int]) -> tuple[int, float]:
def queue_delay_values(enqueued_at: list[float], started_at: list[float]) -> list[float]:
def queue_delay(enqueued_at: list[float], started_at: list[float]) -> tuple[list[float], float]:
def queue_utilization(queue_depth: int, queue_capacity: int) -> tuple[float, bool]:
def queue_age_percentiles(queue_ages: list[float]) -> tuple[float, float]:
def queue_backlog_ratio(queue_ages: list[float], target_age: float) -> tuple[list[float], float]:
def saturation_rate(utilizations: list[float], threshold: float = 1.0) -> tuple[int, float]:
```

## When To Use What

- Use SLA compliance when you need a direct product-facing latency summary.
- Use queue delay and queue-age percentiles when overload is building before full request latency breaks.
- Use queue utilization and saturation rate when capacity pressure is the main operational risk.
- Use backlog ratio when queue age needs to be normalized against an internal target.
- Use retry rate when infrastructure flakiness or overload is causing second attempts to rise.

## Run tests

```bash
pytest modules/ml/mlops/service-reliability-metrics/python -q
```
