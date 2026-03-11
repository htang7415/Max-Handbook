# Sequential Test Stopping

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Sequential test stopping checks incoming benchmark results as they arrive and decides whether the evidence already supports the baseline, supports the candidate, or is still inconclusive.

## Key Points

- Sequential tests can stop earlier than fixed-size tests when evidence becomes strong enough.
- The log-likelihood ratio summarizes whether recent outcomes favor the null or alternative rate.
- Upper and lower boundaries make `accept-alt`, `accept-null`, and `continue` explicit.

## Minimal Code Mental Model

```python
boundaries = sprt_boundaries(alpha=0.05, beta=0.2)
log_lr = sprt_log_likelihood_ratio(successes=18, failures=4, null_rate=0.5, alt_rate=0.7)
route = sprt_route(log_lr, boundaries["upper"], boundaries["lower"])
```

## Function

```python
def sprt_log_likelihood_ratio(successes: int, failures: int, null_rate: float, alt_rate: float) -> float:
def sprt_boundaries(alpha: float, beta: float) -> dict[str, float]:
def sprt_route(log_likelihood_ratio: float, upper_boundary: float, lower_boundary: float) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/sequential-test-stopping/python -q
```
