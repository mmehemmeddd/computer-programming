import math


def kalkulyator():
    print("--- Python Kalkulyatoruna Xoş Gəlmisiniz! ---")
    print("Əməliyyatlar: +, -, *, /, ** (qüvvət), sqrt (kök altı)")
    print("Çıxmaq üçün 'exit' yazın.\n")

    while True:
        sual = input("Misalı yazın (məsələn 25 + 75): ").lower()

        if sual == 'exit':
            print("Kalkulyator bağlanır. Sağ olun!")
            break

        try:

            if "sqrt" in sual:
                reqem = float(sual.replace("sqrt", "").strip())
                neticə = math.sqrt(reqem)
            else:
                # eval funksiyası yazılan mətni riyazi olaraq hesablayır
                neticə = eval(sual)

            print(f"Nəticə: {neticə}")
            print("-" * 20)

        except ZeroDivisionError:
            print("Xəta: Sıfıra bölmək olmaz!")
        except Exception:
            print("Xəta: Düzgün formatda yazın (məsələn: 15 * 4)")


# Proqramı başladırıq
kalkulyator()