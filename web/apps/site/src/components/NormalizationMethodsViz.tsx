"use client";

import { useMemo, useState } from "react";

const BASE_MATRIX = [
  [1.2, -0.3, 0.8, 2.1],
  [0.5, -1.1, 1.4, 1.7],
  [2.3, 0.2, -0.4, 1.0],
];

function mean(values: number[]) {
  return values.reduce((sum, value) => sum + value, 0) / values.length;
}

function variance(values: number[]) {
  const avg = mean(values);
  return values.reduce((sum, value) => sum + (value - avg) ** 2, 0) / values.length;
}

function batchNorm(matrix: number[][]) {
  const features = matrix[0]?.length ?? 0;
  const means = Array.from({ length: features }, (_, feature) =>
    mean(matrix.map((row) => row[feature] ?? 0))
  );
  const variances = Array.from({ length: features }, (_, feature) =>
    variance(matrix.map((row) => row[feature] ?? 0))
  );
  return matrix.map((row) =>
    row.map((value, feature) => (value - means[feature]) / Math.sqrt(variances[feature] + 1e-5))
  );
}

function layerNorm(matrix: number[][]) {
  return matrix.map((row) => {
    const rowMean = mean(row);
    const rowVariance = variance(row);
    return row.map((value) => (value - rowMean) / Math.sqrt(rowVariance + 1e-5));
  });
}

function rmsNorm(matrix: number[][]) {
  return matrix.map((row) => {
    const rms = Math.sqrt(row.reduce((sum, value) => sum + value ** 2, 0) / row.length + 1e-5);
    return row.map((value) => value / rms);
  });
}

function colorForValue(value: number) {
  const magnitude = Math.min(Math.abs(value) / 2, 1);
  if (value >= 0) {
    return `rgba(37, 99, 235, ${0.12 + magnitude * 0.32})`;
  }
  return `rgba(245, 158, 11, ${0.12 + magnitude * 0.32})`;
}

export default function NormalizationMethodsViz() {
  const [method, setMethod] = useState<"batchnorm" | "layernorm" | "rmsnorm">("layernorm");
  const [shift, setShift] = useState(0.4);
  const [spike, setSpike] = useState(1.2);

  const inputMatrix = useMemo(() => {
    return BASE_MATRIX.map((row, rowIndex) =>
      row.map((value, columnIndex) => {
        const shifted = value + shift;
        if (rowIndex === 0 && columnIndex === 3) {
          return shifted + spike;
        }
        return shifted;
      })
    );
  }, [shift, spike]);

  const outputMatrix = useMemo(() => {
    if (method === "batchnorm") return batchNorm(inputMatrix);
    if (method === "layernorm") return layerNorm(inputMatrix);
    return rmsNorm(inputMatrix);
  }, [inputMatrix, method]);

  const outputMean = mean(outputMatrix.flat());
  const outputRms = Math.sqrt(
    outputMatrix.flat().reduce((sum, value) => sum + value ** 2, 0) /
      outputMatrix.flat().length
  );

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Normalization Methods</div>
        <p className="observable-viz-subtitle">
          Change the batch shift and outlier spike, then compare how BatchNorm,
          LayerNorm, and RMSNorm share statistics across rows and features.
        </p>
      </div>

      <div className="observable-controls">
        <label className="observable-control">
          <span className="observable-control-label">Method</span>
          <select
            className="observable-control-select"
            value={method}
            onChange={(event) =>
              setMethod(event.target.value as "batchnorm" | "layernorm" | "rmsnorm")
            }
          >
            <option value="batchnorm">BatchNorm</option>
            <option value="layernorm">LayerNorm</option>
            <option value="rmsnorm">RMSNorm</option>
          </select>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Batch shift</span>
          <input
            className="observable-control-input"
            type="range"
            min="-1.2"
            max="1.2"
            step="0.1"
            value={shift}
            onChange={(event) => setShift(Number(event.target.value))}
          />
          <span className="observable-control-value">{shift.toFixed(1)}</span>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Feature spike</span>
          <input
            className="observable-control-input"
            type="range"
            min="0"
            max="2.4"
            step="0.1"
            value={spike}
            onChange={(event) => setSpike(Number(event.target.value))}
          />
          <span className="observable-control-value">{spike.toFixed(1)}</span>
        </label>
      </div>

      <div className="norm-viz-grids">
        <div className="norm-viz-grid-card">
          <div className="norm-viz-grid-title">Input activations</div>
          <div className="norm-viz-grid">
            {inputMatrix.map((row, rowIndex) =>
              row.map((value, columnIndex) => (
                <span
                  key={`input-${rowIndex}-${columnIndex}`}
                  className="norm-viz-cell"
                  style={{ background: colorForValue(value) }}
                >
                  {value.toFixed(2)}
                </span>
              ))
            )}
          </div>
        </div>
        <div className="norm-viz-grid-card">
          <div className="norm-viz-grid-title">Normalized output</div>
          <div className="norm-viz-grid">
            {outputMatrix.map((row, rowIndex) =>
              row.map((value, columnIndex) => (
                <span
                  key={`output-${rowIndex}-${columnIndex}`}
                  className="norm-viz-cell"
                  style={{ background: colorForValue(value) }}
                >
                  {value.toFixed(2)}
                </span>
              ))
            )}
          </div>
        </div>
      </div>

      <div className="observable-stats">
        <div className="observable-stat-row">
          <span>Method</span>
          <span className="observable-stat-value">{method}</span>
        </div>
        <div className="observable-stat-row">
          <span>Output mean</span>
          <span className="observable-stat-value">{outputMean.toFixed(2)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Output RMS</span>
          <span className="observable-stat-value">{outputRms.toFixed(2)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Shared stats</span>
          <span className="observable-stat-value">
            {method === "batchnorm"
              ? "batch per feature"
              : method === "layernorm"
                ? "per example"
                : "per example rms"}
          </span>
        </div>
      </div>
    </div>
  );
}
