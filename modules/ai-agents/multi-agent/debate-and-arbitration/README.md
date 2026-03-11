# Debate and Arbitration

> Track: `ai-agents` | Topic: `multi-agent`

## Concept

Debate and arbitration collect multiple worker answers, measure how much they agree, and pick a simple winner for the coordinator.

## Key Points

- Arbitration only helps when workers can produce different plausible answers.
- Simple normalization is often enough before counting votes.
- Low agreement is a useful signal that the coordinator may need review or more evidence.

## Minimal Code Mental Model

```python
counts = vote_counts(["Ship now", "ship now", "Delay"])
agreement = agreement_rate(["Ship now", "ship now", "Delay"])
winner = arbitrate_majority(["Ship now", "ship now", "Delay"])
```

## Function

```python
def normalize_candidate(text: str) -> str:
def vote_counts(candidates: list[str]) -> dict[str, int]:
def agreement_rate(candidates: list[str]) -> float:
def arbitrate_majority(candidates: list[str]) -> str | None:
```

## Run tests

```bash
pytest modules/ai-agents/multi-agent/debate-and-arbitration/python -q
```
