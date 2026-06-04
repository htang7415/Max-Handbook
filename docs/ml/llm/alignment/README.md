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

## Alignment Stack

1. SFT teaches the instruction format.
2. Preference data ranks acceptable and unacceptable outputs.
3. DPO-style objectives optimize pairwise preferences without a separate online RL loop.
4. RLHF-style pipelines add reward modeling and policy optimization when that extra machinery is justified.
5. KL or PTX anchoring keeps the aligned model from losing useful base behavior.

## Engineering Boundary

This guide is the alignment map. The dense formulas and runnable helpers live in `alignment-methods`; use this page to decide which training stage or failure mode matters.

## Canonical Modules

- Main stack: `alignment-methods`

## Supporting Modules

- Group-based optimization: `group-based-optimization`
- Judge-based support: `judge-evaluation-methods`

## When To Use What

- Start with SFT before any preference optimization.
- Use DPO inside `alignment-methods` when pairwise data is strong and you want a simpler path than RLHF.
- Use RLHF inside `alignment-methods` when reward modeling and online policy improvement are central.
- Use KL or PTX anchoring inside `alignment-methods` when the aligned model starts losing useful base-model behavior.
