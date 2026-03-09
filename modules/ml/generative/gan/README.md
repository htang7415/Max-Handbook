# GAN

> Track: `ml` | Topic: `generative`

## Concept

A GAN trains a generator and discriminator in opposition. The generator tries to
map latent noise $z$ into realistic samples; the discriminator tries to tell
real samples from generated ones.

From first principles, the discriminator supplies a learned training signal:
instead of comparing generated outputs to a fixed target pixel by pixel, the
generator is rewarded when it makes the discriminator uncertain.

This adversarial setup can produce sharp samples, but it is also fragile. If
the discriminator becomes too confident, generator gradients can become weak or
unhelpful. That is why GAN training often needs stabilization tricks.

## Math

The minimax objective for the GAN value function is:

$$\min_G \max_D \; \mathbb{E}_{x \sim p_{\text{data}}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))]$$

The discriminator loss for a single sample pair is:

$$\mathcal{L}_D = -\log D(x) - \log(1 - D(G(z)))$$

- $D(x)$ -- discriminator output (probability that $x$ is real)
- $G(z)$ -- generator output given noise $z$
- $p_{\text{data}}$ -- true data distribution
- $p_z$ -- prior distribution over latent noise (typically $\mathcal{N}(0, I)$)
- $\mathbb{E}$ -- expectation
- $x$ -- real data sample
- $z$ -- latent noise sample
- $\mathcal{L}_D$ -- discriminator loss
- $\mathcal{N}$ -- normal (Gaussian) distribution
- $I$ -- identity covariance matrix in the Gaussian prior

## Key Points

- GAN training is inherently unstable because the generator and discriminator can oscillate rather than converge to a Nash equilibrium.
- Mode collapse is the most common failure: the generator learns to produce only a few outputs that fool the discriminator, ignoring the full data distribution.
- Wasserstein loss with gradient penalty (WGAN-GP) provides more meaningful gradients and is often the first remedy for training instability.
- GANs produce sharper samples than VAEs but offer no direct way to compute likelihoods or encode data into a latent space.

## Function

```python
def gan_loss(d_real: float, d_fake: float) -> float:
```

- `d_real` -- discriminator output on a real sample, $D(x)$
- `d_fake` -- discriminator output on a generated sample, $D(G(z))$

## Run tests

```bash
pytest modules/ml/generative/gan/python -q
```
