"use client";

import { useMemo, useState } from "react";

const EXAMPLES = [
  { id: "a", probability: 0.97, label: 1 },
  { id: "b", probability: 0.91, label: 1 },
  { id: "c", probability: 0.84, label: 0 },
  { id: "d", probability: 0.76, label: 1 },
  { id: "e", probability: 0.67, label: 0 },
  { id: "f", probability: 0.58, label: 1 },
  { id: "g", probability: 0.46, label: 0 },
  { id: "h", probability: 0.39, label: 1 },
  { id: "i", probability: 0.31, label: 0 },
  { id: "j", probability: 0.23, label: 0 },
  { id: "k", probability: 0.15, label: 1 },
  { id: "l", probability: 0.08, label: 0 },
] as const;

function ratio(numerator: number, denominator: number) {
  return denominator === 0 ? 0 : numerator / denominator;
}

export default function ClassificationMetricsViz() {
  const [threshold, setThreshold] = useState(0.55);

  const summary = useMemo(() => {
    let tp = 0;
    let tn = 0;
    let fp = 0;
    let fn = 0;

    const rows = EXAMPLES.map((example) => {
      const predicted = example.probability >= threshold ? 1 : 0;
      if (predicted === 1 && example.label === 1) tp += 1;
      if (predicted === 0 && example.label === 0) tn += 1;
      if (predicted === 1 && example.label === 0) fp += 1;
      if (predicted === 0 && example.label === 1) fn += 1;
      return { ...example, predicted };
    });

    const precision = ratio(tp, tp + fp);
    const recall = ratio(tp, tp + fn);
    const accuracy = ratio(tp + tn, rows.length);
    const f1 = ratio(2 * precision * recall, precision + recall);

    return { rows, tp, tn, fp, fn, precision, recall, accuracy, f1 };
  }, [threshold]);

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Classification Metrics Core</div>
        <p className="observable-viz-subtitle">
          Slide the decision threshold and watch the same probability scores change
          the confusion matrix, precision, recall, F1, and accuracy.
        </p>
      </div>

      <div className="observable-controls">
        <label className="observable-control">
          <span className="observable-control-label">Threshold</span>
          <input
            className="observable-control-input"
            type="range"
            min="0.1"
            max="0.9"
            step="0.01"
            value={threshold}
            onChange={(event) => setThreshold(Number(event.target.value))}
          />
          <span className="observable-control-value">{threshold.toFixed(2)}</span>
        </label>
      </div>

      <div className="metric-viz-layout">
        <div className="metric-viz-examples">
          {summary.rows.map((row) => (
            <div
              key={row.id}
              className={`metric-viz-row ${
                row.predicted === row.label
                  ? "metric-viz-row-correct"
                  : "metric-viz-row-error"
              }`}
            >
              <div className="metric-viz-row-header">
                <strong>{row.id}</strong>
                <span>
                  y={row.label} / y^={row.predicted}
                </span>
              </div>
              <div className="metric-viz-bar">
                <span style={{ width: `${row.probability * 100}%` }} />
                <i style={{ left: `${threshold * 100}%` }} />
              </div>
            </div>
          ))}
        </div>

        <div className="metric-viz-matrix">
          <div className="metric-viz-cell">
            <small>TP</small>
            <strong>{summary.tp}</strong>
          </div>
          <div className="metric-viz-cell">
            <small>FP</small>
            <strong>{summary.fp}</strong>
          </div>
          <div className="metric-viz-cell">
            <small>FN</small>
            <strong>{summary.fn}</strong>
          </div>
          <div className="metric-viz-cell">
            <small>TN</small>
            <strong>{summary.tn}</strong>
          </div>
        </div>
      </div>

      <div className="observable-stats">
        <div className="observable-stat-row">
          <span>Accuracy</span>
          <span className="observable-stat-value">{summary.accuracy.toFixed(2)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Precision</span>
          <span className="observable-stat-value">{summary.precision.toFixed(2)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Recall</span>
          <span className="observable-stat-value">{summary.recall.toFixed(2)}</span>
        </div>
        <div className="observable-stat-row">
          <span>F1</span>
          <span className="observable-stat-value">{summary.f1.toFixed(2)}</span>
        </div>
      </div>
    </div>
  );
}
