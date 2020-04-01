# Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.

# def pole(prom):
#     print(3.14*prom**2)
#
# print(pole(3))

# Napisać funkcję, która sprawdza czy liczba jest parzysta.

# def parzysta(liczba):
#     if liczba % 2 == 0:
#         print("Parzysta")
#     else:
#         print("Nieparzysta")
#
# print(parzysta(134))


# Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.

# def sumuj(a,b,c):
#     print(a+b+c)
# sumuj(234,4,36)

# Napisz funkcję, która pyta o dwie liczby i mówi czy są one równe a jeśli nie to mówi jaka jest różnica między nimi.
#
# def rowne(x,y):
#     if x == y:
#         print("Są równe")
#     else:
#         print(x-y)
# x = int(input("Podaj liczbę: "))
# y = int(input("Podaj liczbę: "))
# rowne(x,y)

# Napisz funkcję, która oblicza przychód po odliczeniu podatku od dochodu. Dochód i wielkośd podatku (w procentach)
# podaje użytkownik (program musi go o to zapytad).

def przychod(dochod,podatek):
    przych = (dochod/(1+podatek/100))
    print(przych)

# dochod = int(input("Podaj wielkość dochodu: "))
# podatek = int(input("Podaj wysokość podatku %: "))

przychod(4000,23)