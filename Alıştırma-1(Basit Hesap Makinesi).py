print("Basit Hesap Makinesi Programına Hoş Geldiniz.\nBu Programda İşlemler Çeşitli Sayılar İle İfade Edilir.")
islem = int(input("1-) Toplama İşlemi İçin 1'i\n2-) Çıkarma İşlemi İçin 2'yi\n3-) Çarpma İşlemi İçin 3'ü\n4-) Bölme İşlemi İçin 4'ü tuşlayınız."))

sayi1 = int(input("Lütfen İşlem Yapılacak İlk Sayıyı Giriniz:"))

sayi2 = int(input("Lütfen İşlem Yapılacak İkinci Sayıyı Giriniz:"))

if islem == 1:
    print("İşlem Sonucunuz: {0} + {1} = {2}".format(sayi1, sayi2, sayi1 + sayi2))
elif islem == 2:
    print("İşlem Sonucunuz: {0} - {1} = {2}".format(sayi1, sayi2, sayi1 - sayi2))
elif islem == 3:
    print("İşlem Sonucunuz: {0} X {1} = {2}".format(sayi1, sayi2, sayi1 * sayi2))
elif islem == 4:
    print("İşlem Sonucunuz: {0} / {1} = {2}".format(sayi1, sayi2, sayi1 / sayi2))
else:
    print("Maalesef Hatalı Giriş! Tekrar Deneyiniz.")
