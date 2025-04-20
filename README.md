# heart-disease-app
 
# Heart Disease Prediction App

A Machine Learning web app built with **Streamlit** to predict the risk of heart disease based on medical input features. This app uses a **Random Forest Classifier** trained on the UCI Heart Disease dataset.

---

## 🚀 Demo

🔗 Live App: [Click here to open the app](https://heart-disease-predictionapp.streamlit.app/)  
🧠 Model: Random Forest Classifier  
📊 Dataset: [UCI Heart Disease](https://www.kaggle.com/datasets/rishidamarla/heart-disease-prediction)

---

## 💻 Features

- Interactive web UI using Streamlit
- Predicts heart disease risk based on:
  - Age, sex, cholesterol, blood pressure, etc.
- Displays:
  - Risk status (Low/High)
  - Prediction probability
- Responsive and mobile-friendly

---

## 📁 Project Structure
heart-disease-app/
- app.py                     # Streamlit app
- heart_disease_model.pkl    # Trained ML model
- scaler.pkl                 # Fitted scaler
- requirements.txt           # Python dependencies
- README.md                  # Project overview

---

## 🧠 Model Details

- **Model**: Random Forest Classifier
- **Training Dataset**: 303 samples, 13 features
- **Features Used**:
  - Age, Sex, Chest Pain Type, Resting BP, Cholesterol, FBS, etc.
- **Evaluation**:
  - Accuracy ~85–90%
  - ROC AUC used for threshold analysis

---

## 🛠 Installation (For Local Use)

```bash
# Clone the repo
git clone https://github.com/rushabh1605/heart-disease-app.git
cd heart-disease-predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py