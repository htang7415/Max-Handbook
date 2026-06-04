# Assessments

Use this page to check whether the ML track is building engineering judgment, not just formula recall.

## Purpose

Use this page to test whether you can:
- choose the right metric for the product failure mode
- connect model quality to calibration, latency, and cost
- explain when a simpler model or retrieval baseline is the better choice
- identify whether a failure comes from data, training, evaluation, serving, or rollout

## First Principles

- A model is useful only when its measured behavior matches the product risk.
- Offline metrics are necessary but not sufficient; serving behavior and monitoring decide whether a model stays useful.
- Modern LLM work needs evaluation sets, judge checks, retrieval diagnostics, and release gates, not only benchmark scores.
- Good ML engineering separates model selection, threshold choice, rollout policy, and incident response.

## Section Checks

- Fundamentals: Can you explain the target quantity before writing code?
- Data and Representation: Can you name the leakage, missingness, or embedding failure that would break the result?
- Classical Models: Can you choose a baseline that exposes whether a deep model is actually needed?
- Evaluation and Calibration: Can you choose a metric, confidence summary, and threshold together?
- Optimization and Training: Can you identify instability from loss curves, gradients, or schedules?
- Deep Learning: Can you explain the role of normalization, initialization, loss choice, and regularization?
- LLMs: Can you separate tokenization, retrieval, reasoning, alignment, evaluation, and serving failures?
- Generative and Vision: Can you explain what evidence shows output quality, not just image or sample plausibility?
- Systems and MLOps: Can you state the latency, cost, capacity, drift, and rollout gates?
- Reinforcement Learning: Can you explain reward, policy, off-policy data, and safety boundaries?

## Capstone Readiness

You are ready for ML capstones when you can do all of these:

- define a target behavior and a metric that actually measures it
- build or choose a small baseline
- describe the evaluation dataset and its known blind spots
- explain calibration or uncertainty for the decision threshold
- name the serving budget and rollback signal
- state what should happen when monitoring detects drift or regression

## Graduation Check

The track is working if you can review a proposed ML system and answer these six questions quickly:

1. What product behavior is the model responsible for?
2. What data assumption can break it?
3. Which metric decides whether it improved?
4. How confident is the threshold or decision?
5. What are the serving latency and cost budgets?
6. What stops rollout or triggers rollback?

## Weak Signals

You probably need another pass through the foundations if:

- you optimize a model before defining the target behavior
- you trust an average metric without slice or calibration checks
- you ship an LLM change without retrieval, judge, or regression cases
- you cannot say what rollback signal protects users
