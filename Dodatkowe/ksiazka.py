### Książka adresowa:
# Program przechowujący danę kontaktowe znajomych/klientów.
# - Program wyświetla menu wypisujące komendy jakie należy wpisać, aby program wykonał dane zadanie. Zadania to:
#     - Wyświetlenie wszystkich wpisów
#     - Stworzenie nowego wpisu (dane wczytywane z klawiatury)
#     - Usunięcie wpisu
#     - Zakończenie pracy programu
# - Program powinien na starcie mieć już wprowadzone kilka wpisów.


ksiazka_adresowa = {'imie':'Maria','nazwisko':'Piotrowska','ulica':'Mickiewicza','miasto':'Poznań','telefon':'601453432','e-mail':'m.piotrowska@wp.pl'}

for k, v in ksiazka_adresowa.items():
    print(f"{k} - {v}")

