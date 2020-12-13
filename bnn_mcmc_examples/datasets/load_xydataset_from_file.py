import torch

from torch.utils.data import DataLoader

from eeyore.datasets import XYDataset

def load_xydataset_from_file(path, dtype=torch.float32):
    dataset = XYDataset.from_file(path=path, dtype=dtype)
    dataloader = DataLoader(dataset, batch_size=len(dataset))
    return dataset, dataloader