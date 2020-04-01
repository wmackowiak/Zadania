#Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika jest podzielna
# przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

liczba = input("Podaj liczbę")
liczba = int(liczba)
#wynik = liczba % 3
#print(wynik)

if liczba % 3 == 0:
    print("Twoja liczba jest podzielna przez 3")
else:
    print("Niestety")

