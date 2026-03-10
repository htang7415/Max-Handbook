# LLM Inference Serving

Serving quality depends on latency, memory, batching, and hardware efficiency more than on model architecture alone.

## Current Anchors

- KV cache sizing (`modules/ml/llm/kv-cache`)
- Prefix-cache reuse (`modules/ml/llm/prefix-cache`)
- Prefix-cache savings metrics (`modules/ml/systems/prefix-cache-metrics`)
- Speculative decoding verification (`modules/ml/llm/speculative-decoding`)
- Inference head pruning (`modules/ml/llm/inference-head-pruning`)
- Numeric formats and quantization (`modules/ml/llm/precision-and-quantization`)
- Request batching (`modules/ml/mlops/request-batching`)
- Continuous batching (`modules/ml/systems/continuous-batching`)
- Chunked prefill rounds (`modules/ml/systems/chunked-prefill`)
- Roofline analysis (`modules/ml/systems/roofline-analysis`)

## Concepts to Cover Well

- TTFT, ITL, and tokens/sec
- Continuous batching and chunked prefill
- KV cache memory budgets and eviction
- Prefix cache reuse
- Prefix cache hit lengths and saved-token metrics
- Speculative decoding and verification
