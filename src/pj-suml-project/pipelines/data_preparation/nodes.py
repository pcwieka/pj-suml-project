from sklearn.model_selection import train_test_split


def remove_columns(data, cols_to_remove):
    """

    Args:
        data: dataset to be cleaned
        cols_to_remove: columns to be removed

    Returns: cleaned dataset

    """
    data = data.copy()
    original_cols = data.shape[1]
    data = data.drop(cols_to_remove, axis=1)
    columns_after_removal = data.shape[1]
    print(f"Original columns: {original_cols}")
    print(f"Columns after removal: {columns_after_removal}")
    return data


def transform_text_values(data, cols_to_transform):
    """

    Args:
        data: dataset to be cleaned
        cols_to_transform: columns to be transformed

    Returns: transformed dataset

    """
    data = data.copy()
    for column, mapping in cols_to_transform.items():
        if column in data.columns:
            data[column] = data[column].replace(mapping)
    return data.infer_objects(copy=False)


def fill_missing_vals(data):
    """

    Args:
        data: dataset to be filled with missing values

    Returns: dataset with missing values filled

    """
    data = data.copy()
    missing_before = data.isnull().sum().sum()
    print(f"Missing values before: {missing_before}")
    for column in data.columns:
        data[column] = data[column].fillna(data[column].mean()
                                           if data[column].dtype in ['float64', 'int64']
                                           else data[column].mode()[0])
    missing_after = data.isnull().sum().sum()
    print(f"Missing values after: {missing_after}")

    return data


def clean_outliers(data):
    """

    Args:
        data: dataset to be cleaned

    Returns: dataset with cleaned outliers

    """
    data = data.copy()
    before_rows = data.shape[0]
    print(f"Clean outliers before rows: {before_rows}")
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    q1 = data[numeric_cols].quantile(0.25)
    q3 = data[numeric_cols].quantile(0.75)
    iqr = q3 - q1
    data = data[~((data[numeric_cols] < (q1 - 1.5 * iqr)) | (data[numeric_cols] > (q3 + 1.5 * iqr))).any(axis=1)]
    after_rows = data.shape[0]
    print(f"Clean outliers after rows: {after_rows}")
    return data


def normalize(data, cols_to_normalize):
    """

    Args:
        data: dataset to be normalized
        cols_to_normalize: columns to be normalized

    Returns: normalized dataset

    """
    data = data.copy()
    for column in cols_to_normalize:
        if column in data.columns:
            data[column] = data[column] / data[column].abs().max()
    return data


def split_data(data, params):
    """

    Args:
        data: dataset to split
        params: parameters for data splitting

    Returns: train, validate and test sets

    """
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
    """
    Args:
        data: report data to save
        output_path: output path file for saving data
    """
    data.to_csv(output_path, index=False)
