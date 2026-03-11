# Retrieval Quality and Citations

> Track: `ai-agents` | Topic: `rag`

## Concept

Retrieval quality and citations measure how much of an answer is backed by evidence and which claims still lack support.

## Key Points

- A grounded answer should cover its important claims with evidence.
- Missing citations are often more useful than one coarse retrieval score.
- Citation summaries should stay simple enough to inspect by hand.

## Minimal Code Mental Model

```python
coverage = citation_coverage(["c1", "c2", "c3"], {"c1": ["doc1"], "c3": ["doc2"]})
missing = uncited_claims(["c1", "c2", "c3"], {"c1": ["doc1"], "c3": ["doc2"]})
source_counts = cited_source_counts({"c1": ["doc1"], "c2": ["doc1", "doc2"]})
```

## Function

```python
def citation_coverage(claim_ids: list[str], citations: dict[str, list[str]]) -> float:
def uncited_claims(claim_ids: list[str], citations: dict[str, list[str]]) -> list[str]:
def cited_source_counts(citations: dict[str, list[str]]) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/ai-agents/rag/retrieval-quality-and-citations/python -q
```
