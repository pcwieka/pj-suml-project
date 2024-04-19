from kedro.pipeline import Pipeline, node

from .nodes import split_data, remove_columns, transform_text_values, fill_missing_vals, clean_outliers, normalize


def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=remove_columns,
            name="remove_columns_node",
            inputs=["obesity_data", "params:cleaning.cols_to_remove"],
            outputs="dataset_columns_removed"
        ),
        node(
            func=transform_text_values,
            name="transform_text_values_node",
            inputs=["dataset_columns_removed", "params:cleaning.cols_to_transform"],
            outputs="dataset_columns_transformed",
        ),
        node(
            func=fill_missing_vals,
            name="fill_missing_vals_node",
            inputs=["dataset_columns_transformed"],
            outputs="dataset_filled_missing_vals",
        ),
        node(
            func=clean_outliers,
            name="clean_outliers_node",
            inputs=["dataset_filled_missing_vals"],
            outputs="dataset_cleaned_outliers",
        ),
        node(
            func=normalize,
            name="normalize_node",
            inputs=["dataset_cleaned_outliers", "params:cleaning.cols_to_normalize"],
            outputs="dataset_normalized",
        ),
        node(
            func=split_data,
            name="split_data_node",
            inputs=["dataset_normalized", "params:splitting"],
            outputs=["train_set", "test_set", "validate_set"]
        ),
        node(
            func=lambda x: x,
            inputs="dataset_normalized",
            outputs="dataset_normalized_csv",
            name="save_normalized_data_node"
        )
    ])
