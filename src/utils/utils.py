from glob import glob
import os
import pandas as pd


def read_dataset(dataset_name):
    datasets = glob("../data/processed/*.csv")
    data_path = {os.path.basename(name).split(
        ".")[0]: name for name in datasets}
    return pd.read_csv(data_path[dataset_name])

