import os
from io import BytesIO
from pathlib import Path

import joblib
import pandas as pd
import requests
from sklearn.preprocessing import StandardScaler

model_url = os.getenv("CHAMPION_MODEL_URL")
model_path = Path("data/models/champion_model.pkl")

columns_transform = {
    "Gender": {"Male": 0, "Female": 1},
    "family_history_with_overweight": {"yes": 1, "no": 0},
    "FAVC": {"yes": 1, "no": 0},
    "SMOKE": {"yes": 1, "no": 0},
    "SCC": {"yes": 1, "no": 0},
    "CAEC": {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3},
    "CALC": {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3},
    "MTRANS": {"Public_Transportation": 0, "Walking": 1, "Automobile": 2, "Motorbike": 3, "Bike": 4}
}

def load_model():
    if model_url:
        response = requests.get(model_url)
        if response.status_code == 200:
            return joblib.load(BytesIO(response.content))
        else:
            raise ValueError(f"Error loading the model from {model_url}")
    else:
        if model_path.exists():
            return joblib.load(model_path)
        else:
            raise ValueError(f"Model file not found at {model_path}")

def preprocess(input_data):
    for column, mapping in columns_transform.items():
        input_data[column] = input_data[column].map(mapping)
    cols_to_normalize = ["Age", "Height", "Weight", "FCVC", "NCP", "CH2O", "FAF", "TUE"]
    scaler = StandardScaler()
    input_data[cols_to_normalize] = scaler.fit_transform(input_data[cols_to_normalize])
    return input_data

def predict(input_data):
    input_df = pd.DataFrame([input_data.dict()])
    preprocessed_data = preprocess(input_df)
    model = load_model()
    prediction = model.predict(preprocessed_data)
    return prediction[0]
