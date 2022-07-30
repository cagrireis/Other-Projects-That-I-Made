print("Ad, Soyad, Numara Yazdırma Programına Hoş Geldiniz.")

Ad = input("Lütfen Adınızı Giriniz:")
Soyad = input("Lütfen Soyadınızı Giriniz:")
Numara = int(input("Lütfen Numaranızı Giriniz:"))

Toplam = {"Ad":Ad, "Soyad":Soyad, "Numara":Numara}
print("Bastırılıyor................")
print("Adınız: {0}\nSoyadınız: {1}\nNumaranız: {2}\n".format(Toplam["Ad"],Toplam["Soyad"],Toplam["Numara"]))