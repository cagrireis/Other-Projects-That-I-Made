def asal_mi(sayi):
    if (sayi == 1):
        return False
    elif (sayi == 2):
        return True
    else:
        for element in range(2, sayi):
            if (sayi % element == 0):
                return False
            else:
                return True
while True:
    X = input("Asal Olup Olmadığı Test Edilecek Sayıyı Girin, Eğer Programdan Çıkmak İstiyorsanız 'q' Tuşlayınız: ")
    if (X == "q"):
        print("Program Çıkılıyor................")
        break
    else:
        if (asal_mi(int(X)) == True):
            print("Girdiğiniz '{0}' sayısı asal sayıdır.".format(X))
        else:
            print("Girdiğiniz '{0}' sayısı asal sayı değildir.".format(X))