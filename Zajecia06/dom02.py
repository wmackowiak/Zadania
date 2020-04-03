# lista_liter = ['a','b','c','d']
# for i in range(len(lista_liter)):
#     print("_", end=" ")
# # print(len(lista_liter))

lista_liter = ['a','b','c','d','e','f','g','h']

print(len(lista_liter))
print("-"*8)

for i in range(len(lista_liter)):
    print(lista_liter[i])

print("-"*8)
znak = 'x'
lista_liter[0] = str(znak)
lista_liter[1] = 'z'
lista_liter[-1] = 'y'
print(lista_liter)


# znak = 'g'
# znak_2 = 'a'
# for i in range(len(lista_liter)):
#     # print(lista_liter[i])
#     if lista_liter[i] == znak:
#         lista_liter[i] = znak_2
