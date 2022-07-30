# tam bölen bulma
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def bölen_bul(sayi):
    liste = []
    if (sayi == 1):
        return 1
    elif (sayi == 0):
        return 0
    else:
        for element in range(1,sayi+1):
            if (sayi % element == 0):
                liste.append(element)
    return liste
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while (True):
    X = input("Tam Bölenlerinin Bulunacağı Sayıyı Girin Lütfen: ")
    if (X == "q"):
        print("Programdan Çıkılıyor......................")
        break
    else:
        print("Tam Bölenler:", bölen_bul(int(X)))