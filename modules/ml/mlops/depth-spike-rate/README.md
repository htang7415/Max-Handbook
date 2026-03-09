# Depth Spike Rate

> Track: `ml` | Topic: `mlops`

## Concept

Depth spike rate measures how often queue depth rises above a configured backlog threshold.

## Math

$$
\mathrm{DepthSpikeRate} = \frac{\sum_{i=1}^{N} \mathbf{1}[d_i > \tau]}{N}
$$

- $d_i$ -- observed queue depth at time step $i$
- $\tau$ -- spike threshold

## Key Points

- This metric highlights intermittent backlog spikes, not just average load.
- It complements queue utilization and queue-age metrics.
- This module returns both the spike count and the spike fraction.

## Function

```python
def depth_spike_rate(depths: list[int], threshold: int) -> tuple[int, float]:
```

## Run tests

```bash
pytest modules/ml/mlops/depth-spike-rate/python -q
```
