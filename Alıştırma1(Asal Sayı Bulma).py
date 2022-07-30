#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def asal(X):
    liste = []
    for element in range(1,X+1):
        if (X % element == 0):
            liste.append(element)
    if (len(liste) == 2):
        print("Girdiğiniz {0} sayısı asaldır.".format(X))
    else:
        print("Girdiğiniz '{0}' sayısı asal değildir.".format(X))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while (True):
    X = input("Asal olup olmadığını kontrol etmek istediğiniz sayıyı giriniz: ")
    if (X == "q"):
        print("Programdan Çıkılıyor................")
        break
    else:
        asal(int(X))
# cevap doğru. fakat hocanın yaptığının aynısını yazıcam ben de.