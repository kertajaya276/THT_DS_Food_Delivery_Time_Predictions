import streamlit as st
import pandas as pd
import cloudpickle
import matplotlib.pyplot as plt

def tampilkan_prediksi():
    # Load model
    with open("best_ridge_model.pkl", "rb") as f:
        model = cloudpickle.load(f)

    st.title("🚴‍♂️ Food Delivery Time Prediction")
    st.write("Prediksi durasi pengiriman makanan menggunakan Ridge Regression (Hypertuning).")

    # Sidebar info tambahan 
    st.sidebar.markdown("### ℹ️ Tentang Aplikasi")
    st.sidebar.info("""
    Aplikasi ini memprediksi estimasi durasi pengiriman makanan berdasarkan input pesanan dan kondisi pengiriman.
    
    Model: Ridge Regression
    """)

    # Input fitur dari user
    st.header("Masukkan Data Pesanan")

    distance = st.number_input("Jarak (km)", min_value=0.0, step=0.1)
    prep_time = st.number_input("Waktu persiapan (menit)", min_value=0, step=1)
    experience = st.number_input("Pengalaman kurir (tahun)", min_value=0, step=1)

    weather = st.selectbox("Cuaca", ["Clear", "Rainy", "Foggy", "Snowy", "Windy", ])
    traffic = st.selectbox("Tingkat Kemacetan", ["Low", "Medium", "High"])
    timeofday = st.selectbox("Waktu dalam sehari", ["Morning", "Afternoon", "Evening", "Night"])
    vehicle = st.selectbox("Jenis Kendaraan", ["Bike", "Scooter", "Car"])

    # DataFrame dari input user
    input_df = pd.DataFrame({
        "Distance_km": [distance],
        "Preparation_Time_min": [prep_time],
        "Courier_Experience_yrs": [experience],
        "Weather": [weather],
        "Traffic_Level": [traffic],
        "Time_of_Day": [timeofday],
        "Vehicle_Type": [vehicle]
    })

    st.subheader("📋 Ringkasan Input")
    st.dataframe(input_df)

    # Validasi input 
    if distance == 0.0 and prep_time == 0 and experience == 0:
        st.warning("⚠️ Masukkan nilai yang masuk akal sebelum prediksi.")
        return

    # Prediksi
    if st.button("Prediksi Durasi Pengiriman"):
        prediction = model.predict(input_df)
        waktu_prediksi = round(prediction[0], 2)

        # Tampilkan hasil prediksi
        st.success(f"⏰ Perkiraan durasi pengiriman: {waktu_prediksi} menit")

