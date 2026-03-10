# Generative Models

Generative modeling is about learning a distribution that can produce useful new samples.

## Purpose

Use this page to choose the right modern generative family:
- autoregressive generation
- latent-variable modeling
- adversarial modeling
- diffusion and denoising

## First Principles

- A generative model tries to explain or sample from data, not just classify it.
- Different families trade sample quality, training stability, and controllability.
- In 2026, diffusion is the most important family to understand well, but GAN and VAE intuition still matter.
- Sampling and guidance are part of the model story, not an afterthought.

## Core Math

- Likelihood idea:
  $$
  p_\theta(x)
  $$
- VAE objective:
  $$
  \mathbb{E}_{q(z \mid x)}[\log p(x \mid z)] - \mathrm{KL}(q(z \mid x)\|p(z))
  $$
- Diffusion training learns to reverse a noise process by predicting noise or denoised structure.

## Minimal Code Mental Model

```python
noise = sample_noise(x.shape)
noisy_x = add_noise(x, noise, t)
predicted_noise = model(noisy_x, t)
loss = mse(predicted_noise, noise)
```

## Canonical Modules

- Family choice: `autoregressive`, `vae`, `gan`, `diffusion-models`, `model-selection`
- Diffusion core: `ddpm-sampling`, `ddim-sampling`, `diffusion-guidance-tradeoffs`, `ema-diffusion-weights`
- Failure modes: `gan-mode-collapse`, `vae-posterior-collapse`

## Supporting Guides

- Diffusion guide (`docs/ml/generative/diffusion`)

## When To Use What

- Start with `diffusion-models` if you want the most relevant 2026 generative family.
- Use `model-selection` when the real question is GAN vs VAE vs diffusion.
- Use `ddpm-sampling`, `ddim-sampling`, and guidance only after the forward/reverse diffusion picture is clear.
- Use GAN and VAE modules mainly for core intuition and comparison, not as the main modern path.
