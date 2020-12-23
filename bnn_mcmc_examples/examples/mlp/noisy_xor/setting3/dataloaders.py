# %% Import packages

from bnn_mcmc_examples.datasets import load_xydataset_from_file
from bnn_mcmc_examples.datasets.noisy_xor.data2.constants import test_data_path, training_data_path
from bnn_mcmc_examples.examples.mlp.noisy_xor.setting3.constants import dtype, mcmc_batch_size

# %% Load training dataloader

_, training_dataloader = load_xydataset_from_file(training_data_path, dtype=dtype, batch_size=mcmc_batch_size)

# %% Load test dataloader

_, test_dataloader = load_xydataset_from_file(test_data_path, dtype=dtype)