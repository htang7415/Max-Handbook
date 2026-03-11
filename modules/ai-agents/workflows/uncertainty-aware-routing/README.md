# Uncertainty-Aware Routing

> Track: `ai-agents` | Topic: `workflows`

## Concept

Uncertainty-aware routing decides whether to execute the best route, ask for clarification, or send the case to review based on score strength and route ambiguity.

## Key Points

- A strong route is not just the top score; it should also beat the alternatives clearly.
- Low absolute confidence and high relative ambiguity are different failure modes.
- Entropy and top-vs-second margin give a compact uncertainty picture.

## Minimal Code Mental Model

```python
distribution = normalized_route_scores(route_scores)
entropy = route_entropy(route_scores)
route = uncertainty_route(
    route_scores,
    min_top_score=0.6,
    min_margin=0.15,
    max_entropy=0.9,
)
```

## Function

```python
def normalized_route_scores(route_scores: dict[str, float]) -> list[dict[str, object]]:
def route_entropy(route_scores: dict[str, float]) -> float:
def uncertainty_route(
    route_scores: dict[str, float],
    min_top_score: float,
    min_margin: float,
    max_entropy: float,
) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/workflows/uncertainty-aware-routing/python -q
```
