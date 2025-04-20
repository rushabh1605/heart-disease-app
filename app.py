import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('heart_disease_model.pkl')
scaler = joblib.load('scaler.pkl')

st.set_page_config(page_title="Heart Disease Predictor", layout='centered')
st.title("❤️ Heart Disease Prediction App")
st.write("Fill in the details below to predict the risk of heart disease.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
cp = st.selectbox("Chest Pain Type (cp)", options=[0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=50, max_value=250, value=120)
chol = st.number_input("Serum Cholesterol in mg/dl (chol)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", options=[0, 1])
restecg = st.selectbox("Resting ECG Results (restecg)", options=[0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=60, max_value=250, value=150)
exang = st.selectbox("Exercise Induced Angina (exang)", options=[0, 1])
oldpeak = st.number_input("ST Depression Induced by Exercise (oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.selectbox("Slope of the Peak Exercise ST Segment (slope)", options=[0, 1, 2])
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (ca)", options=[0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia (thal)", options=[0, 1, 2, 3])

# Predict button
if st.button("Predict"):
    # Create input array
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    
    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction[0] == 1:
        st.error(f"⚠️ High risk of heart disease ({probability:.2%} probability). Please consult a doctor.")
    else:
        st.success(f"✅ Low risk of heart disease ({probability:.2%} probability). Keep up the healthy lifestyle!")