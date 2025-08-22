import streamlit as st
import pandas as pd
import cloudpickle 

# === Load model ===
with open("best_ridge_model.pkl", "rb") as f:
    model = cloudpickle.load(f)

# === Judul Aplikasi ===
st.title("🚴‍♂️ Food Delivery Time Prediction")
st.write("Prediksi waktu pengiriman makanan menggunakan Ridge Regression (Hypertuning).")

# === Input fitur dari user ===
st.header("Masukkan Data Pesanan")

distance = st.number_input("Jarak (km)", min_value=0.0, step=0.1)
prep_time = st.number_input("Waktu persiapan (menit)", min_value=0, step=1)
experience = st.number_input("Pengalaman kurir (tahun)", min_value=0, step=1)

weather = st.selectbox("Cuaca", ["Sunny", "Rainy", "Cloudy", "Snowy"])
traffic = st.selectbox("Tingkat Kemacetan", ["Low", "Medium", "High"])
timeofday = st.selectbox("Waktu dalam sehari", ["Morning", "Afternoon", "Evening", "Night"])
vehicle = st.selectbox("Jenis Kendaraan", ["Bike", "Motorcycle", "Car"])

# === Buat DataFrame dari input user ===
input_df = pd.DataFrame({
    "Distance_km": [distance],
    "Preparation_Time_min": [prep_time],
    "Courier_Experience_yrs": [experience],
    "Weather": [weather],
    "Traffic_Level": [traffic],
    "Time_of_Day": [timeofday],
    "Vehicle_Type": [vehicle]
})

# === Prediksi ===
if st.button("Prediksi Waktu Pengiriman"):
    prediction = model.predict(input_df)
    st.success(f"⏰ Perkiraan waktu pengiriman: {prediction[0]:.2f} menit")
