# %% Load packages

import copy

from joblib import Parallel, delayed

from eeyore.chains import ChainLists

from bnn_mcmc_examples.examples.mlp.mnist.constants import dtype, num_chains, num_classes, pred_iter_thres
from bnn_mcmc_examples.examples.mlp.mnist.datascanners import test_dataloader
from bnn_mcmc_examples.examples.mlp.mnist.model import model
from bnn_mcmc_examples.examples.mlp.mnist.prior.constants import sampler_output_run_paths
from bnn_mcmc_examples.inference import predict_multi_class

# %% Load chain lists

chain_lists = ChainLists.from_file(sampler_output_run_paths, keys=['sample'], dtype=dtype)

# %% Drop burn-in samples

for i in range(num_chains):
    chain_lists.vals['sample'][i] = chain_lists.vals['sample'][i][pred_iter_thres:]

# %% Compute and save predictive priors

Parallel(n_jobs=num_chains, prefer="threads")(
    delayed(predict_multi_class)(c, s, d, m, p1, p2, t)
    for c, s, d, m, p1, p2, t in zip(
        [num_classes for _ in range(num_chains)],
        chain_lists.vals['sample'],
        [copy.deepcopy(test_dataloader) for _ in range(num_chains)],
        [copy.deepcopy(model) for _ in range(num_chains)],
        [sampler_output_run_paths[k].joinpath('pred_prior_on_test.csv') for k in range(num_chains)],
        [sampler_output_run_paths[k].joinpath('pred_prior_on_test_num_dropped_samples.txt') for k in range(num_chains)],
        [dtype for _ in range(num_chains)]
    )
)
