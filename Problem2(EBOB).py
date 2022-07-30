# EBOB BULUCU.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def EBOB(X,Y):
    liste1 = []
    liste2 = []
    liste3 = []
    for element1 in range(1,X+1):
        if (X % element1 == 0):
            liste1.append(element1)
    for element2 in range(1,Y+1):
        if (Y % element2 == 0):
            liste2.append(element2)
    for element3 in liste1:
        for element4 in liste2:
            if (element3 == element4):
                liste3.append(element3)
    liste3.sort()
    return (liste3[len(liste3) - 1])
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    giris1 = input("Lütfen EBOB'unu Bulmak İstediğiniz İlk Sayıyı Giriniz, Eğer programdan Çıkmak İstiyorsanız 'q' tuşayınız: ")
    giris2 = input("Lütfen EBOB'unu Bulmak İstediğiniz İkinci Sayıyı Giriniz, Eğer programdan Çıkmak İstiyorsanız 'q' tuşayınız: ")
    if (giris1 == "q" or giris2 == "q"):
        print("Programdan Çıkılıyor..........")
        break
    else:
        print("EBOB:", EBOB(int(giris1), int(giris2)))