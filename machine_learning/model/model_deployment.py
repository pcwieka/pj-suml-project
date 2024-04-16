import os
import joblib
from sklearn.base import BaseEstimator


class ModelDeployment:

    def __init__(self, model: BaseEstimator):
        self.model = model

    def deploy(self):
        print("Deploying model...")
        self.save()

    def save(self, filename='final_model.pkl'):
        filepath = 'output/' + filename
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump(self.model, filepath)
        print(f"Model saved to {filepath}")
