from kedro.pipeline import Pipeline, node
from .nodes import train_model, predict_model, evaluate_model, validate_model


def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=train_model,
            inputs=["train_set", "params:model"],
            outputs="trained_model",
            name="train_model_node"
        ),
        node(
            func=predict_model,
            inputs=["test_set", "trained_model", "params:model"],
            outputs="predictions",
            name="predict_model_node"
        ),
        node(
            func=evaluate_model,
            inputs=["test_set", "predictions", "params:model"],
            outputs=["eval_accuracy", "eval_conf_matrix", "eval_class_report"],
            name="evaluate_model_node"
        ),
        node(
            func=validate_model,
            inputs=["validate_set", "trained_model", "params:model"],
            outputs=["val_accuracy", "val_conf_matrix", "val_class_report"],
            name="validate_model_node"
        )
    ])
