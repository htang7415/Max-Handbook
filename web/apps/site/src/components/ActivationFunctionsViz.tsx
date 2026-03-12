"use client";

import { useMemo, useState } from "react";

function sigmoid(x: number) {
  return 1 / (1 + Math.exp(-x));
}

function relu(x: number) {
  return Math.max(0, x);
}

function leakyRelu(x: number, alpha = 0.08) {
  return x > 0 ? x : alpha * x;
}

function gelu(x: number) {
  return 0.5 * x * (1 + Math.tanh(Math.sqrt(2 / Math.PI) * (x + 0.044715 * x ** 3)));
}

function swish(x: number) {
  return x * sigmoid(x);
}

function derivative(fn: (value: number) => number, x: number) {
  const eps = 1e-3;
  return (fn(x + eps) - fn(x - eps)) / (2 * eps);
}

const FUNCTIONS = [
  { id: "relu", label: "ReLU", color: "#2563eb", fn: relu },
  { id: "leaky", label: "Leaky ReLU", color: "#0ea5e9", fn: leakyRelu },
  { id: "sigmoid", label: "Sigmoid", color: "#f59e0b", fn: sigmoid },
  { id: "gelu", label: "GeLU", color: "#8b5cf6", fn: gelu },
  { id: "swish", label: "Swish", color: "#10b981", fn: swish },
] as const;

export default function ActivationFunctionsViz() {
  const [inputX, setInputX] = useState(0.8);
  const [focus, setFocus] = useState<"all" | "relu-family" | "smooth">("all");

  const visibleFunctions = useMemo(() => {
    if (focus === "relu-family") {
      return FUNCTIONS.filter((item) => item.id === "relu" || item.id === "leaky");
    }
    if (focus === "smooth") {
      return FUNCTIONS.filter(
        (item) => item.id === "sigmoid" || item.id === "gelu" || item.id === "swish"
      );
    }
    return FUNCTIONS;
  }, [focus]);

  const width = 340;
  const height = 220;
  const padding = { top: 16, right: 18, bottom: 26, left: 30 };
  const innerWidth = width - padding.left - padding.right;
  const innerHeight = height - padding.top - padding.bottom;
  const xScale = (x: number) => padding.left + ((x + 4) / 8) * innerWidth;
  const yScale = (y: number) => height - padding.bottom - ((y + 1.5) / 5.5) * innerHeight;

  const paths = useMemo(
    () =>
      visibleFunctions.map((item) => {
        const points: string[] = [];
        for (let x = -4; x <= 4.001; x += 0.12) {
          const px = xScale(x);
          const py = yScale(item.fn(x));
          points.push(`${points.length === 0 ? "M" : "L"} ${px.toFixed(2)} ${py.toFixed(2)}`);
        }
        return { ...item, path: points.join(" ") };
      }),
    [visibleFunctions]
  );

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Activation Functions</div>
        <p className="observable-viz-subtitle">
          Compare sparse ReLU-style activations with smoother sigmoid, GeLU, and Swish
          shapes, then inspect the local output and gradient at one input.
        </p>
      </div>

      <div className="observable-controls">
        <label className="observable-control">
          <span className="observable-control-label">Focus</span>
          <select
            className="observable-control-select"
            value={focus}
            onChange={(event) =>
              setFocus(event.target.value as "all" | "relu-family" | "smooth")
            }
          >
            <option value="all">All</option>
            <option value="relu-family">ReLU family</option>
            <option value="smooth">Smooth</option>
          </select>
        </label>
        <label className="observable-control">
          <span className="observable-control-label">Input x</span>
          <input
            className="observable-control-input"
            type="range"
            min="-4"
            max="4"
            step="0.1"
            value={inputX}
            onChange={(event) => setInputX(Number(event.target.value))}
          />
          <span className="observable-control-value">{inputX.toFixed(1)}</span>
        </label>
      </div>

      <div className="observable-chart">
        <svg
          viewBox={`0 0 ${width} ${height}`}
          className="observable-chart-svg"
          role="img"
          aria-label="Activation function curves"
        >
          <rect
            x={padding.left}
            y={padding.top}
            width={innerWidth}
            height={innerHeight}
            className="activation-viz-plot"
          />
          <line
            x1={xScale(-4)}
            x2={xScale(4)}
            y1={yScale(0)}
            y2={yScale(0)}
            className="activation-viz-axis"
          />
          <line
            x1={xScale(0)}
            x2={xScale(0)}
            y1={yScale(-1.5)}
            y2={yScale(4)}
            className="activation-viz-axis"
          />
          {paths.map((item) => (
            <path
              key={item.id}
              d={item.path}
              fill="none"
              stroke={item.color}
              strokeWidth="2.2"
              strokeLinecap="round"
            />
          ))}
          {visibleFunctions.map((item) => (
            <circle
              key={`${item.id}-point`}
              cx={xScale(inputX)}
              cy={yScale(item.fn(inputX))}
              r="4.5"
              fill={item.color}
              stroke="#fff"
              strokeWidth="1.5"
            />
          ))}
        </svg>
      </div>

      <div className="activation-viz-legend">
        {visibleFunctions.map((item) => (
          <span key={item.id} className="activation-viz-legend-item">
            <i style={{ background: item.color }} />
            {item.label}
          </span>
        ))}
      </div>

      <div className="activation-viz-stats">
        {visibleFunctions.map((item) => (
          <div key={item.id} className="activation-viz-stat">
            <strong>{item.label}</strong>
            <span>y = {item.fn(inputX).toFixed(2)}</span>
            <span>dy/dx = {derivative(item.fn, inputX).toFixed(2)}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
