# Decision Cost Matrices

> Track: `ai-agents` | Topic: `guardrails`

## Concept

Decision cost matrices choose between allow, review, and block by comparing the expected cost of each action under the current safety outcome probabilities.

## Key Points

- Expected cost is often the right guardrail objective when mistakes have different consequences.
- Review is useful when both false allows and false blocks are expensive.
- The best decision is the action with the lowest expected cost, not the loudest rule.

## Minimal Code Mental Model

```python
outcome_probs = {"safe": 0.7, "unsafe": 0.3}
ranking = ranked_actions_by_cost(action_cost_matrix, outcome_probs)
decision = cost_matrix_decision(action_cost_matrix, outcome_probs)
```

## Function

```python
def expected_action_cost(
    outcome_probabilities: dict[str, float],
    action_costs: dict[str, float],
) -> float:
def ranked_actions_by_cost(
    action_cost_matrix: dict[str, dict[str, float]],
    outcome_probabilities: dict[str, float],
) -> list[dict[str, object]]:
def cost_matrix_decision(
    action_cost_matrix: dict[str, dict[str, float]],
    outcome_probabilities: dict[str, float],
) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/guardrails/decision-cost-matrices/python -q
```
