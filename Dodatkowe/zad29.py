# To są wyrazy do wyboru: ARA , BereKA , GONabEACH
# Wybierz numer wyrazu,który ma być przeliterowany?
#     Podaj liczbę: 1, 2 lub 3: 2
# wybrałeś słowo: BereKA
# B
# e
# r
# e
# K
# A


lista = ['ARA' , 'BereKA' , 'GONabEACH']
for i in lista:
    print(i,end=' ')

print("Wybierz numer wyrazu,który ma być przeliterowany?")
liczba = int(input("Podaj liczbę: 1, 2 lub 3:")) -1
print(("Wybrałeś słowo: "+lista[liczba]))
for x in (lista[liczba]):
    print(x)




