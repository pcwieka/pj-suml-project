from kedro.pipeline import Pipeline, node
from .nodes import save_model


def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=save_model,
            inputs=["trained_model", "params:trained_model_filepath"],
            outputs=None,
            name="save_model_node"
        )
    ])
