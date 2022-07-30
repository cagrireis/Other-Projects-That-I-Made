print("""****************************************************************
GİRİLEN ŞEKLİN TİPİNİ BELİRLEME PROGRAMINA HOŞ GELDİNİZ.
****************************************************************
""")

print("Bu Program Sizden Bir Şekil Tipi Seçmenizi İsteyecek Ve Siz Şeklin Kenar Uzunluklarını Girdikten Sonra Size Girdiğiniz Cismin Tipini Söyleyecektir.")

print("Bir Üçgennin Tipini Bulmak İstiyorsanız 1'i,\nBir Dörtgenin Tipini Bulmak İstiyorsanız 2'yi Tuşlayınız.")

sekil = int(input("Lütfen Şekle Göre Sayıyı Tuşlayınız: "))

if (sekil == 1):
    kenar1 = int(input("Lütfen Üçgenin İlk Kenarını Giriniz: "))
    kenar2 = int(input("Lütfen Üçgenin İkinci Kenarını Giriniz: "))
    kenar3 = int(input("Lütfen Üçgenin Üçüncü Ve Son Kenarını Giriniz: "))
    if ((abs(kenar1 - kenar2) < kenar3 < abs(kenar1 + kenar2)) and (abs(kenar3 - kenar1) < kenar2 < abs(kenar3 + kenar1)) and (abs(kenar2 - kenar3) < kenar1 < abs(kenar2 + kenar3))):
        print("Evet Girdiğiniz Şekil Üçgen Oluşturma Kurallarına Uyup Bir Üçgen İfade Ediyor.")
        print("Girdiğiniz Üçgenin Tipi Çıkarılıyor.................")
        if ((kenar1 == kenar2) or (kenar2 == kenar3) or (kenar3 == kenar1)):
            print("Girdiğiniz Üçgenin Kenarları {0}, {1}, {2} olup; Üçgeniniz '{3}' Üçgendir.".format(kenar1, kenar2, kenar3, "İkizkenar"))
        elif (kenar1 == kenar2 == kenar3):
            print("Girdiğiniz Üçgenin Kenarları {0}, {1}, {2} olup; Üçgeniniz '{3}' Üçgendir.".format(kenar1, kenar2, kenar3, "Eşkenar"))
        else:
            print("Girdiğiniz Üçgenin Kenarları {0}, {1}, {2} olup; Üçgeniniz '{3}' Üçgendir.".format(kenar1, kenar2, kenar3, "Herhangi Bir"))
    else:
        print("Maalesef Girdiğiniz Değerler Üçgen Oluşturma Kurallarına Uymayıp Bir Üçgen İfade Etmemektedir. Lütfen Tekrar Deneyiniz.")
elif (sekil == 2):
    kenar1 = int(input("Lütfen Dörtgenin İlk Kenarını Giriniz."))
    kenar2 = int(input("Lütfen Dörtgenin İkinci Kenarını Giriniz."))
    kenar3 = int(input("Lütfen Dörtgenin Üçüncü Kenarını Giriniz."))
    kenar4 = int(input("Lütfen Dörtgenin Dördüncü Ve Son Kenarını Giriniz."))
    print("Girdiğiniz Dörtgenin Tipi Çıkarılıyor...........")
    if (kenar1 == kenar2 == kenar3 == kenar4):
        print("Girdiğiniz Dörtgenin Kenarları {0}, {1}, {2}, {3} Olup; Dörtgeniniz '{4}' Dörtgendir.".format(kenar1, kenar2, kenar3, kenar4, "Eşkenar Yani 'Kare"))
    elif (kenar1 == kenar2 or kenar3 == kenar4 or kenar2 == kenar4 or kenar1 == kenar3 or kenar2 == kenar3 or kenar1 == kenar4):
        print("Girdiğiniz Dörtgenin Kenarları {0}, {1}, {2}, {3} Olup; Dörtgeniniz '{4}' Dörtgendir.".format(kenar1, kenar2, kenar3, kenar4, "Dikdörtgen"))
    else:
        print("Girdiğiniz Dörtgenin Kenarları {0}, {1}, {2}, {3} Olup; Dörtgeniniz '{4}' Dörtgendir.".format(kenar1, kenar2, kenar3, kenar4, "Herhangi Bir"))
else:
    print("HATA!")