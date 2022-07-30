#print("""**********************
#ÇARPIM TABLOSU
#**********************
#""")
#liste1 = []
#liste2 = []
#liste3 = []
#liste4 = []
#liste5 = []
#liste6 = []
#liste7 = []
#liste8 = []
#liste9 = []
#liste10 = []
#
#print("1'den 10'a Kadar Olan Sayıların Çarpım Tablosu")
#for element in range(1,11):
#    for sıralar in range(1,11):
#        if element == 1:
#            liste1.append(sıralar)
#        elif element == 2:
#            liste2.append(sıralar * element)
#        elif element == 3:
#            liste3.append(sıralar * element)
#        elif element == 4:
#            liste4.append(sıralar * element)
#        elif element == 5:
#            liste5.append(sıralar * element)
#        elif element == 6:
#            liste6.append(sıralar * element)
#        elif element == 7:
#            liste7.append(sıralar * element)
#        elif element == 8:
#            liste8.append(sıralar * element)
#        elif element == 9:
#            liste9.append(sıralar * element)
#        elif element == 10:
#            liste10.append(sıralar * element)
#        else:
#            print("HATA!")
# print(liste1, liste2, liste3, liste4, liste5, liste6, liste7, liste8, liste9, liste10, sep="\n")








# Bursaı ilk yaptığım Çarpım tablosu farklı şekillerde yapmışız hocanın yaptığı şekilde yapmam lazım.



print("""**********************
ÇARPIM TABLOSU
**********************
""")

X = int(input("Çarpım Tablosu Yapılacak Sayıları Hangi Sayıya Göre Çarpalım?"))
Y = int(input("Çarpım Tablosu Yapılacak Sayıları Girin Lütfen: "))



print("Çarpım Tablonuz:  ")

for element in range(1,X):
    print("***************************************************************************")
    for sayi in range(1,Y):
            print("{0} X {1} = {2}".format(element, sayi, element * sayi))









