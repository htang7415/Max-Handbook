# Answer Grounding Checks

> Track: `ai-agents` | Topic: `rag`

## Concept

Answer grounding checks compare generated claims against retrieved evidence and summarize how much of the answer is actually supported.

## Key Points

- Grounding checks happen after answer generation, not before retrieval.
- Claim-level support is more actionable than one coarse answer score.
- Unsupported claims should be easy to list for review or regeneration.

## Minimal Code Mental Model

```python
support = claim_support_map(["csv is required", "weekly report due friday"], evidence)
grounded = grounded_claim_rate(support)
unsupported = unsupported_claims(support)
```

## Function

```python
def claim_support_map(claims: list[str], evidence: list[str]) -> dict[str, bool]:
def grounded_claim_rate(support_map: dict[str, bool]) -> float:
def unsupported_claims(support_map: dict[str, bool]) -> list[str]:
```

## Run tests

```bash
pytest modules/ai-agents/rag/answer-grounding-checks/python -q
```
