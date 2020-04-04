# Wisielec. Utwórz plik zawierający listę słów wg kategorii np. zwierzęta, owoce etc. Poproś użytkownika o podanie
# kategorii przed rozpoczęciemy gry. Następny wczytaj listę haseł do programu, wylosuj jedno hasło z listy. Rozgrywka
# powinna być maksymalnie intuicyjna.

import random

kategoria = input("Wybierz kategorię 'owoce','warzywa','zwierzeta': ")

if kategoria == 'owoce':
    with open('owoce.txt', 'r', encoding='utf-8') as fopen:
        content = fopen.read()
        print(content)
elif kategoria == 'warzywa':
    with open('warzywa.txt', 'r', encoding='utf-8') as fopen:
        content = fopen.read()
        print(content)
elif kategoria == 'zwierzeta':
    with open('zwierzeta.txt', 'r', encoding='utf-8') as fopen:
        content = fopen.read()
        print(content)

print("")
print("Wylosowane słowo: ")
content = content.split()
slowo = random.choice(content)

print(slowo)
lista_liter = list(slowo.lower())
print(lista_liter)

print("::::::::::::::::::")
for i in range(len(lista_liter)):
    lista_liter[i] = '_'
    # print(lista_liter, end=" ")
print(' '.join(lista_liter))
print("::::::::::::::::::")

zycia = 6
while zycia > 0:

    print("Twoja litera:")
    zgadnij = input()

    if zgadnij in list(slowo.lower()):
        for i in range(len(lista_liter)):
            if list(slowo.lower())[i] == zgadnij:
                lista_liter[i] = zgadnij
                print(' '.join(lista_liter))

        if slowo.lower() == (''.join(lista_liter)):
            print("Brawo, udało Ci się!")
            break

        # print("Oto", slowo.lower())         # gruszka
        # print("To", lista_liter)            # ['g', '_', '_', '_', '_', '_', '_']
        # print(''.join(lista_liter))

        # for znak in lista_liter:
        #     print(znak,end="")
    else:
        zycia -= 1
        print(f"Nie udało się, pozostały Ci {zycia} życia")







