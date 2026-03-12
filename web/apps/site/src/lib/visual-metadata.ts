export interface VisualDefinition {
  id: string;
  title: string;
  summary: string;
  track: string;
  topic: string;
  href: string;
  parallax: number;
  slug?: string;
  showOnTopicPage?: boolean;
}

export function getVisualRegistryKey(track: string, topic: string, slug: string) {
  return `${track}/${topic}/${slug}`;
}

export const VISUALS: VisualDefinition[] = [
  {
    id: "attention-map-preview",
    title: "Attention map preview",
    summary: "Causal masking and locality change which earlier tokens a query can still attend to.",
    track: "ml",
    topic: "llm",
    href: "/track/ml/llm",
    parallax: 8,
  },
  {
    id: "next-token-distribution",
    title: "Next-token distribution",
    summary: "Temperature sharpens or flattens the probability mass over candidate tokens.",
    track: "ml",
    topic: "llm",
    href: "/track/ml/llm",
    parallax: 6,
  },
  {
    id: "positional-encoding",
    title: "Positional encoding",
    summary: "Sinusoidal signals show how token position becomes usable numeric structure.",
    track: "ml",
    topic: "llm",
    href: "/track/ml/llm",
    parallax: 6,
  },
  {
    id: "attention-mechanisms",
    title: "Attention mechanisms",
    summary: "Compare full, causal, and local masking to see which token pairs can interact and how weights change.",
    track: "ml",
    topic: "llm",
    slug: "attention-mechanisms",
    href: "/track/ml/llm",
    parallax: 8,
    showOnTopicPage: true,
  },
  {
    id: "tokenization-trade-offs",
    title: "Tokenization trade-offs",
    summary: "Compare character-like, subword-like, and word-like tokenization against the same context budget.",
    track: "ml",
    topic: "llm",
    slug: "tokenization",
    href: "/track/ml/llm",
    parallax: 8,
    showOnTopicPage: true,
  },
  {
    id: "long-context-and-caching",
    title: "Long context and caching",
    summary: "See how prompt length drives quadratic work and how cached prefixes cut fresh prefill cost.",
    track: "ml",
    topic: "llm",
    slug: "long-context-and-caching",
    href: "/track/ml/llm",
    parallax: 8,
    showOnTopicPage: true,
  },
  {
    id: "decoding-policy-explorer",
    title: "Decoding policy explorer",
    summary: "Compare greedy, top-k, top-p, and beam-style selection from the same next-token score surface.",
    track: "ml",
    topic: "llm",
    slug: "decoding-methods",
    href: "/track/ml/llm",
    parallax: 8,
    showOnTopicPage: true,
  },
  {
    id: "retrieval-metrics",
    title: "Retrieval metrics",
    summary: "Compare baseline and reranked retrieval at different cutoffs using recall, precision, F1, reciprocal rank, and rerank gain.",
    track: "ml",
    topic: "llm",
    slug: "retrieval-metrics",
    href: "/track/ml/llm",
    parallax: 8,
    showOnTopicPage: true,
  },
  {
    id: "reasoning-and-test-time-compute",
    title: "Reasoning and test-time compute",
    summary: "See how extra traces change quality wrappers like best-of-n and majority vote while multiplying token cost.",
    track: "ml",
    topic: "llm",
    slug: "reasoning-and-test-time-compute",
    href: "/track/ml/llm",
    parallax: 8,
    showOnTopicPage: true,
  },
  {
    id: "vote-metrics",
    title: "Vote metrics",
    summary: "Grouped sampled answers reveal how normalization changes agreement, margin, entropy, and disagreement.",
    track: "ml",
    topic: "llm",
    slug: "vote-metrics",
    href: "/track/ml/llm",
    parallax: 8,
    showOnTopicPage: true,
  },
  {
    id: "reliability-diagram",
    title: "Reliability diagram",
    summary: "Confidence can move away from observed accuracy even when rank order stays roughly intact.",
    track: "ml",
    topic: "evaluation",
    slug: "calibration",
    href: "/track/ml/evaluation",
    parallax: 7,
    showOnTopicPage: true,
  },
  {
    id: "gradient-descent-playground",
    title: "Gradient descent playground",
    summary: "See how learning rate, step count, and starting point change the optimization path.",
    track: "ml",
    topic: "fundamentals",
    slug: "gradient-descent",
    href: "/track/ml/fundamentals",
    parallax: 10,
    showOnTopicPage: true,
  },
  {
    id: "activation-functions",
    title: "Activation functions",
    summary: "Compare sparse and smooth nonlinearities by curve shape, local output, and local gradient.",
    track: "ml",
    topic: "deep-learning",
    slug: "activation-functions",
    href: "/track/ml/deep-learning",
    parallax: 8,
    showOnTopicPage: true,
  },
  {
    id: "normalization-methods",
    title: "Normalization methods",
    summary: "Compare BatchNorm, LayerNorm, and RMSNorm by which axes they normalize over.",
    track: "ml",
    topic: "deep-learning",
    slug: "normalization-methods",
    href: "/track/ml/deep-learning",
    parallax: 8,
    showOnTopicPage: true,
  },
  {
    id: "matrix-transform-explorer",
    title: "Matrix transform explorer",
    summary: "Adjust a 2D matrix and vector to make linear transforms visible instead of symbolic.",
    track: "ml",
    topic: "fundamentals",
    slug: "vectors-matrices",
    href: "/track/ml/fundamentals",
    parallax: 7,
    showOnTopicPage: true,
  },
  {
    id: "composite-btree-path",
    title: "Composite B-tree path",
    summary: "Compare a full table scan with a composite index path for a common filtered, ordered query.",
    track: "databases",
    topic: "indexing",
    slug: "btree-basics",
    href: "/track/databases/indexing",
    parallax: 8,
    showOnTopicPage: true,
  },
  {
    id: "monotonic-stack-walkthrough",
    title: "Monotonic stack walkthrough",
    summary: "Step through daily temperatures and watch unresolved indices stay on the stack until a warmer day resolves them.",
    track: "dsa",
    topic: "monotonic-stack",
    slug: "monotonic-stack",
    href: "/track/dsa/monotonic-stack",
    parallax: 7,
    showOnTopicPage: true,
  },
  {
    id: "retries-and-fallbacks",
    title: "Retries and fallbacks",
    summary: "See when transient failures should retry, when to stop, and when to degrade to a cheaper fallback path.",
    track: "software-engineering",
    topic: "reliability",
    slug: "retries-and-fallbacks",
    href: "/track/software-engineering/reliability",
    parallax: 8,
    showOnTopicPage: true,
  },
  {
    id: "classification-metrics-core",
    title: "Classification metrics core",
    summary: "Move the threshold and watch the confusion matrix, precision, recall, F1, and accuracy change together.",
    track: "ml",
    topic: "evaluation",
    slug: "classification-metrics-core",
    href: "/track/ml/evaluation",
    parallax: 8,
    showOnTopicPage: true,
  },
];

export function countVisualsForTrack(track: string) {
  return VISUALS.filter((visual) => visual.track === track).length;
}

export function countTopicVisuals(track: string, topic: string) {
  return VISUALS.filter(
    (visual) =>
      visual.showOnTopicPage &&
      visual.track === track &&
      visual.topic === topic
  ).length;
}
