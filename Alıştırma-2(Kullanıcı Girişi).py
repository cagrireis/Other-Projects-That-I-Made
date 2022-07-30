#print("""************************
#Kullanıcı Girişi
#************************
#""")
#
#sys_kullanici_adi = "Vocaimus"
#sys_password = "2003cr2012or"
#
#kullanici_adi_giris = input("Sisteme Giriş İçin Lütfen Kullanıcı Adınızı Giriniz: ")
#password_giris = input("Sisteme Giriş İçin Lütfen Şifrenizi Giriniz.")
#
#if (kullanici_adi_giris == sys_kullanici_adi):
#    if (password_giris == sys_password):
#        print("Girdiğiniz Bütün Bilgiler Doğru Sisteme Giriş Yaptınız!")
#    else:
#        print("Girdiğiniz Şifre Giriş Yapmaya Çalıştığınız Kullanıcı İle Eşleşmiyor Lütfen Tekrar Deneyiniz.")
#else:
#    print("Öyle Bir Kullanıcı Yok Lütfen Tekrar Deneyiniz.")
#
# Burada Yaptıklarım büyük ölçekte doğr ufakat aynı anda ölçmek için yetersiz. Diğer çözümünü Aşağıya yapacağım.
#
#print("""************************
#Kullanıcı Girişi
#************************
#""")
#
#sys_kullanici_adi = "Vocaimus"
#sys_password = "2003cr2012or"
#
#kullanici_adi_giris = input("Sisteme Giriş İçin Lütfen Kullanıcı Adınızı Giriniz: ")
#password_giris = input("Sisteme Giriş İçin Lütfen Şifrenizi Giriniz.")
#
#if (kullanici_adi_giris == sys_kullanici_adi and password_giris != sys_password):
#    print("Girdiğiniz Şifre Sistemdeki Kullanıcı İle Uyuşmuyor.")
#
#elif (kullanici_adi_giris != sys_kullanici_adi):
#    print("Sistemde Öyle Bir Kullanıcı Yok, Tekrar Deneyin Lütfen.")
#
#elif (kullanici_adi_giris == sys_kullanici_adi and password_giris == sys_password):
#    print("Girdiğiniz Bilgiler Doğru! Sisteme Giriş Yapılıyor.........")
#else:
#    print("Hata!")

#Bu da aynı aslında bir deneme daha yapacağım.


print("""*************************
Kullanıcı Girişi
*************************
""")

dkullaniciadi = "Vocaimus"
dsifre = "2003cr2012or"

giriskullaniciadi = input("Kullanıcı Adınızı Girin Lütfen:")

if (giriskullaniciadi != dkullaniciadi):
    print("Böyle Bir Kullanıcı Adı Yok! Yanlış Girmiş Olmalısınız. Lütfen Tekrar Deneyiniz.")
else:
    girissifre = input("Şifrenizi Girin Lütfen:")
    if (girissifre == dsifre):
        print("Sisteme Giriş Yapılıyor........")
    else:
        print("Yanlış Şifre Girişi! Lütfen Tekrar Deneyiniz.")

# OLDU!


























