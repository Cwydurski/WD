print("Podaj poczatek zakresu: ")
poczatek = input()
poczatek = int(poczatek)
print("Podaj koniec zakresu: ")
koniec = input()
koniec = int(koniec)

for i in range(poczatek,koniec):
    i = int(i)
    i += 1
    if i % 5 == 0: 
           print("liczba:",i)