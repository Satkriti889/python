import streamlit as st
import pandas as pd
import joblib

# Load model only
model = joblib.load('house_price_model.pkl')  

# App Title
st.title("🏠 House Price Prediction App")
st.markdown("Enter the details of the house to estimate its price.")

# Sidebar input fields
area = st.number_input("Area (in square feet)", min_value=100, max_value=20000, value=1000)
bedrooms = st.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5,6,7,8,9,10])
bathrooms = st.selectbox("Number of Bathrooms", [1, 2, 3, 4,5,6,7,8,9,10])
stories = st.selectbox("Number of Stories", [1, 2, 3, 4,5])

mainroad = st.radio("Is there access to Main Road?", ["Yes", "No"])
guestroom = st.radio("Is there a Guest Room?", ["Yes", "No"])
basement = st.radio("Is there a Basement?", ["Yes", "No"])
hotwaterheating = st.radio("Hot Water Heating Available?", ["Yes", "No"])
airconditioning = st.radio("Air Conditioning Available?", ["Yes", "No"])
parking = st.selectbox("Number of Parking Spaces", [0, 1, 2, 3, 4,5])
prefarea = st.radio("Is it a Preferred Area?", ["Yes", "No"])
furnishingstatus = st.selectbox("Furnishing Status", ["furnished", "semi-furnished", "unfurnished"])

# Mapping categorical input to encoded values
binary_map = {'Yes': 1, 'No': 0}
furnishing_map = {'furnished': 0, 'semi-furnished': 1, 'unfurnished': 2}

# Prepare input data
input_data = pd.DataFrame([{
    'area': area,
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'stories': stories,
    'mainroad': binary_map[mainroad],
    'guestroom': binary_map[guestroom],
    'basement': binary_map[basement],
    'hotwaterheating': binary_map[hotwaterheating],
    'airconditioning': binary_map[airconditioning],
    'parking': parking,
    'prefarea': binary_map[prefarea],
    'furnishingstatus': furnishing_map[furnishingstatus]
}])

# Predict button
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"🏡 Estimated House Price: ₹{prediction:,.2f}")
