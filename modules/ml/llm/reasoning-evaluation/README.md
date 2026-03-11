# Reasoning Evaluation

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to evaluate reasoning systems when both answer quality and
inference cost matter.

## First Principles

- Final accuracy alone misses the cost of extra reasoning tokens or repeated samples.
- Reasoning systems are often compared by single-trace accuracy, vote gain, and success under a budget.
- Multi-sample reasoning only helps if aggregation improves answer quality enough to justify the extra cost.
- Good reasoning evaluation should make both quality and compute visible.

## Core Math

Accuracy:

$$
\mathrm{Acc} = \frac{1}{n}\sum_{i=1}^{n} y_i
$$

Compute-adjusted successes per 1k tokens:

$$
\mathrm{SuccPer1k} = 1000 \cdot \frac{\sum_i y_i}{\sum_i c_i}
$$

Majority-vote gain:

$$
\mathrm{Gain} = \mathrm{Acc}_{vote} - \mathrm{Acc}_{single}
$$

Budgeted success:

$$
\mathrm{BudgetAcc}(B) = \frac{\sum_i y_i \mathbf{1}[c_i \le B]}{\sum_i \mathbf{1}[c_i \le B]}
$$

- $n$ -- number of evaluated examples
- $y_i$ -- binary correctness flag for example $i$
- $c_i$ -- token cost for example $i$
- $B$ -- maximum allowed token budget per example

## From Math To Code

- Start with per-example correctness flags.
- Add token costs only when you need to compare reasoning quality against inference expense.
- Treat vote gain as a delta over the single-trace baseline, not as a standalone score.
- Use budgeted success when product limits cap the allowed tokens per request.

## Minimal Code Mental Model

```python
acc = reasoning_accuracy([1, 0, 1, 1])
efficiency = successes_per_1k_tokens([1, 0, 1, 1], [1800, 2000, 1600, 2200])
gain = majority_vote_gain(single_success_rate=0.42, vote_success_rate=0.55)
budgeted = success_under_token_budget([1, 0, 1, 1], [1800, 2000, 1600, 2200], max_tokens=1900)
```

## Functions

```python
def reasoning_accuracy(correct: list[int]) -> float:
def successes_per_1k_tokens(correct: list[int], token_costs: list[int]) -> float:
def majority_vote_gain(single_success_rate: float, vote_success_rate: float) -> float:
def success_under_token_budget(correct: list[int], token_costs: list[int], max_tokens: int) -> float:
```

## When To Use What

- Use `reasoning_accuracy` for a clean one-number task score.
- Use `successes_per_1k_tokens` when comparing reasoning settings with very different token costs.
- Use `majority_vote_gain` when testing whether multi-sample self-consistency is worth it.
- Use `success_under_token_budget` when a serving or product budget is the main constraint.

## Run tests

```bash
pytest modules/ml/llm/reasoning-evaluation/python -q
```
