# Agent Decision Methods

This page groups the main quantitative decision patterns used across the `ai-agents` track.

## Purpose

Use this page to choose the right kind of decision logic:
- scores and rankings
- thresholds and gates
- priors and posterior updates
- budgets and constrained choices
- stopping rules and trade-off frontiers

## First Principles

- A score is useful when the system must rank alternatives on one scale.
- A threshold is useful when the system must map a score to `allow`, `review`, `block`, or similar routes.
- A posterior is useful when decisions should update from observed evidence instead of staying fixed.
- A budget is useful when steps or policies must fit within hard limits on cost, latency, or risk.
- A stopping rule is useful when more evidence or more steps are not always worth continuing.

## Core Patterns

- Scores and rankings:
  `routing-scorecards`, `expected-value-tool-selection`, `risk-adjusted-benchmark-summaries`
- Thresholds and gates:
  `risk-scoring-and-thresholds`, `decision-cost-matrices`, `planning-stop-conditions`
- Priors and posteriors:
  `posterior-routing`, `bayesian-benchmark-updating`
- Budgets and constraints:
  `latency-budget-accounting`, `budgeted-multi-step-planning`, `constrained-optimization-for-budgeted-agent-policies`
- Stopping rules:
  `utility-aware-stopping`, `sequential-test-stopping`
- Trade-off sets:
  `pareto-front-benchmark-comparisons`, `hierarchical-benchmark-aggregation`
- Adaptive exploration:
  `bandit-style-exploration-exploitation`

## When To Use What

- Use a scorecard when several signals should combine into one comparable rank.
- Use thresholds when the route depends on crossing a known safety or quality bar.
- Use a posterior when repeated evidence should update route choice or benchmark belief over time.
- Use budgets when the main question is feasibility under hard resource limits.
- Use stopping rules when the system must decide whether continuing is still worth it.
- Use Pareto or hierarchical summaries when one scalar score would hide too much structure.

## Cross-Topic Links

- Workflow decisions: `routing-scorecards`, `posterior-routing`, `uncertainty-aware-routing`
- Tool decisions: `expected-value-tool-selection`, `bandit-style-exploration-exploitation`
- Planning decisions: `utility-aware-stopping`, `budgeted-multi-step-planning`, `constrained-optimization-for-budgeted-agent-policies`
- Evaluation decisions: `bayesian-benchmark-updating`, `sequential-test-stopping`, `pareto-front-benchmark-comparisons`, `hierarchical-benchmark-aggregation`
- Guardrail decisions: `decision-cost-matrices`, `policy-decision-tables`, `risk-scoring-and-thresholds`
