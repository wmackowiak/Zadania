# Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby.
# Jeśli liczba znajduje się na krotce wyswietl jej indeks.

calkowite = (0,1,6,1,33,4,35,47,8,9)
print(type(calkowite))

liczba = input("Podaj liczbę: ")
liczba = int(liczba)
if liczba in calkowite:
    print(calkowite.index(liczba))
    print(f"Indeks liczby {liczba} to {calkowite.index(liczba)}")
else:
    print("Nie znalazłem")

