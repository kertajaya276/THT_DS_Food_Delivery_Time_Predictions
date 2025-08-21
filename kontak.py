import streamlit as st

def tampilkan_kontak():
    st.title("📞 Contact")

    st.write("Silakan hubungi saya melalui tautan di bawah ini:")

    # Membuat kolom untuk tata letak horizontal
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔗 LinkedIn")
        st.markdown("[Klik untuk membuka profil LinkedIn](https://www.linkedin.com/in/snkertajaya)")

    with col2:
        st.markdown("### 🐙 GitHub")
        st.markdown("[Klik untuk membuka profil GitHub](https://github.com/kertajaya276)")

    st.markdown("---")
    st.markdown("### 📧 Email")
    st.write("kertajaya630@gmail.com")
