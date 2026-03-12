import Link from "next/link";
import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";
import { sortTopicsForTrack } from "@/lib/roadmap";
import { countTopicVisuals, countVisualsForTrack } from "@/lib/visual-metadata";
import { notFound } from "next/navigation";

const ML_STUDY_PATHS: Record<string, { label: string; note: string }> = {
  "path-interview": {
    label: "Interview Path",
    note: "Fast recall on core ML trade-offs, metrics, and modern model intuition.",
  },
};

function TopicLink({
  href,
  accentVar,
  name,
  meta,
  note,
  badge,
}: {
  href: string;
  accentVar: string;
  name: string;
  meta?: string;
  note?: string;
  badge?: string;
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
      <span className="topic-list-tail">
        {badge ? <span className="topic-list-badge">{badge}</span> : null}
        {meta ? <span className="topic-list-meta">{meta}</span> : null}
      </span>
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
  const trackVisualCount = countVisualsForTrack(track.id);
  const studyPaths = isMlTrack
    ? topics.filter((topic) => topic.topic in ML_STUDY_PATHS)
    : [];
  const sectionTopics = isMlTrack
    ? topics.filter((topic) => !(topic.topic in ML_STUDY_PATHS))
    : topics;

  return (
    <div>
      <div className="flex items-center gap-2.5 mb-1">
        <span
          className="h-2.5 w-2.5 rounded-full"
          style={{ background: `var(${track.accentVar})` }}
        />
        <span className="text-[0.72rem] font-semibold tracking-widest text-[var(--text-muted)]">
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
      {trackVisualCount > 0 ? (
        <p className="mt-1 text-[0.78rem] text-[var(--text-secondary)]">
          <Link href={`/visuals?track=${track.id}`} className="topic-visuals-link">
            Browse {trackVisualCount} visual{trackVisualCount === 1 ? "" : "s"} for this track
          </Link>
        </p>
      ) : null}

      {isMlTrack ? (
        <div className="mt-6">
          <section>
            <h2 className="text-[0.72rem] font-semibold tracking-widest text-[var(--text-muted)]">
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
                  badge={
                    countTopicVisuals(track.id, topic.topic) > 0
                      ? `${countTopicVisuals(track.id, topic.topic)} visual`
                      : undefined
                  }
                />
              ))}
            </div>
          </section>

          <section className="mt-7">
            <h2 className="text-[0.72rem] font-semibold tracking-widest text-[var(--text-muted)]">
              Sections
            </h2>
            <div className="mt-2 space-y-0.5">
              {sectionTopics.map((topic) => {
                const entryCount = topic.docCount + topic.moduleCount;
                const visualCount = countTopicVisuals(track.id, topic.topic);
                return (
                  <TopicLink
                    key={topic.topic}
                    href={`/track/${track.id}/${topic.topic}`}
                    accentVar={track.accentVar}
                    name={topic.name}
                    badge={
                      visualCount > 0
                        ? `${visualCount} visual${visualCount === 1 ? "" : "s"}`
                        : undefined
                    }
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

        </div>
      ) : (
        <div className="mt-6 space-y-0.5">
          {topics.map((topic) => {
            const entryCount = topic.docCount + topic.moduleCount;
            const visualCount = countTopicVisuals(track.id, topic.topic);
            return (
              <TopicLink
                key={topic.topic}
                href={`/track/${track.id}/${topic.topic}`}
                accentVar={track.accentVar}
                name={topic.name}
                badge={
                  visualCount > 0
                    ? `${visualCount} visual${visualCount === 1 ? "" : "s"}`
                    : undefined
                }
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
