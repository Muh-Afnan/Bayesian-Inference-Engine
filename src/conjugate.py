class BetaBinomial:
    def __init__(self, alpha: float = 1, beta: float = 1):
        """
        Beta prior with parameters alpha, beta.
        Uniform prior: alpha=1, beta=1
        """

    def update(self, heads: int, tails: int) -> "BetaBinomial":
        """
        Conjugate update — exact closed form.
        new_alpha = alpha + heads
        new_beta  = beta + tails
        """

    def mean(self) -> float:
        """Expected value of Beta distribution: alpha / (alpha + beta)"""

    def pdf(self, p: float) -> float:
        """Beta PDF at p"""