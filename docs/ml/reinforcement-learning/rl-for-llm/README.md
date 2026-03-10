# RL for LLMs

RL for LLMs is preference optimization under long sequences, expensive sampling, and fragile reward signals.

## Purpose

Use this page to separate the main RL-for-LLM ideas:
- preference data and reward signals
- PPO-style policy updates
- DPO-style direct objectives
- KL anchoring and reward control

## First Principles

- The base model already knows language; RL is usually refining behavior, not teaching language from scratch.
- Preference data is often easier to collect than exact gold outputs.
- PPO-style methods optimize a policy under ratio and KL constraints.
- DPO-style methods avoid an explicit reward model by learning directly from chosen vs rejected pairs.
- Reward hacking and overoptimization are central risks because the reward signal is imperfect.

## Core Math

- PPO-style ratio:
  $$
  r_t(\theta) = \frac{\pi_\theta(a_t \mid s_t)}{\pi_{\text{old}}(a_t \mid s_t)}
  $$
- DPO-style preference signal favors chosen responses over rejected ones.

## Minimal Code Mental Model

```python
scores = judge_or_reward_model(samples)
policy = update_policy(policy, samples, scores, kl_penalty)
```

## Canonical Modules

- Main alignment routes: `alignment-methods`, `dpo-vs-ppo`, `group-based-optimization`
- Reward behavior: `policy-optimization-utilities`
- Anchoring: `alignment-methods`

## Supporting Modules

- Alignment stack: `docs/ml/llm/alignment`

## When To Use What

- Start with the LLM alignment guide before RL-for-LLM specifics.
- Use `dpo-vs-ppo` when choosing the main optimization family.
- Use `group-based-optimization` when sequence-group objectives are the main modern path.
- Use KL controls and the policy-optimization utilities family when the model starts drifting or overoptimizing the reward.
