# EKOK BULUCU
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def EKOK(X,Y):
    liste1 = []
    liste2 = []
    liste3 = []
    for element1 in range(1, X+1):
        liste1.append(element1 * Y)
    for element2 in range(1,Y+1):
        liste2.append(element2 * X)
    for element3 in liste1:
        for element4 in liste2:
            if (element3 == element4):
                liste3.append(element3 or element4)
    liste3.sort()
    return liste3[0]
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    giris1 = input("EKOK'unu Bulmak İstediğiniz İlk Sayıyı Girin, Eğer Programdan Çıkmak İsterseniz 'q' Tuşlayınız: ")
    giris2 = input("EKOK'unu Bulmak İstediğiniz İlk Sayıyı Girin, Eğer Programdan Çıkmak İsterseniz 'q' Tuşlayınız: ")
    if (giris1 == "q" or giris2 == "q"):
        print("Programdan Çıkılıyor.....")
        break
    else:
        print("EKOK:", EKOK(int(giris1), int(giris2)))