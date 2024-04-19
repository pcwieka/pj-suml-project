from sklearn.model_selection import train_test_split


def remove_columns(data, cols_to_remove):
    data = data.copy()
    return data.drop(cols_to_remove)


def transform_text_values(data, cols_to_transform):
    data = data.copy()
    for column, mapping in cols_to_transform.items():
        if column in data.columns:
            data[column] = data[column].replace(mapping)
    return data.infer_objects(copy=False)


def fill_missing_vals(data):
    data = data.copy()
    for column in data.columns:
        if data[column].dtype == 'float64' or data[column].dtype == 'int64':
            data[column] = data[column].fillna(data[column].mean())
        else:
            data[column] = data[column].fillna(data[column].mode()[0])
    return data


def clean_outliers(data):
    data = data.copy()
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    q1 = data[numeric_cols].quantile(0.25)
    q3 = data[numeric_cols].quantile(0.75)
    iqr = q3 - q1
    outliers = (data[numeric_cols] < (q1 - 1.5 * iqr)) | (
            data[numeric_cols] > (q3 + 1.5 * iqr))
    return data[~(outliers.any(axis=1))]


def normalize(data, cols_to_normalize):
    data = data.copy()
    for column in data.columns:
        if column in cols_to_normalize:
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
