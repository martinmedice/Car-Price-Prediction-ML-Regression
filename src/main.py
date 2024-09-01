import pickle
import pandas as pd
import streamlit as st

# Page config
st.set_page_config(
    page_title='Car Price Calculator',
    page_icon="../Car-Price-Prediction-ML-Regression/images/top_icon.png")

# Page title
st.markdown("<h1 style='text-align: center;'>Car Price Calculator</h1>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("../Car-Price-Prediction-ML-Regression/images/car_sales.jpg", width=300)

# User input - using columns to make layout more compact
col1, col2, col3 = st.columns(3)

with col1:
    year = st.slider("Car Year", min_value=1950, max_value=2020, value=2024, step=1)
    cylinders = st.selectbox("Number of Cylinders", 
                             ['12 cylinders', '10 cylinders', '8 cylinders', 
                              '6 cylinders', '5 cylinders', '4 cylinders', 
                              '3 cylinders', 'other'])
    fuel = st.selectbox("Fuel Type", ['gas', 'diesel', 'electric', 'hybrid', 'other'])
    drive = st.selectbox("Drive Type", ['4wd', 'fwd', 'rwd'])

with col2:
    odometer = st.number_input("Odometer [Kms]", min_value=0, max_value=1_000_000, value=0, step=1000)
    condition = st.selectbox("Car Conditions", ['excellent', 'fair', 'good', 'like new', 'new', 'salvage'])
    transmission = st.selectbox("Transmission", ['manual', 'automatic', 'other'])

with col3:
    manufacturer = st.selectbox("Manufacturer", 
                                ['Other', 'acura', 'audi', 'bmw', 'buick', 'cadillac', 
                                 'chevrolet', 'chrysler', 'dodge', 'ford', 'gmc', 
                                 'honda', 'hyundai', 'infiniti', 'jeep', 'kia', 
                                 'lexus', 'lincoln', 'mazda', 'mercedes-benz', 
                                 'nissan', 'ram', 'subaru', 'toyota', 'volkswagen'])
    type_grouped = st.selectbox("Car Type", ['car', 'SUV', 'truck/pickup'])
    color_grouped = st.selectbox("Color of the vehicle", 
                                 ['black', 'blue', 'grey', 'other', 'red', 'silver', 'white'])

# Function to create the model input
def create_input_dataframe(year, odometer, condition, cylinders, fuel, transmission, drive, 
                           manufacturer, type_grouped, color_grouped):
    input_data = {
        'year': [year],
        'odometer': [odometer],
        'condition': [condition],
        'cylinders': [cylinders],
        'fuel': [fuel],
        'transmission': [transmission],
        'drive': [drive],
        'manufacturer_grouped': [manufacturer],
        'type_grouped': [type_grouped],
        'color_grouped': [color_grouped]
    }
    return pd.DataFrame(input_data)

# Predict after pressing the button
if st.button("CALCULATE PRICE"):
    input_df = create_input_dataframe(year, odometer, condition, cylinders, fuel, 
                                      transmission, drive, manufacturer, type_grouped, color_grouped)
    
    # Load Model
    with open('../Car-Price-Prediction-ML-Regression/models/model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    
    # Predict using the model
    predicted_price = model.predict(input_df)
    
    # Showing the result
    st.success(f"The estimated price for the car is: 💰${predicted_price[0]:,.2f}")
