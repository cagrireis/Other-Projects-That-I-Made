# Mükemmel sayı, bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def mükemmel_sayi(sayi):
    toplam = 0
    for element in range(1,sayi):
        if (sayi % element == 0):
            toplam = toplam + element
    if (toplam == sayi):
        return ("Girdiğiniz", sayi, "Sayısı Bir Mükemmel Sayıdır.")
    else:
        return ("Girdiğiniz", sayi, "Sayısı Bir Mükemmel Sayı Değildir.")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while (True):
    X = input("Mükemmel Sayı Olup Olmadığını Kontrol Edeceğiniz Sayıyı Giriniz, Eğer Çıkmak İsterseniz 'q' tuşlayınız: ")
    if (X == "q"):
        print("Programdan Çıkılıyor...............")
        break
    elif(int(X) <= 10000 and int(X) >= 0):
        print(mükemmel_sayi(int(X)))
    else:
        print("Lütfen 1 ile 1000 sayısı arasında bir değer giriniz. Ödev bunun ile sınırlandırıldı.")