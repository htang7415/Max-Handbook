# ELBO

> Track: `ml` | Topic: `fundamentals`

## Concept

The evidence lower bound (ELBO) is the objective used in variational inference
when exact log-likelihood is hard to optimize directly. It turns inference into
an optimization problem by balancing reconstruction quality against how far the
approximate posterior strays from the prior.

## Math

$$\mathrm{ELBO} = \mathbb{E}_q[\log p(x|z)] - \mathrm{KL}(q\|p)$$

- $\mathrm{ELBO}$ -- evidence lower bound
- $\mathrm{KL}$ -- Kullback-Leibler divergence
- $\mathbb{E}$ -- expectation
- $q$ -- approximate posterior over latent variables
- $p$ -- generative model term being compared against $q$
- $x$ -- observed data
- $z$ -- latent variable

## Key Points

- The first term rewards explanations of the data that reconstruct well.
- The KL term regularizes the latent representation toward the prior.
- Maximizing the ELBO also maximizes a lower bound on the true log-likelihood.

## Function

```python
def elbo(recon: float, kl: float) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/elbo/python -q
```
