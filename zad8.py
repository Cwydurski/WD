print("Ile liczb ma miec lista:  ")
liczba = input()
liczba = int(liczba)
lista = []

i = 0

while i < liczba: 
    i+=1    
    print("Podaj liczbe: ")
    a = input()
    a = int(a)
    lista.append(int(a))

print("Elementy listy:",lista)