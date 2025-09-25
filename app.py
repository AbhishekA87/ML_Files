
import streamlit as st
import joblib
import pandas as pd

st.title("📊 My ML Portfolio")

# Load model
model = joblib.load("models/model.pkl")

# User input
age = st.number_input("Age", 18, 70, 30)
distance = st.slider("Trip Distance", 1, 500, 50)

# Predict button
if st.button("Predict"):
    df = pd.DataFrame([[age, distance]], columns=["age", "distance"])
    result = model.predict(df)[0]
    st.success(f"Prediction: {result}")
