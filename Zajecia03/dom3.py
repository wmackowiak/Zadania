"""Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu."""

print("Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.")
password = input("Wprowadz hasło: ")
liczba_znakow = len(password)
#print(liczba_znakow)

char_upper = 0
digit = 0
for litera in password:
    if litera.isupper():
        char_upper +=1
    if litera.isdecimal():
        digit +=1
#print({char_upper},{digit})

if liczba_znakow < 8:
    print("Hasło za krótkie")
elif char_upper < 1:
    print("Brak wielkiej litery")
elif digit < 1:
    print("Brak cyfry")
else:
    print("Twoje hasło jest w porządku")

