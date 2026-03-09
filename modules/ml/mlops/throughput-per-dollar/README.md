# Throughput Per Dollar

> Track: `ml` | Topic: `mlops`

## Concept

Throughput per dollar measures how many requests a system can serve for one dollar of spend.

## Math

$$
\mathrm{throughput\_per\_dollar} = \frac{\mathrm{requests\_per\_second} \cdot 3600}{\mathrm{dollars\_per\_hour}}
$$

- $\mathrm{requests\_per\_second}$ -- observed serving throughput
- $\mathrm{dollars\_per\_hour}$ -- infrastructure cost rate

## Key Points

- This is the inverse view of cost per request.
- It is useful for comparing serving setups with different unit economics.
- Higher is better.

## Function

```python
def throughput_per_dollar(requests_per_second: float, dollars_per_hour: float) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/throughput-per-dollar/python -q
```
