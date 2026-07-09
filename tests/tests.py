def test_posterior_sums_to_one(): ...
def test_uniform_prior_with_all_heads(): ...      # should shift strongly toward p=1
def test_strong_prior_resists_evidence(): ...     # strong prior changes slowly
def test_sequential_updates_converge(): ...        # more data = narrower posterior
def test_beta_conjugate_update(): ...             # alpha/beta update correctly
def test_credible_interval_contains_truth(): ...  # 95% CI contains true p
def test_posterior_predictive(): ...              # prediction using full posterior