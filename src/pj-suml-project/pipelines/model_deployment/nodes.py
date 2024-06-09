import os
import joblib
import requests

def save_model_locally(model, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    joblib.dump(model, filepath)

def save_model_metrics_locally(metrics, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    joblib.dump(metrics, filepath)

def save_model_remotely(model, model_url):
    with open("temp_model.pkl", "wb") as temp_file:
        joblib.dump(model, temp_file)
    with open("temp_model.pkl", "rb") as temp_file:
        response = requests.post(f"{model_url}/upload", files={"file": temp_file})
    if response.status_code == 200:
        os.remove("temp_model.pkl")
    else:
        raise ValueError(f"Error uploading the model to {model_url}")

def save_model_metrics_remotely(metrics, model_url):
    with open("temp_metrics.pkl", "wb") as temp_file:
        joblib.dump(metrics, temp_file)
    with open("temp_metrics.pkl", "rb") as temp_file:
        response = requests.post(f"{model_url}/upload_metrics", files={"file": temp_file})
    if response.status_code == 200:
        os.remove("temp_metrics.pkl")
    else:
        raise ValueError(f"Error uploading the metrics to {model_url}")

def deploy_best_model(best_model, trained_model, eval_accuracy, eval_conf_matrix, eval_class_report, deployment_params):
    model_url = os.getenv("MODEL_URL")

    if best_model == "trained_model":
        model_to_deploy = trained_model
        model_metrics = {
            "accuracy": eval_accuracy,
            "conf_matrix": eval_conf_matrix,
            "class_report": eval_class_report
        }

        if model_url:
            save_model_remotely(model_to_deploy, model_url)
            save_model_metrics_remotely(model_metrics, model_url)
        else:
            save_model_locally(model_to_deploy, deployment_params["model_filepath"])
            save_model_metrics_locally(model_metrics, deployment_params["metrics_filepath"])

        print("New trained model deployed as champion.")
    else:
        print("Nothing deployed. The trained model is worse than current champion. Champion model is already deployed.")

    return best_model
