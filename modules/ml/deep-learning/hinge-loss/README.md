# Hinge Loss

> Track: `ml` | Topic: `deep-learning`

## Concept

Hinge loss trains a margin-based binary classifier. It does not just ask for the
correct sign; it asks the score to be confidently correct by at least a margin
of 1.

## Math

$$L = \max(0, 1 - y \cdot \text{score})$$

- $L$ -- loss value
- $y \in \{-1, 1\}$ -- binary class label encoded as a sign
- $\text{score}$ -- model score before thresholding

## Key Points

- If $y \cdot \text{score} \ge 1$, the example is correctly classified with margin and loss is 0.
- If the margin is violated, the loss increases linearly.
- Hinge loss is central to support vector machines and other margin-based methods.

## Function

```python
def hinge_loss(score: float, label: int) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/hinge-loss/python -q
```
