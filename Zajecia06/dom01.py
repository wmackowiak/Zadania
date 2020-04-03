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

for i in range(len(lista_liter)):
    lista_liter = '_'
    print(lista_liter, end=" ")
print("")

zgadnij = input("Twoja litera: ")

for i in range(len(lista_liter)):
    if lista_liter[i] == str(zgadnij):
        lista_liter[i] = str(zgadnij)
        print(lista_liter)
    else:
        print(zgadnij)








