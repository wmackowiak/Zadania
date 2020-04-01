# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika,
# ale nie większe niż 8).
# Przykłady:
#     0! = 1
#     1! = 1
#     3! = 1⋅2⋅3 = 6
#     4! = 1⋅2⋅3⋅4 = 24
#     6! = 1⋅2⋅3⋅4⋅5⋅6 = 720

liczba = int(input("Podaj liczbę: "))
if liczba <= 8:
    a=1
    if liczba == 0:
        print("Silnia: 1")
    else:
        while liczba >= 1:
            a = liczba * a
            liczba = liczba - 1
        print("Silnia: ",a)
else:
    print("Koniec")
