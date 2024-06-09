from kedro.pipeline import Pipeline, node
from .nodes import deploy_best_model

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=deploy_best_model,
            inputs=[
                "best_model",
                "trained_model",
                "eval_accuracy",
                "eval_conf_matrix",
                "eval_class_report",
                "params:deployment"
            ],
            outputs="deployed_model",
            name="deploy_best_model_node"
        )
    ])
