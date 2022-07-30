import math
numara = input("öğrenci numaranızı girin lütfen")
a = "2" + str(numara[5])
b = "2" + str(numara[6])
c = "2" + str(numara[7])
d = "1" + str(numara[6]) + str(numara[7])
lenght = float(0)
Lenght = float(int(d))
T1 = float(int(a))
T2 = float(int(b))
T3 = float(int(c))
t = 1
print("Hesaplanıyor.......")
while lenght <= Lenght:
    if (Lenght == round(lenght)):
        print("{0}. günde istenilen uzunluğa kavuşur.".format(t))
        break
    else:
        lenght = lenght + (20 / 3) * (math.e ** (-0.04 * t))
        t = t + 1
        if (Lenght == round(lenght)):
            print("{0}. günde istenilen uzunluğa kavuşur.".format(t))
            break
        else:
            lenght = lenght + (29 / 3) * (math.e ** (-0.04 * t))
            t = t + 1
            if (Lenght == round(lenght)):
                print("{0}. günde istenilen uzunluğa kavuşur.".format(t))
                break
            else:
                lenght = lenght + (29 / 3) * (math.e ** (-0.04 * t))
                t = t + 1