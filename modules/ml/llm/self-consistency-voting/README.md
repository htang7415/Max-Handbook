# Self-Consistency Voting

> Track: `ml` | Topic: `llm`

## Concept

Self-consistency voting samples multiple reasoning paths and picks the answer that appears most often.

## Math

$$
\hat{y} = \arg\max_a \sum_{i=1}^{n} \mathbf{1}[a_i = a]
$$

- $a_i$ -- normalized answer from sample $i$
- $\hat{y}$ -- voted answer
- $n$ -- number of sampled completions

## Key Points

- Voting can stabilize answers when individual reasoning traces are noisy.
- The final confidence proxy is the vote share, not a calibrated probability.
- This module uses lightweight normalization and first-seen tie breaking.

## Function

```python
def self_consistency_vote(answers: list[str]) -> tuple[str, float]:
```

## Run tests

```bash
pytest modules/ml/llm/self-consistency-voting/python -q
```
