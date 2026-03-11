# Bucketed Calibration Diagnostics

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Bucketed calibration diagnostics group runs by reported confidence so you can compare mean confidence and observed accuracy inside each bucket instead of looking only at one global average.

## Key Points

- Global calibration can hide local problems in the high-confidence range.
- Buckets make overconfidence and underconfidence visible by confidence band.
- Expected calibration error summarizes the bucket gaps into one number.

## Minimal Code Mental Model

```python
table = bucketed_calibration_table(confidences, outcomes, bucket_count=5)
ece = expected_calibration_error(confidences, outcomes, bucket_count=5)
route = calibration_diagnostic_route(ece, max_ece=0.08)
```

## Function

```python
def confidence_bucket_index(confidence: float, bucket_count: int) -> int:
def bucketed_calibration_table(
    confidences: list[float],
    outcomes: list[bool],
    bucket_count: int,
) -> list[dict[str, object]]:
def expected_calibration_error(
    confidences: list[float],
    outcomes: list[bool],
    bucket_count: int,
) -> float:
def calibration_diagnostic_route(ece: float, max_ece: float) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/bucketed-calibration-diagnostics/python -q
```
