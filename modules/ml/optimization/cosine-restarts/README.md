# Cosine Restarts

> Track: `ml` | Topic: `optimization`

## Concept

Cosine restarts repeat cosine decay cycles so the learning rate periodically jumps back up instead of only decaying once.

## Math

$$
\mathrm{lr}(t) = \frac{\eta}{2} \left(1 + \cos\left(\pi \frac{t \bmod C}{C}\right)\right)
$$

- $\eta$ -- base learning rate
- $t$ -- training step
- $C$ -- cycle length

## Key Points

- Restarts can help re-explore flatter regions during long training runs.
- This is a natural extension of plain cosine decay.
- The module uses fixed-length cycles to keep the schedule minimal.

## Function

```python
def cosine_restart_lr(base_lr: float, step: int, cycle_length: int) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/cosine-restarts/python -q
```
