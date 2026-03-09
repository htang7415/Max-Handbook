# Diffusion Sampling and Guidance Trade-offs

> Track: `ml` | Topic: `generative`

## Concept

Classifier-free guidance steers diffusion sampling toward a condition, such as a
text prompt, by comparing two denoising predictions: one conditional and one
unconditional. The unconditional prediction captures the model's generic prior;
the conditional prediction says how the prompt wants the sample to change.

Guidance works by moving from the unconditional prediction toward the
conditional one. If the scale is small, the model stays diverse but less prompt
faithful. If the scale is large, the model follows the prompt more aggressively
but can oversaturate or collapse diversity.

From first principles, guidance is just extrapolation in prediction space:
"start from what the model would do without the prompt, then move some multiple
of the prompt-specific correction."

## Math

The guided noise prediction blends conditional and unconditional estimates:

$$\tilde{\epsilon} = \epsilon_\theta(x_t) + w\bigl(\epsilon_\theta(x_t, c) - \epsilon_\theta(x_t)\bigr)$$

This makes the endpoints easy to read:

$$w = 0 \Rightarrow \tilde{\epsilon} = \epsilon_\theta(x_t),\qquad
w = 1 \Rightarrow \tilde{\epsilon} = \epsilon_\theta(x_t, c)$$

- $w$ -- guidance scale (0 = unconditional, higher = stronger conditioning)
- $\epsilon_\theta(x_t, c)$ -- noise prediction conditioned on $c$
- $\epsilon_\theta(x_t)$ -- unconditional noise prediction (condition dropped)
- $c$ -- conditioning signal (e.g., text embedding, class label)
- $x_t$ -- noisy sample at timestep $t$
- $\tilde{\epsilon}$ -- guided noise prediction used for sampling

## Key Points

- At $w = 0$ the model samples unconditionally; increasing $w$ trades diversity for stronger adherence to the conditioning signal.
- At $w = 1$ the guided prediction equals the conditional prediction.
- Typical guidance scales are $w \in [3, 15]$; values beyond this range tend to produce oversaturated images with artifacts.
- Classifier-free guidance requires no external classifier -- the model is trained to handle both conditional and unconditional denoising by randomly dropping the condition.
- The fidelity-diversity trade-off from guidance is analogous to the temperature parameter in language models: higher guidance concentrates the output distribution.
- Guidance can be applied per-step, and dynamic schedules (e.g., higher guidance early, lower late) can improve results.

## Function

```python
def guided_step(base: float, cond: float, scale: float) -> float:
```

- `base` -- unconditional noise prediction $\epsilon_\theta(x_t)$
- `cond` -- conditional noise prediction $\epsilon_\theta(x_t, c)$
- `scale` -- guidance scale $w$

## Run tests

```bash
pytest modules/ml/generative/diffusion-guidance-tradeoffs/python -q
```
