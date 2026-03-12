"use client";

import { useMemo, useState } from "react";

interface BucketSummary {
  accuracy: number;
  count: number;
  end: number;
  gap: number;
  meanConfidence: number;
  start: number;
}

const BASE_PROBABILITIES = [
  0.08, 0.12, 0.16, 0.21, 0.27, 0.33, 0.38, 0.44,
  0.49, 0.55, 0.6, 0.66, 0.72, 0.77, 0.81, 0.86,
  0.9, 0.94, 0.41, 0.58, 0.24, 0.69, 0.31, 0.83,
];

function clamp(value: number, min: number, max: number) {
  return Math.min(Math.max(value, min), max);
}

function round(value: number) {
  return value.toFixed(2);
}

function buildBuckets(
  confidences: number[],
  outcomes: number[],
  bucketCount: number
) {
  const buckets = Array.from({ length: bucketCount }, (_, index) => ({
    start: index / bucketCount,
    end: (index + 1) / bucketCount,
    count: 0,
    confidenceSum: 0,
    outcomeSum: 0,
  }));

  confidences.forEach((confidence, index) => {
    const bucketIndex =
      confidence >= 1
        ? bucketCount - 1
        : Math.min(bucketCount - 1, Math.floor(confidence * bucketCount));
    const bucket = buckets[bucketIndex];
    bucket.count += 1;
    bucket.confidenceSum += confidence;
    bucket.outcomeSum += outcomes[index] ?? 0;
  });

  return buckets.map<BucketSummary>((bucket) => {
    const meanConfidence =
      bucket.count > 0 ? bucket.confidenceSum / bucket.count : 0;
    const accuracy = bucket.count > 0 ? bucket.outcomeSum / bucket.count : 0;
    return {
      start: bucket.start,
      end: bucket.end,
      count: bucket.count,
      meanConfidence,
      accuracy,
      gap: Math.abs(meanConfidence - accuracy),
    };
  });
}

export default function CalibrationViz() {
  const [bias, setBias] = useState(0);
  const [sharpness, setSharpness] = useState(1);

  const bucketCount = 6;
  const width = 340;
  const height = 220;
  const padding = { top: 18, right: 18, bottom: 28, left: 34 };
  const innerWidth = width - padding.left - padding.right;
  const innerHeight = height - padding.top - padding.bottom;

  const summary = useMemo(() => {
    const samples = BASE_PROBABILITIES.map((baseProbability, index) => {
      const outcomeSeed = ((index * 37 + 11) % 100) / 100;
      const outcome = outcomeSeed < baseProbability ? 1 : 0;
      const confidence = clamp(
        0.5 + (baseProbability - 0.5) * sharpness + bias,
        0.02,
        0.98
      );
      return { confidence, outcome };
    });

    const confidences = samples.map((sample) => sample.confidence);
    const outcomes = samples.map((sample) => sample.outcome);
    const buckets = buildBuckets(confidences, outcomes, bucketCount);
    const ece =
      buckets.reduce((total, bucket) => total + bucket.count * bucket.gap, 0) /
      samples.length;
    const brier =
      samples.reduce(
        (total, sample) => total + (sample.confidence - sample.outcome) ** 2,
        0
      ) / samples.length;
    const meanConfidence =
      confidences.reduce((total, value) => total + value, 0) / confidences.length;
    const accuracy =
      outcomes.reduce((total, value) => total + value, 0) / outcomes.length;

    return {
      buckets,
      ece,
      brier,
      meanConfidence,
      accuracy,
      route: ece <= 0.08 ? "pass" : "review",
    };
  }, [bias, sharpness]);

  const xScale = (value: number) => padding.left + value * innerWidth;
  const yScale = (value: number) => height - padding.bottom - value * innerHeight;

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Reliability Diagram</div>
        <p className="observable-viz-subtitle">
          Shift the confidence curve to see how calibration changes even when the
          ranking stays similar.
        </p>
      </div>

      <div className="observable-controls">
        <label className="observable-control">
          <span className="observable-control-label">Confidence bias</span>
          <input
            className="observable-control-input"
            type="range"
            min="-0.3"
            max="0.3"
            step="0.02"
            value={bias}
            onChange={(event) => setBias(Number(event.target.value))}
          />
          <span className="observable-control-value">{round(bias)}</span>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Sharpness</span>
          <input
            className="observable-control-input"
            type="range"
            min="0.7"
            max="1.4"
            step="0.05"
            value={sharpness}
            onChange={(event) => setSharpness(Number(event.target.value))}
          />
          <span className="observable-control-value">{round(sharpness)}</span>
        </label>
      </div>

      <div className="observable-chart">
        <svg
          viewBox={`0 0 ${width} ${height}`}
          className="observable-chart-svg"
          role="img"
          aria-label="Calibration reliability diagram"
        >
          <rect
            x={padding.left}
            y={padding.top}
            width={innerWidth}
            height={innerHeight}
            className="calibration-viz-plot"
          />

          {[0, 0.25, 0.5, 0.75, 1].map((tick) => (
            <g key={`grid-${tick}`}>
              <line
                x1={xScale(tick)}
                x2={xScale(tick)}
                y1={yScale(0)}
                y2={yScale(1)}
                className="calibration-viz-grid"
              />
              <line
                x1={xScale(0)}
                x2={xScale(1)}
                y1={yScale(tick)}
                y2={yScale(tick)}
                className="calibration-viz-grid"
              />
            </g>
          ))}

          <line
            x1={xScale(0)}
            y1={yScale(0)}
            x2={xScale(1)}
            y2={yScale(1)}
            className="calibration-viz-diagonal"
          />

          {summary.buckets
            .filter((bucket) => bucket.count > 0)
            .map((bucket, index) => {
              const x = xScale(bucket.meanConfidence);
              const y = yScale(bucket.accuracy);
              const idealY = yScale(bucket.meanConfidence);
              return (
                <g key={`bucket-${index}`}>
                  <line
                    x1={x}
                    x2={x}
                    y1={idealY}
                    y2={y}
                    className="calibration-viz-gap"
                  />
                  <circle cx={x} cy={y} r="5" className="calibration-viz-point" />
                  <text
                    x={x + 8}
                    y={Math.max(y - 8, padding.top + 12)}
                    className="calibration-viz-label"
                  >
                    b{index + 1}
                  </text>
                </g>
              );
            })}

          <text x={xScale(1)} y={height - 6} textAnchor="end" className="calibration-viz-axis">
            confidence
          </text>
          <text x={6} y={padding.top + 8} className="calibration-viz-axis">
            accuracy
          </text>
        </svg>
      </div>

      <div className="observable-stats">
        <div className="observable-stat-row">
          <span>ECE</span>
          <span className="observable-stat-value">{round(summary.ece)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Brier</span>
          <span className="observable-stat-value">{round(summary.brier)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Mean conf.</span>
          <span className="observable-stat-value">{round(summary.meanConfidence)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Accuracy</span>
          <span className="observable-stat-value">{round(summary.accuracy)}</span>
        </div>
        <div className="observable-stat-row">
          <span>Route</span>
          <span
            className={`observable-stat-value calibration-viz-route calibration-viz-route-${summary.route}`}
          >
            {summary.route}
          </span>
        </div>
      </div>

      <div className="calibration-viz-buckets">
        {summary.buckets.map((bucket, index) => (
          <div key={`summary-${index}`} className="calibration-viz-bucket">
            <strong>
              Bin {index + 1}
            </strong>
            <span>{round(bucket.start)} to {round(bucket.end)}</span>
            <span>{bucket.count} samples</span>
            <span>conf {round(bucket.meanConfidence)}</span>
            <span>acc {round(bucket.accuracy)}</span>
            <span>gap {round(bucket.gap)}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
