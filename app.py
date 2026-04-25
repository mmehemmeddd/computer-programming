import streamlit as st

# Səhifənin tənzimlənməsi (Geniş ekran rejimi əlavə edildi)
st.set_page_config(page_title="B.A.K.U. Pass | Hackathon", page_icon="🚇", layout="centered")

# Rəngli Başlıqlar üçün xüsusi HTML/CSS
st.markdown("""
<style>
.main-title { color: #E63946; text-align: center; font-size: 3em; font-weight: 800; font-family: sans-serif; }
.sub-title { color: #1D3557; text-align: center; font-size: 1.2em; font-weight: bold; margin-bottom: 20px;}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🚇 B.A.K.U. Pass</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Baku Actual Kilometer Usage (Stansiya Modeli)</div>", unsafe_allow_html=True)

# Tətbiqi iki hissəyə (Tab) bölürük: Simulyasiya və Məlumat
tab1, tab2 = st.tabs(["🚀 Canlı Simulyasiya", "🚇 Bakı Metrosu Haqqında"])

with tab1:
    st.subheader("📍 :blue[Səyahət Simulyasiyası]")

    # Stansiyalar ardıcıl xətt üzrə siyahıya alınıb (Qırmızı Xətt nümunəsi)
    stations = [
        "İçərişəhər", "Sahil", "28 May", "Gənclik", "Nərimanov",
        "Ulduz", "Koroğlu", "Qara Qarayev", "Neftçilər",
        "Xalqlar Dostluğu", "Əhmədli", "Həzi Aslanov"
    ]

    col1, col2 = st.columns(2)
    with col1:
        tap_in = st.selectbox("🟢 Giriş (Tap-in) stansiyası:", stations)
    with col2:
        tap_out = st.selectbox("🔴 Çıxış (Tap-out) stansiyası:", stations)

    st.write("---")
    st.markdown("### 🤖 :orange[Süni İntellekt Tənzimləmələri]")
    # Tıxac saatı toggle (düymə) şəklində daha modern görünür
    is_peak_hour = st.toggle("🚦 Pik Saat Rejimi (Səhər 08:00-09:30 / Axşam 18:00-19:30)")

    if st.button("Səyahəti Hesabla və Ödənişi Çıx", type="primary", use_container_width=True):

        # Stansiya indekslərini tapırıq
        idx_in = stations.index(tap_in)
        idx_out = stations.index(tap_out)

        if idx_in == idx_out:
            st.error("🚨 Giriş və çıxış stansiyası eyni ola bilməz!")
        else:
            # Neçə stansiya keçildiyini hesablayırıq
            station_count = abs(idx_out - idx_in)

            # Qiymət Strategiyası (Stansiya başına)
            base_fare = 0.10  # İlkin turniket giriş haqqı (10 qəpik)
            per_station_rate = 0.05  # Hər stansiya üçün əlavə 5 qəpik

            # AI qiymətləndirmə
            ai_multiplier = 1.5 if is_peak_hour else 1.0
            total_fare = base_fare + (station_count * per_station_rate * ai_multiplier)

            # 📌 MAKSİMUM QİYMƏT LİMİTİ (0.80 AZN - 80 qəpik)
            MAX_FARE = 0.80
            limit_applied = False

            if total_fare > MAX_FARE:
                total_fare = MAX_FARE
                limit_applied = True

            # Eko-Xal (Gamification): Pik saatda getməyənlərə həvəsləndirici xal verilir
            eco_points = 0 if is_peak_hour else station_count * 5

            # Vizual Nəticələr
            st.success("✅ Çıxış (Tap-out) uğurla qeydə alındı!")
            st.write("---")
            st.subheader("📊 B.A.K.U. AI Analizi Nəticələri")

            c1, c2, c3, c4 = st.columns(4)
            c1.metric(label="🚉 Keçilən Stansiya", value=f"{station_count}")
            c2.metric(label="🚦 Status (AI)", value="Pik Saat" if is_peak_hour else "Normal")
            c3.metric(label="🍃 Eko-Xal", value=f"+{eco_points}")

            if limit_applied:
                c4.metric(label="💳 Yekun Ödəniş", value=f"{total_fare:.2f} AZN", delta="🛡️ 80 qəpik Limit!",
                          delta_color="normal")
                st.warning(
                    "🛡️ **Sosial Qoruma Sistemi Aktivdir:** Sərnişin uzun məsafə qət etsə də, B.A.K.U. alqoritmi maksimum limit olan **80 qəpik**dən artıq vəsait çıxılmasına icazə vermədi.")
            else:
                c4.metric(label="💳 Yekun Ödəniş", value=f"{total_fare:.2f} AZN")

            st.info(
                "💡 Ənənəvi sistemdə sərnişin 1 stansiya getsə də 50 qəpik ödəyir. B.A.K.U. sistemi ilə yalnız gedilən stansiya sayına görə ədalətli ödəniş edilir!")

with tab2:
    st.subheader("🚇 Bakı Metropoliteni: Keçmişdən Gələcəyə")

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Baku_Metro_logo.svg/1024px-Baku_Metro_logo.svg.png",
        width=100)

    st.markdown("""
    **Bakı Metropoliteni** — 1967-ci il noyabrın 6-da istifadəyə verilmiş, həm tarixi, həm də memarlıq baxımından unikal bir yeraltı nəqliyyat şəbəkəsidir. Şərqdə və Müsəlman aləmində açılan ilk metrodur.

    ### 📊 Statistik Göstəricilər:
    * **Ümumi Uzunluq:** 40.7 kilometr
    * **Stansiya Sayı:** 27 aktiv stansiya
    * **Xətlər:** 3 xətt (Qırmızı, Yaşıl, Bənövşəyi)
    * **Gündəlik Sərnişin:** Təqribən 600,000 - 800,000 nəfər.

    ### 🎯 Niyə məhz B.A.K.U. sistemi tətbiq olunmalıdır?
    Hazırda mövcud olan sabit ödəniş (50 qəpik) sistemi şəhərin genişlənməsi fonunda həm sərnişinlər, həm də dövlət üçün səmərəsizliyə səbəb olur. 
    1. **Qısaməsafəli Ədalətsizlik:** İçərişəhərdən Sahilə (1 stansiya) gedən də 50 qəpik ödəyir, Həzi Aslanovdan Dərnəgülə (15 stansiya) gedən də.
    2. **Tıxacın İdarəolunmazlığı:** Səhər 08:00-da hamı eyni anda metroya hücum edir, çünki qiymət dəyişmir.

    **B.A.K.U. (Based on Actual Kilometer Usage - Stansiya Modeli)** bu problemi kökündən həll edir. Biz "Tap-in / Tap-out" məntiqi ilə sərnişinə həm ədalətli qiymət təqdim edirik, həm də maksimum 80 qəpik limitlə onun cibini qoruyuruq!
    """)