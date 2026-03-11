# Policy Decision Tables

> Track: `ai-agents` | Topic: `guardrails`

## Concept

Policy decision tables make guardrail behavior explicit by listing condition combinations and the action each combination should trigger.

## Key Points

- Decision tables replace hidden prompt heuristics with small auditable rules.
- More specific rules should win over more general ones.
- A default route is still necessary when no rule matches.

## Minimal Code Mental Model

```python
rules = [
    {"conditions": {"contains_pii": True, "needs_tool": True}, "action": "review"},
    {"conditions": {"blocked_term": True}, "action": "block"},
]
ranked = ranked_policy_rules(rules)
route = decision_table_action(
    {"contains_pii": True, "needs_tool": True, "blocked_term": False},
    rules,
    default_action="allow",
)
```

## Function

```python
def rule_specificity(rule: dict[str, object]) -> int:
def ranked_policy_rules(rules: list[dict[str, object]]) -> list[dict[str, object]]:
def decision_table_action(
    signals: dict[str, bool],
    rules: list[dict[str, object]],
    default_action: str,
) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/guardrails/policy-decision-tables/python -q
```
