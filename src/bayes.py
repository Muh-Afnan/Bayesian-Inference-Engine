class factorial:
    def factorial(self, n: int) -> int:
        n = int(n)
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)


class BayesianInference:
    def __init__(self, prior: list[float], hypotheses: list[float]):
        """
        prior: probability for each hypothesis
        hypotheses: possible values of the parameter (e.g. p=0.1, 0.2, ..., 1.0)
        """
        self.prior = prior
        self.hypotheses = hypotheses
        self.factorial = factorial().factorial

    def combination(self, n: int, k: int) -> float:
        return self.factorial(n) / (self.factorial(k) * self.factorial(n - k))

    def likelihood(self, n: int, k: int) -> list[float]:
        """
        Binomial likelihood: P(data heads | n flips, hypothesis h)
        """
        likli = []
        comb = self.combination(n, k)
        for item in self.hypotheses:
            item_like = comb * (item**k) * ((1 - item) ** (n - k))
            likli.append(item_like)
        return likli

    def norm_constant(self, likelihood_data: list[int | float]) -> float:
        sum = 0
        for single_liklihood, single_prior in zip(likelihood_data, self.prior):
            sum += single_liklihood * single_prior
        return sum

    def update(self, n: int, k: int) -> list[float]:
        """
        Apply Bayes theorem. Update posterior given observed data.
        Returns new posterior.
        """
        liklihood_array = self.likelihood(n, k)
        constant = self.norm_constant(liklihood_array)
        result_array = []
        for single_likli, prior in zip(liklihood_array, self.prior):
            result = (single_likli * prior) / constant
            result_array.append(result)
        return result_array

    def predict(self, n_future: int) -> float:
        """
        Posterior predictive: expected number of heads in n_future flips.
        """
        expected_heads = 0
        for h, p in zip(self.hypotheses, self.prior):
            expected_heads += n_future * h * p
        return expected_heads


if __name__ == "__main__":
    bi = BayesianInference([0.25, 0.25, 0.25, 0.25], [0.1, 0.5, 0.6, 0.9])
    print(bi.update(10, 7))
