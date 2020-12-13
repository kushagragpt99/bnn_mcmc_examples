# %% Import packages

import numpy as np

from pathlib import Path

from bnn_mcmc_examples.datasets import data_paths

# %% Define constants

data_base_name = 'data1'
training_data_name = 'training'
test_data_name = 'test'

data_path = data_paths['noisy_xor'].joinpath(data_base_name)
training_data_path = data_base_name.joinpath(training_data_name)
test_data_path = data_base_name.joinpath(test_data_name)
output_path = Path.home().joinpath('output', 'bnn_mcmc_examples', 'data', 'noisy_xor', data_base_name)

num_classes = 4
num_training_samples = np.repeat(125, num_classes)
num_test_samples = np.repeat(30, num_classes)
