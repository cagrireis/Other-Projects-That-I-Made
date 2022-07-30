print("""*************************
SONSUZ SAYI BULUCU
*************************
""")
Toplam = 0
while (True):
    sayi = input("Daha önce yazdığınız sayılar ile toplanacak sayıyı girin lütfen: ")
    if (sayi == "q"):
        print("Girdiğiniz Sayıların Toplamı {0}'dır. ".format(Toplam))
        break
    else:
        Toplam = Toplam + int(sayi)