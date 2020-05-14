while True:

    print("Podaj liczbe: ")
    liczba = input()
    liczba = int(liczba)
    potega = liczba * liczba
    print("potega z liczby",liczba ,"wynosi: ",potega)
    print("Liczymy dalej T/N: ")

    b = input()

    if b == 'n' :
        print("Koniec pracy Programu") 
        break 