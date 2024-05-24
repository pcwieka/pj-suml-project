from kedro.pipeline import Pipeline, node
from .nodes import compare_models, load_champion_metrics

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=load_champion_metrics,
            inputs=["params:deployment"],
            outputs=["champion_eval_accuracy", "champion_eval_conf_matrix", "champion_eval_class_report"],
            name="load_champion_metrics_node"
        ),
        node(
            func=compare_models,
            inputs=["eval_accuracy", "eval_conf_matrix", "eval_class_report",
                    "champion_eval_accuracy", "champion_eval_conf_matrix", "champion_eval_class_report"],
            outputs="best_model",
            name="compare_models_node"
        )
    ])
