# Vote and Minority-Cluster Metrics

Vote metrics summarize how multiple sampled answers agree, disagree, or fragment into alternatives.

## Metric Families

- Agreement metrics: answer stability, majority-vote margin, vote frequency gap
- Diversity metrics: answer uniqueness rate, answer repeat rate, candidate diversity
- Concentration metrics: vote concentration, top vote share, runner-up vote share
- Tail metrics: vote tail mass, nonmajority vote share, minority vote share
- Minority-cluster metrics: count, share, entropy, dominance, balance
- Residual-tail metrics: tail entropy, tail gap, tail ratio, tail concentration

## How to Use Them

- Start with stability, majority-vote margin, and vote entropy for a quick read on self-consistency.
- Use uniqueness and candidate diversity when you care about exploration, not just consensus.
- Use concentration metrics when one answer is winning but you need to know how decisively.
- Use minority-cluster metrics when alternatives form structured competing groups instead of random noise.
- Use residual-tail metrics when you need to distinguish one strong alternative from a noisy long tail.

## Good Defaults

- Start with the canonical module `vote-metrics`
- Use `answer_stability` for repeated-run consistency
- Use `majority_vote_margin` plus `vote_entropy` for confidence-style summaries
- Use `answer_uniqueness_rate` for diversity
- Use `minority_cluster_entropy` when disagreement structure matters
