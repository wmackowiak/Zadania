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

print("Wylosowano słowo: ")
content = content.split()
slowo = random.choice(content)
print(slowo)

liczba_znakow = len(slowo)
print("_ " * liczba_znakow)

zgadnij = input("Twoja litera: ")

for litera in slowo:
    if zgadnij == litera:
        print("Tak")
    else:
        print("Nie")