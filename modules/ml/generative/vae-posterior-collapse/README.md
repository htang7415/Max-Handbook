# VAE Blurry Samples and Posterior Collapse

> Track: `ml` | Topic: `generative`

## Concept

Posterior collapse happens when a VAE decoder becomes so capable that it stops
using the latent variable at all. The encoder then learns to match the prior
instead of encoding information about the data.

From first principles, the failure mode is:
1. The decoder can already reconstruct well on its own.
2. Using the latent code gives little extra benefit.
3. The optimizer reduces KL cost by pushing the posterior toward the prior.
4. The latent channel becomes uninformative.

The result is a model with a nominal latent space that carries almost no useful
signal for interpolation or controlled generation.

## Math

The ELBO objective decomposes as:

$$\text{ELBO} = \underbrace{\mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)]}_{\text{reconstruction}} - \underbrace{D_{KL}(q_\phi(z|x) \| p(z))}_{\text{regularization}}$$

During posterior collapse, the KL term vanishes:

$$q_\phi(z|x) \approx p(z) \implies D_{KL}(q_\phi(z|x) \| p(z)) \approx 0$$

KL annealing introduces a weight $\lambda$ that ramps from 0 to 1:

$$\mathcal{L} = \mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)] - \lambda \cdot D_{KL}(q_\phi(z|x) \| p(z))$$

- $\lambda$ -- annealing coefficient, linearly increased from 0 to 1 during training
- $q_\phi(z|x)$ -- approximate posterior (encoder output)
- $p(z)$ -- prior distribution, typically $\mathcal{N}(0, I)$
- $\mathrm{ELBO}$ -- evidence lower bound
- $\mathbb{E}$ -- expectation
- $\phi$ -- model/encoder parameters
- $\theta$ -- decoder parameters
- $z$ -- latent variable
- $x$ -- observed data sample
- $\mathcal{L}$ -- loss function
- $\mathcal{N}$ -- normal (Gaussian) distribution
- $I$ -- identity covariance matrix

## Key Points

- The hallmark of posterior collapse is a KL term near zero combined with poor latent representations; the decoder reconstructs without using $z$.
- KL annealing (warmup) is the simplest fix: start with $\lambda = 0$ and linearly ramp to $\lambda = 1$ over training, giving the encoder time to learn before regularization dominates.
- The free-bits strategy enforces a minimum KL per dimension (e.g., $\geq 0.25$ nats), preventing individual latent dimensions from being ignored.
- Stronger decoders make posterior collapse worse; deliberately limiting decoder capacity forces the model to rely on the latent code.
- Monitoring per-dimension KL values during training is the most reliable way to detect which latent dimensions have collapsed.

## Function

```python
def kl_is_low(kl: float, threshold: float = 0.1) -> bool:
```

- `kl` -- measured KL divergence value $D_{KL}(q(z|x) \| p(z))$
- `threshold` -- KL value below which posterior collapse is flagged (default 0.1)

## Run tests

```bash
pytest modules/ml/generative/vae-posterior-collapse/python -q
```
