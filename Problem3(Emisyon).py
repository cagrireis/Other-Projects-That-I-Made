print("Aracın Ne kadar Yaktığını Bulan Programa Hoş Geldiniz.")

litreBenzin = 30

arac = float(input("Aracınız Kilometre Başına Kaç Litre Benzin Yakıyor?"))

km = float(input("Aracınız İle Kaç Kilometre Yapacaksınız?"))

print("Hesaplanıyor..........")

liste = [arac,km,litreBenzin]

print("Girdiğiniz Girdiler Sonucuna Aracınız Toplam {0} Tl'lik Yakıt Yakacaktır.".format(liste[2]*liste[1]*liste[0]))

#Problem 4'de kaldım oradan devam ederim.