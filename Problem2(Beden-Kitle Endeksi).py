print("Beden-Kitle Endeksi Hesaplayıcıya Hoş Geldiniz.")

kilo = float(input("Lütfen Kilonuzu Kg Cinsinden Yazınız:"))
boy  = float(input("Lütfen Boyunuzu Metre Cinsinden Yazınız:"))

base = {"boy":boy, "kilo":kilo, "endeks":(kilo/boy**2)}

print("Girdiğiniz Değerler Sonucunda;\nBeden Kitle Endeksiniz ;{0}".format(base["endeks"]))