# Runner-Up Vote Share

> Track: `ml` | Topic: `llm`

## Concept

Runner-up vote share measures how much support the second-most common normalized answer receives.

## Math

For normalized answer vote shares $p_{(1)} \ge p_{(2)} \ge \dots$:

$$
\mathrm{RunnerUpVoteShare} = p_{(2)}
$$

If there is only one unique answer, the runner-up share is zero.

## Key Points

- Runner-up vote share helps explain ambiguity in repeated decoding.
- It complements top-vote share and majority-vote margin.
- This module normalizes answers before counting votes.

## Function

```python
def runner_up_vote_share(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/runner-up-vote-share/python -q
```
