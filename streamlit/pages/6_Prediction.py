import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Customer Prediction",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Customer Subscription Prediction")

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "models" / "saved_models" / "best_model.pkl"
DATA_PATH = BASE_DIR / "data" / "raw" / "bank-full.csv"

# -----------------------------
# Load Model and Data
# -----------------------------
model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATA_PATH, sep=";")

# -----------------------------
# Input Form
# -----------------------------
st.subheader("Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 95, 35)
    balance = st.number_input("Balance", value=1000)
    duration = st.number_input("Call Duration (seconds)", value=200)

with col2:
    campaign = st.number_input("Campaign Contacts", value=1)
    previous = st.number_input("Previous Contacts", value=0)
    pdays = st.number_input("Days Since Last Contact", value=999)

# -----------------------------
# Simple Prediction
# -----------------------------
if st.button("Predict Subscription"):

    # Create a dummy feature vector with zeros
    X = pd.get_dummies(df.drop("y", axis=1), drop_first=True)

    input_data = pd.DataFrame(0, index=[0], columns=X.columns)

    # Fill numerical features
    for col, val in {
        "age": age,
        "balance": balance,
        "duration": duration,
        "campaign": campaign,
        "pdays": pdays,
        "previous": previous
    }.items():
        if col in input_data.columns:
            input_data[col] = val

    prediction = model.predict(input_data)[0]

    st.markdown("---")

    if prediction == 1:
        st.success("Customer is likely to subscribe to the term deposit.")
    else:
        st.error("Customer is unlikely to subscribe to the term deposit.")

st.info("This prediction uses the trained Random Forest model from the ML pipeline.")