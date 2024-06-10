import os
import time
import requests
import streamlit as st

# API endpoint URL
API_URL = os.getenv("API_URL")

# Function to make prediction request
def get_prediction(data):
    """
    Args:
        data: data to predict for

    Returns: response from the server with prediction
    """
    response = requests.post(API_URL + "/predict", json=data)
    if response.status_code == 200:
        return response.json()
    st.error(f"Error: {response.status_code}")
    return None

# Streamlit application
def main():
    st.set_page_config(
        page_title="Obesity Level Prediction",
        page_icon=":weight_lifter:",
        layout="centered"
    )

    # Custom CSS to style the app
    st.markdown("""
        <style>
        .main {
            background-color: #f0f2f6;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
        }
        .stSelectbox, .stSlider, .stNumberInput, .stTextInput {
            border: 1px solid #ccc;
            padding: 10px;
            font-size: 16px;
            background-color: #f9f9f9;
            border-radius: 5px;
        }
        .stTitle {
            color: #ff6347;
            font-weight: bold;
        }
        .stHeader {
            color: #ff6347;
        }
        .result {
            font-size: 24px;
            font-weight: bold;
            color: #ff6347;
            text-align: center;
            margin-top: 20px;
            padding: 10px;
            border: 2px solid #ff6347;
            border-radius: 10px;
            background-color: #fff;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Predict Your Obesity Level")

    st.image("https://depthtraining.b-cdn.net/wp-content/uploads/2020/02/healthy-habits.jpg", use_column_width=True)

    # User input form
    with st.form("obesity_form"):
        st.subheader("Enter your details:")
        gender = st.selectbox("Gender", ["Male", "Female"])
        age = st.slider("Age", 1, 100)
        height = st.text_input("Height (m)", value="1.75")
        weight = st.number_input("Weight (kg)", step=1, value=60)
        family_history = st.selectbox("Family History with Overweight", ["yes", "no"])
        favc = st.selectbox("Frequent Consumption of High Caloric Food", ["yes", "no"])
        fcvc = st.slider("Frequency of Consumption of Vegetables", 1, 3)
        ncp = st.slider("Number of Main Meals", 1, 4)
        caec = st.selectbox("Consumption of Food Between Meals", ["no", "Sometimes", "Frequently", "Always"])
        smoke = st.selectbox("Smoke", ["yes", "no"])
        ch2o = st.slider("Daily Water Intake (liters)", 1, 3)
        scc = st.selectbox("Calories Consumption Monitoring", ["yes", "no"])
        faf = st.slider("Physical Activity Frequency (times per week)", 0, 7)
        tue = st.slider("Time Using Technology Devices (hours per day)", 0, 24)
        calc = st.selectbox("Consumption of Alcohol", ["no", "Sometimes", "Frequently", "Always"])
        mtrans = st.selectbox("Transportation Used", ["Public_Transportation", "Walking", "Automobile", "Motorbike", "Bike"])

        # Submit button
        submitted = st.form_submit_button("Predict")

    if submitted:
        # Validate height input to ensure it only contains a dot ('.') as the decimal separator
        try:
            height = float(height.replace(",", "."))
        except ValueError:
            st.error("Invalid height value. Please use a dot ('.') as the decimal separator.")
            return

        # Show loading spinner while waiting for the response
        with st.spinner('Waiting for prediction...'):
            # Prepare the input data
            input_data = {
                "Gender": gender,
                "Age": age,
                "Height": height,
                "Weight": int(weight),
                "family_history_with_overweight": family_history,
                "FAVC": favc,
                "FCVC": fcvc,
                "NCP": ncp,
                "CAEC": caec,
                "SMOKE": smoke,
                "CH2O": ch2o,
                "SCC": scc,
                "FAF": faf,
                "TUE": tue,
                "CALC": calc,
                "MTRANS": mtrans
            }

            # Get prediction
            prediction = get_prediction(input_data)
            if prediction:
                time.sleep(0.2)
                st.markdown(f'<div class="result">Predicted Obesity Level: {prediction["NObeyesdad"]}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
