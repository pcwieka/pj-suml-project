import os
import joblib


def save_model(model, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    joblib.dump(model, filepath)


def save_model_metrics(metrics, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    joblib.dump(metrics, filepath)


def deploy_best_model(best_model, trained_model, eval_accuracy, eval_conf_matrix, eval_class_report, deployment_params):
    if best_model == "trained_model":
        model_to_deploy = trained_model
        model_metrics = {
            "accuracy": eval_accuracy,
            "conf_matrix": eval_conf_matrix,
            "class_report": eval_class_report
        }
        save_model(model_to_deploy, deployment_params["model_filepath"])
        save_model_metrics(model_metrics, deployment_params["metrics_filepath"])
        print("New trained model deployed as champion.")
    else:
        print("Nothing deployed. The trained model is worse than current champion. Champion model is already deployed.")

    return best_model
