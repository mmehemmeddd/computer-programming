try:
    a = 5
    b = 8
    c = a/b
    d = x
except:
    print("Bir xeta bas verdi!")

print(a, b, c)

try:
    a = 5
    b = 8
    c = a/b
    d = c/0
    print(d)
except:
    print("Bir xeta bas verdi!")
    print("Sifira bolme!")

print(a, b, c)

try:
    a = 5
    b = 8
    c = a/b
    d = x
    ad = "Ekber"
    simvol = ad[10]
except ZeroDivisionError:
    print("Sifira bolme!")
except NameError:
    print("Deyishen elan edilmedi!")

print(a, b, c)

try:
    a = 5
    b = 8
    c = a/b
    x = 9
    d = x
    ad = "Ekber"
    simvol = ad[10]
except ZeroDivisionError:
    print("Sifira bolme!")
except NameError:
    print("Deyishen elan edilmedi!")
except IndexError:
    print("Indeksde sehv askarlandi!")

print(a, b, c)
try:
    a = 5
    b = 0
    c = a/b
    x = 9
    d = x
    ac = "Salam"
    simvol = ac[4]
except ZeroDivisionError:
    print("Sifira bolme!")
except NameError:
    print("Deyishen elan edilmedi!")
except IndexError:
    print("Indeks sehv yazilib!")
except Exception:
    print("Namelum xeta")