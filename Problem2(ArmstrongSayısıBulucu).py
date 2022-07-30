print("""*******************************
ARMSTRONG SAYISI BULUCU
*******************************
""")

print("Program Girdiğiniz Sayının Armstrong Sayısı Olup Olmadığını Size Söyleyecektir.")

while (True):
    toplam = 0
    liste = []
    sayi = input("Armstrong Olup Olmadığını Kontrol Etmek İstediğiniz Sayıyı Girin Lütfen: ")

    if (sayi == "q"):
        print("Programdan Çıkılıyor.......")
        break
    else:
        for element in sayi:
            liste.append(element)
        if (len(liste) == 3):
                for x in liste:
                    toplam = toplam + int(x) ** 3
                if (toplam == int(sayi)):
                    print("Tebrikler Girdiğiniz {0} Sayısı Bir Armstrong Sayısıdır.".format(sayi))
                else:
                    print("Maalesef Girdiğiniz {0} Sayısı Armstrong Sayısı Değil Lütfen Tekrar Deneyiniz.".format(int(sayi)))
        elif (len(liste) == 4):
                for e in liste:
                    toplam = toplam + int(e) ** 4
                if (toplam == int(sayi)):
                    print("Tebrikler Girdiğiniz {0} Sayısı Bir Armstrong Sayısıdır.".format(int(sayi)))
                else:
                    print("Maalesef Girdiğiniz {0} Sayısı Armstrong Sayısı Değil Lütfen Tekrar Deneyiniz.".format(int(sayi)))
        else:
            print("HATA, ARMSTRONG SAYILARI 3 VEYA 4 BASAMAKLIDIR! LÜTFEN TEKRAR DENEYİNİZ.")