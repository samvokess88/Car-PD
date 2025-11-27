import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("linear_reg_model.pkl")

st.title("Car Price Prediction Model")

st.write("Enter your car details:")

Distance_Km = st.number_input("Distance (Km)", value=20000)
Location_cat = st.number_input("Location Category Code", value=1)
Maker_cat = st.number_input("Maker Category Code", value=1)
Year_cat = st.number_input("Year Category Code", value=1)
Colour_cat = st.number_input("Colour Category Code", value=1)
Type_cat = st.number_input("Type Category Code", value=1)

# Prepare input for prediction
input_data = pd.DataFrame([{
    "Distance_Km": Distance_Km,
    "Location_cat": Location_cat,
    "Maker_cat": Maker_cat,
    "Year_cat": Year_cat,
    "Colour_cat": Colour_cat,
    "Type_cat": Type_cat
}])

if st.button("Predict"):
    result = model.predict(input_data)[0]
    st.success(f"Estimated Price: ₦{result:.2f} Million")
