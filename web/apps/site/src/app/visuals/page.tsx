import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";
import Link from "next/link";
import type { CSSProperties } from "react";
import { VISUAL_COMPONENTS } from "@/lib/visual-registry";
import { countVisualsForTrack, VISUALS } from "@/lib/visual-metadata";

export default async function VisualsPage({
  searchParams,
}: {
  searchParams?: Promise<{ track?: string }>;
}) {
  const resolvedSearchParams = searchParams ? await searchParams : {};
  const content = contentData as ContentIndex;
  const trackMap = new Map(content.tracks.map((track) => [track.id, track]));
  const trackFilters = content.tracks.filter((track) => countVisualsForTrack(track.id) > 0);
  const selectedTrack = trackFilters.some((track) => track.id === resolvedSearchParams.track)
    ? resolvedSearchParams.track ?? "all"
    : "all";
  const visuals =
    selectedTrack === "all"
      ? VISUALS
      : VISUALS.filter((visual) => visual.track === selectedTrack);

  return (
    <div className="visuals-page">
      <section className="visuals-hero">
        <div>
          <div className="visuals-eyebrow">Visual notebooks</div>
          <h1>Interactive demos for learning & sharing.</h1>
          <p>
            These labs are designed to make core ideas tangible. Filter by track,
            jump back to the teaching page, and connect the math to the code.
          </p>
        </div>
        <div className="visuals-hero-cta">
          <Link href="/search" className="home-cta-secondary">
            Explore the library
          </Link>
          <Link
            href="/track/ml/fundamentals"
            className="home-cta-primary"
          >
            Start with fundamentals
          </Link>
        </div>
      </section>

      <section className="visuals-filters">
        <Link
          href="/visuals"
          className={`visuals-filter ${selectedTrack === "all" ? "visuals-filter-active" : ""}`}
        >
          All
          <span>{VISUALS.length}</span>
        </Link>
        {trackFilters.map((track) => (
          <Link
            key={track.id}
            href={`/visuals?track=${track.id}`}
            className={`visuals-filter ${selectedTrack === track.id ? "visuals-filter-active" : ""}`}
            style={{ "--filter-accent": `var(${track.accentVar})` } as CSSProperties}
          >
            {track.name}
            <span>{countVisualsForTrack(track.id)}</span>
          </Link>
        ))}
      </section>

      <section className="visuals-grid">
        {visuals.map((visual) => {
          const Viz = VISUAL_COMPONENTS[visual.id];
          const track = trackMap.get(visual.track);
          return (
            <article
              key={visual.id}
              className="visuals-card"
              data-parallax={String(visual.parallax)}
            >
              <div className="visuals-card-shell">
                <div className="visuals-card-copy">
                  <div className="visuals-card-track">
                    {track?.name ?? visual.track}
                  </div>
                  <Link href={visual.href} className="visuals-card-title">
                    {visual.title}
                  </Link>
                  <p className="visuals-card-summary">{visual.summary}</p>
                  <Link href={visual.href} className="visuals-card-link">
                    Open topic
                  </Link>
                </div>
                <Viz />
              </div>
            </article>
          );
        })}
      </section>

      <section className="visuals-footer">
        <div>
          <h2>Shareable by default</h2>
          <p>
            Every demo is paired with concise theory and code. Copy it, remix it,
            and build your own visual explanations.
          </p>
        </div>
        <Link href="/search" className="home-section-link">
          Browse all content
        </Link>
      </section>
    </div>
  );
}
