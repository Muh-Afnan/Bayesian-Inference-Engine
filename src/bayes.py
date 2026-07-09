
class BayesianInference:
    def __init__(self, prior: list[float], hypotheses: list[float]):
        """
        prior: probability for each hypothesis
        hypotheses: possible values of the parameter (e.g. p=0.1, 0.2, ..., 1.0)
        """
        self.prior = prior
        self.hypotheses = hypotheses

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def comibniation(self, n: int, k: float)->float:
        n_fact = self.factorial(n)
        r_fact = self.factorial(k)
        return n_fact / ((n_fact-r_fact) * r_fact)
    
    def likelihood(self, data: int, n: int) -> list[float]:
        """
        Binomial likelihood: P(data heads | n flips, hypothesis h)
        """
        likli = []
        for item in self.prior:
            item_like = self.comibniation(n=n,k=data) * (item)**data *(1-item)**(n-data)
            likli.append(item_like)
        return likli
    
    def norm_constant(self, likelihood_data:list[int|float])->list[float]:
        constant = []
        for single_liklihood, single_prior in zip(likelihood_data, self.prior):
            constant += single_liklihood * single_prior
        return constant


    def update(self, data: int, n: int) -> list[float]:
        """
        Apply Bayes theorem. Update posterior given observed data.
        Returns new posterior.
        """
        liklihood_array = self.likelihood(data,n)
        constant = self.norm_constant(liklihood_array)
        result_array = []
        for single_likli,prior in zip(liklihood_array, self.prior):
            result = (single_likli * prior) / constant
            result_array.append(result)
        return result_array



    def predict(self, n_future: int) -> float:
        """
        Posterior predictive: expected number of heads in n_future flips.
        """
    
if __name__ == "__main__":
    bi = BayesianInference([0.25,0.25,0.25,0.25], [0.1,0.5,0.6,0.9])
    print(bi.update(7, 10))