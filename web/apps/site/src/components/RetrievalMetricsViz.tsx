"use client";

import { useMemo, useState } from "react";

const BASELINE_IDS = ["d2", "d7", "d4", "d1", "d3", "d6", "d5", "d8"] as const;
const RERANKED_IDS = ["d3", "d2", "d5", "d7", "d1", "d4", "d6", "d8"] as const;
const RELEVANT_IDS = new Set(["d3", "d5", "d7"]);

function recallAtK(retrievedIds: string[], relevantIds: Set<string>, k: number) {
  return [...new Set(retrievedIds.slice(0, k))].filter((id) => relevantIds.has(id)).length / relevantIds.size;
}

function precisionAtK(retrievedIds: string[], relevantIds: Set<string>, k: number) {
  return [...new Set(retrievedIds.slice(0, k))].filter((id) => relevantIds.has(id)).length / k;
}

function f1AtK(retrievedIds: string[], relevantIds: Set<string>, k: number) {
  const precision = precisionAtK(retrievedIds, relevantIds, k);
  const recall = recallAtK(retrievedIds, relevantIds, k);
  return precision + recall === 0 ? 0 : (2 * precision * recall) / (precision + recall);
}

function reciprocalRank(retrievedIds: string[], relevantIds: Set<string>) {
  const first = retrievedIds.findIndex((id) => relevantIds.has(id));
  return first === -1 ? 0 : 1 / (first + 1);
}

function disagreementRate(baselineIds: string[], rerankedIds: string[], k: number) {
  let disagreements = 0;
  for (let index = 0; index < k; index += 1) {
    if (baselineIds[index] !== rerankedIds[index]) {
      disagreements += 1;
    }
  }
  return disagreements / k;
}

export default function RetrievalMetricsViz() {
  const [k, setK] = useState(4);

  const summary = useMemo(() => {
    const baselineRR = reciprocalRank([...BASELINE_IDS], RELEVANT_IDS);
    const rerankedRR = reciprocalRank([...RERANKED_IDS], RELEVANT_IDS);
    return {
      baseline: {
        recall: recallAtK([...BASELINE_IDS], RELEVANT_IDS, k),
        precision: precisionAtK([...BASELINE_IDS], RELEVANT_IDS, k),
        f1: f1AtK([...BASELINE_IDS], RELEVANT_IDS, k),
        rr: baselineRR,
      },
      reranked: {
        recall: recallAtK([...RERANKED_IDS], RELEVANT_IDS, k),
        precision: precisionAtK([...RERANKED_IDS], RELEVANT_IDS, k),
        f1: f1AtK([...RERANKED_IDS], RELEVANT_IDS, k),
        rr: rerankedRR,
      },
      gain: rerankedRR - baselineRR,
      disagreement: disagreementRate([...BASELINE_IDS], [...RERANKED_IDS], k),
    };
  }, [k]);

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Retrieval Metrics</div>
        <p className="observable-viz-subtitle">
          Move the cutoff `k` and compare baseline retrieval with reranked output.
          Recall, precision, F1, reciprocal rank, and rerank gain highlight different
          retrieval failure modes.
        </p>
      </div>

      <div className="observable-controls">
        <label className="observable-control">
          <span className="observable-control-label">k</span>
          <input
            className="observable-control-input"
            type="range"
            min="1"
            max="8"
            step="1"
            value={k}
            onChange={(event) => setK(Number(event.target.value))}
          />
          <span className="observable-control-value">{k}</span>
        </label>
      </div>

      <div className="retrieval-viz-layout">
        <div className="retrieval-viz-card">
          <div className="retrieval-viz-title">Baseline ranking</div>
          <div className="retrieval-viz-list">
            {BASELINE_IDS.map((id, index) => (
              <div
                key={id}
                className={`retrieval-viz-item ${
                  index < k ? "retrieval-viz-item-active" : ""
                } ${RELEVANT_IDS.has(id) ? "retrieval-viz-item-relevant" : ""}`}
              >
                <span>#{index + 1}</span>
                <strong>{id}</strong>
                <small>{RELEVANT_IDS.has(id) ? "relevant" : "non-relevant"}</small>
              </div>
            ))}
          </div>
        </div>

        <div className="retrieval-viz-card">
          <div className="retrieval-viz-title">Reranked output</div>
          <div className="retrieval-viz-list">
            {RERANKED_IDS.map((id, index) => (
              <div
                key={id}
                className={`retrieval-viz-item ${
                  index < k ? "retrieval-viz-item-active" : ""
                } ${RELEVANT_IDS.has(id) ? "retrieval-viz-item-relevant" : ""}`}
              >
                <span>#{index + 1}</span>
                <strong>{id}</strong>
                <small>{RELEVANT_IDS.has(id) ? "relevant" : "non-relevant"}</small>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="retrieval-viz-metrics">
        <div className="retrieval-viz-metric-card">
          <div className="retrieval-viz-title">Baseline</div>
          <span>Recall@k: {summary.baseline.recall.toFixed(2)}</span>
          <span>Precision@k: {summary.baseline.precision.toFixed(2)}</span>
          <span>F1@k: {summary.baseline.f1.toFixed(2)}</span>
          <span>RR: {summary.baseline.rr.toFixed(2)}</span>
        </div>
        <div className="retrieval-viz-metric-card">
          <div className="retrieval-viz-title">Reranked</div>
          <span>Recall@k: {summary.reranked.recall.toFixed(2)}</span>
          <span>Precision@k: {summary.reranked.precision.toFixed(2)}</span>
          <span>F1@k: {summary.reranked.f1.toFixed(2)}</span>
          <span>RR: {summary.reranked.rr.toFixed(2)}</span>
        </div>
      </div>

      <div className="observable-stats">
        <div className="observable-stat-row">
          <span>Rerank gain</span>
          <span className="observable-stat-value">{summary.gain.toFixed(2)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Disagreement@k</span>
          <span className="observable-stat-value">{summary.disagreement.toFixed(2)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Relevant docs</span>
          <span className="observable-stat-value">{RELEVANT_IDS.size}</span>
        </div>
        <div className="observable-stat-row">
          <span>Cutoff</span>
          <span className="observable-stat-value">{k}</span>
        </div>
      </div>
    </div>
  );
}
