# Confidence Calibration

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Confidence calibration checks whether the agent's reported confidence matches how often it is actually correct across a set of runs.

## Key Points

- High confidence is only useful when it matches observed accuracy.
- Calibration gaps are about alignment, not just raw quality.
- A confidence gate should review agents that are both overconfident and inaccurate.

## Minimal Code Mental Model

```python
confidence = mean_confidence([0.9, 0.8, 0.7])
accuracy = observed_accuracy([True, True, False])
gap = calibration_gap(confidence, accuracy)
route = calibration_route(confidence, accuracy, max_gap=0.1, min_accuracy=0.75)
```

## Function

```python
def mean_confidence(confidences: list[float]) -> float:
def observed_accuracy(outcomes: list[bool]) -> float:
def calibration_gap(mean_confidence_value: float, observed_accuracy_value: float) -> float:
def calibration_route(
    mean_confidence_value: float,
    observed_accuracy_value: float,
    max_gap: float,
    min_accuracy: float,
) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/confidence-calibration/python -q
```
