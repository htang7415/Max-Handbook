# VAE

> Track: `ml` | Topic: `generative`

## Concept

A variational autoencoder learns two things at once: how to compress an observed
example $x$ into a latent distribution, and how to reconstruct $x$ from a
latent sample $z$. Unlike a plain autoencoder, the encoder does not output a
single code; it outputs a distribution over possible latent codes.

The first-principles idea is to turn representation learning into probabilistic
inference. The encoder approximates "which latent causes could have produced
this example?", and the decoder approximates "what examples would this latent
cause generate?"

The reparameterization trick makes the stochastic latent sample differentiable:
instead of sampling $z$ directly, we sample noise $\epsilon$ and transform it
using the encoder's mean and scale. That preserves randomness while keeping the
computation trainable with backpropagation.

## Math

The ELBO objective that VAEs maximize is:

$$\text{ELBO} = \mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)] - D_{KL}(q_\phi(z|x) \| p(z))$$

The reparameterization trick computes latent samples as:

$$z = \mu + \sigma \odot \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)$$

- $q_\phi(z|x)$ -- encoder (approximate posterior) parameterized by $\phi$
- $p_\theta(x|z)$ -- decoder (likelihood) parameterized by $\theta$
- $p(z)$ -- prior, typically $\mathcal{N}(0, I)$
- $D_{KL}$ -- Kullback-Leibler divergence regularizing the latent distribution
- $\mathrm{ELBO}$ -- evidence lower bound
- $\mathbb{E}$ -- expectation
- $\phi$ -- model/encoder parameters
- $\theta$ -- decoder parameters
- $z$ -- latent variable
- $x$ -- observed data sample
- $\mathcal{N}$ -- normal (Gaussian) distribution
- $\mu$ -- latent mean
- $\sigma$ -- latent standard deviation
- $\epsilon$ -- auxiliary Gaussian noise
- $I$ -- identity covariance matrix

## Key Points

- The ELBO balances reconstruction quality (first term) against latent regularization (KL term); tuning the weight between them controls sample sharpness versus latent smoothness.
- VAE samples are typically blurrier than GAN outputs because the Gaussian decoder averages over modes, but training is much more stable.
- The smooth latent space enables meaningful interpolation between data points -- a property GANs do not guarantee.
- Posterior collapse occurs when the decoder becomes powerful enough to ignore $z$, causing the KL term to vanish (see VAE Posterior Collapse module).

## Function

```python
def elbo(recon: float, kl: float) -> float:
```

- `recon` -- reconstruction log-likelihood term, $\mathbb{E}_{q(z|x)}[\log p(x|z)]$
- `kl` -- KL divergence between the approximate posterior and the prior, $D_{KL}(q(z|x) \| p(z))$

## Run tests

```bash
pytest modules/ml/generative/vae/python -q
```
