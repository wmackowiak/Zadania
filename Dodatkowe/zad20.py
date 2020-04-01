# Używając pętli proszę wypisać imiona w ten sposób, aby program pokazywał ile liter ma każde imię. Funkcja zliczająca
# litery w wyrazie to len().
#
# Adrian 6
# Piotrek 7
# Ewa 3
# Bonifacy 8


lista = ['Adrian','Piotrek','Ewa','Bonifacy']
for i in lista:
    znak = len(i)
    print(i + " " + str(znak))

