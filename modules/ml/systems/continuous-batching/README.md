# Continuous Batching Step

> Track: `ml` | Topic: `systems`

## Concept

Continuous batching keeps a decode batch full by removing finished requests and immediately admitting queued requests into newly free slots.

## Math

$$a_t' = \{ r - 1 \mid r \in a_t, \; r > 1 \}$$

$$
a_{t+1} = a_t' \cup \mathrm{admit}(q_t, C - |a_t'|)
$$

- $a_t$ -- active requests represented by remaining decode steps
- $a_t'$ -- active requests after one decode step and removal of completed requests
- $q_t$ -- queued requests waiting for admission
- $C$ -- batch capacity

## Key Points

- Continuous batching improves throughput by keeping hardware busy.
- Finished requests leave slots that can be filled immediately.
- This is different from static batching, which waits for a whole batch boundary.

## Function

```python
def continuous_batch_step(
    active_requests: list[int],
    queued_requests: list[int],
    capacity: int,
) -> tuple[list[int], list[int]]:
```

## Run tests

```bash
pytest modules/ml/systems/continuous-batching/python -q
```
