print("""**************************************
BEDEN KİTLE ENDEKSİ HESAPLAYICIYA HOŞGELDİNİZ
**************************************
""")

boy = float(input("Lütfen Boyunuzu Metre Cinsinden Giriniz: "))
kilo = float(input("Lütfen Kilonuzu Kilogram Cinsinden Giriniz: "))
endeks = kilo / boy ** 2

liste = [boy, kilo, endeks]

if (liste[2] < 18.5):
    print("Beden Kitle Endeksiniz {0}'dir Ve Zayıf Vücut Kategorisindesiniz.".format(liste[2]))
elif (liste[2] < 25):
    print("Beden Kitle Endeksiniz {}'dir Ve Normal Vücut Kategorisindesiniz.".format(liste[2]))
elif (liste[2] < 30):
    print("Beden Kitle Endeksiniz {}'dir Ve Fazla Kilolu Vücut Kategorisindesiniz.".format(liste[2]))
elif (liste[2] > 30):
    print("Beden Kitle Endeksiniz {}'dir Ve Obez Vücut Kategorisindesiniz.".format(liste[2]))
else:
    print("HATALI GİRİŞ!")

#and ile de yazılabilir
