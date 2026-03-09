# 2D vs 3D CNN

> Track: `ml` | Topic: `computer-vision`

## Concept

2D CNNs convolve over height and width, while 3D CNNs also convolve over a
depth or time axis. This makes 3D CNNs useful for video and volumetric data,
where patterns span multiple frames or slices.

## Math
$$d_{\text{out}} = d_{\text{in}} - k_d + 1$$

- $d_{\text{in}}$ -- input depth or number of frames/slices
- $k_d$ -- kernel depth
- $d_{\text{out}}$ -- output depth after valid convolution

## Key Points

- 2D convolutions treat frames independently if applied frame by frame.
- 3D convolutions can learn motion or volumetric patterns across the extra axis.
- The extra dimension increases compute and memory cost.

## Function

```python
def output_depth(input_depth: int, kernel_depth: int) -> int:
```

## Run tests

```bash
pytest modules/ml/computer-vision/cnn-2d-vs-3d/python -q
```
