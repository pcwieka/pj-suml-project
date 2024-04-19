import os
import joblib


def save_model(model, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    joblib.dump(model, filepath)
