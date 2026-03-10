# Vote Metrics

> Track: `ml` | Topic: `llm`

## Concept

Vote metrics summarize how repeated sampled answers agree, fragment, or form a
strong alternative cluster after answer normalization.

## Math

- Normalized vote share:
  $$
  p_i = \frac{c_i}{N}
  $$
- Vote entropy:
  $$
  H = -\sum_i p_i \log p_i
  $$
- Majority-vote margin:
  $$
  p_{(1)} - p_{(2)}
  $$
- Uniqueness rate:
  $$
  \frac{\#\{\text{unique normalized answers}\}}{N}
  $$

- $c_i$ -- count for normalized answer $i$
- $N$ -- number of sampled answers
- $p_{(1)}$ -- largest vote share
- $p_{(2)}$ -- second-largest vote share

## Key Points

- Use answer stability when you want a pairwise agreement view.
- Use majority-vote margin and top-vote share when you want a confidence-style summary.
- Use vote entropy when disagreement structure matters more than the winner.
- Use uniqueness rate or candidate diversity when exploration matters.
- Use minority-cluster entropy when you care about structured alternatives, not just noise.

## Function

```python
def normalize_answer(text: str) -> str:
def answer_stability(answers: list[str]) -> float:
def majority_vote_margin(answers: list[str]) -> float:
def vote_entropy(answers: list[str]) -> float:
def answer_uniqueness_rate(answers: list[str]) -> float:
def candidate_diversity(answers: list[str]) -> float:
def top_vote_share(answers: list[str]) -> float:
def consensus_disagreement_rate(answers: list[str]) -> float:
def minority_cluster_entropy(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/vote-metrics/python -q
```
