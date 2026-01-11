import streamlit as st
import pandas as pd
import pickle

# Page Config
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

# Load Model
with open("car_model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("🚗 Car Price Prediction App")
st.markdown("Predict the **selling price of a car** using Machine Learning")

st.divider()

# Sidebar
st.sidebar.header("Enter Car Details")

year = st.sidebar.slider("Year of Purchase", 1995, 2024, 2015)
present_price = st.sidebar.number_input("Showroom Price (in Lakhs)", 0.0, 50.0, 5.0)
kms_driven = st.sidebar.number_input("Kilometers Driven", 0, 500000, 50000)

fuel_type = st.sidebar.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.sidebar.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.sidebar.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.sidebar.selectbox("Owner", [0, 1, 2, 3])

# Encoding
fuel_petrol = 1 if fuel_type == "Petrol" else 0
fuel_diesel = 1 if fuel_type == "Diesel" else 0

seller_individual = 1 if seller_type == "Individual" else 0
transmission_manual = 1 if transmission == "Manual" else 0

car_age = 2024 - year

# Prediction Button
if st.button("🔍 Predict Price"):
    input_data = pd.DataFrame([[
        present_price,
        kms_driven,
        owner,
        car_age,
        fuel_diesel,
        fuel_petrol,
        seller_individual,
        transmission_manual
    ]])

    prediction = model.predict(input_data)[0]

    st.success(f"💰 Estimated Car Price: **₹ {round(prediction, 2)} Lakhs**")

st.divider()

# Footer
st.markdown(
    "<center>Made with ❤️ using Streamlit</center>",
    unsafe_allow_html=True
)
