"use client";

import { useMemo, useState } from "react";

const TOKENS = ["The", "agent", "read", "the", "docs", "carefully"] as const;

type AttentionMode = "full" | "causal" | "local";

function softmax(values: number[]) {
  const maximum = Math.max(...values);
  const exps = values.map((value) => Math.exp(value - maximum));
  const total = exps.reduce((sum, value) => sum + value, 0);
  return exps.map((value) => value / total);
}

function baseScore(queryIndex: number, keyIndex: number, head: number) {
  const distance = Math.abs(queryIndex - keyIndex);
  const locality = head === 0 ? 1.2 : 2.8;
  const diagonalBias = queryIndex === keyIndex ? 0.7 : 0;
  const backwardBias = keyIndex < queryIndex ? 0.25 : 0;
  return -distance / locality + diagonalBias + backwardBias;
}

export default function AttentionMechanismsViz() {
  const [mode, setMode] = useState<AttentionMode>("causal");
  const [queryIndex, setQueryIndex] = useState(4);
  const [windowSize, setWindowSize] = useState(2);
  const [head, setHead] = useState(0);

  const weights = useMemo(() => {
    return TOKENS.map((_, qIndex) => {
      const maskedScores = TOKENS.map((_, kIndex) => {
        const blockedByCausal = mode === "causal" && kIndex > qIndex;
        const blockedByWindow = mode === "local" && Math.abs(qIndex - kIndex) > windowSize;
        if (blockedByCausal || blockedByWindow) {
          return Number.NEGATIVE_INFINITY;
        }
        return baseScore(qIndex, kIndex, head);
      });

      const finiteScores = maskedScores.filter(Number.isFinite);
      if (finiteScores.length === 0) {
        return maskedScores.map(() => 0);
      }

      const rowSoftmax = softmax(
        maskedScores.map((value) => (Number.isFinite(value) ? value : -1e9))
      );
      return rowSoftmax;
    });
  }, [head, mode, windowSize]);

  const selectedRow = weights[queryIndex] ?? [];
  const visiblePairs = weights.flat().filter((value) => value > 0).length;

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Attention Mechanisms</div>
        <p className="observable-viz-subtitle">
          Switch between full, causal, and local masking to see how attention scores
          become weights and which token pairs are allowed to interact.
        </p>
      </div>

      <div className="observable-controls">
        <label className="observable-control">
          <span className="observable-control-label">Mask</span>
          <select
            className="observable-control-select"
            value={mode}
            onChange={(event) => setMode(event.target.value as AttentionMode)}
          >
            <option value="full">Full attention</option>
            <option value="causal">Causal mask</option>
            <option value="local">Local window</option>
          </select>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Query token</span>
          <input
            className="observable-control-input"
            type="range"
            min="0"
            max={String(TOKENS.length - 1)}
            step="1"
            value={queryIndex}
            onChange={(event) => setQueryIndex(Number(event.target.value))}
          />
          <span className="observable-control-value">{queryIndex}</span>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Head</span>
          <input
            className="observable-control-input"
            type="range"
            min="0"
            max="1"
            step="1"
            value={head}
            onChange={(event) => setHead(Number(event.target.value))}
          />
          <span className="observable-control-value">{head + 1}</span>
        </label>
        {mode === "local" ? (
          <label className="observable-control">
            <span className="observable-control-label">Window</span>
            <input
              className="observable-control-input"
              type="range"
              min="0"
              max="5"
              step="1"
              value={windowSize}
              onChange={(event) => setWindowSize(Number(event.target.value))}
            />
            <span className="observable-control-value">{windowSize}</span>
          </label>
        ) : null}
      </div>

      <div className="attention-viz-layout">
        <div className="attention-viz-grid">
          {weights.map((row, qIndex) =>
            row.map((value, kIndex) => {
              const active = qIndex === queryIndex;
              const alpha = value === 0 ? 0.06 : 0.14 + value * 0.76;
              return (
                <div
                  key={`${qIndex}-${kIndex}`}
                  className={`attention-viz-cell ${active ? "attention-viz-cell-active" : ""}`}
                  style={{ background: `rgba(37, 99, 235, ${alpha.toFixed(3)})` }}
                  title={`q${qIndex} -> k${kIndex}: ${value.toFixed(2)}`}
                >
                  {value === 0 ? "x" : value.toFixed(2)}
                </div>
              );
            })
          )}
        </div>

        <div className="attention-viz-panel">
          <div className="attention-viz-panel-title">
            Query token: <strong>{TOKENS[queryIndex]}</strong>
          </div>
          <div className="attention-viz-token-bars">
            {selectedRow.map((value, index) => (
              <div key={`${queryIndex}-${index}`} className="attention-viz-token-row">
                <span>{TOKENS[index]}</span>
                <div className="attention-viz-token-bar">
                  <span style={{ width: `${value * 100}%` }} />
                </div>
                <strong>{value.toFixed(2)}</strong>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="observable-stats">
        <div className="observable-stat-row">
          <span>Mask</span>
          <span className="observable-stat-value">{mode}</span>
        </div>
        <div className="observable-stat-row">
          <span>Visible pairs</span>
          <span className="observable-stat-value">{visiblePairs}</span>
        </div>
        <div className="observable-stat-row">
          <span>Selected head</span>
          <span className="observable-stat-value">{head + 1}</span>
        </div>
        <div className="observable-stat-row">
          <span>Strongest key</span>
          <span className="observable-stat-value">
            {TOKENS[
              selectedRow.reduce(
                (bestIndex, value, index, values) =>
                  value > (values[bestIndex] ?? -1) ? index : bestIndex,
                0
              )
            ]}
          </span>
        </div>
      </div>
    </div>
  );
}
