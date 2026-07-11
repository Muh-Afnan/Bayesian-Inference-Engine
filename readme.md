# Day 8 — Bayesian Inference Engine

A Bayesian inference engine built from scratch. No scipy. No stats libraries. Pure Python math.

## What It Does

- Discrete Bayesian inference over explicit hypothesis buckets
- Beta-Binomial conjugate model for continuous bias estimation
- Four visualizations showing how beliefs update with evidence
- 7 tests covering posterior correctness, conjugate updates, and credible intervals

## Project Structure

day-08-bayesian-inference-engine/
├── src/
│   ├── bayes.py          # BayesianInference — discrete updater
│   ├── conjugate.py      # BetaBinomial — continuous conjugate model
│   └── visualizer.py     # Four visualization functions
├── tests/
│   └── tests.py          # 7 tests
├── outputs/              # Saved plots
├── demo.py               # Runs all visualizations end to end
├── problem_statement.md
├── approach.md
├── learnings.md
└── README.md

## Quick Start

```bash
pip install matplotlib
python demo.py
```

## Core Classes

### BayesianInference

Discrete Bayesian updater over a fixed set of hypotheses.

```python
bi = BayesianInference(
    prior=[0.25, 0.25, 0.25, 0.25],
    hypotheses=[0.1, 0.5, 0.6, 0.9]
)

posterior = bi.update(n=10, k=7)    # 7 heads in 10 flips
predicted = bi.predict(n_future=5)  # expected heads in 5 future flips

# Result: [2.2e-05, 0.3008, 0.5518, 0.1473]
# h=0.6 wins — consistent with 7/10 heads
```

### BetaBinomial

Continuous conjugate model. Treats bias as a Beta-distributed random variable.

```python
bb = BetaBinomial(alpha=1, beta=1)  # uniform prior — no opinion
bb = bb.update(heads=7, tails=3)    # observe 7 heads, 3 tails
print(bb.mean())                     # 0.6667
print(bb.pdf(0.6))                  # ~2.36
```

Update rule: `alpha += heads`, `beta += tails`. No integration needed.

## Visualizations

| Function | Chart Type | What It Shows |
|---|---|---|
| `plot_prior_likelihood_posterior` | Grouped bar | How evidence shifts belief across hypotheses |
| `plot_sequential_updating` | Line chart | Belief evolution flip by flip |
| `plot_beta_updating` | Curve plot | Beta PDF sharpening with evidence |
| `plot_credible_interval` | Bar chart | Which hypotheses are inside the 95% interval |

## Tests

```bash
python -m pytest tests/tests.py
```
7 passed in 0.13s

| Test | What It Verifies |
|---|---|
| `test_posterior_sums_to_one` | Posterior is a valid probability distribution |
| `test_uniform_prior_with_all_heads` | All heads evidence correctly shifts posterior |
| `test_strong_prior_resists_evidence` | Strong prior dominates with weak evidence |
| `test_sequential_updates_converge` | Posterior stabilizes with large data |
| `test_beta_conjugate_update` | Alpha and beta update correctly |
| `test_credible_interval_contains_truth` | Posterior mean falls in expected range |
| `test_posterior_predictive` | Predicted heads falls in sensible range |

## Math

**Bayes Theorem:**
P(H|E) = P(E|H) × P(H) / P(E)

**Binomial Likelihood:**

P(k heads | n flips, bias h) = C(n,k) × h^k × (1-h)^(n-k)

**Beta-Binomial Conjugate Update:**
Prior:     Beta(α, β)
Posterior: Beta(α + heads, β + tails)
Mean:      α / (α + β)

## Key Insight

Bayes theorem never changes. Only the likelihood formula changes depending on what generated the data. This engine uses Binomial likelihood — swap that one function and the entire framework supports Poisson, Gaussian, or any other distribution.

## Dependencies

- `matplotlib` — visualizations only
- No scipy, no numpy, no stats libraries