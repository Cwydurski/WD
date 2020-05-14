print("podaj a")
a = input()
a = int(a)
print("podaj b")
b = input()
b = int(b)
print("podaj c")
c = input()
c = int(c)
if (a >= 0 and a<=10):
    print("a nalezy do przedzialu od 0 do 10")
    if(a > b):
        print("a jest wieksze od b")
    elif(b > c):
        print("b jest wieksze od c")
    elif(a == b and b == c):
        print("liczby sa rowne")
    else:
        print("c jest najwieksze")
else:
    print("a nie nalezy do przedzialu od 0 do 10")