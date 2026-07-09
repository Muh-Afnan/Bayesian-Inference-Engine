# Problem Statement

## Why This Day Exists

The Central Limit Theorem is the reason statistics works.

It is the reason you can take 30 measurements and make confident claims about a population of millions. It is the reason Gaussian distributions appear everywhere in ML even when the underlying data is not Gaussian. It is the reason averaging data is so powerful.

Most people learn CLT as a statement — "sample means converge to Gaussian." Few people ever see it happen. Day 7 builds the visual proof — an interactive tool where you can watch the convergence happen in real time by dragging a slider.

## The Theorem

No matter what distribution you sample from, if you take the mean of n samples, that mean will be approximately Gaussian. The approximation improves as n increases.

```
X₁, X₂, ..., Xₙ ~ any distribution with mean μ and variance σ²

Sample mean X̄  →  N(μ, σ²/n)  as n → ∞
```

This holds for Uniform, Exponential, Bernoulli, Poisson — any distribution with finite mean and variance.

## The Goal

Build a simulator that:
- Takes any distribution from Day 6
- Runs thousands of sampling experiments
- Plots the distribution of sample means
- Overlays the theoretical Gaussian prediction
- Provides an interactive slider to see convergence in real time

The slider is the proof. Drag from n=1 to n=50 and watch a skewed or flat distribution transform into a bell curve.