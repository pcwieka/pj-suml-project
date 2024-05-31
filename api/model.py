import joblib
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler

model_path = Path("data/models/champion_model.pkl")
try:
    model = joblib.load(model_path)
except Exception as e:
    raise ValueError(f"Error loading the model: {e}")

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
    prediction = model.predict(preprocessed_data)
    return prediction[0]
