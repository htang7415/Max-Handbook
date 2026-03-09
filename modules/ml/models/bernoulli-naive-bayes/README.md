# Bernoulli Naive Bayes

> Track: `ml` | Topic: `models`

## Concept

Bernoulli Naive Bayes models each feature as a binary on/off event conditioned
on the class. It is a natural fit for bag-of-words presence features and other
binary indicator vectors.

## Math
$$p(x\mid y)=\prod_i p_i^{x_i}(1-p_i)^{1-x_i}$$

- $x$ -- binary feature vector
- $y$ -- class label
- $x_i \in \{0,1\}$ -- i-th binary feature
- $p_i$ -- probability that feature $i$ is present under class $y$
- $p(x \mid y)$ -- class-conditional Bernoulli likelihood
- $i$ -- index

## Key Points

- Bernoulli NB cares about feature presence or absence, not raw counts.
- The likelihood multiplies probabilities for present features and complements for absent ones.
- Log-likelihood is used in practice to avoid numerical underflow.

## Function

```python
def bernoulli_log_likelihood(x: list[int], prob: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/models/bernoulli-naive-bayes/python -q
```
