# Alignment Methods

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to learn the main LLM alignment stack in one place:
supervised fine-tuning, pairwise preference objectives, RLHF reward modeling,
and the anchoring terms that keep the model from drifting too far.

## First Principles

- Alignment usually starts after pretraining, not before.
- SFT teaches the instruction format with direct token supervision.
- Preference objectives learn which answer is better when exact references are weak.
- RLHF uses a reward model before policy optimization.
- KL and PTX anchoring keep useful base-model behavior while the aligned model changes.

## Core Math

SFT loss:

$$
\mathcal{L}_{\text{SFT}} = -\frac{1}{\sum_i m_i}\sum_i m_i \log p_\theta(y_i \mid x_i)
$$

Pairwise preference loss:

$$
\mathcal{L}_{\text{pref}} = -\log \sigma(s_{\text{chosen}} - s_{\text{rejected}})
$$

DPO loss:

$$
\mathcal{L}_{\text{DPO}} = -\log \sigma\left(\beta(\Delta \log \pi - \Delta \log \pi_{\text{ref}})\right)
$$

Anchored objective:

$$
\mathcal{L} = (1-\alpha)\mathcal{L}_{\text{align}} + \alpha \mathcal{L}_{\text{ptx}}
$$

## From Math To Code

- SFT averages token-level negative log-likelihood over kept tokens.
- Preference learning starts from a chosen-minus-rejected margin.
- DPO turns the policy-vs-reference margin gap into one scalar logit before the logistic loss.
- Anchoring mixes the alignment loss with a stabilizing KL or PTX-style term.

## Minimal Code Mental Model

```python
sft = sft_loss(logits, targets, mask)
margin = preference_margin(score_chosen, score_rejected)
pref = preference_loss(score_chosen, score_rejected)
dpo_term = dpo_logit(delta_logp, delta_logp_ref, beta=0.1)
dpo = dpo_loss(delta_logp, delta_logp_ref, beta=0.1)
total = anchored_loss(align_loss=dpo, ptx_loss=sft, alpha=0.1)
```

## Function

```python
def sft_loss(logits: list[list[float]], targets: list[int], mask: list[int]) -> float:
def preference_margin(score_chosen: float, score_rejected: float) -> float:
def preference_loss(score_chosen: float, score_rejected: float) -> float:
def dpo_logit(delta_logp: float, delta_logp_ref: float, beta: float = 0.1) -> float:
def dpo_loss(delta_logp: float, delta_logp_ref: float, beta: float = 0.1) -> float:
def reward_model_loss(chosen: float, rejected: float) -> float:
def kl_penalty(p: list[float], q: list[float], beta: float) -> float:
def anchored_loss(align_loss: float, ptx_loss: float, alpha: float) -> float:
```

## When To Use What

- Use SFT first to teach the model the instruction format.
- Use pairwise preference losses when ranked comparisons are easier to collect than exact labels.
- Use DPO when you want a simpler preference-optimization path than RLHF.
- Use RLHF reward modeling when explicit reward scores are part of the training loop.
- Use KL or PTX anchoring when the aligned model starts drifting away from useful base behavior.

## Run tests

```bash
pytest modules/ml/llm/alignment-methods/python -q
```
