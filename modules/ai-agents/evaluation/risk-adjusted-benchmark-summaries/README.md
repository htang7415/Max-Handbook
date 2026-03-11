# Risk-Adjusted Benchmark Summaries

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Risk-adjusted benchmark summaries combine task success with safety or high-risk failure rates so a benchmark does not look good just because it is aggressive.

## Key Points

- A benchmark score should penalize success that comes with too many risky failures.
- Risk penalties make security and reliability tradeoffs visible in one comparable number.
- A candidate can beat the raw success rate and still lose after adjustment.

## Minimal Code Mental Model

```python
score = risk_adjusted_score(success_rate=0.88, high_risk_failure_rate=0.02, risk_penalty=2.0)
summary = benchmark_risk_summary("candidate", 0.88, 0.02, 2.0)
route = risk_adjusted_route(candidate_score=summary["risk_adjusted_score"], baseline_score=0.75, min_score=0.7, max_drop=0.05)
```

## Function

```python
def risk_adjusted_score(success_rate: float, high_risk_failure_rate: float, risk_penalty: float) -> float:
def benchmark_risk_summary(
    name: str,
    success_rate: float,
    high_risk_failure_rate: float,
    risk_penalty: float,
) -> dict[str, object]:
def risk_adjusted_route(
    candidate_score: float,
    baseline_score: float,
    min_score: float,
    max_drop: float,
) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/risk-adjusted-benchmark-summaries/python -q
```
