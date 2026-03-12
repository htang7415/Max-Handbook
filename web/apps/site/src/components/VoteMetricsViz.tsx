"use client";

import { useMemo, useState } from "react";

function normalizeAnswer(text: string) {
  return text
    .toLowerCase()
    .replace(/[!"#$%&'()*+,./:;<=>?@[\\\]^_`{|}~-]/g, "")
    .replace(/\b(a|an|the)\b/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

const SCENARIOS = {
  stable: [
    "Paris",
    "paris.",
    "The Paris",
    "Paris",
    "Paris",
    "paris",
  ],
  twoCamps: [
    "42",
    "42.",
    "forty two",
    "43",
    "43",
    "forty-three",
  ],
  fragmented: [
    "cache hit",
    "prefix reuse",
    "cache-hit",
    "reuse cache",
    "cache miss",
    "prefix cache",
  ],
} as const;

function countsFor(answers: string[], normalized: boolean) {
  const counts = new Map<string, number>();
  for (const answer of answers) {
    const key = normalized ? normalizeAnswer(answer) : answer;
    counts.set(key, (counts.get(key) ?? 0) + 1);
  }
  return [...counts.entries()].sort((left, right) => right[1] - left[1]);
}

function entropy(entries: Array<[string, number]>, total: number) {
  return -entries.reduce((sum, [, count]) => {
    const p = count / total;
    return p === 0 ? sum : sum + p * Math.log(p);
  }, 0);
}

export default function VoteMetricsViz() {
  const [scenario, setScenario] = useState<keyof typeof SCENARIOS>("stable");
  const [normalized, setNormalized] = useState(true);

  const summary = useMemo(() => {
    const answers = [...SCENARIOS[scenario]];
    const counts = countsFor(answers, normalized);
    const total = answers.length;
    const topShare = counts[0] ? counts[0][1] / total : 0;
    const runnerUp = counts[1] ? counts[1][1] / total : 0;
    const uniqueRate = counts.length / total;
    const disagreeRate = 1 - topShare;
    const voteEntropy = entropy(counts, total);
    const minority = counts.slice(1);
    const minorityTotal = minority.reduce((sum, [, count]) => sum + count, 0);
    const minorityEntropy =
      minorityTotal === 0 ? 0 : entropy(minority, minorityTotal);
    return {
      answers,
      counts,
      topShare,
      margin: topShare - runnerUp,
      uniqueRate,
      disagreeRate,
      voteEntropy,
      minorityEntropy,
    };
  }, [normalized, scenario]);

  const topCount = summary.counts[0]?.[1] ?? 1;

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Vote Metrics</div>
        <p className="observable-viz-subtitle">
          Repeated sampled answers can look stable, split into two camps, or fragment
          into many alternatives. Normalization changes the agreement picture.
        </p>
      </div>

      <div className="observable-controls">
        <label className="observable-control">
          <span className="observable-control-label">Scenario</span>
          <select
            className="observable-control-select"
            value={scenario}
            onChange={(event) => setScenario(event.target.value as keyof typeof SCENARIOS)}
          >
            <option value="stable">Stable</option>
            <option value="twoCamps">Two camps</option>
            <option value="fragmented">Fragmented</option>
          </select>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Normalize</span>
          <select
            className="observable-control-select"
            value={normalized ? "yes" : "no"}
            onChange={(event) => setNormalized(event.target.value === "yes")}
          >
            <option value="yes">Yes</option>
            <option value="no">No</option>
          </select>
        </label>
      </div>

      <div className="vote-viz-layout">
        <div className="vote-viz-card">
          <div className="vote-viz-title">Samples</div>
          <div className="vote-viz-samples">
            {summary.answers.map((answer, index) => (
              <span key={`${answer}-${index}`} className="vote-viz-sample">
                {answer}
              </span>
            ))}
          </div>
        </div>

        <div className="vote-viz-card">
          <div className="vote-viz-title">Grouped vote counts</div>
          <div className="vote-viz-bars">
            {summary.counts.map(([answer, count]) => (
              <div key={answer} className="vote-viz-bar-row">
                <span>{answer || "(empty)"}</span>
                <div className="vote-viz-bar">
                  <span style={{ width: `${(count / topCount) * 100}%` }} />
                </div>
                <strong>{count}</strong>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="observable-stats">
        <div className="observable-stat-row">
          <span>Top vote share</span>
          <span className="observable-stat-value">{summary.topShare.toFixed(2)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Margin</span>
          <span className="observable-stat-value">{summary.margin.toFixed(2)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Entropy</span>
          <span className="observable-stat-value">{summary.voteEntropy.toFixed(2)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Uniqueness</span>
          <span className="observable-stat-value">{summary.uniqueRate.toFixed(2)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Disagreement</span>
          <span className="observable-stat-value">{summary.disagreeRate.toFixed(2)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Minority entropy</span>
          <span className="observable-stat-value">{summary.minorityEntropy.toFixed(2)}</span>
        </div>
      </div>
    </div>
  );
}
