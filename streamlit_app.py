# streamlit_app.py
import streamlit as st
import pandas as pd
import joblib, json

st.title("🎬 Movie Revenue Prediction")

# Load artifacts
features = json.load(open("artifacts/feature_list.json"))["features"]
model = joblib.load("artifacts/rf_pipeline.joblib")

# Inputs
vals = {}
for f in features:
    vals[f] = st.number_input(f, value=0.0)
X = pd.DataFrame([vals])

# Predict
pred = model.predict(X)[0]
st.metric("Predicted Revenue", f"${pred:,.0f}")