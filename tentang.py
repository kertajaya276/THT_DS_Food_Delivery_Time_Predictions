import streamlit as st

def tampilkan_tentang():
    st.title("Tentang Saya")
    
    st.subheader("👨‍💻 Sang Nyoman Kertajaya")
    st.image("Sang Nyoman Kertajayaa.jpeg")
    st.write("""
    Perkenalkan, saya **Sang Nyoman Kertajaya** berasal dari Bali, Indonesia.
    
    Saat ini saya berdomisili dan bekerja di Jepang di sektor pertanian, sambil melanjutkan studi di **Universitas Terbuka**.
    
    Saya memiliki ketertarikan dalam bidang data dan saat ini sedang mengikuti program belajar di **Dibimbing.id** untuk melakukan *switch career* menjadi seorang **Data Scientist**.
    
    Salam kenal dan terima kasih telah mengunjungi proyek ini!
    """)
    
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

