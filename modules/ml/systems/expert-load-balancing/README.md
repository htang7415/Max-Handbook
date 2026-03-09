# Expert Load Balancing Loss

> Track: `ml` | Topic: `systems`

## Concept

Sparse Mixture-of-Experts systems need the router to spread traffic across experts instead of overloading only a few of them.
This module computes a simple Switch-style load-balancing auxiliary loss.

## Math

$$L = E \sum_{i=1}^{E} f_i P_i$$

- $E$ -- number of experts
- $f_i$ -- fraction of tokens assigned to expert $i$
- $P_i$ -- average router probability mass on expert $i$
- $L$ -- load-balancing loss

## Key Points

- Balanced routing tends to keep the loss near $1$.
- Collapsing many tokens onto one expert increases the loss.
- This auxiliary term complements routing and dispatch logic, it does not replace them.

## Function

```python
def expert_load_balance_loss(
    router_probs: list[list[float]],
    assignments: list[int],
) -> float:
```

## Run tests

```bash
pytest modules/ml/systems/expert-load-balancing/python -q
```
