import pandas as pd

melumat = {
    "Telebeler": ["Əli", "Aytən", "Vəli", "Nəzrin", "Rəşad"],
    "Riyaziyyat_Qiymeti": [85, 92, 78, 95, 60],
    "Davamliliq_Faizi": [90, 95, 80, 100, 70]
}
df = pd.DataFrame(melumat)
print("Bütün Cədvəl:")
print(df)
print("-" * 30)