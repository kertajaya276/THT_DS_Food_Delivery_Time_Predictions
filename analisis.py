import streamlit as st 
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def tampilkan_analisis():
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Business Understanding", "Data Understanding", "Data Preparation", "Exploratory Data Analysis & Insight", "Conclusion & Recommendation" ])

    with tab1:
        st.header("Business Understanding")
        st.image("https://cdn.builtin.com/cdn-cgi/image/f=auto,fit=cover,w=1200,h=635,q=80/sites/www.builtin.com/files/food-delivery-companies.jpg", width=700)
        with st.expander("Background"):
            st.write("""
                    Dalam industri delivery, durasi pengiriman adalah faktor yang krusial dalam industri dan waktu pengiriman yang cepat akan dapat meningkatkan reputasi perusahaan, sehingga untuk mempercepat durasi pengantaran akan dilakukan analisis faktor-faktor yang memengaruhi durasi pengantaran.
                     Selain itu akan, diperlukan alat bantu berbasis data yang mampu memprediksi durasi pengiriman secara akurat.
                     Dengan bantuan machine learning, prediksi durasi pengiriman dapat dilakukan untuk membantu meningkatkan layanan perusahaan dan meningkatkan kepuasan pelanggan dalam melakukan transaksi.
                     """)
        with st.expander("Problem"):
            st.write("""
                    1. Apa saja faktor yang mempengaruhi target variabel `Delivery_Time_min` dengan akurasi tinggi?
                    2. Apakah ada model prediksi yang dapat memprediksi target variabel `Delivery_Time_min` secara akurat?
                    """)
        with st.expander("Goals"):
            st.write("""
                    1. Mengindentifikasi variabel/faktor yang memengaruhi `Delivery_Time_min`
                    2. Mengembangkan model untuk memprediksi `Delivery_Time_min` dengan performa yang andal dan akurat.
                     """)

    with tab2:
        st.header("Data Understanding")
        st.image("https://static.vecteezy.com/system/resources/previews/002/076/168/non_2x/food-delivery-banner-design-flat-design-online-order-vector.jpg", width=700)
        data = pd.read_csv("Food_Delivery_Time_Prediction_cleaned-2.csv")
        st.write(data)

        with st.expander("Data Dictionary"):
            st.write('''
                    1. Order_ID : Identifikator unik untuk setiap pesanan.
                    2. Distance_km : Jarak pengiriman dalam kilometer.
                    3. Weather : Kondisi cuaca selama pengiriman, termasuk (Clear, Rainy, Snowy, Foggy, and Windy).
                    4. Traffic_Level : Kondisi lalu lintas yang dikategorikan sebagai Low, Medium, or High.
                    5. Time_of_Day : Waktu saat pengiriman berlangsung, dikategorikan sebagai Morning, Afternoon, Evening, or Night.
                    6. Vehicle_Type : Jenis kendaraan yang digunakan untuk pengiriman, termasuk Bike, Scooter, and Car.
                    7. Preparation_Time_min : Waktu yang dibutuhkan untuk menyiapkan pesanan, diukur dalam menit.
                    8. Courier_Experience_yrs : Pengalaman kurir dalam tahun..
                    9. Delivery_Time_min: Total durasi pengiriman dalam menit (variabel target).
                    ''')
            
        with st.expander("Data Understanding"):
            st.write("""
                    1. Data terdiri dari 9 kolom dan 1000 baris
                    2. `Delivery_Time_min` akan menjadi target variabel
                    3. Missing value pada fitur-fitur tertentu akan di-handling
                    4. Variabel target  `Delivery_Time_min` memiliki distribusi skewness positif/kanan, yang artinya durasi pengiriman cenderung cepat.
                    5. Fitur lainnya terlihat normal dan fitur dengan missing value akan diisi dengan mode atau mean.
                     """)

    with tab3:
        st.header("Data Preparation")
        st.image("https://www.make.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fun655fb9wln6%2Fblog-image-944%2F5908968daefa9c30d62caa234b68c419%2Fon-its-way-a-no-code-food-ordering-system-for-your-restaurant.png&w=3840&q=100", width=700)
        st.write("""
                1. Dataset memiliki missing value terdapat pada beberapa fitur, namun sudah diisi dengan mode atau mean. 
                2. Fitur yang menjadi fokus yaitu durasi pengiriman `Delivery_Time_min`.
                3. Tidak ada data duplikat.
                4. Adanya outlier pada `Delivery_Time_min` namun masih dalam batas wajar dan fitur lainnya tidak memiliki outlier.
                 """)
    
    with tab4:
        st.header("Exploratory Data Analysis & Insight")
        st.image("https://barn2.com/wp-content/uploads/2018/01/Restaurant-ordering-system-e1569334281278.png", width=700)  
        with st.expander("Bivariate Analysis"):
            st.subheader('Numerical & Categorical Features vs Delivery Time')
            st.write("Grafik Analisis Delivery Time Berdasarkan Berbagai Fitur")
            df = pd.read_csv('Food_Delivery_Time_Prediction_cleaned-2.csv')
            cols = ['Distance_km', 'Preparation_Time_min', 'Courier_Experience_yrs', 'Weather', 'Traffic_Level', 'Time_of_Day', 'Vehicle_Type']

            fig, axes = plt.subplots(4, 2, figsize=(12, 12), dpi=1000)
            axes = axes.flatten()

            for i, col in enumerate(cols):
                if df[col].dtype in ['int64', 'float64']:
                    sns.scatterplot(data=df, x=col, y='Delivery_Time_min', ax=axes[i], color='red', alpha=0.5)
                    sns.regplot(data=df, x=col, y='Delivery_Time_min', ax=axes[i], scatter=False, color='blue')
                else: 
                    sns.boxplot(data=df, x=col, y='Delivery_Time_min', ax=axes[i], palette='Set2')
                
                axes[i].set_title(f'Delivery Time by {col}', fontsize=10)

            # Hapus subplot kosong
            if len(cols) < len(axes):
                for j in range(len(cols), len(axes)):
                    fig.delaxes(axes[j])

            plt.tight_layout()
            st.pyplot(fig)

            st.write('''
                1. Jarak `Distance_km` memiliki korelasi positif dengan `Delivery_Time_min`, semakin jauh jarak semakin lama durasi pengiriman
                2. Waktu persiapan pengiriman `Preparation_Time_min` memiliki korelasi positif dengan `Delivery_Time_min`, semakin lama waktu persiapana semakin lama durasi pengiriman.
                3. Pengalaman kurir `Courier_Experience_yrs` memiliki korelasi negatif dengan `Delivery_Time_min`, semakin lama pengalaman kurir semakin cepat durasi pengiriman. Namun korelasi ini tidak sekuat dengan Jarak
                4. Cuaca yang cerah `Clear` cenderung memiliki durasi pengiriman yang cepat dan cuaca yang buruk `Snow` cenderung memiliki durasi pengiriman yang lama.
                5. Kondisi lalu lintas `Traffic_Level` yang semakin tinggi, akan cenderung memiliki durasi pengiriman semakin lama.
                6. Waktu pengiriman `Time_of_Day` Pagi Hari memiliki durasi pengiriman yang cenderung lebih cepat.
                7. Tipe kendaraan `Vehicle_Type` Bike cenderung lebih cepat dibanding lainnya
                    ''')
                    

        with st.expander("Multivariate Analysis"):
            st.subheader('Correlation Matrix')
            st.write("Grafik Berikut Menunjukkan Multivariate Analysis")

            col = ['Distance_km', 'Preparation_Time_min', 'Courier_Experience_yrs', 'Delivery_Time_min']

            fig, ax = plt.subplots(figsize=(8, 6), dpi=1000)
            sns.heatmap(df[col].corr(), annot=True, cmap='crest', ax=ax)
            ax.set_title('Correlation Matrix')

            st.pyplot(fig)
            st.write('''
                    Fitur yang paling berpengaruh terhadap `Delivery_Time_min` adalah `Distance_km` dengan korelasi linear, positif dan kuat. Yang mana semakin jauh jarak maka semakin lama durasi pengiriman.
                    Fitur waktu persiapan `Preparation_Time_min` juga memiliki korelasi linear, positif walaupun tidak sekuat fitur jarak. 
                    ''')
    with tab5:
            st.header("Conclusion & Recommendations")
            st.image("https://www.icoderzsolutions.com/blog/wp-content/uploads/2019/05/Food-Delivery-App-Blog-post.jpg", width=700)

            with st.expander("Conclusion"):
                st.write('''
                    Dari hasil analisis dapat diketahui bahwa :
                    1. Fitur yang paling memengaruhi durasi pengiriman adalah `Distance_km` dan `Preparation_Time_min`.
                    2. Pengalaman kurir yang tinggi membuat durasi pengiriman sedikit lebih cepat.
                    3. Semakin buruk cuaca maka semakin lama durasi pengiriman.
                    4. Semakin tinggi traffic level maka semakin lama durasi pengiriman.
                    5. Pengantaran di pagi hari cenderung cepat.
                    6. Jenis kendaraan bike cenderung lebih cepat dari yang lainnya.
                        ''')
                
            with st.expander("Recommendations"):
                st.write("""
                    Rekomendasi :
                    1. Untuk delivery jarak jauh dan cuaca yang buruk, disarankan diberikan kepada kurir yang pengalamannya tinggi, guna meningkatkan efisiensi dan menjaga keselamatan kurir yang baru
                    2. Meningkatkan kesiapan kurir sebelum pesanan datang guna mengurangi waktu persiapan seperti berada didekat restoran yang sering dipesan pelanggan atau memerhatikan kondisi lalu lintas dan cuaca agar bisa melakukan antisipasi terhadap hal yang tidak terduga.
                    3. Untuk kurir, diutamakan menggunakan bike atau scooter, karena akan membantu saat kondisi lalu lintas yang padat/tinggi seperti di daerah perkotaan. Dan disarankan menggunakan mobil khususnya disaat jaraknya jauh diluar kota dan cuacanya buruk.
                    4. Khusus saat cuaca bersalju disarankan menggunakan bike atau scooter dan menambahkan fitur peringatan pada kurir dan pelanggan bahwa karena cuaca buruk durasi pengiriman akan bertambah lama.
                        """)

