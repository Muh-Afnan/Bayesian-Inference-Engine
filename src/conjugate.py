from src.bayes import factorial

class BetaBinomial:
    def __init__(self, alpha: float = 1, beta: float = 1):
        """
        Beta prior with parameters alpha, beta.
        Uniform prior: alpha=1, beta=1
        """
        self.alpha = alpha
        self.beta = beta
        self.factorial = factorial().factorial

    def update(self, heads: int, tails: int) -> "BetaBinomial":
        """
        Conjugate update — exact closed form.
        new_alpha = alpha + heads
        new_beta  = beta + tails
        """
        new_alpha = self.alpha + heads
        new_beta = self.beta + tails
        return BetaBinomial(new_alpha, new_beta)

    def mean(self) -> float:
        """Expected value of Beta distribution: alpha / (alpha + beta)"""
        return self.alpha / (self.alpha + self.beta)

    def pdf(self, p: float) -> float:
        """Beta PDF at p"""
        b = self.factorial(self.alpha - 1) * self.factorial(self.beta - 1) / self.factorial(self.alpha + self.beta - 1)
        return (p ** (self.alpha - 1)) * ((1 - p) ** (self.beta - 1)) / b

if __name__ == "__main__":
    print(BetaBinomial(1, 1).update(7, 3).mean())
    bb = BetaBinomial(8, 4)
    print(bb.pdf(0.6))
