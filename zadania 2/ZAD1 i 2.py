import sys


lista = []
for x in range(1,20,1):
    if x%4==0:
        lista.append(x)


plik=open("zad1.txt","a+")


plik.writelines(str(lista))


plik.close()


with open("zad1.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")