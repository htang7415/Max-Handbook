"use client";

import { useMemo, useState } from "react";

const TOKENS = ["the", "model", "answer", "maybe", "because", "<eos>"] as const;
const LOGITS = [2.8, 2.2, 1.6, 1.2, 0.7, 0.3] as const;
const PREFIXES = [
  { tokens: ["The"], score: -0.32, next: [-0.22, -0.51, -1.03, -1.28] },
  { tokens: ["A"], score: -0.41, next: [-0.36, -0.48, -0.82, -1.45] },
] as const;
const BEAM_TOKENS = ["model", "answer", "because", "<eos>"] as const;

function softmax(values: number[]) {
  const maxValue = Math.max(...values);
  const exps = values.map((value) => Math.exp(value - maxValue));
  const total = exps.reduce((sum, value) => sum + value, 0);
  return exps.map((value) => value / total);
}

function formatPercent(value: number) {
  return `${(value * 100).toFixed(1)}%`;
}

export default function DecodingMethodsViz() {
  const [temperature, setTemperature] = useState(0.9);
  const [topK, setTopK] = useState(3);
  const [topP, setTopP] = useState(0.85);
  const [mode, setMode] = useState<"greedy" | "top-k" | "top-p" | "beam">("top-p");
  const [beamWidth, setBeamWidth] = useState(2);

  const scaledLogits = useMemo(
    () => LOGITS.map((logit) => logit / temperature),
    [temperature]
  );
  const probabilities = useMemo(() => softmax([...scaledLogits]), [scaledLogits]);

  const ranked = useMemo(
    () =>
      probabilities
        .map((probability, index) => ({ index, token: TOKENS[index], probability }))
        .sort((left, right) => right.probability - left.probability),
    [probabilities]
  );

  const candidateSet = useMemo(() => {
    if (mode === "greedy") {
      return [ranked[0]?.index ?? 0];
    }
    if (mode === "top-k") {
      return ranked.slice(0, topK).map((item) => item.index);
    }
    if (mode === "top-p") {
      let cumulative = 0;
      const kept: number[] = [];
      for (const item of ranked) {
        kept.push(item.index);
        cumulative += item.probability;
        if (cumulative >= topP) break;
      }
      return kept;
    }
    return ranked.slice(0, topK).map((item) => item.index);
  }, [mode, ranked, topK, topP]);

  const beamRows = useMemo(() => {
    const rows = PREFIXES.flatMap((beam, beamIndex) =>
      beam.next.map((tokenScore, tokenIndex) => ({
        id: `${beamIndex}-${tokenIndex}`,
        prefix: beam.tokens.join(" "),
        token: BEAM_TOKENS[tokenIndex],
        score: beam.score + tokenScore,
      }))
    ).sort((left, right) => right.score - left.score);
    return rows;
  }, []);

  const keptBeamRows = beamRows.slice(0, beamWidth);
  const winnerIndex = candidateSet[0] ?? 0;
  const selectedProbability = probabilities[winnerIndex] ?? 0;

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Decoding Policy Explorer</div>
        <p className="observable-viz-subtitle">
          Temperature reshapes probabilities first. Greedy, top-k, top-p, and beam
          then choose different candidate sets from that same score surface.
        </p>
      </div>

      <div className="observable-controls">
        <label className="observable-control">
          <span className="observable-control-label">Mode</span>
          <select
            className="observable-control-select"
            value={mode}
            onChange={(event) =>
              setMode(event.target.value as "greedy" | "top-k" | "top-p" | "beam")
            }
          >
            <option value="greedy">Greedy</option>
            <option value="top-k">Top-k</option>
            <option value="top-p">Top-p</option>
            <option value="beam">Beam</option>
          </select>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Temperature</span>
          <input
            className="observable-control-input"
            type="range"
            min="0.5"
            max="1.6"
            step="0.05"
            value={temperature}
            onChange={(event) => setTemperature(Number(event.target.value))}
          />
          <span className="observable-control-value">{temperature.toFixed(2)}</span>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Top-k</span>
          <input
            className="observable-control-input"
            type="range"
            min="1"
            max="6"
            step="1"
            value={topK}
            onChange={(event) => setTopK(Number(event.target.value))}
          />
          <span className="observable-control-value">{topK}</span>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Top-p</span>
          <input
            className="observable-control-input"
            type="range"
            min="0.4"
            max="1"
            step="0.05"
            value={topP}
            onChange={(event) => setTopP(Number(event.target.value))}
          />
          <span className="observable-control-value">{topP.toFixed(2)}</span>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Beam width</span>
          <input
            className="observable-control-input"
            type="range"
            min="1"
            max="4"
            step="1"
            value={beamWidth}
            onChange={(event) => setBeamWidth(Number(event.target.value))}
          />
          <span className="observable-control-value">{beamWidth}</span>
        </label>
      </div>

      <div className="decoding-viz-grid">
        <div className="decoding-viz-distribution">
          {ranked.map((item) => {
            const kept = candidateSet.includes(item.index);
            const isWinner = item.index === winnerIndex;
            return (
              <div
                key={item.token}
                className={`decoding-viz-token ${
                  kept ? "decoding-viz-token-kept" : "decoding-viz-token-pruned"
                } ${isWinner && mode !== "beam" ? "decoding-viz-token-winner" : ""}`}
              >
                <div className="decoding-viz-token-header">
                  <strong>{item.token}</strong>
                  <span>{formatPercent(item.probability)}</span>
                </div>
                <div className="decoding-viz-bar">
                  <span style={{ width: `${item.probability * 100}%` }} />
                </div>
              </div>
            );
          })}
        </div>

        <div className="decoding-viz-panel">
          {mode === "beam" ? (
            <>
              <div className="decoding-viz-panel-title">Beam expansions</div>
              <div className="decoding-viz-beams">
                {beamRows.map((row) => (
                  <div
                    key={row.id}
                    className={`decoding-viz-beam-row ${
                      keptBeamRows.some((beam) => beam.id === row.id)
                        ? "decoding-viz-beam-row-kept"
                        : ""
                    }`}
                  >
                    <span>{row.prefix} + {row.token}</span>
                    <strong>{row.score.toFixed(2)}</strong>
                  </div>
                ))}
              </div>
            </>
          ) : (
            <>
              <div className="decoding-viz-panel-title">Selected candidate set</div>
              <div className="decoding-viz-chips">
                {candidateSet.map((index) => (
                  <span key={TOKENS[index]} className="decoding-viz-chip">
                    {TOKENS[index]}
                  </span>
                ))}
              </div>
              <p className="decoding-viz-note">
                {mode === "greedy"
                  ? "Greedy keeps only the highest-probability next token."
                  : mode === "top-k"
                    ? "Top-k keeps a fixed-size shortlist after temperature scaling."
                    : "Top-p keeps the smallest prefix whose cumulative probability crosses p."}
              </p>
            </>
          )}
        </div>
      </div>

      <div className="observable-stats">
        <div className="observable-stat-row">
          <span>Mode</span>
          <span className="observable-stat-value">{mode}</span>
        </div>
        <div className="observable-stat-row">
          <span>Winner</span>
          <span className="observable-stat-value">
            {mode === "beam"
              ? keptBeamRows[0]
                ? `${keptBeamRows[0].prefix} ${keptBeamRows[0].token}`
                : "n/a"
              : TOKENS[winnerIndex]}
          </span>
        </div>
        <div className="observable-stat-row">
          <span>Winner prob</span>
          <span className="observable-stat-value">
            {mode === "beam" ? "sequence score" : formatPercent(selectedProbability)}
          </span>
        </div>
        <div className="observable-stat-row">
          <span>Candidates</span>
          <span className="observable-stat-value">
            {mode === "beam" ? keptBeamRows.length : candidateSet.length}
          </span>
        </div>
      </div>
    </div>
  );
}
