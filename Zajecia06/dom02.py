# lista_liter = ['a','b','c','d']
# for i in range(len(lista_liter)):
#     print("_", end=" ")
# # print(len(lista_liter))

# lista_liter = ['a','b','c','d','e','f','g','h']
#
# print(len(lista_liter))
# print("-"*8)
#
# for i in range(len(lista_liter)):
#     print(lista_liter[i])
#
# print("-"*8)
# znak = 'x'
# lista_liter[0] = str(znak)
# lista_liter[1] = 'z'
# lista_liter[-1] = 'y'
# print(lista_liter)


# znak = 'g'
# znak_2 = 'a'
# for i in range(len(lista_liter)):
#     # print(lista_liter[i])
#     if lista_liter[i] == znak:
#         lista_liter[i] = znak_2
# ---
# slowo = 'abrakadabra'
# dlugoscslowa = len(slowo)
# pustemiejsca = "_ "*dlugoscslowa
#
#
# print (pustemiejsca, "[", dlugoscslowa, "liter ]")
# ---
# lista = ['a','b','c','d','e']
# # for count, l in enumerate(lista):
# #     print('Iteracja nr.', count,' Wartość:', l)
#
# zgadnij = input()
# if zgadnij in lista:
#     print("Tak")
# else:
#     print("Nie")
#     ---
# for i in range(5):


# lista = [1, 2, 3, 4, 5]
#
# # Wywołanie elementu listy za pomocą indeksu
# print(lista[1])  # zwróci nam wartość drugiego elementu listy, czyli tutaj liczba 2




def wybór_kategorii(kategoria)
    with open('kategoria.txt', 'r', encoding='utf-8') as fopen:
        content = fopen.read()


kategoria = input("Wybierz kategorię 'owoce','warzywa','zwierzeta': ")


# if kategoria == 'owoce':
#     with open('owoce.txt', 'r', encoding='utf-8') as fopen:
#         content = fopen.read()
# elif kategoria == 'warzywa':
#     with open('warzywa.txt', 'r', encoding='utf-8') as fopen:
#         content = fopen.read()
# elif kategoria == 'zwierzeta':
#     with open('zwierzeta.txt', 'r', encoding='utf-8') as fopen:
#         content = fopen.read()