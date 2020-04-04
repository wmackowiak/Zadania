# ### Wisielec:
# Program, będący implementacją gry "wisielec".
# - Użytkownik ma za zadanie odgadnąć hasło, które ukryte jest w programie.
# - Program pokazuje ile liter ma hasło i te litery, które zostały już odgadnięte
# - Użytkownik podaje po jednej literze. Użytkownik ma ograniczoną ilość prób.
# - W każdym momencie, zamiast podania litery użytkownik może spróbować odgadnąć całe hasło.
# - Popraw kod wisielca, tak by pobierać hasła do gry z pliku hangman.json. Plik powinnien zawierać conamniej jedno
#   zagnieżdżenie odpowiadające kategoriom, które użytkownik może wybrać w grze. Kategorie pobrane z pliku JSON pojawiają
#   się jako elementy menu start.

import random

kategoria = input("Wybierz kategorię 'owoce','warzywa','zwierzeta': ")

if kategoria == 'owoce':
    with open('owoce.txt', 'r', encoding='utf-8') as fopen:
        content = fopen.read()
elif kategoria == 'warzywa':
    with open('warzywa.txt', 'r', encoding='utf-8') as fopen:
        content = fopen.read()
elif kategoria == 'zwierzeta':
    with open('zwierzeta.txt', 'r', encoding='utf-8') as fopen:
        content = fopen.read()

content = content.split()
slowo = random.choice(content)
lista_liter = list(slowo.lower())
ilosc_liter = len(slowo)

print(f"Hasło składa się z {ilosc_liter} liter")
for i in range(len(lista_liter)):
    lista_liter[i] = '_'
print(' '.join(lista_liter))

zycia = 6
while zycia > 0:
    print("Twoja litera:")
    zgadnij = input()
    zgadnij = zgadnij.lower()

    if zgadnij in list(slowo.lower()):
        for i in range(len(lista_liter)):
            if list(slowo.lower())[i] == zgadnij:
                lista_liter[i] = zgadnij
                print(' '.join(lista_liter))
        if slowo.lower() == (''.join(lista_liter)):
            print("Brawo, udało Ci się!")
            break
    else:
        zycia -= 1
        print(f"Nie udało się, pozostały Ci {zycia} życia")