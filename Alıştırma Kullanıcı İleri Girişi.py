print("KULLANICI GİRİŞİNE HOŞ GELDİNİZ. GİRİŞ YAPMAK İÇİN 5 HAKKINIZ BULUNMAKTA")
hak = 1
username = "Vocaimus"
password = "2003cr2012or"

while (hak <= 6):
    if (hak >= 6):
        print("Giriş Hakkınız Doldu Programdan Çıkarılıyorsunuz.")
        break
    print("""**************************
    KULLANICI GİRİŞİ
    **************************
    """)
    entered_username = input("Kullanıcı Adınızı Girin Lütfen: ")
    if (entered_username == username):
        entered_password = input("Şifrenizi Girin Lütfen: ")
        if (entered_password == password):
            print("Girdiğiniz Bilgiler Doğru Giriş Yapılıyor.......")
            break
        elif (entered_password != password):
            print("Girdiğiniz Şifre Yanlış.")
            hak = hak + 1
        else:
            print("HATA!")
            hak = hak + 1
    elif (entered_username != username):
        print("Böyle Bir Kullanıcı Bulunmamaktadır.")
        hak = hak + 1
    else:
        print("HATA!")
        hak = hak + 1