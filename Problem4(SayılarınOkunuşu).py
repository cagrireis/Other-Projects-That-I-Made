# Sayıların Okunuşu
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def okunus(X):
    sözlük1 = {1:"On", 2:"Yirmi", 3:"Otuz", 4:"Kırk", 5:"Elli", 6:"Altmış", 7:"Yetmiş", 8:"Seksen", 9:"Doksan", 0:""}
    sözlük2 = {1:"Bir", 2:"İki", 3:"Üç", 4:"Dört", 5:"Beş", 6:"Altı", 7:"Yedi", 8:"Sekiz", 9:"Dokuz", 0:""}
    liste = []
    if (int(X) == 0):
        return "Sıfır"
    else:
        for element in X:
            liste.append(element)
        if (len(liste) == 1):
            return sözlük2[int(X)]
        else:
            return sözlük1[int(liste[0])] + " " + sözlük2[int(liste[1])]
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    sayi = input("Okunuşunu Göremek İstediğiniz Sayıyı Girin Lütfen (Sayı En Fazla 2 Basamaklı Olmalıdır.), Ayrıca Programdan Çıkmak İçin 'q' Tuşlayınız: ")
    if (sayi == "q"):
        print("Programdan Çıkılıyor...............")
        break
    else:
        print("Sayının Okunuşu:", okunus(sayi))