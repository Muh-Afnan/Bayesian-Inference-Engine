from src.bayes import BayesianInference
from src.conjugate import BetaBinomial


def test_posterior_sums_to_one():
    prior = [0.2, 0.5, 0.3]
    hypotheses = [0.1, 0.5, 0.9]
    baye = BayesianInference(prior, hypotheses)
    posterior = baye.update(10, 7)
    assert abs(sum(posterior) - 1) < 1e-6


def test_uniform_prior_with_all_heads():
    prior = [1 / 3, 1 / 3, 1 / 3]
    hypotheses = [0.1, 0.5, 0.9]
    baye = BayesianInference(prior, hypotheses)
    posterior = baye.update(10, 10)
    assert posterior[2] > posterior[1] > posterior[0]


def test_strong_prior_resists_evidence():
    prior = [0.9, 0.05, 0.05]
    hypotheses = [0.1, 0.5, 0.9]
    baye = BayesianInference(prior, hypotheses)
    posterior = baye.update(3, 2)  # only 3 flips — weak evidence
    assert posterior[0] > posterior[2]  # prior still dominates


def test_sequential_updates_converge():
    prior = [0.2, 0.5, 0.3]
    hypotheses = [0.1, 0.5, 0.9]
    baye = BayesianInference(prior, hypotheses)
    posterior1 = baye.update(10, 7)
    posterior2 = baye.update(20, 14)
    posterior3 = baye.update(100, 70)
    posterior4 = baye.update(200, 140)
    assert abs(posterior3[1] - posterior4[1]) < 0.05  # converges at large n


def test_beta_conjugate_update():
    beta_binomial = BetaBinomial(1, 1)
    updated_beta = beta_binomial.update(7, 3)
    assert abs(updated_beta.alpha - 8) < 1e-6
    assert abs(updated_beta.beta - 4) < 1e-6


def test_credible_interval_contains_truth():
    beta_binomial = BetaBinomial(1, 1)
    updated_beta = beta_binomial.update(7, 3)
    mean = updated_beta.mean()
    assert 0.6 < mean < 0.8


def test_posterior_predictive():
    prior = [0.2, 0.5, 0.3]
    hypotheses = [0.1, 0.5, 0.9]
    baye = BayesianInference(prior, hypotheses)
    posterior = baye.update(10, 7)
    expected_heads = baye.predict(5)
    assert 2 < expected_heads < 4
