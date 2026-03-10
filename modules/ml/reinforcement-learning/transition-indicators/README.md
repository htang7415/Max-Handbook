# Transition Indicators

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Transition indicators convert episode termination state into masks, fractions,
and numeric tensors used for bootstrapping and batched RL updates.

## Math

- Terminal indicator:
  $$
  \mathbf{1}[\text{done}]
  $$
- Continuation mask:
  $$
  1 - \mathbf{1}[\text{done}]
  $$
- Done fraction:
  $$
  \frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[\text{done}_i]
  $$

## Key Points

- Masks are the most important form because they directly control bootstrap terms.
- Fractions are useful for replay-buffer or rollout diagnostics.
- Numeric indicators are useful when the training code expects floats instead of booleans.
- Batch helpers should stay simple wrappers around the same done-state logic.

## Function

```python
def terminal_mask(done_flags: list[bool]) -> list[float]:
def continuation_mask(done_flags: list[bool]) -> list[float]:
def done_fraction(done_flags: list[bool]) -> float:
def terminal_indicator(done: bool) -> float:
def nonterminal_indicator(done: bool) -> float:
def continuing_transition_batch(done_flags: list[bool]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/transition-indicators/python -q
```
