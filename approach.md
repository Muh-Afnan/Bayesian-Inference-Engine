# Approach

## Core Design — BayesianInference

`BayesianInference` takes a list of hypotheses and a prior and applies Bayes theorem discretely:

## Discrete Inference (bayes.py)
- Define hypotheses as possible coin biases
- Compute Binomial likelihood for each hypothesis
- Normalise using law of total probability
- Return posterior as updated belief distribution

## Conjugate Model (conjugate.py)
- Beta(α, β) as prior over continuous bias
- Conjugate update: α += heads, β += tails
- Mean = α / (α + β)
- PDF computed from Beta formula using factorial

## Visualizer (visualizer.py)
- Grouped bar chart: prior vs likelihood vs posterior
- Line chart: sequential belief updating flip by flip
- Curve plot: Beta PDF sharpening with evidence
- Bar chart: credible interval highlighting