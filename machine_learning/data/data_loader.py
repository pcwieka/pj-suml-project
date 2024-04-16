import os
import pandas as pd


class DataLoader:

    def __init__(self, filename):
        self.dataset_path = os.path.join(os.path.curdir, 'resources/datasets', filename)
        self.dataset = pd.read_csv(self.dataset_path)

    def get_dataset(self):
        return self.dataset
