import streamlit as st

def tampilkan_overview():
    st.title("Tentang Proyek")
    st.subheader("📦 Food Delivery Time Prediction")
    st.write("""
    Dalam industri layanan pengantaran (*delivery*), **durasi pengantaran** adalah faktor krusial yang memengaruhi **reputasi perusahaan** dan **kepuasan pelanggan**.

    Proyek ini bertujuan untuk:
    
    - Menganalisis faktor-faktor yang memengaruhi durasi pengantaran.
    - Mengembangkan model prediksi berbasis **machine learning** untuk memprediksi durasi pengantaran dengan akurat.
    
    Dengan alat bantu prediksi ini, perusahaan diharapkan dapat meningkatkan efisiensi pengiriman dan memberikan layanan yang lebih baik kepada pelanggan.
    """)
    
    st.subheader("🧠 Problem Statement")
    st.markdown("""
    1. Apa saja **faktor-faktor** yang memengaruhi variabel target `Delivery_Time_min`?
    2. Apakah bisa dikembangkan **model prediksi** yang mampu memprediksi `Delivery_Time_min` secara akurat?
    """)

    st.subheader("🎯 Goals")
    st.markdown("""
    - Mengidentifikasi variabel/faktor yang **mempengaruhi `Delivery_Time_min`**.
    - Mengembangkan **model prediksi** `Delivery_Time_min` dengan **performa yang andal dan akurat**.
    """)

