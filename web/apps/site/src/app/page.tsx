import type { CSSProperties } from "react";
import Link from "next/link";
import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";
import { sortTracks } from "@/lib/roadmap";
import HomeSoftmaxViz from "@/components/HomeSoftmaxViz";
import HomeSignalViz from "@/components/HomeSignalViz";
import { countVisualsForTrack, VISUALS } from "@/lib/visual-metadata";

export default function Home() {
  const content = contentData as ContentIndex;
  const tracks = sortTracks(content.tracks);
  const topics = content.topics;
  const { modules } = content;
  const docs = content.docs ?? [];
  const primaryTrack = tracks[0];
  const stats = [
    { label: "Topics", value: topics.length },
    { label: "Labs", value: modules.length },
    { label: "Notes", value: docs.length },
  ];
  const updatedAt = content.generated_at
    ? new Date(content.generated_at)
    : null;
  const updatedAtLabel = updatedAt
    ? updatedAt.toLocaleDateString("en-US", {
        month: "short",
        day: "2-digit",
        year: "numeric",
        timeZone: "UTC",
      })
    : "recently";
  const totalModules = tracks.reduce((sum, track) => sum + track.moduleCount, 0);
  const trackLabelMap: Record<string, string> = {
    dsa: "DSA",
    ml: "ML",
    "ai-agents": "AI",
    databases: "DB",
    "software-engineering": "SE",
  };
  const trackSpectrum = tracks.map((track) => {
    const words = track.name
      .replace(/&/g, " ")
      .split(" ")
      .filter(Boolean);
    const shortLabel =
      trackLabelMap[track.id] ??
      (words.length === 1
        ? words[0].slice(0, 2).toUpperCase()
        : words.map((word) => word[0]).join("").toUpperCase().slice(0, 4));
    const share = totalModules > 0 ? track.moduleCount / totalModules : 0;
    return {
      id: track.id,
      label: shortLabel,
      name: track.name,
      moduleCount: track.moduleCount,
      accentVar: track.accentVar,
      share,
    };
  });
  const trackSpotlights = tracks.map((track) => {
    const trackTopics = topics.filter((topic) => topic.track === track.id);
    const trackNotes = trackTopics.reduce(
      (sum, topic) => sum + (topic.docCount ?? 0),
      0
    );
    const visualCount = countVisualsForTrack(track.id);

    return { track, trackNotes, visualCount };
  });
  const featuredVisuals = VISUALS.slice(0, 4);

  return (
    <div className="home-page">
      <section className="home-hero">
        <div className="home-hero-text">
          <div className="home-eyebrow">Open knowledge • Visual labs • Shareable code</div>
          <h1 className="home-title">
            Dense, visual knowledge you can run.
          </h1>
          <p className="home-lede">
            Notes, equations, and runnable labs—organized for fast learning.
          </p>
          <div className="home-cta">
            {primaryTrack ? (
              <Link
                href={`/track/${primaryTrack.id}`}
                className="home-cta-primary"
              >
                Start with {primaryTrack.name}
              </Link>
            ) : null}
            <Link href="/search" className="home-cta-secondary">
              Explore
            </Link>
            <Link href="/visuals" className="home-cta-tertiary">
              Visuals
            </Link>
          </div>
        </div>
        <div className="home-hero-viz">
          <div className="home-dashboard" data-parallax="10">
            <div className="home-dashboard-header">
              <div>
                <h3>Index</h3>
              </div>
              <div className="home-dashboard-updated">
                <span className="home-dashboard-dot" />
                <span>{updatedAtLabel}</span>
              </div>
            </div>
            <div className="home-dashboard-metrics">
              {stats.map((stat) => (
                <div key={stat.label}>
                  <span>{stat.label}</span>
                  <strong>{stat.value}</strong>
                </div>
              ))}
            </div>
            <div className="home-dashboard-spectrum">
              {trackSpectrum.map((track) => (
                <div
                  key={track.id}
                  className="home-dashboard-track"
                  style={
                    {
                      "--track-accent": `var(${track.accentVar})`,
                      "--track-share": `${Math.max(track.share * 100, 12).toFixed(2)}%`,
                    } as CSSProperties
                  }
                  title={`${track.name} · ${track.moduleCount} labs`}
                >
                  <div className="home-dashboard-track-header">
                    <span>{track.label}</span>
                    <strong>{track.moduleCount}</strong>
                  </div>
                  <div className="home-dashboard-track-bar">
                    <span />
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className="home-knowledge">
        <div className="home-section-header">
          <div>
            <h2>Atlas</h2>
          </div>
          <Link href="/search" className="home-section-link">
            All
          </Link>
        </div>
        <div className="home-track-cards">
          {trackSpotlights.map(({ track, trackNotes, visualCount }) => (
            <article
              key={track.id}
              className="home-track-card"
              style={
                {
                  "--track-accent": `var(${track.accentVar})`,
                } as CSSProperties
              }
              data-parallax="8"
            >
              <div className="home-track-card-header">
                <span className="home-track-card-dot" />
                <Link href={`/track/${track.id}`} className="home-track-card-title">
                  {track.name}
                </Link>
                <span className="home-track-card-badge">
                  {track.moduleCount} labs
                </span>
              </div>
              <div className="home-track-card-meta">
                <span>
                  <strong>{track.topicCount}</strong>
                  Topics
                </span>
                <span>
                  <strong>{trackNotes}</strong>
                  Notes
                </span>
                <span>
                  <strong>{track.moduleCount}</strong>
                  Labs
                </span>
                {visualCount > 0 ? (
                  <span>
                    <strong>{visualCount}</strong>
                    Visuals
                  </span>
                ) : null}
              </div>
              {visualCount > 0 ? (
                <div className="home-track-card-links">
                  <Link href={`/visuals?track=${track.id}`} className="home-track-card-link">
                    Browse visuals
                  </Link>
                </div>
              ) : null}
            </article>
          ))}
        </div>
      </section>

      <section className="home-insight-strip">
        <div className="home-insight-card" data-parallax="6">
          <span>Notes</span>
          <strong>Eqns + theory</strong>
        </div>
        <div className="home-insight-card" data-parallax="6">
          <span>Labs</span>
          <strong>Run + tweak</strong>
        </div>
        <div className="home-insight-card" data-parallax="6">
          <span>Tests</span>
          <strong>Quick checks</strong>
        </div>
      </section>

      <section className="home-lab-grid">
        <div className="home-lab-intro">
          <h2>Labs</h2>
          <p>
            Quick previews: attention, token probabilities, encodings. The site now has
            {" "}
            {VISUALS.length}
            {" "}
            interactive visuals.
          </p>
          <div className="home-lab-links">
            {featuredVisuals.map((visual) => (
              <Link key={visual.id} href={visual.href} className="home-lab-link">
                {visual.title}
              </Link>
            ))}
            <Link href="/visuals" className="home-lab-link home-lab-link-all">
              All visuals
            </Link>
          </div>
        </div>
        <div className="home-lab-cards">
          <HomeSoftmaxViz />
          <HomeSignalViz />
        </div>
      </section>
    </div>
  );
}
