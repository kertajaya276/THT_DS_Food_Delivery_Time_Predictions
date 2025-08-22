import streamlit as st
st.set_page_config(page_title="Portfolio",
                   layout="wide", page_icon=":rocket:")
st.title("Food Delivery Time Prediction")
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman",
                        ["About Me", "Project Overview", "Analysis", "Prediction", "Contact"])

if page == 'Contact':
    import kontak
    kontak.tampilkan_kontak()
elif page == 'Project Overview':
    import overview
    overview.tampilkan_overview()
elif page == 'About Me':
    import tentang
    tentang.tampilkan_tentang()
elif page == 'Analysis':
    import analisis
    analisis.tampilkan_analisis()
elif page == 'Prediction':
    import prediksi
    prediksi.tampilkan_prediksi()