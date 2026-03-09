# Gaussian Naive Bayes

> Track: `ml` | Topic: `models`

## Concept

Gaussian Naive Bayes assumes each feature is conditionally independent given
the class label, and that each feature distribution within a class is Gaussian.
Prediction compares how likely the observed feature vector would be under each
class-specific Gaussian model.

## Math
$$p(x\mid y)=\prod_i \mathcal{N}(x_i;\mu_i,\sigma_i^2)$$

- $\mathcal{N}$ -- normal (Gaussian) distribution
- $x$ -- observed feature vector
- $y$ -- class label
- $x_i$ -- i-th feature value
- $\mu_i$ -- class-conditional mean of feature $i$
- $\sigma_i^2$ -- class-conditional variance of feature $i$
- $p(x \mid y)$ -- likelihood of features under class $y$
- $i$ -- index

## Key Points

- “Naive” means the features are assumed independent once the class is known.
- The model compares class likelihoods feature by feature and sums them in log-space.
- Even with a crude independence assumption, Naive Bayes can work surprisingly well.

## Function

```python
def gaussian_log_likelihood(x: list[float], mean: list[float], var: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/models/gaussian-naive-bayes/python -q
```
