# Breach Bucket Metrics

Breach bucket metrics summarize overload severity after turning capacity breaches into severity buckets.

## Purpose

Use this guide when overload has already been bucketized into severity bands and you need the right summary:
- overall burden
- concentration across severities
- escalation shape
- where mild overload turns into severe overload

## First Principles

- Bucketized overload is a second-stage summary; the first-stage check is still the raw breach rate.
- Distribution shape matters because two systems can have the same breach mass but very different severity profiles.
- Threshold-location metrics are useful when operators need a simple “where does it get bad” signal.
- Bucket metrics are only worthwhile when severity buckets reflect an actual operational policy.

## Core Math

- Breach share by bucket:
  $$
  \frac{n_b}{N}
  $$
- Bucket entropy:
  $$
  -\sum_b p_b \log p_b
  $$
- Slope and curvature summarize how quickly severity mass moves toward worse buckets.

## Minimal Code Mental Model

```python
buckets = bucketize_breaches(load, thresholds)
share = breach_bucket_share(buckets)
entropy = breach_bucket_entropy(buckets)
slope = breach_bucket_slope(buckets)
```

## Canonical Modules

- Family module: `capacity-stress-metrics`

## When To Use What

- Start with `capacity-stress-metrics` before narrower bucket summaries.
- Use breach share or mass for the base severity distribution.
- Use entropy when you care about concentration across severity levels.
- Use slope or curvature when abrupt escalation matters more than average burden.
- Use knee or threshold-location summaries when operations needs a simple escalation boundary.
