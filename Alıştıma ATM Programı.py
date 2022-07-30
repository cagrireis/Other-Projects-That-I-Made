print("""********************************
ATM MAKİNESİ
********************************
""")
print("ATM makinesine hoş geldiniz.")
print("""
İŞLMELER;
1-) BAKİYE SORGULAMA
2-) PARA YATIRMA
3-) PARA ÇEKME
!!! PROGRAMDAN ÇIKMAK İÇİN 'q' ya basınız.
""")
bakiye = 3256.82

while (True):
    islem = input("Hangi İşlemi Yapmak İstiyorsanız Tabloda Onun Önünde Bulunan Sayıyı Tuşlayınız :")
    if (islem == "q"):
        print("Programdan Çıkılıyor...............")
        break
    elif (int(islem) == 2):
        print("Para yatırma Sekmesine Yönlendirildiniz.")
        islem2 = input("Hesabınıza Kaç TL Yatırmak İstiyorsunuz? ")
        if (islem2 == "q"):
            print("Programdan Çıkılıyor.....")
            break
        else:
            print("İşleminiz Yapılıyor................")
            print("Yatırdığınız Miktar İle Birlikte Hesabınızdaki Toplam Para {0} TL Oldu.".format(bakiye + int(islem2)))
            bakiye = bakiye + int(islem2)
    elif (int(islem) == 3):
        print("Para Çekme Sekmesine Yönlendirildiniz.")
        islem3 = input("Hesabınızdan Kaç TL Çekmek İstiyorsunuz?")
        if (islem3 == "q"):
            print("Programdan Çıkılıyor...............")
            break
        elif(bakiye < int(islem3)):
            print("Hata, Bu parayı Çekemezsiniz, Hesabınızda Bu Kadar Para Yok.")
        else:
            print("İşleminiz Yapılıyor................")
            print("Para Çekme İşleminizden Sonra Hesabınızda {} TL Kaldı.".format(bakiye - int(islem3)))
            bakiye = bakiye - int(islem3)
    elif (int(islem) == 1):
        print("Bakiyeniz {0} TL".format(bakiye))
    else:
        print("HATA!")