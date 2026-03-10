# MLOps and Production ML

Production ML is mostly about keeping a useful model useful after deployment.

## Purpose

Use this page to reason about:
- safe rollout
- monitoring and alerting
- serving behavior and latency
- cost, capacity, and failure budgets

## First Principles

- A working production system needs clean data, reliable serving, safe rollout, and useful monitoring.
- Monitoring should catch user harm, not just metric movement.
- Rollout should be staged so bad models fail small before they fail big.
- Capacity and latency limits matter because a correct model that misses SLA is still a bad system.
- Cost matters because model quality must survive the budget, not just the benchmark.

## Core Math

- SLA compliance:
  $$
  \frac{\#\{\text{requests within target}\}}{\#\{\text{requests}\}}
  $$
- Error budget:
  $$
  1 - \mathrm{SLO}
  $$
- PSI-style drift:
  $$
  \sum_i (p_i - q_i)\log\frac{p_i}{q_i}
  $$
- Cost per request:
  $$
  \frac{\mathrm{total\ cost}}{\mathrm{request\ count}}
  $$

## Minimal Code Mental Model

```python
if drift_score > threshold or queue_delay > budget:
    page_team()
if canary_metrics_ok:
    rollout_fraction += step
cost = total_spend / request_count
```

## Canonical Modules

- Data quality and ingestion: `etl-pipeline`, `data-quality-checks`
- Monitoring and drift: `feature-drift-psi`, `drift-detection`, `prediction-monitoring`
- Safe rollout: `canary-deployment`, `canary-rollout`, `online-shadow-mode`, `ab-testing`, `sequential-testing`
- Serving and control: `offline-online-inference`, `batch-vs-realtime`, `request-sla`, `admission-control`, `request-batching`
- Cost and budgets: `error-budget`, `cost-per-request`, `throughput-per-dollar`, `tail-latency-budget`, `capacity-stress-metrics`

## Supporting Guides

- Monitoring map (`docs/ml/mlops/monitoring`)
- Serving map (`docs/ml/mlops/serving`)
- Breach bucket metrics (`docs/ml/mlops/breach-buckets`)

## When To Use What

- Use shadow or canary rollout before direct replacement.
- Use drift and prediction monitoring when the input or output distribution may change.
- Use request-SLA and queue metrics when latency is part of product quality.
- Use `capacity-stress-metrics` when capacity pressure is the main production risk.
- Use error budgets when deployment speed must be balanced with reliability.
- Use cost-per-request and throughput-per-dollar when scaling model size or serving changes.
