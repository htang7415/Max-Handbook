# Diffusion Models

> Track: `ml` | Topic: `generative`

## Concept

Diffusion models learn to reverse a simple corruption process. The forward
process gradually adds Gaussian noise until a sample becomes nearly pure noise;
the reverse model learns how to denoise one step at a time.

The first-principles picture is straightforward:
1. Start with a real sample.
2. Corrupt it slightly, then more, then more.
3. Train a network to predict the noise that was added.
4. Reverse that process during generation.

Because each reverse step is local and relatively simple, the model can learn a
high-quality generative process. The main cost is speed: generation requires
many denoising steps.

## Math

The forward process adds noise at each timestep:

$$q(x_t | x_{t-1}) = \mathcal{N}\!\left(x_t;\, \sqrt{1 - \beta_t}\, x_{t-1},\, \beta_t I\right)$$

The closed-form noisy sample at timestep $t$ is:

$$x_t = \sqrt{\bar{\alpha}_t}\, x_0 + \sqrt{1 - \bar{\alpha}_t}\, \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)$$

The simplified training loss is:

$$\mathcal{L} = \mathbb{E}_{t, x_0, \epsilon}\!\left[\|\epsilon - \epsilon_\theta(x_t, t)\|^2\right]$$

- $x_0$ -- clean (original) sample
- $x_t$ -- noisy sample at step $t$
- $x_{t-1}$ -- noisy sample at step $t-1$
- $x_T$ -- pure noise sample at step $T$
- $\beta_t$ -- noise variance at step $t$
- $\bar{\alpha}_t$ -- cumulative product term at step $t$
- $\epsilon$ -- Gaussian noise sample
- $\epsilon_\theta$ -- noise predictor network
- $q$ -- forward noising distribution
- $\mathbb{E}$ -- expectation
- $\mathcal{N}$ -- normal (Gaussian) distribution
- $\mathcal{L}$ -- training loss
- $I$ -- identity covariance matrix
- $t$ -- timestep

## Key Points

- Diffusion models produce the highest-quality samples among current generative approaches, with excellent mode coverage and diversity.
- Sampling is slow by default ($T = 1000$ steps), but DDIM and other ODE-based solvers can reduce this to 20-50 steps with minimal quality loss.
- The forward noising process uses a fixed schedule ($\beta_t$) and requires no training; only the reverse denoiser is learned.
- Diffusion models connect to score-based models through the equivalence between predicting noise and estimating the score $\nabla_x \log p(x)$.

## Function

```python
def add_noise(x: float, noise: float, alpha: float) -> float:
```

- `x` -- clean data sample $x_0$
- `noise` -- Gaussian noise sample $\epsilon$
- `alpha` -- cumulative signal retention factor $\bar{\alpha}_t$

## Run tests

```bash
pytest modules/ml/generative/diffusion-models/python -q
```
