from matplotlib import pyplot as plt
from bayes import BayesianInference
from conjugate import BetaBinomial


def plot_prior_likelihood_posterior(prior, likelihood, posterior, hypotheses):
    likelihood_norm = [l / sum(likelihood) for l in likelihood]
    x = list(range(len(hypotheses)))
    width = 0.2

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar([i - width for i in x], prior, width=width, label="Prior")
    ax.bar(x, likelihood_norm, width=width, label="Likelihood (normalised)")
    ax.bar([i + width for i in x], posterior, width=width, label="Posterior")

    ax.set_xticks(x)
    ax.set_xticklabels(hypotheses)
    ax.set_xlabel("Hypotheses")
    ax.set_ylabel("Probability")
    ax.set_title("Prior, Likelihood, and Posterior")
    ax.legend()
    plt.tight_layout()
    plt.show()


def plot_sequential_updating(observations, hypotheses, prior):
    baye = BayesianInference(prior, hypotheses)
    heads = 0
    tails = 0
    history = []
    for obs in observations:
        if obs == 1:
            heads += 1
        else:
            tails += 1
        posterior = baye.update(heads + tails, heads)
        history.append(posterior)

    fig, ax = plt.subplots(figsize=(10, 6))
    for j, h in enumerate(hypotheses):
        y = [history[i][j] for i in range(len(observations))]
        ax.plot(range(1, len(observations) + 1), y, label=f"Hypothesis {h}")
    ax.set_xlabel("Flip Number")
    ax.set_ylabel("Posterior Probability")
    ax.legend()
    ax.set_title("Sequential Updating of Posterior Probabilities")
    plt.tight_layout()
    plt.show()


def plot_beta_updating(heads: int, tails: int):
    beta_binomial = BetaBinomial(1, 1)
    updated_beta = beta_binomial.update(heads, tails)

    p_values = [i / 100 for i in range(101)]
    prior_pdf = [beta_binomial.pdf(p) for p in p_values]
    posterior_pdf = [updated_beta.pdf(p) for p in p_values]

    plt.figure(figsize=(10, 6))
    plt.plot(p_values, prior_pdf, label="Prior PDF (Beta(1,1))", color="blue")
    plt.plot(
        p_values,
        posterior_pdf,
        label=f"Posterior PDF (Beta({updated_beta.alpha},{updated_beta.beta}))",
        color="orange",
    )
    plt.title(f"Beta-Binomial Updating: {heads} Heads and {tails} Tails")
    plt.xlabel("Probability of Success (p)")
    plt.ylabel("Density")
    plt.legend()
    plt.grid()
    plt.show()


def plot_credible_interval(posterior, hypotheses, credibility=0.95):
    sorted_indices = sorted(
        range(len(posterior)), key=lambda i: posterior[i], reverse=True
    )
    cumulative_prob = 0.0
    credible_set = []

    for i in sorted_indices:
        cumulative_prob += posterior[i]
        credible_set.append(hypotheses[i])
        if cumulative_prob >= credibility:
            break
    fig, ax = plt.subplots(figsize=(10, 6))
    x = list(range(len(hypotheses)))
    ax.bar(x, posterior, color="lightblue", label="Posterior")
    for h in credible_set:
        idx = hypotheses.index(h)
        ax.bar(
            idx,
            posterior[idx],
            color="orange",
            label="Credible Interval" if h == credible_set[0] else "",
        )

    ax.set_xticks(x)
    ax.set_xticklabels(hypotheses)
    ax.set_title(f"{int(credibility * 100)}% Credible Interval")
    ax.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Example usage
    posterior = [2.2e-05, 0.3008, 0.5518, 0.1473]
    hypotheses = [0.1, 0.5, 0.6, 0.9]
    plot_credible_interval(posterior, hypotheses, 0.95)

    # plot_prior_likelihood_posterior(prior, likelihood, posterior, hypotheses)
    # plot_sequential_updating(observations, hypotheses, prior)
    # plot_beta_updating(7, 3)
    plot_credible_interval(posterior, hypotheses, credibility=0.95)
