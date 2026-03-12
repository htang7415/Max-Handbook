import type { ComponentType } from "react";
import ActivationFunctionsViz from "@/components/ActivationFunctionsViz";
import AttentionMechanismsViz from "@/components/AttentionMechanismsViz";
import BTreeBasicsViz from "@/components/BTreeBasicsViz";
import CalibrationViz from "@/components/CalibrationViz";
import ClassificationMetricsViz from "@/components/ClassificationMetricsViz";
import DecodingMethodsViz from "@/components/DecodingMethodsViz";
import GradientDescentViz from "@/components/GradientDescentViz";
import HomeHeroViz from "@/components/HomeHeroViz";
import HomeSoftmaxViz from "@/components/HomeSoftmaxViz";
import HomeSignalViz from "@/components/HomeSignalViz";
import LongContextCachingViz from "@/components/LongContextCachingViz";
import MonotonicStackViz from "@/components/MonotonicStackViz";
import NormalizationMethodsViz from "@/components/NormalizationMethodsViz";
import ReasoningTestTimeComputeViz from "@/components/ReasoningTestTimeComputeViz";
import RetrievalMetricsViz from "@/components/RetrievalMetricsViz";
import RetriesFallbacksViz from "@/components/RetriesFallbacksViz";
import TokenizationViz from "@/components/TokenizationViz";
import VectorsMatricesViz from "@/components/VectorsMatricesViz";
import VoteMetricsViz from "@/components/VoteMetricsViz";
import { getVisualRegistryKey, VISUALS } from "@/lib/visual-metadata";

export const VISUAL_COMPONENTS: Record<string, ComponentType> = {
  "attention-map-preview": HomeHeroViz,
  "next-token-distribution": HomeSoftmaxViz,
  "positional-encoding": HomeSignalViz,
  "attention-mechanisms": AttentionMechanismsViz,
  "tokenization-trade-offs": TokenizationViz,
  "long-context-and-caching": LongContextCachingViz,
  "decoding-policy-explorer": DecodingMethodsViz,
  "retrieval-metrics": RetrievalMetricsViz,
  "reasoning-and-test-time-compute": ReasoningTestTimeComputeViz,
  "vote-metrics": VoteMetricsViz,
  "reliability-diagram": CalibrationViz,
  "gradient-descent-playground": GradientDescentViz,
  "activation-functions": ActivationFunctionsViz,
  "normalization-methods": NormalizationMethodsViz,
  "matrix-transform-explorer": VectorsMatricesViz,
  "composite-btree-path": BTreeBasicsViz,
  "monotonic-stack-walkthrough": MonotonicStackViz,
  "retries-and-fallbacks": RetriesFallbacksViz,
  "classification-metrics-core": ClassificationMetricsViz,
};

export const VIZ_REGISTRY: Partial<Record<string, ComponentType>> = Object.fromEntries(
  VISUALS.filter((visual) => visual.showOnTopicPage && visual.slug).map((visual) => [
    getVisualRegistryKey(visual.track, visual.topic, visual.slug ?? ""),
    VISUAL_COMPONENTS[visual.id],
  ])
);
