# Bayesian Benchmark Updating

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Bayesian benchmark updating keeps a running belief about benchmark success by combining prior expectations with new pass/fail evidence.

## Key Points

- A Beta prior gives a compact running belief for binary benchmark outcomes.
- Posterior mean tracks expected success rate after each new batch.
- Posterior variance makes low-data confidence explicit instead of hiding it.

## Minimal Code Mental Model

```python
posterior = updated_beta_posterior(prior_alpha=2.0, prior_beta=2.0, successes=18, failures=2)
summary = posterior_benchmark_summary(posterior["alpha"], posterior["beta"])
route = benchmark_belief_route(summary["posterior_mean"], summary["posterior_variance"], min_mean=0.8, max_variance=0.01)
```

## Function

```python
def updated_beta_posterior(prior_alpha: float, prior_beta: float, successes: int, failures: int) -> dict[str, float]:
def posterior_benchmark_summary(alpha: float, beta: float) -> dict[str, float]:
def benchmark_belief_route(posterior_mean: float, posterior_variance: float, min_mean: float, max_variance: float) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/bayesian-benchmark-updating/python -q
```
