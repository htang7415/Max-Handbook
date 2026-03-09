# Introduction to Dynamic Programming

> Track: `dsa` | Topic: `dynamic-programming`

## What This Module Covers

This introduction frames dynamic programming as the process of defining reusable subproblems, writing transitions between them, and solving the whole problem from those smaller answers.

## Recognition Cues

- Brute force repeats the same subproblems.
- The answer can be built from smaller states.
- You need to count, optimize, or decide over many overlapping choices.

## Core Ideas

- A DP solution needs a state definition, base cases, and a transition rule.
- Initialization is part of correctness, not just setup.
- Loop order matters because it determines which prior states are already valid.

## Common Mistakes

- Starting with transitions before defining what the state means.
- Forgetting base cases or empty-prefix behavior.
- Compressing space too early and breaking dependency order.

## Connections

- Knapsack problems teach capacity-state thinking.
- Sequence DP teaches prefix and interval states.
- Stock problems teach small-state finite-state modeling.

## Self-Check

- What does one DP state represent?
- Which earlier states are needed to compute the current one?
- What initialization makes the transition valid from the start?
