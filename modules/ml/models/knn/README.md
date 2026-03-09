# K-Nearest Neighbors

> Track: `ml` | Topic: `models`

## Concept

K-nearest neighbors predicts by looking up the labels of nearby training points.
It stores the dataset instead of learning explicit parameters, which is why KNN
is often described as a lazy learner.

## Math
$$\hat{c} = \arg\max_c \sum_{i \in \mathcal{N}_k} \mathbb{I}[y_i=c]$$

- $\mathbb{I}$ -- indicator function
- $\mathcal{N}_k$ -- set of the $k$ nearest neighbors
- $y_i$ -- label of neighbor $i$
- $\hat{c}$ -- predicted class
- $i$ -- index
- $k$ -- number of neighbors used for voting
- $c$ -- candidate class

## Key Points

- Prediction depends entirely on the distance metric and the neighborhood size.
- Small `k` can be noisy; large `k` can oversmooth class boundaries.
- KNN is simple but can be expensive at inference because it compares against stored examples.

## Function

```python
def knn_predict(distances: list[float], labels: list[int], k: int) -> int:
```

## Run tests

```bash
pytest modules/ml/models/knn/python -q
```
