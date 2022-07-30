print("""********************************
FAKTORİYEL BULMA PROGRAMI
********************************
""")

print("Çıkış İçin Programın İçerisindeyken 'q''Ya Basın Lütfen.")

while (True):
    faktoriyel = 1
    sayı = input("Faktoriyeli Alınacak Sayıyı Girin Lütfen: ")

    if (sayı == "q"):
        print("Çıkış Yapılıyor...........")
        break

    else:
        sayılar = range(1, int(sayı)+1)
        for element in sayılar:
            faktoriyel = faktoriyel * element
            print("Sırası İle; Faktoriyel: {0}, Sayı: {1}".format(faktoriyel, element))

    print("Girdiğiniz Sayının Faktoriyeli: {0}'dir.".format(faktoriyel))