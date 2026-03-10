import Link from "next/link";
import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";
import { sortTopicsForTrack } from "@/lib/roadmap";
import { notFound } from "next/navigation";

const ML_STUDY_PATHS: Record<string, { label: string; note: string }> = {
  "path-beginner": {
    label: "Beginner Path",
    note: "Practical foundation across data, models, evaluation, and deep learning.",
  },
  "path-interview": {
    label: "Interview Path",
    note: "Fast recall on core ML trade-offs, metrics, and modern model intuition.",
  },
  "path-llm-systems": {
    label: "LLM Systems Path",
    note: "Inference, retrieval, serving, and evaluation for modern LLM applications.",
  },
  "path-math-first": {
    label: "Math-First Path",
    note: "Equations, likelihood, and optimization before broader model coverage.",
  },
};

function TopicLink({
  href,
  accentVar,
  name,
  meta,
  note,
}: {
  href: string;
  accentVar: string;
  name: string;
  meta?: string;
  note?: string;
}) {
  return (
    <Link href={href} className="topic-list-item" data-parallax="4">
      <span className="topic-list-dot" style={{ background: `var(${accentVar})` }} />
      <span className="min-w-0 flex-1">
        <span className="topic-list-name">{name}</span>
        {note ? (
          <span className="mt-0.5 block text-[0.76rem] text-[var(--text-muted)]">{note}</span>
        ) : null}
      </span>
      {meta ? <span className="topic-list-meta">{meta}</span> : null}
    </Link>
  );
}

export function generateStaticParams() {
  const content = contentData as ContentIndex;
  return content.tracks.map((track) => ({ track: track.id }));
}

export default async function TrackPage({ params }: { params: Promise<{ track: string }> }) {
  const { track: trackId } = await params;
  const content = contentData as ContentIndex;
  const track = content.tracks.find((item) => item.id === trackId);
  if (!track) return notFound();

  const topics = sortTopicsForTrack(
    content.topics.filter((topic) => topic.track === track.id),
    track.id
  );
  const isMlTrack = track.id === "ml";
  const studyPaths = isMlTrack
    ? topics.filter((topic) => topic.topic in ML_STUDY_PATHS)
    : [];
  const roadmapTopic = isMlTrack ? topics.find((topic) => topic.topic === "roadmap") : undefined;
  const sectionTopics = isMlTrack
    ? topics.filter((topic) => !(topic.topic in ML_STUDY_PATHS) && topic.topic !== "roadmap")
    : topics;

  return (
    <div>
      <div className="flex items-center gap-2.5 mb-1">
        <span
          className="h-2.5 w-2.5 rounded-full"
          style={{ background: `var(${track.accentVar})` }}
        />
        <span className="text-[0.72rem] font-semibold uppercase tracking-widest text-[var(--text-muted)]">
          Track
        </span>
      </div>
      <h1 className="text-2xl font-semibold tracking-tight">{track.name}</h1>
      <p className="mt-1.5 text-[0.88rem] text-[var(--text-secondary)] max-w-lg">
        {track.description}
      </p>
      <p className="mt-2 text-[0.75rem] text-[var(--text-muted)]">
        {topics.length} topics
      </p>

      {isMlTrack ? (
        <div className="mt-6">
          <section>
            <h2 className="text-[0.72rem] font-semibold uppercase tracking-widest text-[var(--text-muted)]">
              Study Paths
            </h2>
            <div className="mt-2 space-y-0.5">
              {studyPaths.map((topic) => (
                <TopicLink
                  key={topic.topic}
                  href={`/track/${track.id}/${topic.topic}`}
                  accentVar={track.accentVar}
                  name={ML_STUDY_PATHS[topic.topic]?.label ?? topic.name}
                  note={ML_STUDY_PATHS[topic.topic]?.note}
                />
              ))}
            </div>
          </section>

          <section className="mt-7">
            <h2 className="text-[0.72rem] font-semibold uppercase tracking-widest text-[var(--text-muted)]">
              Sections
            </h2>
            <div className="mt-2 space-y-0.5">
              {sectionTopics.map((topic) => {
                const entryCount = topic.docCount + topic.moduleCount;
                return (
                  <TopicLink
                    key={topic.topic}
                    href={`/track/${track.id}/${topic.topic}`}
                    accentVar={track.accentVar}
                    name={topic.name}
                    meta={
                      entryCount > 0
                        ? `${entryCount} ${entryCount === 1 ? "entry" : "entries"}`
                        : undefined
                    }
                  />
                );
              })}
            </div>
          </section>

          {roadmapTopic ? (
            <section className="mt-7">
              <h2 className="text-[0.72rem] font-semibold uppercase tracking-widest text-[var(--text-muted)]">
                Utility
              </h2>
              <div className="mt-2 space-y-0.5">
                <TopicLink
                  href={`/track/${track.id}/${roadmapTopic.topic}`}
                  accentVar={track.accentVar}
                  name="Roadmap"
                  note="Coverage, pruning, and canonical-vs-legacy audit."
                />
              </div>
            </section>
          ) : null}
        </div>
      ) : (
        <div className="mt-6 space-y-0.5">
          {topics.map((topic) => {
            const entryCount = topic.docCount + topic.moduleCount;
            return (
              <TopicLink
                key={topic.topic}
                href={`/track/${track.id}/${topic.topic}`}
                accentVar={track.accentVar}
                name={topic.name}
                meta={
                  entryCount > 0
                    ? `${entryCount} ${entryCount === 1 ? "entry" : "entries"}`
                    : undefined
                }
              />
            );
          })}
        </div>
      )}
    </div>
  );
}
