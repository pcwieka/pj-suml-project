from kedro.pipeline import Pipeline, node
from .nodes import train_autogluon_model, evaluate_autogluon_model, validate_autogluon_model

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=train_autogluon_model,
            inputs=["train_set", "params:model"],
            outputs="trained_model",
            name="train_autogluon_model_node"
        ),
        node(
            func=evaluate_autogluon_model,
            inputs=["test_set", "trained_model", "params:model"],
            outputs=["eval_accuracy", "eval_conf_matrix", "eval_class_report"],
            name="evaluate_autogluon_model_node"
        ),
        node(
            func=validate_autogluon_model,
            inputs=["validate_set", "trained_model", "params:model"],
            outputs=["val_accuracy", "val_conf_matrix", "val_class_report"],
            name="validate_autogluon_model_node"
        )
    ])
