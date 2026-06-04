import type { ContentIndex, Track, Topic } from "./content";

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
    "workflow-and-ai-tooling",
    "contracts-and-apis",
    "testing-and-verification",
    "security-and-trust",
    "concurrency-and-state",
    "observability-and-operations",
    "reliability-and-delivery",
    "performance-and-cost",
    "system-design-and-patterns",
    "implementation-and-practice",
  ],
  "databases": [
    "relational-core",
    "schema-design",
    "sql-and-analytics",
    "indexing-and-access-paths",
    "transactions-and-concurrency",
    "query-plans-and-performance",
    "caching",
    "streaming-and-cdc",
    "nosql-and-distributed-data",
    "vector-retrieval-and-memory",
  ],
  "ml": [
    "fundamentals",
    "data-and-representation",
    "classical-models",
    "evaluation-and-calibration",
    "optimization-and-training",
    "deep-learning",
    "llms",
    "generative-and-vision",
    "systems-and-mlops",
    "reinforcement-learning",
  ],
  "ai-agents": [
    "overview-and-architecture",
    "prompting-and-context",
    "tool-use-and-mcp",
    "retrieval-and-memory",
    "planning-and-workflows",
    "observability-and-tracing",
    "evaluation-and-benchmarks",
    "guardrails-and-security",
    "multi-agent-systems",
    "practice-and-capstones",
  ],
};

export interface HandbookTopicGroup {
  track: string;
  topic: string;
  name: string;
  sourceTopics: string[];
}

export const HANDBOOK_TOPIC_GROUPS: Record<string, HandbookTopicGroup[]> = {
  "ml": [
    {
      track: "ml",
      topic: "fundamentals",
      name: "Fundamentals",
      sourceTopics: [
        "fundamentals",
        "path-beginner",
        "path-interview",
        "path-math-first",
        "roadmap",
      ],
    },
    {
      track: "ml",
      topic: "data-and-representation",
      name: "Data And Representation",
      sourceTopics: ["data", "representation"],
    },
    {
      track: "ml",
      topic: "classical-models",
      name: "Classical Models",
      sourceTopics: ["models"],
    },
    {
      track: "ml",
      topic: "evaluation-and-calibration",
      name: "Evaluation And Calibration",
      sourceTopics: ["evaluation"],
    },
    {
      track: "ml",
      topic: "optimization-and-training",
      name: "Optimization And Training",
      sourceTopics: ["optimization"],
    },
    {
      track: "ml",
      topic: "deep-learning",
      name: "Deep Learning",
      sourceTopics: ["deep-learning"],
    },
    {
      track: "ml",
      topic: "llms",
      name: "LLMs",
      sourceTopics: ["llm", "path-llm-systems"],
    },
    {
      track: "ml",
      topic: "generative-and-vision",
      name: "Generative And Vision",
      sourceTopics: ["generative", "computer-vision"],
    },
    {
      track: "ml",
      topic: "systems-and-mlops",
      name: "Systems And MLOps",
      sourceTopics: ["systems", "mlops"],
    },
    {
      track: "ml",
      topic: "reinforcement-learning",
      name: "Reinforcement Learning",
      sourceTopics: ["reinforcement-learning"],
    },
  ],
  "ai-agents": [
    {
      track: "ai-agents",
      topic: "overview-and-architecture",
      name: "Overview And Architecture",
      sourceTopics: ["overview"],
    },
    {
      track: "ai-agents",
      topic: "prompting-and-context",
      name: "Prompting And Context",
      sourceTopics: ["prompting"],
    },
    {
      track: "ai-agents",
      topic: "tool-use-and-mcp",
      name: "Tool Use And MCP",
      sourceTopics: ["tool-use"],
    },
    {
      track: "ai-agents",
      topic: "retrieval-and-memory",
      name: "Retrieval And Memory",
      sourceTopics: ["rag", "memory"],
    },
    {
      track: "ai-agents",
      topic: "planning-and-workflows",
      name: "Planning And Workflows",
      sourceTopics: ["planning", "workflows"],
    },
    {
      track: "ai-agents",
      topic: "observability-and-tracing",
      name: "Observability And Tracing",
      sourceTopics: ["observability"],
    },
    {
      track: "ai-agents",
      topic: "evaluation-and-benchmarks",
      name: "Evaluation And Benchmarks",
      sourceTopics: ["evaluation", "evals"],
    },
    {
      track: "ai-agents",
      topic: "guardrails-and-security",
      name: "Guardrails And Security",
      sourceTopics: ["guardrails"],
    },
    {
      track: "ai-agents",
      topic: "multi-agent-systems",
      name: "Multi-Agent Systems",
      sourceTopics: ["multi-agent"],
    },
    {
      track: "ai-agents",
      topic: "practice-and-capstones",
      name: "Practice And Capstones",
      sourceTopics: ["assessments", "capstones"],
    },
  ],
  "databases": [
    {
      track: "databases",
      topic: "relational-core",
      name: "Relational Core",
      sourceTopics: ["relational"],
    },
    {
      track: "databases",
      topic: "schema-design",
      name: "Schema Design",
      sourceTopics: ["schema-design"],
    },
    {
      track: "databases",
      topic: "sql-and-analytics",
      name: "SQL And Analytics",
      sourceTopics: ["sql-patterns"],
    },
    {
      track: "databases",
      topic: "indexing-and-access-paths",
      name: "Indexing And Access Paths",
      sourceTopics: ["indexing"],
    },
    {
      track: "databases",
      topic: "transactions-and-concurrency",
      name: "Transactions And Concurrency",
      sourceTopics: ["transactions"],
    },
    {
      track: "databases",
      topic: "query-plans-and-performance",
      name: "Query Plans And Performance",
      sourceTopics: ["query-plans"],
    },
    {
      track: "databases",
      topic: "caching",
      name: "Caching",
      sourceTopics: ["caching"],
    },
    {
      track: "databases",
      topic: "streaming-and-cdc",
      name: "Streaming And CDC",
      sourceTopics: ["streaming"],
    },
    {
      track: "databases",
      topic: "nosql-and-distributed-data",
      name: "NoSQL And Distributed Data",
      sourceTopics: ["nosql"],
    },
    {
      track: "databases",
      topic: "vector-retrieval-and-memory",
      name: "Vector Retrieval And Memory",
      sourceTopics: ["vector-db"],
    },
  ],
  "software-engineering": [
    {
      track: "software-engineering",
      topic: "workflow-and-ai-tooling",
      name: "Workflow And AI Tooling",
      sourceTopics: ["tooling"],
    },
    {
      track: "software-engineering",
      topic: "contracts-and-apis",
      name: "Contracts And APIs",
      sourceTopics: ["apis"],
    },
    {
      track: "software-engineering",
      topic: "testing-and-verification",
      name: "Testing And Verification",
      sourceTopics: ["testing"],
    },
    {
      track: "software-engineering",
      topic: "security-and-trust",
      name: "Security And Trust",
      sourceTopics: ["security-basics"],
    },
    {
      track: "software-engineering",
      topic: "concurrency-and-state",
      name: "Concurrency And State",
      sourceTopics: ["concurrency"],
    },
    {
      track: "software-engineering",
      topic: "observability-and-operations",
      name: "Observability And Operations",
      sourceTopics: ["observability"],
    },
    {
      track: "software-engineering",
      topic: "reliability-and-delivery",
      name: "Reliability And Delivery",
      sourceTopics: ["reliability", "platform-and-delivery"],
    },
    {
      track: "software-engineering",
      topic: "performance-and-cost",
      name: "Performance And Cost",
      sourceTopics: ["performance"],
    },
    {
      track: "software-engineering",
      topic: "system-design-and-patterns",
      name: "System Design And Patterns",
      sourceTopics: ["system-design", "design-patterns"],
    },
    {
      track: "software-engineering",
      topic: "implementation-and-practice",
      name: "Implementation And Practice",
      sourceTopics: [
        "python",
        "rust",
        "typescript",
        "learning-paths",
        "assessments",
        "capstones",
      ],
    },
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

function topicFromGroup(content: ContentIndex, group: HandbookTopicGroup): Topic {
  const sourceTopicSet = new Set(group.sourceTopics);
  const docCount = content.docs.filter(
    (doc) => doc.track === group.track && sourceTopicSet.has(doc.topic)
  ).length;
  const moduleCount = content.modules.filter(
    (module) => module.track === group.track && sourceTopicSet.has(module.topic)
  ).length;

  return {
    track: group.track,
    topic: group.topic,
    name: group.name,
    path: `/track/${group.track}/${group.topic}`,
    hasDoc: docCount > 0,
    docCount,
    moduleCount,
  };
}

export function hasHandbookGroups(trackId: string) {
  return (HANDBOOK_TOPIC_GROUPS[trackId] ?? []).length > 0;
}

export function getHandbookTopics(content: ContentIndex, trackId?: string): Topic[] {
  const groupedTrackIds = new Set(Object.keys(HANDBOOK_TOPIC_GROUPS));
  const groupedTopics = Object.entries(HANDBOOK_TOPIC_GROUPS)
    .filter(([groupTrackId]) => !trackId || groupTrackId === trackId)
    .flatMap(([, groups]) => groups.map((group) => topicFromGroup(content, group)));

  const ungroupedTopics = content.topics.filter(
    (topic) =>
      !groupedTrackIds.has(topic.track) &&
      (!trackId || topic.track === trackId)
  );

  return sortTopics([...ungroupedTopics, ...groupedTopics]);
}

export function resolveHandbookTopic(
  content: ContentIndex,
  trackId: string,
  topicId: string
): { topic: Topic; sourceTopics: string[]; isGrouped: boolean } | undefined {
  const group = HANDBOOK_TOPIC_GROUPS[trackId]?.find(
    (candidate) => candidate.topic === topicId
  );
  if (group) {
    return {
      topic: topicFromGroup(content, group),
      sourceTopics: group.sourceTopics,
      isGrouped: true,
    };
  }

  const topic = content.topics.find(
    (candidate) => candidate.track === trackId && candidate.topic === topicId
  );
  if (!topic) return undefined;
  return { topic, sourceTopics: [topic.topic], isGrouped: false };
}

export function getCanonicalTopicId(trackId: string, sourceTopic: string) {
  const group = HANDBOOK_TOPIC_GROUPS[trackId]?.find((candidate) =>
    candidate.sourceTopics.includes(sourceTopic)
  );
  return group?.topic ?? sourceTopic;
}

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
