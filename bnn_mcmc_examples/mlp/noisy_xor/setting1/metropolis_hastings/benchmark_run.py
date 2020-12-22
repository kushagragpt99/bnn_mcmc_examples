# %% Import packages

from bnn_mcmc_examples.mlp.noisy_xor.setting1.constants import (
    num_chains, num_mcmc_epochs, num_mcmc_burnin_epochs, verbose, mcmc_verbose_step
)
from bnn_mcmc_examples.mlp.noisy_xor.setting1.metropolis_hastings.constants import sampler_output_path
from bnn_mcmc_examples.mlp.noisy_xor.setting1.metropolis_hastings.sampler import sampler

# %% Benchmark Metropolis-Hastings sampler

sampler.benchmark(
    num_chains=num_chains,
    num_epochs=num_mcmc_epochs,
    num_burnin_epochs=num_mcmc_burnin_epochs,
    path=sampler_output_path,
    check_conditions=lambda chain, runtime : 0.15 <= chain.acceptance_rate() <= 0.50,
    verbose=verbose,
    verbose_step=mcmc_verbose_step,
    print_acceptance=True,
    print_runtime=True
)
