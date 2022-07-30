#print("""*************************
#LİST COMPROHERSION
#*************************
#""")

#liste1 = range(1,101)
#liste2 = []
#for element in liste1:
#    if element % 2 == 0:
#        liste2.append(element)
#    else:
#        continue
#liste3 = [i for i in liste2]
#print(liste3)


# bu benim ilk yaptığım başka yolu var mı diye bakıcam.

print("""*************************
LİST COMPROHERSION
*************************
""")


liste2 = [x for x in range(1,101) if x % 2 == 0]

print(liste2)

# bu şekilde yapılmalıymış.