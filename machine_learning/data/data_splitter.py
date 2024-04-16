import pandas as pd
from sklearn.model_selection import train_test_split


class DataSplitter:

    def __init__(self, dataset, train=0.8, test=0.15, validation=0.05, seed=50):
        self.full_dataset = dataset
        self.train_set = pd.DataFrame
        self.validate_set = pd.DataFrame
        self.test_set = pd.DataFrame
        self.train_proportion = train
        self.test_proportion = test
        self.validate_proportion = validation
        self.seed = seed

    def split_data(self):
        self.train_set, self.test_set = train_test_split(
            self.full_dataset,
            test_size=1 - self.train_proportion,
            random_state=self.seed
        )
        validate_size = self.validate_proportion / (self.validate_proportion + self.test_proportion)
        self.test_set, self.validate_set = train_test_split(
            self.test_set,
            test_size=validate_size,
            random_state=self.seed
        )

        self.train_set.to_csv('output/train_set.csv', index=False)
        self.test_set.to_csv('output/test_set.csv', index=False)
