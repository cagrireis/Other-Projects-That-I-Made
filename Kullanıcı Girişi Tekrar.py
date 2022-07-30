print("""**********************************
KULLANICI GİRİŞİ
***********************************
""")

d_kullanici = "Vocaimus"
d_sifre = "2003cr2012or"

girilenkullaniciadi = input("Lütfen Kullanıcı Adınızı Giriniz: ")

if (girilenkullaniciadi == d_kullanici):
    girilensifre = input("Lütfen Şifrenizi Giriniz: ")
    if (girilensifre == d_sifre):
        print("Tebrikler! Başarı İle Giriş Yaptınız.")
    elif (girilensifre != d_sifre):
        print("Maalesef Girdiğiniz Şifre Yanlış! Lütfen Tekrar Deneyiniz.")
    else:
        print("HATA!")
elif (girilenkullaniciadi != d_kullanici):
    print("Böyle Bir Kullanıcı Yok Lütfen Tekrar Deneyiniz.")
else:
    print("Hata!")