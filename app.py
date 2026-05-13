import streamlit as st
import numpy as np
import pickle

# Load saved model and scalers
model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))
mx = pickle.load(open('minmaxscaler.pkl', 'rb'))

# Crop dictionary

crop_dict = {
    1: "rice",
    2: "maize",
    3: "chickpea",
    4: "kidneybeans",
    5: "pigeonpeas",
    6: "mothbeans",
    7: "mungbean",
    8: "blackgram",
    9: "lentil",
    10: "pomegranate",
    11: "grapes",
    12: "mango",
    13: "banana",
    14: "watermelon",
    15: "muskmelon",
    16: "apple",
    17: "orange",
    18: "papaya",
    19: "coconut",
    20: "cotton",
    21: "jute",
    22: "coffee"
}

# Streamlit page config
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="centered"
)

# Title
st.title("🌱 Crop Recommendation System")
st.write("Enter the soil and weather details to get the best crop recommendation.")

# User Inputs
N = st.text_input("Nitrogen (N)", placeholder="Enter Nitrogen value")
P = st.text_input("Phosphorus (P)", placeholder="Enter Phosphorus value")
K = st.text_input("Potassium (K)", placeholder="Enter Potassium value")
temp = st.text_input("Temperature (°C)", placeholder="Enter Temperature")
humidity = st.text_input("Humidity (%)", placeholder="Enter Humidity")
ph = st.text_input("pH Value", placeholder="Enter pH value")
rainfall = st.text_input("Rainfall (mm)", placeholder="Enter Rainfall")

# Predict Button
if st.button("Predict Crop"):

    try:
        # Convert inputs to float
        feature_list = [
            float(N),
            float(P),
            float(K),
            float(temp),
            float(humidity),
            float(ph),
            float(rainfall)
        ]
        single_pred = np.array(feature_list).reshape(1, -1)

        # Scale features
        mx_features = mx.transform(single_pred)
        sc_mx_features = sc.transform(mx_features)

        # Prediction
        prediction = model.predict(sc_mx_features)

        # Display result
        if prediction[0] in crop_dict:
            crop = crop_dict[prediction[0]]
            st.success(f"✅ {crop} is the best crop to be cultivated.")
        else:
            st.error("❌ Sorry, could not determine the best crop.")
    except ValueError:
        st.warning("⚠ Please enter valid numeric values.")