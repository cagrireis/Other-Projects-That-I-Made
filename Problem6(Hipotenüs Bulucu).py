print("Hipotenüs Bulucu Programa Hoş Geldiniz.")
x = int(input("Lütfen Üçgenin Dik kenarlarından Birinin Santimetre Cinsinden Uzunluğunu Girin:"))
y = int(input("Lütfen Üçgenin Kalan Dik Kenarının Santimetre Cinsinden Uzunluğunu Girin:"))

Liste = [x, y, (x ** 2 + y ** 2) ** 0.5]
print("Hesaplanıyor...........")
print("Girdiğiniz Değerler Sonucunda Üçgenin Hipotenüsü = {0}".format(Liste[2]))