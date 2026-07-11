from src.bayes import BayesianInference
from src.conjugate import BetaBinomial
from src.visualizer import (
    plot_prior_likelihood_posterior,
    plot_sequential_updating,
    plot_beta_updating,
    plot_credible_interval
)

# Setup
prior = [0.25, 0.25, 0.25, 0.25]
hypotheses = [0.1, 0.5, 0.6, 0.9]
bi = BayesianInference(prior, hypotheses)

# 1. Prior, Likelihood, Posterior
likelihood = bi.likelihood(10, 7)
posterior = bi.update(10, 7)
plot_prior_likelihood_posterior(prior, likelihood, posterior, hypotheses)

# 2. Sequential updating
observations = [1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
plot_sequential_updating(observations, hypotheses, prior)

# 3. Beta updating
plot_beta_updating(7, 3)

# 4. Credible interval
plot_credible_interval(posterior, hypotheses, credibility=0.95)

# 5. Predict
predicted = bi.predict(10)
print(f"Expected heads in 10 future flips: {predicted:.2f}")