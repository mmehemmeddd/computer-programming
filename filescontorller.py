# import PyPDF2
#
# file_path = r"C:\Users\muham\OneDrive\Masaüstü\Public Speaking\thank-you-for-arguing.pdf"
#
# try:
#     with open(file_path, "rb") as f:
#         pdf_reader = PyPDF2.PdfReader(f)
#         print(f"Səhifə sayı: {len(pdf_reader.pages)}")
#
#         # İlk səhifəni oxuyaq
#         first_page = pdf_reader.pages[0]
#         print(first_page.extract_text())
# except FileNotFoundError:
#     print("Xəta: Fayl tapılmadı. Yolu yoxlayın.")
# except Exception as e:
#     print(f"Gözlənilməz xəta: {e}")
import PyPDF2
import sys  # Gözlənilməz xətaları idarə etmək üçün

# Fayl yolunu 'r' (raw string) ilə yazmaq \ simvollarında xəta almağın qarşısını alır
file_path = r"C:\Users\muham\OneDrive\Masaüstü\Diskret Riyaziyyat\Çoxluqlar nəzəriyyəsinin bəzi elementləri-1.pdf"

# PyPDF2 kitabxanasının quraşdırıldığından əmin olun:
# pip install PyPDF2

try:
    # 'with' blokundan istifadə etmək daha təhlükəsizdir (faylı avtomatik bağlayır)
    with open(file_path, "rb") as f:
        # Yeni versiyalarda PdfReader istifadə olunur
        pdfReader = PyPDF2.PdfReader(f)

        # Səhifə sayını öyrənmək üçün len(reader.pages) istifadə olunur
        print(f"Ümumi səhifə sayı: {len(pdfReader.pages)}")

        # Faylda səhifə olub-olmadığını yoxlayaq
        if len(pdfReader.pages) > 0:
            # İlk səhifəni əldə etmək (indeks 0-dan başlayır)
            pageObj = pdfReader.pages[0]

            # Mətni çıxarmaq
            text = pageObj.extract_text()

            if text and text.strip():
                print("\nBirinci səhifənin mətni:\n")
                print(text)
            else:
                print(
                    "\nBirinci səhifədən mətn çıxarmaq mümkün olmadı. Səhifə şəkil və ya mürəkkəb formatda ola bilər.")
        else:
            print("PDF faylında heç bir səhifə tapılmadı.")

except FileNotFoundError:
    print(f"XƏTA: '{file_path}' faylı tapılmadı. Zəhmət olmasa fayl yolunu yoxlayın.")
except Exception as e:
    # PyPDF2-dən gələ biləcək digər xətaları da tutmaq üçün (məsələn, zədələnmiş fayl)
    print(f"Gözlənilməz bir xəta baş verdi: {e}", file=sys.stderr)
    print("Faylın zədələnmədiyindən və ya şifrəli olmadığından əmin olun.", file=sys.stderr)

