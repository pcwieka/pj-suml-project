import wandb
from sklearn.model_selection import train_test_split


def remove_columns(data, cols_to_remove):
    data = data.copy()
    original_cols = data.shape[1]
    data = data.drop(cols_to_remove)
    wandb.log({"original_columns": original_cols, "columns_after_removal": data.shape[1]})
    return data


def transform_text_values(data, cols_to_transform):
    data = data.copy()
    for column, mapping in cols_to_transform.items():
        if column in data.columns:
            data[column] = data[column].replace(mapping)
    return data.infer_objects(copy=False)


def fill_missing_vals(data):
    data = data.copy()
    missing_before = data.isnull().sum().sum()
    for column in data.columns:
        data[column] = data[column].fillna(data[column].mean() if data[column].dtype in ['float64', 'int64'] else data[column].mode()[0])
    missing_after = data.isnull().sum().sum()
    wandb.log({"missing_before": missing_before, "missing_after": missing_after})
    return data


def clean_outliers(data):
    data = data.copy()
    before_rows = data.shape[0]
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    q1 = data[numeric_cols].quantile(0.25)
    q3 = data[numeric_cols].quantile(0.75)
    iqr = q3 - q1
    data = data[~((data[numeric_cols] < (q1 - 1.5 * iqr)) | (data[numeric_cols] > (q3 + 1.5 * iqr))).any(axis=1)]
    after_rows = data.shape[0]
    wandb.log({"rows_before": before_rows, "rows_after": after_rows})
    return data


def normalize(data, cols_to_normalize):
    data = data.copy()
    for column in cols_to_normalize:
        if column in data.columns:
            data[column] = data[column] / data[column].abs().max()
    return data


def split_data(data, params):
    train_ratio = params['train_ratio']
    test_ratio = params['test_ratio']
    validation_ratio = params['validation_ratio']
    seed = params['seed']
    train_set, test_set = train_test_split(
        data,
        test_size=1 - train_ratio,
        random_state=seed
    )
    validate_size = validation_ratio / (validation_ratio + test_ratio)
    test_set, validate_set = train_test_split(
        test_set,
        test_size=validate_size,
        random_state=seed
    )
    return train_set, test_set, validate_set


def save_data(data, output_path):
    data.to_csv(output_path, index=False)
