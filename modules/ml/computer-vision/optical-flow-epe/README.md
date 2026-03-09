# Optical Flow (EPE)

> Track: `ml` | Topic: `computer-vision`

## Concept

Endpoint error (EPE) measures how far a predicted optical-flow vector is from
the ground-truth flow vector at a pixel. Because optical flow has horizontal and
vertical components, EPE is just Euclidean distance in 2D flow space.

## Math

$$\mathrm{EPE} = \sqrt{(u-u^*)^2 + (v-v^*)^2}$$

- $\mathrm{EPE}$ -- endpoint error
- $u^*$ -- horizontal flow component (ground truth)
- $v^*$ -- vertical flow component (ground truth)
- $u$ -- horizontal flow component (prediction)
- $v$ -- vertical flow component (prediction)

## Key Points

- EPE is zero only when both horizontal and vertical components match exactly.
- Larger EPE means the predicted motion vector is farther from the true motion.
- Because it is an Euclidean distance, EPE combines direction and magnitude errors into one number.

## Function

```python
def epe(pred: tuple[float, float], target: tuple[float, float]) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/optical-flow-epe/python -q
```
