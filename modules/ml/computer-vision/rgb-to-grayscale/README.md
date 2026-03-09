# RGB to Grayscale

> Track: `ml` | Topic: `computer-vision`

## Concept

Convert an RGB pixel into one luminance value by weighting the red, green, and
blue channels according to human visual sensitivity.

## Math

$$Y = 0.299R + 0.587G + 0.114B$$

- $R$ -- red channel intensity
- $G$ -- green channel intensity
- $B$ -- blue channel intensity
- $Y$ -- grayscale luminance value

## Key Points

- Green contributes the most because human vision is most sensitive there.
- The result is one brightness value, not a three-channel color pixel.
- This is a fixed linear transform, not a learned model.

## Function

```python
def rgb_to_gray(r: int, g: int, b: int) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/rgb-to-grayscale/python -q
```
