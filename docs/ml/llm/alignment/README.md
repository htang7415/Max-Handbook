# LLM Alignment

Alignment is the stack that turns a capable next-token model into one that follows instructions and preferences.

## Purpose

Use this page to keep alignment in the right order:
- supervised fine-tuning
- preference learning
- policy optimization
- regularization and anchoring

## First Principles

- Alignment starts with a pretrained model that already knows language.
- SFT teaches the model the task format and instruction style.
- Preference learning teaches relative quality when exact references are weak.
- Policy optimization improves toward preference or reward signals but needs guardrails against drift.
- KL and PTX-style anchoring preserve useful base behavior while aligning the model.

## Core Math

- Preference-style objective shape:
  $$
  \log \sigma(s_{\text{chosen}} - s_{\text{rejected}})
  $$
- KL control penalizes moving too far from a reference policy.

## Minimal Code Mental Model

```python
model = supervised_fine_tune(base_model, demonstrations)
model = optimize_preferences(model, chosen, rejected, kl_penalty)
```

## Canonical Modules

- Main stack: `alignment-methods`

## Supporting Modules

- Group-based optimization: `group-based-optimization`
- Judge-based support: `judge-calibration`, `judge-pairwise`, `judge-agreement-matrix`

## When To Use What

- Start with SFT before any preference optimization.
- Start with SFT inside `alignment-methods`, then move to preference objectives.
- Use DPO inside `alignment-methods` when pairwise data is strong and you want a simpler path than RLHF.
- Use RLHF inside `alignment-methods` when reward modeling and online policy improvement are central.
- Use KL or PTX anchoring inside `alignment-methods` when the aligned model starts losing useful base-model behavior.
