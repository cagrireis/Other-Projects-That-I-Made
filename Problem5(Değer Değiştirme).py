print("Girilen Sayıların Değerlerini Değiştirme Programına Hoş Geldiniz.")
Sayi_1 = int(input("Lütfen Değeri Değiştirilecek İlk Sayıyı Giriniz (Sayı1):"))
Sayi_2 = int(input("Lütfen Değeri Değiştirilecek İkinici Sayıyı Giriniz (Sayı2):"))

x = Sayi_1
y = Sayi_2

print("Değiştirilmeden Önce Sayılar: Sayı1 = {0}, Sayı2 = {1}".format(Sayi_1,Sayi_2))

Sayi_1 = y
Sayi_2 = x

print("Değiştirilme Olayından Sonra Sayılar: Sayı1 = {0}, Sayı2 = {1}".format(Sayi_1,Sayi_2))


# Sayi_1, Sayi_2 = Sayi_2, Say,_1 olarak da yapılabilir kısaca.