# %% Import packages

import numpy as np
import torch

from eeyore.kernels import NormalKernel
from eeyore.samplers import MetropolisHastings

from bnn_mcmc_examples.datasets.noisy_xor.data1.load_data import load_data
from bnn_mcmc_examples.mlp.noisy_xor.setting1.constants import (
    dtype, num_chains, num_epochs, num_burnin_epochs, verbose, verbose_step
)
from bnn_mcmc_examples.mlp.noisy_xor.setting1.metropolis_hastings.constants import sampler_output_path
from bnn_mcmc_examples.mlp.noisy_xor.setting1.model import model

# %% Load dataloader

_, dataloader = load_data(dtype=dtype)

# %% Setup proposal variance and proposal kernel for Metropolis-Hastings sampler

proposal_scale = np.sqrt(0.02)

kernel = NormalKernel(
    torch.zeros(model.num_params(), dtype=model.dtype),
    torch.full([model.num_params()], proposal_scale, dtype=model.dtype)
)

# %% Setup Metropolis-Hastings sampler

sampler = MetropolisHastings(model, theta0=model.prior.sample(), dataloader=dataloader, kernel=kernel)

# %% Benchmark Metropolis-Hastings sampler

sampler.benchmark(
    num_chains=num_chains,
    num_epochs=num_epochs,
    num_burnin_epochs=num_burnin_epochs,
    path=sampler_output_path,
    check_conditions=lambda chain, runtime : 0.15 <= chain.acceptance_rate() <= 0.45,
    verbose=verbose,
    verbose_step=verbose_step,
    print_acceptance=True,
    print_runtime=True
)
