print("""**************************************
GİRİLEN EN BÜYÜK SAYIYI BULMA PROGRAMINA HOŞ GELDİNİZ!
**************************************
""")

sayi1 = int(input("Sıralanacak İlk Sayıyı Girin Lütfen: "))
sayi2 = int(input("Sıralanacak İkinici Sayıyı Girin Lütfen: "))
sayi3 = int(input("Sıralanacak üçüncü Sayıyı Girin Lütfen: "))

if (sayi1 > sayi2 and sayi1 > sayi3):
    if (sayi2 > sayi3):
        print("Sıralama Şu Şekilde: {0} > {1} > {2}".format(sayi1, sayi2, sayi3))
    elif ():
        print("Sıralama Şu Şekilde: {0} > {2} > {1}".format(sayi1, sayi2, sayi3))
    else:
        print("Girilen En Büyük Sayı '1' Ve Geri Kalan Sayılar Eşit.")
elif (sayi2 > sayi1 and sayi2 > sayi3):
    if (sayi1 > sayi3):
        print("Sıralama Şu Şekilde: {1} > {0} > {2}".format(sayi1, sayi2, sayi3))
    elif (sayi3 > sayi1):
        print("Sıralama Şu Şekilde: {1} > {2} > {0}".format(sayi1, sayi2, sayi3))
    else:
        print("Girilen En Büyük Sayı '2' Ve Geri Kalan Sayılar Eşit.")
elif (sayi3 > sayi2 and sayi3 > sayi1):
    if (sayi2 > sayi1):
        print("Sıralama Şu Şekilde: {2} > {1} > {0}".format(sayi1, sayi2, sayi3))
    elif (sayi1 > sayi2):
        print("Sıralama Şu Şekilde: {2} > {0} > {1}".format(sayi1, sayi2, sayi3))
    else:
        print("Girilen En Büyük Sayı '3' Ve Geri Kalan Sayılar Eşit.")
else:
    print("Girdiğiniz Sayılardan hepsi Tanesi Eşit Veya Hatalı Bir Giriş Yaptınız!")