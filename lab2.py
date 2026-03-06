original_list = [4, 5, 1, 2, 3, 12, 23, 11, 14, 19]
list1 = [original_list[i] for i in range(0, 5)]
print(list1)
list = [4, 5, 1, 2, 3, 12, 23, 11, 14, 19]
list2 = [x**2 for x in list if x % 2 == 0]
print(list2)
reqemler = [4, 5, 1, 2, 3, 12, 23, 11, 14, 19]
tek_reqemler_10_qati = [x * 10 for x in reqemler if x % 2 == 1]
print(tek_reqemler_10_qati)
xallar = [45, 80, 30, 95, 55]
qiymetler = ["Keçdi" if xal >= 60 else "Kəsildi" for xal in xallar]
print(qiymetler)


