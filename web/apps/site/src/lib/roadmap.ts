import type { Track, Topic } from "./content";

const TRACK_ORDER = [
  "dsa",
  "software-engineering",
  "databases",
  "ml",
  "ai-agents",
];

const TOPIC_ORDER: Record<string, string[]> = {
  "dsa": [
    "array",
    "linked-list",
    "hash-tables",
    "string",
    "double-pointers",
    "stack-and-queue",
    "binary-tree",
    "backtracking",
    "greedy-algorithm",
    "dynamic-programming",
    "monotonic-stack",
  ],
  "software-engineering": [
    "tooling",
    "python",
    "rust",
    "testing",
    "apis",
    "security-basics",
    "performance",
    "concurrency",
    "design-patterns",
    "system-design",
  ],
  "databases": [
    "relational",
    "schema-design",
    "sql-patterns",
    "indexing",
    "transactions",
    "query-plans",
    "caching",
    "nosql",
    "streaming",
    "vector-db",
  ],
  "ml": [
    "fundamentals",
    "data",
    "models",
    "evaluation",
    "optimization",
    "deep-learning",
    "systems",
    "representation",
    "generative",
    "computer-vision",
    "llm",
    "reinforcement-learning",
    "mlops",
  ],
  "ai-agents": [
    "prompting",
    "tool-use",
    "rag",
    "memory",
    "planning",
    "multi-agent",
    "evals",
    "observability",
    "guardrails",
  ],
};

function buildRankMap(order: string[]) {
  const map = new Map<string, number>();
  order.forEach((id, index) => map.set(id, index));
  return map;
}

const TRACK_RANK = buildRankMap(TRACK_ORDER);
const TOPIC_RANKS = new Map(
  Object.entries(TOPIC_ORDER).map(([trackId, order]) => [trackId, buildRankMap(order)])
);

export function sortTracks(tracks: Track[]): Track[] {
  return tracks.slice().sort((a, b) => {
    const rankA = TRACK_RANK.get(a.id) ?? Number.MAX_SAFE_INTEGER;
    const rankB = TRACK_RANK.get(b.id) ?? Number.MAX_SAFE_INTEGER;
    if (rankA !== rankB) return rankA - rankB;
    return a.name.localeCompare(b.name);
  });
}

export function sortTopics(topics: Topic[]): Topic[] {
  return topics.slice().sort((a, b) => {
    const trackRankA = TRACK_RANK.get(a.track) ?? Number.MAX_SAFE_INTEGER;
    const trackRankB = TRACK_RANK.get(b.track) ?? Number.MAX_SAFE_INTEGER;
    if (trackRankA !== trackRankB) return trackRankA - trackRankB;
    if (a.track !== b.track) return a.track.localeCompare(b.track);

    const topicRank = TOPIC_RANKS.get(a.track);
    const rankA = topicRank?.get(a.topic);
    const rankB = topicRank?.get(b.topic);
    if (rankA != null && rankB != null) return rankA - rankB;
    if (rankA != null) return -1;
    if (rankB != null) return 1;

    return a.name.localeCompare(b.name);
  });
}

export function sortTopicsForTrack(topics: Topic[], trackId: string): Topic[] {
  const topicRank = TOPIC_RANKS.get(trackId);
  return topics.slice().sort((a, b) => {
    const rankA = topicRank?.get(a.topic);
    const rankB = topicRank?.get(b.topic);
    if (rankA != null && rankB != null) return rankA - rankB;
    if (rankA != null) return -1;
    if (rankB != null) return 1;
    return a.name.localeCompare(b.name);
  });
}

export function extractModuleOrder(
  docContent: string | undefined,
  trackId: string,
  topicId: string
): string[] {
  const order: string[] = [];
  const seen = new Set<string>();
  if (!docContent) return order;

  const { canonical, supporting } = extractTopicEntryGroups(
    docContent,
    trackId,
    topicId
  );
  for (const slug of [...canonical, ...supporting]) {
    if (!seen.has(slug)) {
      seen.add(slug);
      order.push(slug);
    }
  }

  const pattern = new RegExp(`modules/${trackId}/${topicId}/([a-z0-9-]+)`, "g");
  let match: RegExpExecArray | null;
  while ((match = pattern.exec(docContent)) !== null) {
    const slug = match[1];
    if (!seen.has(slug)) {
      seen.add(slug);
      order.push(slug);
    }
  }
  return order;
}

function extractSectionBodies(
  docContent: string | undefined,
  headingNames: string[]
): string[] {
  if (!docContent) return [];
  const headingSet = new Set(headingNames.map((heading) => heading.toLowerCase()));
  const lines = docContent.split(/\r?\n/);
  const bodies: string[] = [];
  let active = false;
  let currentLines: string[] = [];

  function flush() {
    if (active && currentLines.length > 0) {
      bodies.push(currentLines.join("\n").trim());
    }
    currentLines = [];
  }

  for (const line of lines) {
    const heading = line.match(/^##\s+(.+)$/);
    if (heading) {
      flush();
      active = headingSet.has(heading[1].trim().toLowerCase());
      continue;
    }
    if (active) currentLines.push(line);
  }
  flush();

  return bodies.filter(Boolean);
}

function extractReferencedSlugs(
  content: string,
  trackId: string,
  topicId: string
): string[] {
  const slugs: string[] = [];
  const seen = new Set<string>();
  const pathPattern = new RegExp(
    `(?:docs|modules)/${trackId}/${topicId}/([a-z0-9-]+)`,
    "g"
  );
  const inlinePattern = /`([^`]+)`/g;

  function push(raw: string) {
    const trimmed = raw.trim();
    let slug: string | undefined;
    const pathMatch = trimmed.match(
      new RegExp(`^(?:docs|modules)/${trackId}/${topicId}/([a-z0-9-]+)$`)
    );
    if (pathMatch) {
      slug = pathMatch[1];
    } else if (/^[a-z0-9-]+$/.test(trimmed)) {
      slug = trimmed;
    }
    if (slug && !seen.has(slug)) {
      seen.add(slug);
      slugs.push(slug);
    }
  }

  let match: RegExpExecArray | null;
  while ((match = inlinePattern.exec(content)) !== null) {
    push(match[1]);
  }
  while ((match = pathPattern.exec(content)) !== null) {
    push(match[1]);
  }

  return slugs;
}

export function extractTopicEntryGroups(
  docContent: string | undefined,
  trackId: string,
  topicId: string
): { canonical: string[]; supporting: string[] } {
  const canonicalBodies = extractSectionBodies(docContent, [
    "canonical modules",
    "canonical families",
    "canonical learning units",
  ]);
  const supportingBodies = extractSectionBodies(docContent, [
    "supporting modules",
    "supporting guides",
    "supporting content",
  ]);

  return {
    canonical: canonicalBodies.flatMap((body) =>
      extractReferencedSlugs(body, trackId, topicId)
    ),
    supporting: supportingBodies.flatMap((body) =>
      extractReferencedSlugs(body, trackId, topicId)
    ),
  };
}
