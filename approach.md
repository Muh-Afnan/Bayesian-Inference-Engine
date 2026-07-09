# Approach

## Core Design — CLTSimulator

`CLTSimulator` wraps any distribution object and runs the sampling experiment:

```
For each of n_experiments:
    Draw sample_size values from distribution
    Compute their mean
    Store it

Return all stored means
```

The result is a list of sample means. As `sample_size` increases, this list becomes more Gaussian.

The theoretical prediction comes from two formulas:
```
mu    = distribution.mean()           ← centre of the predicted Gaussian
sigma = distribution.std() / √n       ← spread of the predicted Gaussian
```

`CLTSimulator` is generic — it works for any distribution that implements `.mean()`, `.std()`, and `.sample()`. This is why Day 6's consistent interface matters.

## Measuring Convergence — Skewness

To quantify how Gaussian the sample means are, skewness is used:

```
skewness = E[(x - mean)³] / std³
```

Perfect Gaussian has skewness = 0. Positive skewness means the distribution has a long right tail. Negative skewness means long left tail.

As sample_size increases, skewness of the sample means approaches 0 — regardless of the original distribution's skewness. This is how convergence speed is measured and plotted.

## The Four Visualisations

**`plot_clt_convergence`** — grid of histograms at different sample sizes. Each histogram overlays the theoretical Gaussian in red. The visual shift from irregular to bell-shaped across the grid is the proof.

**`plot_original_vs_clt`** — side by side comparison. Left: raw samples from the distribution (shows its true shape). Right: sample means (should look Gaussian). The contrast makes CLT immediate.

**`plot_convergence_speed`** — skewness vs sample_size for multiple distributions on the same axes. Symmetric distributions (Uniform, Gaussian) converge fast — skewness drops to near 0 quickly. Skewed distributions (Exponential) converge slower — they need larger sample sizes.

**`plot_interactive`** — matplotlib Slider widget. Dragging the slider changes sample_size in real time. The histogram redraws on every slider move. This is the most powerful visualisation — seeing the transformation happen continuously rather than in discrete steps.

## The Interactive Plot — How It Works

```python
slider.on_changed(update)
```

Every time the slider moves, `update(val)` is called with the new value. Inside `update`:
1. Get new sample_size from slider
2. Run new simulation
3. Clear the axes
4. Redraw histogram and Gaussian overlay
5. Matplotlib refreshes automatically

The key insight: `ax.clear()` before redrawing. Without it, each slider move adds a new histogram on top of the previous one.

## Density=True

All histograms use `density=True`. This normalises the y-axis so area under the histogram equals 1 — the same as a probability density function. Without this, the histogram y-axis is raw counts and the Gaussian PDF overlay (which integrates to 1) would be invisible by comparison.