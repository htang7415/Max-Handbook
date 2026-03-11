# Posterior Routing

> Track: `ai-agents` | Topic: `workflows`

## Concept

Posterior routing uses observed success and failure evidence to rank routes by Bayesian posterior quality instead of relying only on raw heuristics.

## Key Points

- A Beta posterior mean is a compact estimate of route quality after sparse evidence.
- Posterior variance keeps low-data routes from looking more certain than they are.
- A route should win on both quality and confidence before execution.

## Minimal Code Mental Model

```python
scores = posterior_route_scores(route_outcomes)
route = posterior_route(
    route_outcomes,
    min_mean=0.7,
    min_margin=0.1,
    max_variance=0.02,
)
```

## Function

```python
def beta_posterior_mean(successes: int, failures: int, alpha: float = 1.0, beta: float = 1.0) -> float:
def posterior_route_scores(
    route_to_outcomes: dict[str, dict[str, int]],
    alpha: float = 1.0,
    beta: float = 1.0,
) -> list[dict[str, object]]:
def posterior_route(
    route_to_outcomes: dict[str, dict[str, int]],
    min_mean: float,
    min_margin: float = 0.0,
    max_variance: float = 1.0,
    alpha: float = 1.0,
    beta: float = 1.0,
) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/workflows/posterior-routing/python -q
```
