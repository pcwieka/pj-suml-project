from data_prep import Dataset


# prepare dataset
dataset = Dataset('ObesityDataSet.csv')
cols_to_normalize = []
cols_to_remove = []
dataset.remove_columns(cols_to_remove)
dataset.normalize(cols_to_normalize)
dataset.split_data()

# Use following for train/test/validate
# dataset.full_dataset
# dataset.train_set
# dataset.test_set
# dataset.validate_set

