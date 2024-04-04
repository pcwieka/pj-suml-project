import os
import pandas as pd


class Dataset:
    def __init__(self, filename, train=0.8, test=0.15, validation=0.05):
        self.full_dataset_path = os.path.join(os.path.curdir, 'datasets', filename)
        self.full_dataset = pd.read_csv(self.full_dataset_path)
        self.train_set = pd.DataFrame
        self.validate_set = pd.DataFrame
        self.test_set = pd.DataFrame

    def clean_missing_vals(self):
        self.full_dataset.dropna(axis=0, inplace=True)

    def fill_missing_vals(self):
        for column in self.full_dataset.columns:
            self.full_dataset[column] = self.full_dataset[column].fillna().mean()

    def clean_outliers(self):
        q1 = self.full_dataset.quantile(0.25)
        q3 = self.full_dataset.quantile(0.75)
        iqr = q3-q1
        outliers = (self.full_dataset < (q1 - 1.5 * iqr)) | (self.full_dataset > (q3 + 1.5 * iqr))
        self.full_dataset = self.full_dataset[~outliers.any(axis=0)]

    def remove_columns(self, cols_to_remove):
        self.full_dataset.drop(cols_to_remove)

    def normalize(self, cols_to_normalize):
        for column in self.full_dataset.columns:
            if column in cols_to_normalize:
                self.full_dataset[column] = self.full_dataset[column]/self.full_dataset[column].abs().max()


