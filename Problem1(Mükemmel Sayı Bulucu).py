# Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

print("""****************************
MÜKEMMEL SAYI BULUCU
****************************
""")

print("Herhangi bir anda programdan çıkmak isterseniz 'q''ya basınız.")

while (True):
    toplam = 0
    sayi = input("Mükemmel Sayı Olup Olmadığını Kontrol Etmek İstediğiniz Sayıyı Giriniz Lütfen: ")

    if (sayi == "q"):
        print("Programdan Çıkılıyor..............")
        break
    else:
        sıra = range(1, int(sayi))
        for element in sıra:
            if (int(sayi) % element == 0):
                toplam = toplam + element
        if (toplam == int(sayi)):
            print("Girdiğiniz '{0}' sayısı mükemmel sayıdır.".format(sayi))