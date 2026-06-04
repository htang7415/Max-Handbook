# {{TITLE}}

> Track: `dsa` | Topic: `{{TOPIC}}`

## Problem in One Line

<!-- Restate the task in plain English. Keep this to 1-2 sentences. -->

## Recognition Cues

<!--
- What input shape or constraint should trigger this pattern?
- What words in the prompt hint at the right approach?
-->

| Signal | What it suggests |
| --- | --- |
| <!-- input/constraint/prompt cue --> | <!-- pattern implication --> |

## Baseline Idea

<!-- Describe the brute-force or naive approach and why it is too slow. -->

## Core Insight

<!-- State the one observation that unlocks the intended solution. -->

## Invariant / State

<!--
- What stays true during the algorithm?
- For DP: what does each state mean?
- For pointers/windows/stacks: what do the indices or container represent?
-->

## Walkthrough

<!-- Walk through one representative example in a few short steps. -->

| Step | State | Reason |
| --- | --- | --- |
| 1 | <!-- state --> | <!-- why this move is valid --> |

## Complexity

<!--
- Time: O(...)
- Space: O(...)
-->

## Edge Cases

| Case | Expected behavior | Why it matters |
| --- | --- | --- |
| Empty input | <!-- behavior --> | Boundary |
| Single element | <!-- behavior --> | Boundary |
| Duplicates | <!-- behavior --> | Invariant |
| No-solution case | <!-- behavior --> | Contract |

## Pattern Transfer

<!-- List 2-4 nearby problems that reuse the same idea with a twist. -->

## Self-Check

<!--
- Why does this approach work?
- What would break a naive solution?
- What are the key boundary conditions?
-->

## Function

```python
# Replace with the actual function or method signature
```

## Run tests

```bash
pytest modules/dsa/{{TOPIC}}/{{SLUG}}/python -q
```
