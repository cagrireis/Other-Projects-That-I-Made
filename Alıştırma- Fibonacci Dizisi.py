# Fibonacci Dizisi Bir Sayının önceki İki Sayının Toplamının Oluşturduğu Sayı Dizisidir.

print("""*****************************************************
FİBONACCİ DİZİSİ OLUŞTURUCUYA HOŞ GELDİNİZ
*****************************************************
""")

print("Programdan Çıkmak İçin 'q''ya Basınız.")

while (True):
    a = 1
    b = 1
    liste = [a,b]
    sayi = input("Fibonacci'nin Eleman Sayısını Giriniz.")
    if (sayi == "q"):
        print("Programdan Çıkılıyor.........")
        break

    else:
        sayi = int(sayi) - 2
        döngü = range(1, sayi + 1)
        for element in döngü:
            liste.append(a+b)
            print("a: {0}, b: {1}".format(a,b))
            x = a
            a = b
            b = a + x
    print(liste)