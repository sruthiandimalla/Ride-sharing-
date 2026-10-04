import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Ola Fare Prediction", page_icon="🚖")

st.title("🚖 Ola Ride Fare Prediction")
st.write("Enter ride details to predict fare")

# Load Model
model = pickle.load(open("model.pkl", "rb"))

# ----------- STRING INPUTS -------------

pickup_lat = st.number_input("Pickup Latitude")
pickup_lng = st.number_input("Pickup Longitude")
drop_lat = st.number_input("Drop Latitude")
drop_lng = st.number_input("Drop Longitude")
distance_km = st.number_input("Distance (KM)")
surge_multiplier = st.number_input("Surge Multiplier")
estimated_eta_min = st.number_input("Estimated ETA (Minutes)")

# STRING Inputs
time_of_day = st.selectbox("Time of Day",
                           ["Morning", "Afternoon", "Evening", "Night"])

day_type = st.selectbox("Day Type",
                        ["Weekday", "Weekend"])

traffic_level = st.selectbox("Traffic Level",
                             ["Low", "Medium", "High"])

vehicle_type = st.selectbox("Vehicle Type",
                            ["Mini", "Sedan", "SUV"])

driver_availability = st.selectbox("Driver Availability",
                                   ["Available", "Not Available"])

service_provider = st.selectbox("Service Provider",
                                ["Ola", "Uber"])

# ----------- MAPPING STRINGS TO NUMBERS -------------

time_map = {"Morning": 0, "Afternoon": 1, "Evening": 2, "Night": 3}
day_map = {"Weekday": 0, "Weekend": 1}
traffic_map = {"Low": 0, "Medium": 1, "High": 2}
vehicle_map = {"Mini": 0, "Sedan": 1, "SUV": 2}
driver_map = {"Available": 1, "Not Available": 0}
service_map = {"Ola": 0, "Uber": 1}

# Predict Button
if st.button("Predict Fare"):

    input_data = np.array([[pickup_lat, pickup_lng, drop_lat, drop_lng,
                            distance_km,
                            time_map[time_of_day],
                            day_map[day_type],
                            traffic_map[traffic_level],
                            vehicle_map[vehicle_type],
                            surge_multiplier,
                            estimated_eta_min,
                            driver_map[driver_availability],
                            service_map[service_provider]]])

    prediction = model.predict(input_data)

    st.success(f"💰 Estimated Fare: ₹ {prediction[0]:.2f}")
