print("3 Sayı Çarpma Programına Hoş Geldiniz.")

sayi_1 = int(input("Lütfen Çarpılacak Birinci Sayıyı Giriniz"))
sayi_2 = int(input("Lütfen Çarpılacak İkinci Sayıyı Giriniz"))
sayi_3 = int(input("Lütfen Çarpılacak Üçünücü Sayıyı Giriniz."))

Dicti = {"Sayi1":sayi_1, "Sayi2":sayi_2, "Sayi3":sayi_3, "Carpim": (sayi_1 * sayi_2 * sayi_3)}

print("Verdiğiniz Sayılar ile Çıkan Sonuç: {2} * {1} * {0} ={3}".format(Dicti["Sayi1"], Dicti["Sayi2"], Dicti["Sayi3"], Dicti["Carpim"]))