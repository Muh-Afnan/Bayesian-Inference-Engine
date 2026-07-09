# Day 7 — Central Limit Theorem: Interactive Visual Proof

An interactive simulator that proves the Central Limit Theorem visually. Drag a slider and watch any distribution's sample means converge to a Gaussian bell curve in real time.

## What This Does

- Simulates thousands of sampling experiments from any distribution
- Plots the distribution of sample means vs theoretical Gaussian prediction
- Provides an interactive slider to control sample size
- Measures and compares convergence speed across different distributions

## File Structure

```
central_limit_theorem/
├── src/
│   ├── clt.py          # CLTSimulator class
│   └── visualizer.py   # Four visualisation functions + skewness helper
├── tests/
│   └── test_clt.py     # 7 tests
├── outputs/
├── demo.py
├── problem_statement.md
├── approach.md
└── learnings.md
```

## Usage

```python
from src.clt import CLTSimulator
from src.distribution import Exponential

dist = Exponential(lam=1)
sim = CLTSimulator(dist)

# run 1000 experiments, each averaging 30 samples
means = sim.simulate(n_samples=1000, sample_size=30)

# theoretical Gaussian prediction
mu, sigma = sim.theoretical_gaussian(sample_size=30)
print(f"Predicted: N({mu:.3f}, {sigma:.3f})")
```

## Visualisations

```python
from src.visualizer import (
    plot_clt_convergence,
    plot_original_vs_clt,
    plot_convergence_speed,
    plot_interactive,
)

# grid showing convergence at different sample sizes
plot_clt_convergence(Exponential(lam=1), sample_sizes=[1, 5, 10, 30], n_experiments=1000)

# side by side: raw distribution vs sample means
plot_original_vs_clt(Uniform(0, 1), sample_size=30, n_experiments=1000)

# convergence speed comparison across distributions
plot_convergence_speed({
    "Uniform(0,1)": Uniform(0, 1),
    "Exponential(1)": Exponential(lam=1),
    "Bernoulli(0.3)": Bernoulli(p=0.3),
}, sample_sizes=[1, 2, 5, 10, 20, 50])

# interactive slider — drag to see CLT in real time
plot_interactive(Exponential(lam=1))
```

## Key Insight

Skewed distributions (Exponential, Bernoulli with extreme p) converge to Gaussian much slower than symmetric distributions (Uniform, Gaussian). Convergence speed depends on the skewness of the original distribution — not just sample size.

## Test Results

```
7/7 tests passing
```

## Dependencies

```
matplotlib         (visualisation + Slider widget)
sys, os            (path management for Day 6 imports)
Day 6 distributions (Gaussian, Uniform, Exponential, Bernoulli, Poisson, Binomial)
```