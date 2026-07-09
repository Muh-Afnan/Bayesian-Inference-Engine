class BayesianInference:
    def __init__(self, prior: list[float], hypotheses: list[float]):
        """
        prior: probability for each hypothesis
        hypotheses: possible values of the parameter (e.g. p=0.1, 0.2, ..., 1.0)
        """

    def likelihood(self, data: int, n: int, h: float) -> float:
        """
        Binomial likelihood: P(data heads | n flips, hypothesis h)
        """

    def update(self, data: int, n: int) -> list[float]:
        """
        Apply Bayes theorem. Update posterior given observed data.
        Returns new posterior.
        """

    def predict(self, n_future: int) -> float:
        """
        Posterior predictive: expected number of heads in n_future flips.
        """