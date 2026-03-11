# Retrieval Abstention and Coverage

> Track: `ai-agents` | Topic: `rag`

## Concept

Retrieval abstention and coverage decide whether the retrieved evidence is strong enough to answer, whether the system should retrieve more, or whether it should abstain.

## Key Points

- Coverage should reflect how many required claims are actually supported.
- An answer should not proceed just because some evidence exists.
- `Retrieve more` is different from `abstain`: it means the evidence is partial rather than absent.

## Minimal Code Mental Model

```python
coverage = claim_coverage(["c1", "c2", "c3"], ["c1", "c3"])
missing = unsupported_claims(["c1", "c2", "c3"], ["c1", "c3"])
route = rag_abstention_route(coverage, support_count=2, min_coverage=0.7, min_support_count=2)
```

## Function

```python
def claim_coverage(required_claims: list[str], supported_claims: list[str]) -> float:
def unsupported_claims(required_claims: list[str], supported_claims: list[str]) -> list[str]:
def rag_abstention_route(
    coverage: float,
    support_count: int,
    min_coverage: float,
    min_support_count: int,
) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/rag/retrieval-abstention-and-coverage/python -q
```
