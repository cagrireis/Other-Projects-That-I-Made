print("Kök bulma programına hoş geldiniz.\nBu program ax^2+bx+c tabanlı bir fonksiyonun köklerini bulmaya yönelik çalışır. Lütfen 'a', 'b' ve 'c' değerlerini göz önünde bulundurunuz.")
a = int(input("Lütfen 'a' değerini giriniz."))
b = int(input("Lütfen 'b' değerini giriniz."))
c = int(input("Lütfen 'c' değerini giriniz."))

print("Diskriminant değeri: {}'dir.".format(b ** 2 - 4 * a * c))
diskriminant = (b ** 2 - 4 * a * c)
sonuc1 = (- b + diskriminant ** 1 / 2 ) / (2 * a)
sonuc2 = (- b - diskriminant ** 1 / 2 ) / (2 * a)

list = [sonuc1, sonuc2]

print("Kökleriniz:\n1. Kök:{0},\n2.Kök:{1}".format(list[0],list[1]))

