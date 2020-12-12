# %% Import packages

import torch

from torch.distributions import Normal

from eeyore.constants import loss_functions
from eeyore.models import mlp

from bnn_mcmc_examples.mlp.noisy_xor.setting1.constants import dtype, mlp_dims

# %% Setup MLP model

hparams = mlp.Hyperparameters(dims=mlp_dims)

model = mlp.MLP(loss=loss_functions['binary_classification'], hparams=hparams, dtype=dtype)

prior_scale = 1.5

model.prior = Normal(
    torch.zeros(model.num_params(), dtype=model.dtype),
    torch.full([model.num_params()], prior_scale, dtype=model.dtype)
)