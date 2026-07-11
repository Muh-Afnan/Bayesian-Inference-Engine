# Learnings

## Key Concepts

**Hypotheses vs prior** — hypotheses are the possible states of the world (coin bias = 0.1, 0.5, 0.6, 0.9). Prior is how much you believe each one before seeing data. They are parallel lists — index 0 of hypotheses pairs with index 0 of prior.

**Discrete vs continuous inference** — discrete inference forces the true parameter into predefined buckets. If the true bias is 0.63 and your buckets are [0.1, 0.5, 0.6, 0.9], you can never find it. Beta-Binomial removes this constraint entirely.

**Conjugate priors are elegant** — the Beta distribution is conjugate to the Binomial likelihood. This means the posterior has the same form as the prior. No integration, no approximation — just add heads to α and tails to β.

**Strong priors resist evidence, but not forever** — a 90% prior on h=0.1 is completely overwhelmed by 10 flips showing 7 heads. With small data (3 flips), the prior dominates. With large data, evidence always wins.

**Beta(1,1) is a flat line** — it encodes zero opinion, not zero probability. Every bias between 0 and 1 is equally likely. This is the correct uninformative starting point.

## Bugs Fixed

- **Combination formula wrong**: used `n_fact - r_fact` instead of `factorial(n - k)` in the denominator
- **Float passed to factorial**: type hint doesn't enforce types in Python — fixed with explicit `int(n)` cast
- **n and k swapped in update() call**: `update(7, 10)` passed data=7, n=10 correctly but the internal call had them reversed — caused `factorial(-3)` and infinite recursion
- **norm_constant used hypotheses values**: was multiplying likelihood by hypothesis values (0.1, 0.5 etc) instead of prior weights
- **likelihood looped over prior**: used `self.prior` instead of `self.hypotheses` in the Binomial formula — computed wrong probabilities entirely

## Surprises

- A 90% prior on h=0.1 cannot survive 10 flips of 7 heads — the likelihood ratio is too extreme
- Beta(1,1) looks like a uniform distribution because it is one — over the continuous interval [0,1]
- The normalising constant P(E) has no meaning on its own — it only exists to make the posterior sum to 1
- Sequential updating and single-batch updating with the same total evidence give identical posteriors — order doesn't matter, only counts do