print("""*************************
3'E BÖLÜNEN SAYILAR
*************************
""")
liste = []
for element in range(1,101):
    if (element % 3 != 0):
        continue
    else:
        liste.append(element)
print("1'den 100'e kadar 3'e bölünen sayılar = {0}".format(liste))