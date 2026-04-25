import streamlit as st
import random

# Səhifənin tənzimlənməsi
st.set_page_config(page_title="B.A.K.U. Pass", page_icon="🚌", layout="centered")

# Mərkəzi Başlıq
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>B.A.K.U. Pass</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Based on Actual Kilometer Usage</h4>", unsafe_allow_html=True)
st.write("---")

# Simulyasiya üçün saxta dayanacaqlar və onların şərti kilometr (km) mövqeləri
stations = {
    "İçərişəhər": 0.0,
    "Sahil": 1.5,
    "28 May": 3.2,
    "Gənclik": 6.0,
    "Nərimanov": 8.5,
    "Ulduz": 12.0,
    "Koroğlu": 15.5
}

st.subheader("📍 Səyahət Simulyasiyası")

# Tap-in və Tap-out seçimləri
col1, col2 = st.columns(2)
with col1:
    tap_in = st.selectbox("Giriş (Tap-in) dayanacağı:", list(stations.keys()))
with col2:
    tap_out = st.selectbox("Çıxış (Tap-out) dayanacağı:", list(stations.keys()))

# Süni İntellekt Datanın Simulyasiyası (Tıxac və Pik Saat)
is_peak_hour = st.checkbox("Süni İntellekt: Pik Saat və Tıxac Rejimini Aktivləşdir 🤖")

if st.button("Səyahəti Hesabla və Ödənişi Çıx", type="primary"):
    if tap_in == tap_out:
        st.warning("Giriş və çıxış dayanacağı eyni ola bilməz!")
    else:
        # Məsafənin hesablanması
        distance = abs(stations[tap_out] - stations[tap_in])

        # B.A.K.U. Alqoritmi ilə qiymət hesablanması
        base_fare = 0.10  # İlkin giriş haqqı 10 qəpik
        per_km_rate = 0.05  # Hər km üçün 5 qəpik

        # AI dinamik qiymətləndirmə
        ai_multiplier = 1.5 if is_peak_hour else 1.0

        total_fare = base_fare + (distance * per_km_rate * ai_multiplier)

        # Vizual Nəticələr
        st.success("✅ Çıxış (Tap-out) uğurla qeydə alındı!")
        st.write("---")
        st.subheader("📊 B.A.K.U. AI Analizi")

        c1, c2, c3 = st.columns(3)
        c1.metric(label="Qət edilən məsafə", value=f"{distance:.1f} km")
        c2.metric(label="Status (AI)", value="Tıxac / Pik saat" if is_peak_hour else "Normal axın")
        c3.metric(label="Yekun Ödəniş", value=f"{total_fare:.2f} AZN")

        st.info(
            "💡 Ənənəvi sistemdə siz qısa məsafə üçün də standart məbləğ ödəyirdiniz. B.A.K.U. sistemi ilə yalnız getdiyiniz məsafəyə uyğun ədalətli ödəniş etdiniz!")