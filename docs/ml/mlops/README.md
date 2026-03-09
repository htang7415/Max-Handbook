# MLOps and Production ML

Operational concerns for production ML.
Each bullet maps to a module under `modules/ml/mlops/`.

## Production Concepts

- ETL pipeline (`modules/ml/mlops/etl-pipeline`)
- Offline vs online inference (`modules/ml/mlops/offline-online-inference`)
- Batch vs real-time inference (`modules/ml/mlops/batch-vs-realtime`)
- Data quality checks (`modules/ml/mlops/data-quality-checks`)
- Feature drift detection (PSI) (`modules/ml/mlops/feature-drift-psi`)
- Drift detection with KS distance (`modules/ml/mlops/drift-detection`)
- Prediction distribution monitoring (`modules/ml/mlops/prediction-monitoring`)
- Canary deployment (`modules/ml/mlops/canary-deployment`)
- Canary rollout progression (`modules/ml/mlops/canary-rollout`)
- Online shadow mode (`modules/ml/mlops/online-shadow-mode`)
- A/B testing (`modules/ml/mlops/ab-testing`)
- A/B test statistical analysis (`modules/ml/evaluation/ab-test-analysis`)
- Sequential testing (`modules/ml/mlops/sequential-testing`)
- SLA metrics (`modules/ml/mlops/sla-metrics`)
- Request-level SLA compliance (`modules/ml/mlops/request-sla`)
- Request batching (`modules/ml/mlops/request-batching`)
- Error-budget tracking (`modules/ml/mlops/error-budget`)
