import os
import joblib
import requests
from io import BytesIO

def load_champion_metrics(deployment_params):
    model_url = os.getenv("MODEL_URL")

    if model_url:
        response = requests.get(f"{model_url}/champion_metrics.pkl")
        if response.status_code == 200:
            champion_metrics = joblib.load(BytesIO(response.content))
        else:
            return 0.0, [], "No previous champion model found."
    else:
        if not os.path.exists(deployment_params["metrics_filepath"]):
            return 0.0, [], "No previous champion model found."
        champion_metrics = joblib.load(deployment_params["metrics_filepath"])

    return champion_metrics['accuracy'], champion_metrics['conf_matrix'], champion_metrics['class_report']

def compare_models(eval_accuracy, eval_conf_matrix, eval_class_report, champion_eval_accuracy,
                   champion_eval_conf_matrix, champion_eval_class_report):
    # Print metrics for challenger
    print("Challenger Model Metrics:")
    print(f"Accuracy: {eval_accuracy}")
    print(f"Confusion Matrix:\n{eval_conf_matrix}")
    print(f"Classification Report:\n{eval_class_report}")

    # Print metrics for champion
    print("\nChampion Model Metrics:")
    print(f"Accuracy: {champion_eval_accuracy}")
    print(f"Confusion Matrix:\n{champion_eval_conf_matrix}")
    print(f"Classification Report:\n{champion_eval_class_report}")

    model_accuracy = float(eval_accuracy)
    champion_accuracy = float(champion_eval_accuracy)

    print(f"Challenger Accuracy: {model_accuracy}")
    print(f"Champion Accuracy: {champion_accuracy}")

    if model_accuracy > champion_accuracy:
        print(f"Challenger model is better than champion model.")
        return "trained_model"
    else:
        print(f"Current champion model is better than challenger model.")
        return "current_champion"
