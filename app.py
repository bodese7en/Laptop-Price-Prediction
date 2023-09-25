import streamlit as st
import util  
import json

with open("columns.json", "r") as f:
     __data_columns = json.load(f)['data_columns']

# Set a title for Streamlit app
st.title("Laptop Price Prediction App")

# Input widgets for user to provide laptop features
inches = st.number_input("Inches(10-20)", min_value=10.0, max_value=20.0, value=15.6)
ram_gb = st.number_input("RAM (0-64)", min_value=2, max_value=64, value=8)
ssd = st.number_input("SSD(0-2000)", min_value=0, max_value=2000, value=256)
hdd = st.number_input("HDD(0-2000)", min_value=0, max_value=2000, value=1000)
flash_storage = st.number_input("Flash_Storage(0-512)", min_value=0, max_value=512, value=0)
touchscreen = st.number_input("Touchscreen(0='No', 1='Yes')")

# Dropdowns for categorical features (company, type_name, cpu_brand, gpu_brand)
company = st.selectbox("Company", __data_columns[6:][:19])
type_name = st.selectbox("Type Name", __data_columns[25:][:6])
cpu_brand = st.selectbox("CPU Brand", __data_columns[31:][:5])
gpu_brand = st.selectbox("GPU Brand", __data_columns[36:])



# Button to trigger prediction
if st.button("Predict Price"):
    # Call prediction function from the util module
    predicted_price = util.predict_laptop_price(
        inches, ram_gb, ssd, hdd, flash_storage, touchscreen, company, type_name, cpu_brand, gpu_brand
    )

    # Display the predicted price
    st.write(f"Predicted Price: €{predicted_price:.2f}")
