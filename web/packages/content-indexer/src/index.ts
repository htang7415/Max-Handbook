// Content indexer — builds a unified content index for the website.

import {
  readFileSync,
  writeFileSync,
  mkdirSync,
  statSync,
} from "fs";
import { glob } from "glob";
import { resolve, dirname, relative, basename, extname } from "path";
import { fileURLToPath } from "url";

interface ModuleSource {
  path: string;
  language: string;
  content: string;
}

interface ModuleIndexEntry {
  track: string;
  topic: string;
  slug: string;
  title: string;
  path: string;
  summary?: string;
  readme: string;
  sources: ModuleSource[];
}

interface ModuleAliasEntry {
  track: string;
  topic: string;
  slug: string;
  title: string;
  path: string;
  aliasOf: string;
}

interface DocIndexEntry {
  track: string;
  topic: string;
  slug: string;
  title: string;
  path: string;
  summary?: string;
  content: string;
}

interface SearchEntry {
  id: string;
  type: "module" | "doc";
  title: string;
  summary?: string;
  track: string;
  topic: string;
  slug: string;
  href: string;
  trackName: string;
  topicName: string;
}

interface TopicIndexEntry {
  track: string;
  topic: string;
  name: string;
  path: string;
  hasDoc: boolean;
  docCount: number;
  moduleCount: number;
}

interface TrackIndexEntry {
  id: string;
  name: string;
  description: string;
  accent: string;
  accentVar: string;
  topicCount: number;
  moduleCount: number;
}

interface ContentIndex {
  generated_at: string;
  tracks: TrackIndexEntry[];
  topics: TopicIndexEntry[];
  modules: ModuleIndexEntry[];
  moduleAliases: ModuleAliasEntry[];
  docs: DocIndexEntry[];
}

interface SearchIndex {
  generated_at: string;
  entries: SearchEntry[];
}

const TRACKS: Array<Omit<TrackIndexEntry, "topicCount" | "moduleCount">> = [
  {
    id: "dsa",
    name: "Data Structures & Algorithms",
    description: "Core patterns, data structures, and algorithmic analysis.",
    accent: "#1f77b4",
    accentVar: "--track-dsa",
  },
  {
    id: "ml",
    name: "Machine Learning",
    description: "Math foundations, models, optimization, and systems.",
    accent: "#ff7f0e",
    accentVar: "--track-ml",
  },
  {
    id: "ai-agents",
    name: "AI Agents",
    description: "Prompting, tool use, memory, and evaluation.",
    accent: "#2ca02c",
    accentVar: "--track-ai-agents",
  },
  {
    id: "databases",
    name: "Databases",
    description: "Schema design, indexing, transactions, and query plans.",
    accent: "#17becf",
    accentVar: "--track-databases",
  },
  {
    id: "software-engineering",
    name: "Software Engineering",
    description: "APIs, performance, testing, and system design.",
    accent: "#d62728",
    accentVar: "--track-se",
  },
];

const TOPIC_NAMES: Record<string, string> = {
  dp: "Dynamic Programming",
  llm: "LLM",
  mlops: "MLOps",
  gnn: "Graph Neural Networks",
  cnn: "Convolutional Neural Networks",
  rnn: "Recurrent Neural Networks",
  mlp: "Multi-Layer Perceptrons",
  vae: "Variational Autoencoders",
  ai: "AI",
  api: "API",
  apis: "APIs",
  sql: "SQL",
  gpu: "GPU",
  cv: "Cross Validation",
  rl: "Reinforcement Learning",
  "rl-for-llm": "RL for LLM",
};

const MAX_SUMMARY_LENGTH = 180;
const TRACK_ORDER = new Map(TRACKS.map((track, index) => [track.id, index]));

function isDirectory(path: string) {
  try {
    return statSync(path).isDirectory();
  } catch {
    return false;
  }
}

function kebabToTitle(value: string) {
  const lower = value.toLowerCase();
  if (TOPIC_NAMES[lower]) return TOPIC_NAMES[lower];
  return value
    .split("-")
    .map((part) => {
      const key = part.toLowerCase();
      if (TOPIC_NAMES[key]) return TOPIC_NAMES[key];
      return part.charAt(0).toUpperCase() + part.slice(1);
    })
    .join(" ");
}

function extractTitle(markdown: string, fallback: string) {
  const match = markdown.match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : fallback;
}

function extractSummary(markdown: string) {
  const lines = markdown.split(/\r?\n/);
  let inCode = false;
  const paragraph: string[] = [];

  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed.startsWith("```")) {
      inCode = !inCode;
      continue;
    }
    if (inCode) continue;
    if (!trimmed) {
      if (paragraph.length > 0) break;
      continue;
    }
    if (trimmed.startsWith("#")) continue;
    paragraph.push(trimmed);
  }

  if (paragraph.length === 0) return undefined;
  const summary = paragraph.join(" ").replace(/\s+/g, " ").trim();
  if (summary.length <= MAX_SUMMARY_LENGTH) return summary;
  return `${summary.slice(0, MAX_SUMMARY_LENGTH).trim()}…`;
}

function loadMarkdown(filePath: string) {
  return readFileSync(filePath, "utf-8");
}

function parseFrontmatter(markdown: string): {
  body: string;
  data: Record<string, string | boolean>;
} {
  const normalized = markdown.replace(/\r\n/g, "\n");
  if (!normalized.startsWith("---\n")) {
    return { body: markdown, data: {} };
  }

  const end = normalized.indexOf("\n---\n", 4);
  if (end === -1) {
    return { body: markdown, data: {} };
  }

  const rawFrontmatter = normalized.slice(4, end);
  const body = normalized.slice(end + 5);
  const data: Record<string, string | boolean> = {};

  for (const line of rawFrontmatter.split("\n")) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#")) continue;
    const colon = trimmed.indexOf(":");
    if (colon === -1) continue;
    const key = trimmed.slice(0, colon).trim();
    const rawValue = trimmed.slice(colon + 1).trim();
    if (!key || !rawValue) continue;

    if (rawValue === "true") {
      data[key] = true;
    } else if (rawValue === "false") {
      data[key] = false;
    } else {
      data[key] = rawValue.replace(/^["']|["']$/g, "");
    }
  }

  return { body, data };
}

function languageFromPath(filePath: string) {
  const extension = extname(filePath);
  if (extension === ".py") return "python";
  if (extension === ".rs") return "rust";
  if (extension === ".ts" || extension === ".tsx") return "typescript";
  return extension.replace(".", "") || "text";
}

function compareTrackOrder(a: string, b: string) {
  const aIndex = TRACK_ORDER.get(a) ?? Number.MAX_SAFE_INTEGER;
  const bIndex = TRACK_ORDER.get(b) ?? Number.MAX_SAFE_INTEGER;
  if (aIndex !== bIndex) return aIndex - bIndex;
  return a.localeCompare(b);
}

function compareTopicEntries(a: TopicIndexEntry, b: TopicIndexEntry) {
  const trackCompare = compareTrackOrder(a.track, b.track);
  if (trackCompare !== 0) return trackCompare;
  return a.topic.localeCompare(b.topic);
}

function compareSearchEntries(a: SearchEntry, b: SearchEntry) {
  const titleCompare = a.title.localeCompare(b.title);
  if (titleCompare !== 0) return titleCompare;

  const typeCompare = a.type.localeCompare(b.type);
  if (typeCompare !== 0) return typeCompare;

  const trackCompare = compareTrackOrder(a.track, b.track);
  if (trackCompare !== 0) return trackCompare;

  const topicCompare = a.topic.localeCompare(b.topic);
  if (topicCompare !== 0) return topicCompare;

  const slugCompare = a.slug.localeCompare(b.slug);
  if (slugCompare !== 0) return slugCompare;

  return a.id.localeCompare(b.id);
}

function readExistingIndex(filePath: string) {
  try {
    return JSON.parse(readFileSync(filePath, "utf-8")) as Record<string, unknown>;
  } catch {
    return undefined;
  }
}

function stripGeneratedAt(index: Record<string, unknown>) {
  return {
    ...index,
    generated_at: "",
  };
}

function sameIndexContent(
  existing: Record<string, unknown> | undefined,
  candidate: Record<string, unknown>
) {
  if (!existing) return false;
  return JSON.stringify(stripGeneratedAt(existing)) === JSON.stringify(candidate);
}

function resolveGeneratedAt(
  contentPath: string,
  searchPath: string,
  contentCandidate: ContentIndex,
  searchCandidate: SearchIndex
) {
  const existingContent = readExistingIndex(contentPath);
  const existingSearch = readExistingIndex(searchPath);
  const existingGeneratedAt =
    typeof existingContent?.generated_at === "string"
      ? existingContent.generated_at
      : undefined;

  if (
    existingGeneratedAt &&
    sameIndexContent(existingContent, contentCandidate as unknown as Record<string, unknown>) &&
    sameIndexContent(existingSearch, searchCandidate as unknown as Record<string, unknown>)
  ) {
    return existingGeneratedAt;
  }

  return new Date().toISOString();
}

async function main() {
  const __filename = fileURLToPath(import.meta.url);
  const __dirname = dirname(__filename);
  const repoRoot = resolve(__dirname, "../../../../");

  const modulesPattern = "modules/**/README.md";
  const docsPattern = "docs/**/*.md";
  const topicsPattern = "docs/*/*";

  const moduleFiles = await glob(modulesPattern, {
    cwd: repoRoot,
    absolute: true,
    nodir: true,
  });
  const docFiles = await glob(docsPattern, {
    cwd: repoRoot,
    absolute: true,
    nodir: true,
  });
  const topicDirs = (await glob(topicsPattern, {
    cwd: repoRoot,
    absolute: true,
  })).filter(isDirectory);

  const modules: ModuleIndexEntry[] = [];
  const moduleAliases: ModuleAliasEntry[] = [];
  const docs: DocIndexEntry[] = [];

  for (const filePath of moduleFiles.sort()) {
    try {
      const relPath = relative(repoRoot, filePath);
      const parts = relPath.split("/");
      if (parts.length < 5) continue;
      const track = parts[1];
      const topic = parts[2];
      const slug = parts[3];
      const moduleDir = dirname(filePath);
      const rawReadme = loadMarkdown(filePath);
      const { body: readme, data } = parseFrontmatter(rawReadme);
      const title = extractTitle(readme, kebabToTitle(slug));
      const summary = extractSummary(readme);
      const aliasOfValue = data.aliasOf ?? data.alias_of;
      const aliasOf =
        typeof aliasOfValue === "string" && aliasOfValue.trim().length > 0
          ? aliasOfValue.trim()
          : undefined;

      if (aliasOf) {
        moduleAliases.push({
          track,
          topic,
          slug,
          title,
          path: relative(repoRoot, moduleDir),
          aliasOf,
        });
        continue;
      }

      const sources: ModuleSource[] = [];
      const pythonSources = await glob("python/**/*.py", {
        cwd: moduleDir,
        absolute: true,
        nodir: true,
      });
      for (const sourcePath of pythonSources.sort()) {
        const fileName = basename(sourcePath);
        if (fileName.startsWith("test_")) continue;
        if (sourcePath.includes("__pycache__")) continue;
        sources.push({
          path: relative(repoRoot, sourcePath),
          language: languageFromPath(sourcePath),
          content: readFileSync(sourcePath, "utf-8"),
        });
      }

      const typescriptSources = await glob("typescript/**/*.{ts,tsx}", {
        cwd: moduleDir,
        absolute: true,
        nodir: true,
      });
      for (const sourcePath of typescriptSources.sort()) {
        const fileName = basename(sourcePath);
        if (fileName.startsWith("test_")) continue;
        if (sourcePath.endsWith(".d.ts")) continue;
        sources.push({
          path: relative(repoRoot, sourcePath),
          language: languageFromPath(sourcePath),
          content: readFileSync(sourcePath, "utf-8"),
        });
      }

      const rustSources = await glob("rust/src/**/*.rs", {
        cwd: moduleDir,
        absolute: true,
        nodir: true,
      });
      for (const sourcePath of rustSources.sort()) {
        sources.push({
          path: relative(repoRoot, sourcePath),
          language: languageFromPath(sourcePath),
          content: readFileSync(sourcePath, "utf-8"),
        });
      }

      modules.push({
        track,
        topic,
        slug,
        title,
        path: relative(repoRoot, moduleDir),
        summary,
        readme,
        sources,
      });
    } catch (err) {
      console.error(`Warning: could not parse ${filePath}:`, err);
    }
  }

  for (const filePath of docFiles.sort()) {
    try {
      const relPath = relative(repoRoot, filePath);
      const parts = relPath.split("/");
      if (parts.length < 3) continue;
      const track = parts[1];
      const topic = parts[2];
      let slug = basename(filePath, ".md");
      if (slug.toLowerCase() === "readme" && parts.length >= 4) {
        slug = parts[parts.length - 2];
      }
      const markdown = loadMarkdown(filePath);
      const title = extractTitle(markdown, kebabToTitle(slug));
      const summary = extractSummary(markdown);
      docs.push({
        track,
        topic,
        slug,
        title,
        path: relPath,
        summary,
        content: markdown,
      });
    } catch (err) {
      console.error(`Warning: could not parse ${filePath}:`, err);
    }
  }

  const docCountByTopic = new Map<string, number>();
  for (const doc of docs) {
    const key = `${doc.track}/${doc.topic}`;
    docCountByTopic.set(key, (docCountByTopic.get(key) ?? 0) + 1);
  }
  const moduleCountByTopic = new Map<string, number>();
  for (const module of modules) {
    const key = `${module.track}/${module.topic}`;
    moduleCountByTopic.set(key, (moduleCountByTopic.get(key) ?? 0) + 1);
  }

  const trackNameById = new Map(TRACKS.map((track) => [track.id, track.name]));
  const searchEntries: SearchEntry[] = [];
  for (const module of modules) {
    const trackName = trackNameById.get(module.track) ?? kebabToTitle(module.track);
    const topicName = kebabToTitle(module.topic);
    searchEntries.push({
      id: `module:${module.track}/${module.topic}/${module.slug}`,
      type: "module",
      title: module.title,
      summary: module.summary,
      track: module.track,
      topic: module.topic,
      slug: module.slug,
      href: `/track/${module.track}/${module.topic}#${module.slug}`,
      trackName,
      topicName,
    });
  }
  for (const doc of docs) {
    const trackName = trackNameById.get(doc.track) ?? kebabToTitle(doc.track);
    const topicName = kebabToTitle(doc.topic);
    searchEntries.push({
      id: `doc:${doc.track}/${doc.topic}/${doc.slug}`,
      type: "doc",
      title: doc.title,
      summary: doc.summary,
      track: doc.track,
      topic: doc.topic,
      slug: doc.slug,
      href: `/track/${doc.track}/${doc.topic}#${doc.slug}`,
      trackName,
      topicName,
    });
  }

  const topics: TopicIndexEntry[] = topicDirs
    .map((dirPath) => {
      const relPath = relative(repoRoot, dirPath);
      const parts = relPath.split("/");
      const track = parts[1];
      const topic = parts[2];
      const key = `${track}/${topic}`;
      const docCount = docCountByTopic.get(key) ?? 0;
      const moduleCount = moduleCountByTopic.get(key) ?? 0;
      return {
        track,
        topic,
        name: kebabToTitle(topic),
        path: `/track/${track}/${topic}`,
        hasDoc: docCount > 0,
        docCount,
        moduleCount,
      };
    })
    .filter((topic) => Boolean(topic.track) && Boolean(topic.topic))
    .sort(compareTopicEntries);

  const tracks: TrackIndexEntry[] = TRACKS.map((track) => {
    const topicCount = topics.filter((topic) => topic.track === track.id).length;
    const moduleCount = modules.filter((module) => module.track === track.id).length;
    return {
      ...track,
      topicCount,
      moduleCount,
    };
  });

  const outDir = resolve(repoRoot, "web/apps/site/src/content");
  mkdirSync(outDir, { recursive: true });
  const contentPath = resolve(outDir, "content_index.json");
  const searchPath = resolve(outDir, "search_index.json");

  const contentIndexCandidate: ContentIndex = {
    generated_at: "",
    tracks,
    topics,
    modules,
    moduleAliases,
    docs,
  };

  const searchIndexCandidate: SearchIndex = {
    generated_at: "",
    entries: searchEntries
      .slice()
      .sort(compareSearchEntries),
  };

  const generatedAt = resolveGeneratedAt(
    contentPath,
    searchPath,
    contentIndexCandidate,
    searchIndexCandidate
  );

  const contentIndex: ContentIndex = {
    ...contentIndexCandidate,
    generated_at: generatedAt,
  };
  writeFileSync(contentPath, JSON.stringify(contentIndex, null, 2) + "\n");

  const searchIndex: SearchIndex = {
    ...searchIndexCandidate,
    generated_at: generatedAt,
  };
  writeFileSync(searchPath, JSON.stringify(searchIndex, null, 2) + "\n");

  console.log(
    `Indexed ${modules.length} module(s), ${moduleAliases.length} alias(es), ${docs.length} doc(s)`
  );
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
