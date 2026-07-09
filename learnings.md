# Learnings

## Skewness — The Most Surprising Thing

Before this day, the intuition was that all distributions converge to Gaussian roughly at the same speed. The convergence speed plot proved this wrong.

Symmetric distributions — Uniform, Gaussian — have near-zero skewness to begin with. Their sample means look Gaussian even at small sample sizes like n=5. The convergence is almost instant.

Skewed distributions — Exponential, Bernoulli with extreme p — have high skewness. Their sample means take much longer to look Gaussian. Exponential(λ=1) needs sample sizes around 30-50 before the skewness drops close to zero.

This matters practically. When you use CLT-based statistical tests, the required sample size depends on how skewed your underlying distribution is. For symmetric data, n=10 might be enough. For heavily skewed data, you might need n=100 or more.

The `plot_convergence_speed` function made this visible in a way no textbook description had before.

---

## The Slider — Seeing Is Different From Knowing

Knowing that "sample means converge to Gaussian as n increases" is one thing. Watching it happen is completely different.

At n=1, the histogram matches the original distribution's shape — flat for Uniform, skewed right for Exponential. Dragging the slider to n=5 and the shape already starts pulling inward. At n=30 it is clearly a bell curve. At n=100 it is tight and symmetric.

The slider compressed what would take 10 separate charts into a single continuous experience. The transformation feels physical. That's the difference between reading a theorem and having a proof you can interact with.

---

## Plotting Was the Hardest Part

Four specific challenges in order of difficulty:

**`density=True`** — not obvious why this is required until you see the histogram and Gaussian curve on completely different scales without it. The histogram shows counts (hundreds), the Gaussian PDF shows density (fractions). They cannot be compared without normalisation.

**Overlaying curves** — matplotlib layers plots automatically. Each `ax.plot` and `ax.hist` call adds to the same axes. This felt implicit and confusing at first. The mental model that helped: think of each call as placing a transparent layer on the same canvas.

**Subplots** — `axes[0]` vs `axes[0, 0]` depending on 1D vs 2D grid. The indexing convention takes getting used to.

**The slider** — most challenging by far. The `on_changed` callback pattern is not intuitive. The key insight that made it work: `ax.clear()` before redrawing. Without clearing, slider moves stack histograms on top of each other and the plot becomes unreadable. Once `ax.clear()` was understood as "reset the canvas before each redraw," the slider logic became straightforward.

---

## The Standard Error Formula

```
σ_mean = σ / √n
```

This is not just a formula — it explains why sample size matters. Doubling n does not halve the uncertainty, it reduces it by `1/√2`. To halve uncertainty you need to quadruple n. This is why data collection is expensive — precision improves slowly with sample size.

---

## CLT Limitations — What It Doesn't Guarantee

CLT requires finite mean and variance. Distributions with infinite variance (Cauchy distribution) do not satisfy CLT — their sample means never converge to Gaussian. This is a real edge case in heavy-tailed financial data where CLT-based assumptions break down.

CLT describes the distribution of sample means — not individual samples. Raw samples from an Exponential distribution will always look Exponential regardless of how many you collect.