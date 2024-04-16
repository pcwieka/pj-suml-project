

class DataCleaner:

    def __init__(self, dataset, cols_to_remove, cols_to_transform, cols_to_normalize):
        self.dataset = dataset
        self.cols_to_remove = cols_to_remove
        self.cols_to_transform = cols_to_transform
        self.cols_to_normalize = cols_to_normalize

    def clean_data(self):
        self.remove_columns(self.cols_to_remove)
        self.transform_text_values(self.cols_to_transform)
        self.fill_missing_vals()
        self.clean_outliers()
        self.normalize(self.cols_to_normalize)
        self.dataset.to_csv('output/cleaned_data.csv', index=False)

    def clean_missing_vals(self):
        self.dataset.dropna(axis=0, inplace=True)

    def fill_missing_vals(self):
        for column in self.dataset.columns:
            if self.dataset[column].dtype == 'float64' or self.dataset[column].dtype == 'int64':
                self.dataset[column] = self.dataset[column].fillna(self.dataset[column].mean())
            else:
                self.dataset[column] = self.dataset[column].fillna(self.dataset[column].mode()[0])

    def clean_outliers(self):
        numeric_cols = self.dataset.select_dtypes(include=['float64', 'int64']).columns
        q1 = self.dataset[numeric_cols].quantile(0.25)
        q3 = self.dataset[numeric_cols].quantile(0.75)
        iqr = q3 - q1
        outliers = (self.dataset[numeric_cols] < (q1 - 1.5 * iqr)) | (
                self.dataset[numeric_cols] > (q3 + 1.5 * iqr))
        self.dataset = self.dataset[~(outliers.any(axis=1))]

    def remove_columns(self, cols_to_remove):
        self.dataset.drop(cols_to_remove)

    def normalize(self, cols_to_normalize):
        for column in self.dataset.columns:
            if column in cols_to_normalize:
                self.dataset[column] = self.dataset[column] / self.dataset[column].abs().max()

    def transform_text_values(self, trans_dict):
        for column, mapping in trans_dict.items():
            if column in self.dataset.columns:
                self.dataset[column].replace(mapping, inplace=True)
