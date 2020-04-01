# Proszę zdefiniować funkcję z zastosowaniem pętli for.
# Działanie funkcji: dla listy [1,2,12,2] daje wynik 48, ponieważ:
#
# 1*2=2
# 2*12=24
# 24*2 = 48

lista = [1,2,12,2]
   #     0 1  2 3

# for x in lista:
#     print(x)
#     for znak in range(3):
#         wynik = lista[znak] * lista[znak+1]
#                         # 0               1       1,2
#                         # 1               2       2,12
#                         # 2               3       12,2
#                         # 3               4       24,2
#
#         print(wynik)
#         znak+=1

for znak in range(4):
    print(znak)
