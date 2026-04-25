import cv2

# Şəklin adını bura dəqiq yazın
fayl_adi = (""WIN_20251115_12_19_03_Pro.jpg")

# Şəkli oxuyuruq
img = cv2.imread(fayl_adi)

# Yoxlayırıq: Şəkil boşdurmu?
if img is None:
    print(f"XƏTA: '{fayl_adi}' faylı tapılmadı və ya oxuna bilmir!")
    print("Məsləhət: Şəklin kodla eyni qovluqda olduğuna əmin olun.")
else:
    print("Şəkil uğurla yükləndi!")

    # Şəkli ekranda göstəririk
    cv2.imshow('Menim Shekilim', img)

    # Bir düymə basana qədər pəncərəni bağlama (0 = sonsuz gözləmə)
    cv2.waitKey(0)
    cv2.destroyAllWindows()